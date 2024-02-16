import os, csv, zipfile, shutil
from dotenv import load_dotenv
from jira import JIRA

def make_direcotry(directory):
    """
    make directory if not exists
    Args:
        directory (str): path of directory
    """
    if not os.path.exists(directory):
        os.mkdir(directory)

def issues_to_csv(issues, dest_csv):
    """
    export jira issues to csv
    Args:
        issues (Issue[]): list of jira issue
        dest_csv (str): destination csv file path
    """
    with open(dest_csv, "w", newline="") as f:
        all_fields = []
        for issue in issues:
            all_fields.extend([key for key in issue.fields.__dict__.keys() if key not in all_fields])
        writer = csv.DictWriter(f, fieldnames=all_fields)
        writer.writeheader()
        for issue in issues:
            writer.writerow(issue.raw['fields'])

def download_attachments(issues, dest_dir):
    """
    download attachments of issues and archive
    Args:
        issues (Issue[]): list of jira issue
        dest_dir (str): destination directory path
    """
    for issue in issues:
        # Downloard attachments
        if 0 < len(issue.fields.attachment):
            for attachment in issue.fields.attachment:
                issue_dir = f"{dest_dir}/{issue.key}"
                make_direcotry(issue_dir)
                file_path = f"{issue_dir}/{attachment.filename}"
                res = attachment.get()
                with open(file_path, "wb") as f:
                    f.write(res)
            
            # Archive
            zipfile_name = f"{dest_dir}/{issue.key}.zip"
            with zipfile.ZipFile(zipfile_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(issue_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, issue_dir)
                        zipf.write(issue_dir, zipfile_name)
            shutil.rmtree(issue_dir)

if __name__ == '__main__':
    # Load environment variable from .env
    load_dotenv()
    jira_server = os.getenv('jira_server')
    username = os.getenv('username')
    password = os.getenv('password')
    projects = os.getenv('projects').split(',')
    dest_dir = os.getenv('dest_dir')

    options = {'server': jira_server}
    jira = JIRA(options=options, basic_auth=(username, password))
    
    make_direcotry(dest_dir)

    for project in projects:
        project_dir = f"{dest_dir}/{project}"
        make_direcotry(project_dir)

        issues = jira.search_issues(f'project={project}', maxResults=10)
        
        issues_to_csv(issues=issues, dest_csv=f"{project_dir}/{project}_issues.csv")

        # TODO Replace column name from "customfield_XXX"

        download_attachments(issues=issues, dest_dir=project_dir)


