# Jira Download Tool

The **Jira Download Tool** is a utility designed to simplify the process of downloading attachments from Jira issues. Whether you're a developer, tester, or project manager, this tool can help you efficiently retrieve files associated with Jira tickets.

## Getting Started

These instructions will guide you through setting up the project on your local machine for development and testing purposes. If you're interested in deploying the tool to a live system, refer to the deployment section.

### Prerequisites

Before running the tool, ensure that you have the following software installed:

- Python 3.x

### Installing

Follow these steps to set up the development environment:

1. Clone this repository to your local machine.
2. Install the required Python dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```
3. Create an `.env` file and define the following variables
   - jira_server: Jira server url
   - username: Username to log in to jira
   - password: Password to log in to jira
   - projcts: List of target jira porject keys
   - dest_dir: Destination directory for dowonload
   - max_results: Max results to get issues  
  
   For example  
    ```
    jira_server = https://jira.atlassian.com
    username = hogehoge@fugafuga.com
    password = piyopiyo
    projects = PROJECT1,PROJECT2,PROJECT3
    dest_dir = downloads
    max_results = 10
    ```
### Running the Tool

Execute the following command to start the tool:
```
python main.py
```

It will then download all attachments associated with the specified issue.  
The destination directory structure is as follows.

```
.downloads 
    └ PROJECT1 
    │     └ PROJECT1_issues.tsv
    │     └ PROJECT1-001.zip
    │     └ PROJECT1-002.zip
    └ PROJECT2 
    │     └ PROJECT1_issues.tsv
    │     └ PROJECT2-001.zip
    │     └ PROJECT2-002.zip
    　　：
    　　：
```
**Attention!**  
Please ensure you have sufficient storage capacity because all attached files will be downloaded.


### License

Feel free to use this tool as you see fit! 
