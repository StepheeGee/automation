# Project: DevOps

## Author: Stephanie G. Johnson

## Date: 02-01-2024

### Overview

**DevOps** is a set of practices that aims to automate and streamline the processes of software development (Dev) and IT operations (Ops). It focuses on improving collaboration and communication between development teams and operations teams to enhance the efficiency and quality of software delivery. 

**In this project**, we explore the use of **DevOps** in automation.

### Links and Resources

- [DevOps Wikipedia](https://en.wikipedia.org/wiki/DevOps)
- [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration)
- [Continuous Deployment](https://en.wikipedia.org/wiki/Continuous_deployment)

### Virtual Environment Setup

To set up the virtual environment for this project, follow these steps:

1. Install [Python](https://www.python.org/) on your machine if not already installed.
2. Clone this repository: `git clone <https://github.com/StepheeGee/automation.git>`
3. Navigate to the project directory: `cd DevOps`
4. Create a virtual environment: `python -m venv venv`
5. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
6. Install dependencies: `pip install -r requirements.txt`

### How to Run

To run the project, execute the following commands:

```bash
python3 automation/auto.py
```

### Usage

#### DevOps Automation Tools and Processes

This project implements DevOps practices through automation tools and processes. Developers and operators can leverage the following features:

1. **Create a Folder**: Automate the creation of a new folder with a specified name.

2. **Handle Deleted User**: Move a user's documents to a temporary folder, effectively deleting the user while maintaining a record of their documents. For example:

    ```bash
    # Example: Handle a deleted user
    python3 automation/auto.py
    ```

    During execution, the script will prompt for the user folder path and the temporary folder path.

3. **Sort Documents into Folders**: Go through a given folder and sort documents into additional folders based on their file type.

4. **Parse Log File for Errors and Warnings**: Move a log file into the logs folder and parse it for errors and warnings. Create separate log files for errors and warnings in a target directory.

5. **More Info Option**: Get detailed explanations for each automation option.


### Project Structure

The project structure includes:

```plaintext
automation/
|-- auto.py
|-- tests/
|   |-- test_auto.py
|-- user-docs/
|   |-- user1/
|       |-- document1.txt
|       |-- email1.mail
|       |-- log1.log.txt
|   |-- user2/
|       |-- document2.txt
|       |-- email2.mail
|       |-- log2.log.txt
|-- venv/
|-- requirements.txt
|-- README.md
```

### Contributions

I'd like to extend a special thanks to @ekowyawson and @LatherioK0818 for their contributions to this project.
