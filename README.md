# DevOps Health Check
A beginner project for local DevOps checks.

## Requirements
Linux with Bash, Git, and Python 3.

## Run the checks
Run these from the repository root:
    python3 health_check.py
    ./scripts/check_files.sh

## Output and limits
The Python script checks the filesystem containing the current directory.
It writes reports/health_report.txt and replaces that report on each run.
LOW means free space is below the example threshold in the script.
The scripts are educational checks; they do not send alerts.

Run the checks from the repository root.
