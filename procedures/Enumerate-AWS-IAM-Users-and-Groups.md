---
id: 84be455c-dc7b-417c-98a9-04e24f38673d
name: Enumerate-AWS-IAM-Users-and-Groups
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:31.087577+00:00'
updated_at: '2023-05-25T20:07:05.535052+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[T1087.004]]'
sub_techniques: []
tags:
  - '[[tags/AWS]]'
  - '[[tags/Cloud]]'
  - iam
  - discovery
  - enumeration
commands:
  - '[[commands/aws-iam-list-users]]'
  - '[[commands/aws-iam-list-groups]]'
  - '[[commands/aws-iam-get-group-users]]'
tools:
  - '[[tools/AWS-CLI]]'
platforms:
  - Cloud
validated: true
---

# Enumerate-AWS-IAM-Users-and-Groups

## Summary

This procedure enumerates AWS Identity and Access Management (IAM) users, groups, and users within specific groups using AWS CLI commands. It is useful for discovering account structures in an AWS environment during reconnaissance or red team engagements, helping identify potential targets for privilege escalation or lateral movement.

## Description

In AWS environments, IAM controls access to resources. Enumerating users and groups reveals the organizational structure, privileged accounts, and potential weak points like over-privileged service accounts. This procedure assumes access to AWS credentials with read permissions on IAM (e.g., via assumed role or access keys). It uses the AWS CLI to query the IAM service, outputting JSON data that can be parsed for further analysis. This aligns with cloud discovery techniques, enabling attackers to map the attack surface without alerting if API calls are not monitored.

## Requirements

1. AWS CLI installed and configured with credentials that have IAM read permissions (e.g., `iam:ListUsers`, `iam:ListGroups`, `iam:GetGroup`).
2. Network access to AWS APIs (internet or VPC endpoint).
3. Basic familiarity with JSON output parsing (e.g., using `jq` for filtering).

## Defense

- Enable AWS CloudTrail logging for IAM API calls and monitor for unusual `ListUsers`, `ListGroups`, or `GetGroup` invocations from unexpected IPs or roles.
- Implement least privilege: Restrict IAM read access to only necessary roles.
- Use AWS GuardDuty or CloudWatch alarms to detect anomalous IAM enumeration patterns.

## Objectives

1. Identify all IAM users and their basic attributes to target high-privilege accounts.
2. Discover IAM groups to understand access groupings.
3. List users in specific groups to map memberships and potential escalation paths.
4. Collect data for offline analysis or integration into broader attack chains.

## Instructions

### Step 1: List All IAM Users

**Context**: This step retrieves a list of all IAM users in the account, providing usernames, ARNs, and creation dates. It helps identify admin users or service accounts for further targeting. Run this first to get an overview of user population.

**Command** ([[commands/aws-iam-list-users]]):
```bash
aws iam list-users
```

> This command queries the IAM service and returns a JSON array of users. Success is indicated by a non-empty `Users` array. Pipe to `jq` for readability: `aws iam list-users | jq '.Users[].UserName'` to list just usernames.

### Step 2: List All IAM Groups

**Context**: Enumerating groups reveals how access is organized, such as admin or developer groups. This is optional but useful for understanding policy attachments. Perform after user listing to correlate.

**Command** ([[commands/aws-iam-list-groups]]):
```bash
aws iam list-groups
```

> Outputs a JSON array of groups with names and ARNs. If no groups exist, returns an empty array. Use `jq '.Groups[].GroupName'` to extract names. This step has low detection risk if credentials are legitimate.

### Step 3: List Users in a Specific Group

**Context**: For a targeted group (e.g., "Admins"), this retrieves member users, helping pinpoint privileged accounts. Set the `$AWS_IAM_GROUP` variable to a group name from Step 2. This is conditional based on findings.

**Command** ([[commands/aws-iam-get-group-users]]):
```bash
AWS_IAM_GROUP="AdminGroup" && aws iam get-group --group-name $AWS_IAM_GROUP
```

> Returns JSON with group details and a `Users` array listing members. Verify success by checking for populated `Users`. If the group doesn't exist, it errors with `NoSuchEntity`. Use this to chain into credential dumping or role assumption.
