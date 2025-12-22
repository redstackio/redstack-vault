---
id: 7b99933a-748e-404c-9923-ec22b8c563cf
name: AWS-Console-Access-via-API-Keys
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:09.467624+00:00'
updated_at: '2023-04-10T20:20:55.843316+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
  - '[[sub-techniques/Private Keys|T1552.004 - Private Keys]]'
tags:
  - '[[tags/AWS - Gaining AWS Console Access via API Keys]]'
  - '[[tags/Cloud - AWS]]'
commands:
  - '[[commands/git-clone-aws-consoler]]'
  - '[[commands/run-aws-consoler-with-api-keys]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/aws-consoler]]'
validated: true
---

# AWS-Console-Access-via-API-Keys

## Summary

This procedure demonstrates how to gain access to the AWS Management Console using compromised or unsecured API keys (Access Key ID and Secret Access Key). By leveraging these credentials with the aws_consoler tool, an attacker can generate a temporary federated sign-in URL, bypassing direct console login requirements and enabling legitimate-appearing access to AWS resources for actions like resource creation, modification, or deletion.

## Description

In AWS environments, API keys provide programmatic access to services via the CLI or SDKs. If an attacker obtains valid API keys—often through misconfigurations, compromised user accounts, or unsecured storage—they can use tools like aws_consoler to convert these long-term credentials into a short-lived console session. This technique evades traditional MFA prompts for console access and mimics normal user behavior, making detection challenging. The procedure assumes the attacker has the keys but no prior console session. Once accessed, the console allows full interaction based on the key's permissions, potentially leading to data exfiltration, privilege escalation, or persistence via new resource creation. This is particularly effective in cloud environments where API keys are over-provisioned or stored in accessible locations like code repositories or configuration files.

## Requirements

1. Valid AWS Access Key ID and Secret Access Key with sufficient permissions for console access.
2. Python 3.x environment with pip for tool installation.
3. Network access to GitHub and AWS STS endpoints.
4. Git installed for repository cloning.

## Defense

- Rotate and secure API keys regularly, avoiding storage in code, logs, or public repositories; use AWS Secrets Manager or Parameter Store instead.
- Enable MFA for all IAM users and enforce short key rotation periods.
- Monitor CloudTrail logs for unusual STS AssumeRole or console federation events, and set up alerts for sign-ins from unfamiliar IPs or user agents.
- Implement least-privilege policies for API keys, restricting console access where possible.

## Objectives

1. Authenticate to the AWS console using API keys without direct credential entry.
2. Generate a temporary sign-in URL for browser-based console access.
3. Enable post-access actions like resource management or data exfiltration within the AWS environment.

## Instructions

### Step 1: Clone the aws_consoler Repository

**Context**: Obtain the aws_consoler tool from its GitHub repository. This tool uses Boto3 to create a federated session from API keys, generating a console login URL.

**Command** ([[commands/git-clone-aws-consoler]]):
```bash
git clone https://github.com/NetSPI/aws_consoler
```

> This command downloads the tool to a local directory named 'aws_consoler'. Verify the clone by checking for the presence of setup files like requirements.txt or setup.py. If the directory already exists, pull updates with 'git pull'.

### Step 2: Install Dependencies and Run aws_consoler

**Context**: After cloning, install the tool's dependencies (typically Boto3 and other Python libraries) and execute it with the compromised API keys to generate the console URL. The -v flag enables verbose logging for troubleshooting.

**Command** ([[commands/run-aws-consoler-with-api-keys]]):
```bash
aws_consoler -v -a $_ACCESS_KEY_ID -s $_SECRET_ACCESS_KEY
```

> Replace $_ACCESS_KEY_ID and $_SECRET_ACCESS_KEY with the actual values. The tool validates the credentials, creates a temporary federated session via AWS STS, and outputs a sign-in URL valid for a short duration (e.g., 15 minutes). Copy the URL and open it in a browser to access the console. Success is indicated by the URL generation and successful browser login without additional prompts.
