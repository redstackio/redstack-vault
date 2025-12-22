---
type: procedure
description: >-
  Enumerate IAM permissions for AWS credentials using the enumerate-iam tool to
  discover accessible services and actions.
verified: true
submitted: false
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
  - aws
  - iam
  - enumeration
  - cloud
commands:
  - '[[commands/git-clone-enumerate-iam-and-install-requirements]]'
  - '[[commands/run-enumerate-iam-permission-enumeration]]'
  - '[[commands/aws-directconnect-describe-locations]]'
  - '[[commands/aws-gamelift-list-builds]]'
  - '[[commands/aws-cloudformation-list-stack-sets]]'
  - '[[commands/aws-gamelift-describe-matchmaking-rule-sets]]'
  - '[[commands/aws-sqs-list-queues]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-IAM-Permissions-Enumeration

## Summary

The AWS IAM Permissions Enumeration procedure utilizes the open-source enumerate-iam tool to systematically test AWS API endpoints with provided credentials, revealing which services and actions the credentials can access. This helps attackers or red teamers assess the privilege level of compromised AWS keys without triggering excessive alerts, by attempting permission checks in a controlled manner.

## Description

This procedure targets AWS environments to map out IAM permissions for a given access key and secret key pair. The enumerate-iam tool, built on Python and boto3, iterates through hundreds of AWS API calls across services like GameLift, CloudFormation, DirectConnect, and SQS, logging which ones succeed to indicate granted permissions. It is particularly useful in post-compromise scenarios where credentials are obtained via phishing or misconfiguration, allowing discovery of exploitable resources like S3 buckets or EC2 instances. The tool avoids destructive actions, focusing on read-only discovery to minimize detection risk. Expected outcomes include a comprehensive report of accessible actions, enabling prioritization of further exploitation paths such as data exfiltration or lateral movement within the cloud environment.

## Requirements

1. Valid AWS access key ID and secret access key with unknown permissions to enumerate.
2. Python 3.6+ installed on the attacking machine.
3. Git installed for repository cloning.
4. Internet access to clone the GitHub repository and make AWS API calls.
5. Optional: AWS CLI installed for manual verification of specific permissions.

## Defense

- Implement least privilege principles by regularly auditing and scoping IAM policies to only necessary actions.
- Enable AWS CloudTrail logging for all regions and monitor for unusual API call patterns, such as rapid permission probes from unfamiliar IPs.
- Use AWS IAM Access Analyzer to identify and remediate overly permissive roles or policies.
- Rotate access keys immediately upon suspicion of compromise and enforce MFA for root and high-privilege accounts.

## Objectives

1. Identify all AWS services and specific API actions accessible with the provided credentials.
2. Determine the overall privilege level (e.g., read-only, administrative) to scope potential attack vectors.
3. Generate a permission report for planning subsequent cloud exploitation steps, such as resource enumeration or privilege escalation.

## Instructions

### Step 1: Clone Repository and Install Dependencies

**Context**: Obtain the enumerate-iam tool from GitHub and set up its Python dependencies to prepare for execution. This step ensures the script and required libraries (like boto3) are available locally.

**Command** ([[commands/git-clone-enumerate-iam-and-install-requirements]]):
```bash
git clone https://github.com/andresriancho/enumerate-iam.git
cd enumerate-iam
pip install -r requirements.txt
```

> This clones the repository using HTTPS for broader compatibility and installs dependencies via pip. If pip fails due to permissions, use a virtual environment with `python -m venv env` and `source env/bin/activate` (Linux/macOS) or `env\Scripts\activate` (Windows).

**Expected Output**: Successful clone shows repository files; pip output lists installed packages like boto3 without errors.

### Step 2: Execute Permission Enumeration

**Context**: Run the enumerate-iam script with the target AWS credentials to probe API permissions. The tool will attempt calls to various services and log successes, providing insight into credential capabilities.

**Command** ([[commands/run-enumerate-iam-permission-enumeration]]):
```bash
./enumerate-iam.py --access-key $_ACCESS_KEY --secret-key $_SECRET_KEY
```

> Replace $_ACCESS_KEY and $_SECRET_KEY with the actual credential values. Run from the cloned directory. The script outputs logs in real-time, indicating which API calls succeed (e.g., "gamelift.list_builds() worked!") and which fail due to insufficient permissions.

**Expected Output**: Console log starting with "Starting permission enumeration" followed by service-specific successes, such as:
```
2019-05-10 15:58:01,532 - 21345 - [INFO] get_account_authorization_details worked!
2019-05-10 15:58:26,709 - 21345 - [INFO] gamelift.list_builds() worked!
2019-05-10 15:58:26,850 - 21345 - [INFO] cloudformation.list_stack_sets() worked!
2019-05-10 15:58:26,982 - 21345 - [INFO] directconnect.describe_locations() worked!
2019-05-10 15:58:27,021 - 21345 - [INFO] gamelift.describe_matchmaking_rule_sets() worked!
2019-05-10 15:58:27,311 - 21345 - [INFO] sqs.list_queues() worked!
```
Parse the log for a summary of accessible permissions.

### Step 3: Verify Specific Permissions Manually

**Context**: If the tool indicates success for certain APIs, verify manually using AWS CLI equivalents to confirm access and retrieve detailed output. This step is optional for deeper inspection of specific services.

**Command** ([[commands/aws-gamelift-list-builds]]):
```bash
aws gamelift list-builds
```

> This lists GameLift builds if permitted, confirming the tool's finding.

**Expected Output**: JSON array of builds or empty if no builds exist, e.g., {"Builds": [{"BuildId": "build-123", "Name": "MyBuild"}]}. Errors like "AccessDenied" confirm denial.

Similarly, test other indicated permissions:

**Command** ([[commands/aws-cloudformation-list-stack-sets]]):
```bash
aws cloudformation list-stack-sets
```

**Command** ([[commands/aws-directconnect-describe-locations]]):
```bash
aws directconnect describe-locations
```

**Command** ([[commands/aws-gamelift-describe-matchmaking-rule-sets]]):
```bash
aws gamelift describe-matchmaking-rule-sets
```

**Command** ([[commands/aws-sqs-list-queues]]):
```bash
aws sqs list-queues
```

> Each command should succeed without errors if the tool reported access, providing JSON output with resource details.
