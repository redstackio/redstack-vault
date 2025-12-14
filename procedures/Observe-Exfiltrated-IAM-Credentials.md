---
id: proc-observe-iam-creds-001
tags:
  - aws
  - iam
  - credentials
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:24:08.297Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Observe-Exfiltrated-IAM-Credentials

## Summary

This procedure involves reviewing the output from a Groovy script execution in the Jenkins console to capture and validate the exfiltrated AWS IAM credentials, confirming successful data theft.

## Description

After executing a command to fetch AWS metadata, the console displays sensitive credential details in JSON format. This step focuses on observation and extraction, allowing attackers to use the credentials for AWS operations like assuming roles or accessing S3 buckets. It assumes prior access to the Jenkins console and targets AWS EC2 environments with metadata service enabled.

## Requirements

1. Successful execution of the prior exfiltration command
2. Access to the Jenkins console output
3. Optional: AWS CLI installed on attacker's machine for validation

## Defense

Defensive measures and detection strategies:

- Enable AWS CloudTrail logging for credential usage
- Rotate IAM roles and monitor for anomalous API calls
- Implement least-privilege policies to limit metadata exposure

## Objectives

1. Capture valid AWS credentials from console output
2. Verify credential usability
3. Prepare for AWS resource exploitation

## Instructions

### Step 1: Review Console Output

**Context**: Examine the results of the Groovy curl execution for the JSON credential dump.

No command; directly view and copy the output in the Jenkins console.

> Look for keys like AccessKeyId, SecretAccessKey, Token, and Expiration. Test with `aws sts get-caller-identity --access-key-id <id> --secret-access-key <key> --token <token>` if available.

### Step 2: Validate Credentials

**Context**: Confirm the credentials are active and tied to the expected IAM role.

Optional command (local AWS CLI):
```bash
aws sts get-caller-identity
```

> Set environment variables with the exfiltrated creds first. Success shows user/role ARN; failure indicates expiration or invalidity.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- aws
- iam
- credentials
