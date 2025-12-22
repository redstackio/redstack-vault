---
id: 469ce460-c32b-40ef-a201-0fff1e324c24
name: AWS-User-Policy-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:12.236626+00:00'
updated_at: '2023-04-10T20:20:29.222270+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - '[[techniques/Cloud Account Compromise|T1087.004 - Cloud Account]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Credential Access]]'
  - '[[tags/IAM Enumeration]]'
commands:
  - '[[commands/aws-iam-list-attached-user-policies]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-User-Policy-Enumeration

## Summary

AWS User Policy Enumeration involves using AWS CLI to list the IAM policies attached to a specific user, revealing the permissions and access levels granted to that user. This technique allows attackers with valid credentials to map out privilege boundaries, identify high-value accounts, and plan privilege escalation or lateral movement within the AWS environment.

## Description

In AWS, Identity and Access Management (IAM) controls access to services and resources through policies attached to users, groups, or roles. Attackers who have obtained initial credentials (e.g., via phishing or token theft) can enumerate these policies to understand the scope of access. For example, discovering policies that allow S3 bucket access or EC2 instance control can lead to data exfiltration or further compromise. This procedure requires authenticated access to the IAM service and is typically performed after initial access to an AWS account. It provides critical reconnaissance for cloud-based attacks, helping attackers avoid detection by sticking to legitimate API calls while gathering intel on potential escalation paths.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with at least read access to IAM (e.g., iam:ListAttachedUserPolicies permission).
2. AWS CLI installed and configured with the credentials (via `aws configure`).
3. Network access to AWS endpoints (no VPC restrictions blocking IAM API calls).
4. Knowledge of the target IAM user name.

## Defense

- Implement least privilege: Restrict IAM users to minimal policies needed for their roles.
- Enable AWS CloudTrail logging for IAM API calls and monitor for unusual enumeration patterns (e.g., frequent list-attached-user-policies requests).
- Use IAM Access Analyzer to review and audit policy attachments regularly.
- Require MFA for all IAM users and enforce short-lived credentials where possible.
- Set up AWS GuardDuty to detect reconnaissance activities in IAM.

## Objectives

1. Retrieve a list of all managed policies attached to a target IAM user.
2. Analyze policy details to identify accessible AWS resources and potential escalation vectors.
3. Support lateral movement by targeting users with elevated permissions.

## Instructions

### Step 1: List Attached Policies for the Target User

**Context**: This step uses the AWS CLI to query the IAM service for policies attached to a specific user. The command returns a JSON response detailing policy names, ARNs, and attachment status, which can be parsed to understand access rights. Run this from a machine with AWS CLI configured; if the user has no policies, an empty list is returned, indicating potential group or role-based access that may need further enumeration.

**Command** ([[commands/aws-iam-list-attached-user-policies]]):
```bash
aws iam list-attached-user-policies --user-name $_USER_NAME
```

> Replace $_USER_NAME with the target IAM username (e.g., 'admin-user'). The command authenticates via your configured credentials and queries the IAM API. If successful, it outputs a JSON array of attached policies. Pipe to `jq` for easier parsing if needed (e.g., `| jq '.AttachedPolicies[].PolicyName'`). If the user doesn't exist or you lack permissions, it returns an error like AccessDenied or NoSuchEntity.

### Step 2: Analyze the Output for Privilege Insights

**Context**: Review the JSON output to identify policy names and ARNs. Cross-reference with AWS policy documentation or use additional commands (like `aws iam get-policy-version`) to fetch full policy details. This helps pinpoint exploitable permissions, such as those allowing S3 reads or EC2 launches.

**Expected Output** (for Step 1):
```json
{
    "AttachedPolicies": [
        {
            "PolicyName": "AdministratorAccess",
            "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess"
        },
        {
            "PolicyName": "CustomS3ReadPolicy",
            "PolicyArn": "arn:aws:iam::123456789012:policy/CustomS3ReadPolicy"
        }
    ],
    "IsTruncated": false
}
```

> Success is indicated by a non-empty AttachedPolicies array or confirmation of no policies (for baseline assessment). Errors like "User admin-user is not authorized to perform: iam:ListAttachedUserPolicies" mean insufficient permissions—escalation may be needed first.
