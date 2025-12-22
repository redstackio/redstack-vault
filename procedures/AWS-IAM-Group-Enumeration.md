---
id: 42de6dfd-2301-45b7-98d2-33f554cc9932
name: AWS-IAM-Group-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.115704+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - aws-iam
  - discovery
  - enumeration
  - cloud-aws
commands:
  - '[[commands/aws-iam-list-groups]]'
platforms:
  - AWS
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# AWS-IAM-Group-Enumeration

## Summary

This procedure enumerates all IAM groups within an AWS account using the AWS CLI, allowing attackers to map the permission structure and identify groups with elevated privileges for further targeting in a discovery phase.

## Description

In an AWS environment, IAM groups organize users and define shared permissions via attached policies. Enumerating these groups reveals the account's access model, highlighting administrative or privileged groups that could lead to lateral movement or privilege escalation. This technique requires valid AWS credentials with permissions to call the IAM ListGroups API. It is commonly used during initial reconnaissance after obtaining credentials, helping attackers prioritize high-value targets like groups with full access to S3 buckets or EC2 instances. The output provides group names, ARNs, and creation dates, which can inform subsequent enumeration of users or policies.

## Requirements

1. Valid AWS API credentials with iam:ListGroups permission (e.g., via access key ID and secret access key).
2. AWS CLI installed and configured on the attacker's system.
3. Network access to AWS endpoints (no specific ports beyond standard HTTPS/443).

## Defense

- Rotate AWS credentials regularly and use temporary credentials with short lifespans.
- Implement least privilege by limiting iam:ListGroups access to trusted roles only.
- Monitor CloudTrail logs for unusual IAM API calls, such as ListGroups from unknown IPs or excessive frequency.
- Enable AWS GuardDuty for anomaly detection on IAM enumeration patterns.

## Objectives

1. List all IAM groups in the target AWS account.
2. Understand the permission hierarchy to identify privileged groups.
3. Gather metadata (ARNs, creation dates) for planning further discovery attacks.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure the AWS CLI is installed and credentials are set up to authenticate API calls without errors.

Install or verify AWS CLI using [[tools/aws-cli]]. Configure credentials with `aws configure` if not already done, providing access key, secret key, region, and output format (json).

**Expected Output**: Successful configuration confirmation, e.g., no errors on `aws sts get-caller-identity`.

### Step 2: Test IAM Permissions

**Context**: Confirm the credentials have the necessary iam:ListGroups permission before proceeding to avoid alerting defenses.

Run a test command like `aws iam get-account-summary` to validate access.

**Expected Output**: JSON response with account details if permissions are sufficient.

### Step 3: Enumerate IAM Groups

**Context**: Execute the core enumeration to retrieve the list of all IAM groups, providing insight into the account's structure.

**Command** ([[commands/aws-iam-list-groups]]):
```bash
aws iam list-groups
```

> This command queries the IAM service and returns a JSON array of groups. Each entry includes GroupName, GroupId, Arn, and CreateDate. If no groups exist, it returns an empty list. Pipe to `jq` for formatting if needed: `aws iam list-groups | jq '.Groups[] | {GroupName, Arn}'`.

**Expected Output**:
```json
{
    "Groups": [
        {
            "GroupName": "Admins",
            "GroupId": "AIDACKCEVSQ6C2EXAMPLE",
            "Arn": "arn:aws:iam::123456789012:group/Admins",
            "CreateDate": "2015-03-09T18:37:00Z"
        }
    ]
}
```

### Step 4: Analyze Output for High-Value Targets

**Context**: Review the results to identify groups likely to have elevated permissions, such as those named 'Admin' or 'Root'.

Manually inspect the JSON output or use tools like `jq` to filter: `aws iam list-groups | jq '.Groups[] | select(.GroupName | contains("Admin"))'`.

**Expected Output**: Filtered list of potentially privileged groups.

**Success Indicators**:
- JSON response contains group details without permission denied errors.
- At least one group is identified for follow-up enumeration (e.g., list users in group).
