---
id: c595e8c6-b062-4e3d-8749-d64447b6f88e
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.014046+00:00'
updated_at: '2023-04-10T20:20:58.720135+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
  - '[[techniques/Data from Cloud Storage|T1530 - Data from Cloud Storage]]'
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - '[[techniques/Internal Spearphishing|T1534 - Internal Spearphishing]]'
  - '[[techniques/Steal Web Session Cookie|T1539 - Steal Web Session Cookie]]'
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Tools]]'
commands:
  - '[[commands/clone-skyark-repository]]'
  - '[[commands/start-powershell-bypass-session]]'
  - '[[commands/import-skyark-powershell-module]]'
  - '[[commands/start-aws-stealth-scan]]'
  - '[[commands/download-awstealth-powershell-script]]'
  - '[[commands/scan-aws-shadow-admins]]'
  - '[[commands/clone-pacu-repository]]'
  - '[[commands/install-pacu-dependencies]]'
  - '[[commands/run-pacu-session]]'
  - '[[commands/set-pacu-aws-keys]]'
  - '[[commands/list-pacu-modules]]'
  - '[[commands/run-pacu-module-with-args]]'
  - '[[commands/run-pacu-module-in-regions]]'
  - '[[commands/download-bucket-finder-archive]]'
  - '[[commands/search-public-s3-buckets-default]]'
  - '[[commands/search-public-s3-buckets-region-ie]]'
  - '[[commands/download-public-s3-buckets-region-ie]]'
  - '[[commands/search-public-s3-buckets-with-log]]'
  - '[[commands/list-aws-s3-buckets-python]]'
  - '[[commands/install-prowler-dependencies]]'
  - '[[commands/clone-prowler-repository]]'
  - '[[commands/install-jq-package]]'
  - '[[commands/run-prowler-exclude-checks]]'
  - '[[commands/run-prowler-custom-profile-region]]'
  - '[[commands/run-prowler-assume-role]]'
  - '[[commands/install-cloudsplaining]]'
  - '[[commands/download-aws-iam-policies]]'
  - '[[commands/scan-aws-iam-for-privileges]]'
  - '[[commands/clone-scoutsuite-repository]]'
  - '[[commands/show-scoutsuite-help]]'
  - '[[commands/run-scoutsuite-aws-with-keys]]'
  - '[[commands/run-scoutsuite-azure-cli]]'
  - '[[commands/clone-s3-objects-check-repository]]'
  - '[[commands/create-activate-python-venv]]'
  - '[[commands/install-s3-objects-check-deps]]'
  - '[[commands/show-s3-objects-check-help]]'
  - '[[commands/run-s3-objects-check-profiles]]'
  - '[[commands/ec2-describe-instances-weirdaal]]'
  - '[[commands/lambda-get-account-settings-weirdaal]]'
  - '[[commands/lambda-get-function-weirdaal]]'
  - '[[commands/clone-cloudmapper-repository]]'
  - '[[commands/install-cloudmapper-dependencies]]'
  - '[[commands/enter-cloudmapper-pipenv-shell]]'
  - '[[commands/generate-cloudmapper-html-report]]'
  - '[[commands/generate-cloudmapper-iam-report]]'
  - '[[commands/audit-aws-account-cloudmapper]]'
  - '[[commands/collect-aws-metadata-cloudmapper]]'
  - '[[commands/find-aws-admins-roles-cloudmapper]]'
tools:
  - '[[tools/skyark]]'
  - '[[tools/pacu]]'
  - '[[tools/bucket-finder]]'
  - '[[tools/prowler]]'
  - '[[tools/principal-mapper]]'
  - '[[tools/scoutsuite]]'
  - '[[tools/s3-objects-check]]'
  - '[[tools/cloudsplaining]]'
  - '[[tools/weird-aal]]'
  - '[[tools/cloudmapper]]'
platforms:
  - AWS
validated: true
---

# AWS Cloud Security Assessment and Auditing

## Summary

This procedure performs a comprehensive security assessment and audit of an AWS cloud environment using open-source tools to identify misconfigurations, shadow administrators, public S3 buckets, IAM privilege issues, and potential exploitation paths. It combines reconnaissance, enumeration, and analysis techniques to evaluate the overall security posture, helping red teams or auditors discover vulnerabilities like over-privileged roles and exposed storage.

## Description

The procedure systematically audits an AWS account by leveraging tools such as SkyArk for shadow admin detection, Pacu for exploitation testing, Bucket Finder for public S3 discovery, Prowler for best practices compliance, Principal Mapper for IAM graphing, ScoutSuite for multi-cloud scanning, S3 Objects Check for permission evaluation, Cloudsplaining for least privilege violations, WeirdAAL for attack library simulations, and CloudMapper for environment mapping. It assumes access via AWS credentials and focuses on non-destructive enumeration to map risks without altering the environment. This is ideal for penetration testing AWS infrastructures to simulate attacker discovery and lateral movement paths.

## Requirements

1. AWS access credentials (access key ID and secret access key) with read-only permissions to IAM, S3, EC2, Lambda, and related services.
2. A Linux or macOS system with Git, Python 3, pip, PowerShell (for SkyArk), and AWS CLI installed.
3. Internet access for cloning repositories and downloading tools.
4. Sufficient disk space for reports and metadata collection.

## Defense

- Implement least privilege principles in IAM policies and regularly rotate credentials to limit shadow admin risks.
- Enable AWS CloudTrail and GuardDuty for logging and anomaly detection of enumeration activities.
- Use S3 bucket policies to restrict public access and monitor for unauthorized downloads.
- Conduct periodic audits with native AWS tools like IAM Access Analyzer to identify over-permissions.

## Objectives

1. Identify hidden privileged users (shadow admins) and IAM misconfigurations.
2. Enumerate and test for public S3 buckets and exploitable services.
3. Assess compliance against AWS security best practices.
4. Generate reports on potential privilege escalation paths and data exposure risks.
5. Collect metadata for further analysis of the cloud environment.

## Instructions

### Step 1: Discover Shadow Admins with SkyArk

**Context**: SkyArk stealthily scans the AWS environment to identify users and roles with administrative privileges that may not be obvious, helping uncover privilege escalation vectors.

First, clone the repository using [[commands/clone-skyark-repository]]:

```bash
git clone https://github.com/cyberark/SkyArk
```

> Clones the SkyArk tool for shadow admin detection.

Start a PowerShell session with bypass using [[commands/start-powershell-bypass-session]]:

```powershell
powershell -ExecutionPolicy Bypass -NoProfile
```

> Launches PowerShell without execution policy restrictions.

Import the module with [[commands/import-skyark-powershell-module]]:

```powershell
Import-Module .\SkyArk.ps1 -force
```

> Loads the SkyArk PowerShell module.

Start the stealth scan using [[commands/start-aws-stealth-scan]]:

```powershell
Start-AWStealth
```

> Initiates a low-profile scan to gather AWS permissions data.

Alternatively, download and execute the script directly with [[commands/download-awstealth-powershell-script]]:

```powershell
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/cyberark/SkyArk/master/AWStealth/AWStealth.ps1')
```

> Downloads and runs AWStealth in memory for evasion.

Finally, scan for shadow admins using [[commands/scan-aws-shadow-admins]]:

```powershell
Scan-AWShadowAdmins
```

> Outputs a list of discovered shadow administrators and their privileges.

### Step 2: Exploit Testing with Pacu

**Context**: Pacu is used to test for AWS-specific vulnerabilities by running modules that enumerate and exploit configurations like S3 access or EC2 permissions.

Clone the repository with [[commands/clone-pacu-repository]]:

```bash
git clone https://github.com/RhinoSecurityLabs/pacu
```

> Downloads the Pacu exploitation framework.

Install dependencies using [[commands/install-pacu-dependencies]]:

```bash
bash install.sh
```

> Sets up required Python packages.

Launch Pacu with [[commands/run-pacu-session]]:

```bash
python3 pacu.py
```

> Starts the interactive Pacu shell.

Set AWS keys using [[commands/set-pacu-aws-keys]]:

```bash
set_keys
```

> Configures AWS credentials for the session (or use swap_keys for switching).

List modules with [[commands/list-pacu-modules]]:

```bash
ls
```

> Displays available exploitation modules.

Run a module with arguments using [[commands/run-pacu-module-with-args]]:

```bash
run ec2_enum
```

> Executes a module like EC2 enumeration; add --keyword-arguments as needed.

Run in specific regions with [[commands/run-pacu-module-in-regions]]:

```bash
run s3__enum --regions us-east-1,us-west-2
```

> Targets modules to particular AWS regions.

### Step 3: Search for Public S3 Buckets with Bucket Finder

**Context**: This step identifies publicly accessible S3 buckets using a wordlist to brute-force potential names, revealing data exposure risks.

Download the tool archive using [[commands/download-bucket-finder-archive]]:

```bash
wget https://digi.ninja/files/bucket_finder_1.1.tar.bz2 -O bucket_finder_1.1.tar.bz2
```

> Fetches the Bucket Finder Ruby script.

Extract and prepare a wordlist (e.g., my_words).

Search default region with [[commands/search-public-s3-buckets-default]]:

```bash
./bucket_finder.rb my_words
```

> Brute-forces S3 bucket names in the default US region.

Search specific region with [[commands/search-public-s3-buckets-region-ie]]:

```bash
./bucket_finder.rb --region ie my_words
```

> Targets Ireland (eu-west-1) region for public buckets.

Download contents from found buckets using [[commands/download-public-s3-buckets-region-ie]]:

```bash
./bucket_finder.rb --download --region ie my_words
```

> Downloads files from accessible buckets.

Log results with [[commands/search-public-s3-buckets-with-log]]:

```bash
./bucket_finder.rb --log-file bucket.out my_words
```

> Saves output to a file for review.

### Step 4: List S3 Buckets Using Python Script

**Context**: Enumerate all S3 buckets in the account to identify storage resources and potential data sources.

Use the script [[codes/python-script-list-aws-s3-buckets]]:

```python
import boto3

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id='$_AWS_ACCESS_KEY_ID', aws_secret_access_key='$_AWS_SECRET_ACCESS_KEY', region_name='$_AWS_REGION')

try:
    # List all S3 buckets
    result = s3.list_buckets()
    print(result)
except Exception as e:
    print(e)
```

Execute via [[commands/list-aws-s3-buckets-python]]:

> Runs the script to output bucket names and owners.

### Step 5: Assess Best Practices with Prowler

**Context**: Prowler checks AWS services against CIS benchmarks and best practices to flag compliance issues.

Install dependencies with [[commands/install-prowler-dependencies]]:

```bash
pip install awscli ansi2html detect-secrets
```

> Prepares Python environment.

Clone repository using [[commands/clone-prowler-repository]]:

```bash
git clone https://github.com/toniblyx/prowler
```

> Downloads Prowler.

Install jq with [[commands/install-jq-package]]:

```bash
sudo apt install jq
```

> Adds JSON processing tool.

Run excluding checks with [[commands/run-prowler-exclude-checks]]:

```bash
./prowler -E check42,check43
```

> Audits while skipping specified checks.

Run custom profile in region with [[commands/run-prowler-custom-profile-region]]:

```bash
./prowler -p custom-profile -r us-east-1 -c check11
```

> Targets specific checks in a region.

Assume role with [[commands/run-prowler-assume-role]]:

```bash
./prowler -A 123456789012 -R ProwlerRole
```

> Uses STS assume-role for cross-account auditing.

### Step 6: Map IAM Permissions with Principal Mapper

**Context**: Graphs IAM policies to visualize privilege relationships and escalation paths.

Install via pip: `pip install principalmapper`

Create graph: `pmapper graph --create`

Visualize: `pmapper visualize --filetype png`

Analyze: `pmapper analysis --output-type text`

Query for privilege escalation: `pmapper query "preset privesc user/PowerUser"`

These are inline commands; refer to [[tools/principal-mapper]] for details.

### Step 7: Multi-Cloud Audit with ScoutSuite

**Context**: Performs non-intrusive scans of AWS and Azure configurations.

Clone with [[commands/clone-scoutsuite-repository]]:

```bash
git clone https://github.com/nccgroup/ScoutSuite
```

Show help with [[commands/show-scoutsuite-help]]:

```bash
python scout.py aws --help
```

Run AWS scan with [[commands/run-scoutsuite-aws-with-keys]]:

```bash
python scout.py aws --access-keys --access-key-id $_ACCESS_KEY_ID --secret-access-key $_SECRET_ACCESS_KEY --session-token $_SESSION_TOKEN
```

> Generates HTML report on findings.

For Azure, use [[commands/run-scoutsuite-azure-cli]]:

```bash
python scout.py azure --cli
```

> Assumes Azure CLI authentication.

### Step 8: Check S3 Object Permissions

**Context**: Evaluates effective permissions on S3 objects to detect public or over-permissive access.

Clone with [[commands/clone-s3-objects-check-repository]]:

```bash
git clone https://github.com/nccgroup/s3_objects_check
```

Create venv with [[commands/create-activate-python-venv]]:

```bash
python3 -m venv env && source env/bin/activate
```

Install deps with [[commands/install-s3-objects-check-deps]]:

```bash
pip install -r requirements.txt
```

Show help with [[commands/show-s3-objects-check-help]]:

```bash
python s3-objects-check.py -h
```

Run with profiles using [[commands/run-s3-objects-check-profiles]]:

```bash
python s3-objects-check.py -p whitebox-profile -e blackbox-profile
```

> Analyzes permissions using two profiles.

### Step 9: Scan IAM for Least Privilege Violations

**Context**: Identifies IAM policies that violate least privilege by allowing excessive actions.

Install with [[commands/install-cloudsplaining]]:

```bash
pip3 install --user cloudsplaining
```

Download policies with [[commands/download-aws-iam-policies]]:

```bash
cloudsplaining download --profile myawsprofile
```

> Fetches IAM config to local JSON.

Scan with [[commands/scan-aws-iam-for-privileges]]:

```bash
cloudsplaining scan --input-file default.json
```

> Outputs report on privilege risks.

### Step 10: Test AWS Attacks with WeirdAAL

**Context**: Simulates AWS API attacks using the Weird AWS Attack Library.

Run EC2 describe with [[commands/ec2-describe-instances-weirdaal]]:

```bash
python3 weirdAAL.py -m ec2_describe_instances -t demo
```

> Enumerates EC2 instances.

Get Lambda settings with [[commands/lambda-get-account-settings-weirdaal]]:

```bash
python3 weirdAAL.py -m lambda_get_account_settings -t demo
```

> Retrieves Lambda config.

Get function with [[commands/lambda-get-function-weirdaal]]:

```bash
python3 weirdAAL.py -m lambda_get_function -a 'MY_LAMBDA_FUNCTION','us-west-2' -t yolo
```

> Fetches specific Lambda details.

### Step 11: Analyze Environment with CloudMapper

**Context**: Collects and reports on AWS account structure, admins, and misconfigs.

Clone with [[commands/clone-cloudmapper-repository]]:

```bash
git clone https://github.com/duo-labs/cloudmapper.git
```

Install deps with [[commands/install-cloudmapper-dependencies]]:

```bash
sudo apt-get install autoconf automake libtool python3.7-dev python3-tk jq awscli
pipenv install --skip-lock
```

Enter shell with [[commands/enter-cloudmapper-pipenv-shell]]:

```bash
pipenv shell
```

Generate report with [[commands/generate-cloudmapper-html-report]]:

```bash
pipenv run python cloudmapper.py report
```

> Creates full HTML audit report.

IAM report with [[commands/generate-cloudmapper-iam-report]]:

```bash
pipenv run python cloudmapper.py iam_report
```

Audit with [[commands/audit-aws-account-cloudmapper]]:

```bash
pipenv run python cloudmapper.py audit
```

Collect metadata with [[commands/collect-aws-metadata-cloudmapper]]:

```bash
pipenv run python cloudmapper.py collect
```

Find admins with [[commands/find-aws-admins-roles-cloudmapper]]:

```bash
pipenv run python cloudmapper.py find_admins
```

> Identifies admin principals.
