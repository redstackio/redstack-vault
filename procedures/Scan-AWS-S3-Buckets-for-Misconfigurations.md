---
id: d22e18bc-c44e-41e2-bd19-96d320f220ab
name: Scan-AWS-S3-Buckets-for-Misconfigurations
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.864278+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Searching for open buckets]]'
commands:
  - '[[commands/git-clone-zeus-repo]]'
  - '[[commands/pip-install-zeus-requirements]]'
  - '[[commands/python-zeus-s3-scanner]]'
platforms:
  - AWS
  - Linux
tools:
  - '[[tools/Zeus-AWS-Auditor]]'
validated: true
---

# Scan-AWS-S3-Buckets-for-Misconfigurations

## Summary

This procedure uses the Zeus AWS Auditing & Hardening Tool to scan for misconfigured S3 buckets in an AWS environment, identifying publicly accessible buckets that could expose sensitive data such as credentials, customer information, or intellectual property.

## Description

Misconfigured S3 buckets are a common entry point for attackers due to overly permissive IAM policies or public ACLs. This procedure leverages the open-source Zeus tool to enumerate all S3 buckets associated with provided AWS credentials and check their access permissions. It can be executed from an external system with internet access or from within an AWS environment. The scan reports vulnerabilities like public read/write access, providing remediation recommendations. This technique aligns with cloud service discovery to map and exploit infrastructure weaknesses.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with permissions to list and describe S3 buckets (e.g., s3:ListBucket, s3:GetBucketAcl).
2. Python 3.x installed on a Linux or macOS system.
3. Git for cloning the repository.
4. Network access to AWS APIs and GitHub.
5. Optional: AWS CLI configured for credential testing.

## Defense

- Implement least-privilege IAM policies to restrict S3 access.
- Enable S3 Block Public Access at the account and bucket levels.
- Monitor S3 access logs via CloudTrail for anomalous API calls (e.g., ListBuckets from unknown IPs).
- Use AWS Config rules to alert on public bucket configurations.
- Regularly audit bucket policies with tools like Prowler or Scout Suite.

## Objectives

1. Enumerate all S3 buckets in the target AWS account.
2. Identify buckets with public read or write permissions.
3. Report misconfigurations for potential data exfiltration or unauthorized uploads.
4. Gather evidence of exposed sensitive data.

## Instructions

### Step 1: Clone the Zeus Repository

**Context**: Download the Zeus tool from its GitHub repository to obtain the S3 scanner functionality. This step ensures you have the latest version of the auditing scripts.

**Command** ([[commands/git-clone-zeus-repo]]):
```bash
git clone https://github.com/DenizParlak/Zeus.git
```

> This command clones the repository into a local directory named 'Zeus'. Navigate into the directory with `cd Zeus` after execution. Expected output includes progress messages ending with 'Cloning into 'Zeus'...'. Verify success by checking for the presence of `zeus.py` in the directory.

### Step 2: Install Required Python Libraries

**Context**: Install dependencies needed for Zeus, including AWS SDK (boto3) and other libraries for API interactions. This prepares the environment to authenticate with AWS and perform bucket scans.

**Command** ([[commands/pip-install-zeus-requirements]]):
```bash
pip3 install -r requirements.txt
```

> Run this from within the Zeus directory. It installs packages like boto3 for AWS interactions. Expected output lists installed packages without errors. If using a virtual environment, activate it first with `python3 -m venv venv && source venv/bin/activate`.

### Step 3: Run the S3 Bucket Scanner

**Context**: Execute the Zeus S3 scanner with AWS credentials to enumerate and check bucket permissions. This step performs the core discovery, flagging public or misconfigured buckets.

**Command** ([[commands/python-zeus-s3-scanner]]):
```bash
python3 zeus.py --scanner s3 --access-key $_AWS_ACCESS_KEY --secret-key $_AWS_SECRET_KEY
```

> Provide your AWS credentials as parameters. The tool lists all buckets and tests access levels. Expected output includes a report of buckets with details like 'Public Read Access: Yes' for vulnerable ones, along with remediation suggestions. If no credentials are provided, it may prompt interactively. Review the output for any accessible buckets and note ARNs for follow-up exfiltration.
