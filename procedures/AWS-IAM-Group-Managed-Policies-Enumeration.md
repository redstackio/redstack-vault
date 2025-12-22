---
id: 86b36d12-a435-45c5-8618-b46b95af71cb
name: AWS-IAM-Group-Managed-Policies-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.139389+00:00'
updated_at: '2023-04-10T20:19:46.663635+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Application Access Token|T1527 - Application Access Token]]'
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/2. Enumerating Groups IAM]]'
  - '[[tags/Cloud - AWS]]'
  - >-
    [[tags/Listing all managed policies that are attached to the specified IAM
    Group]]
commands:
  - '[[commands/aws-iam-list-attached-group-policies]]'
platforms:
  - AWS
tools: []
validated: true
---

# AWS-IAM-Group-Managed-Policies-Enumeration

## Summary

This procedure enumerates all managed policies attached to a specified IAM group in AWS, revealing the permissions granted to group members. It uses the AWS CLI to query the ListAttachedGroupPolicies API, helping attackers identify privilege escalation opportunities or lateral movement paths by understanding group-level access to AWS resources.

## Description

AWS Identity and Access Management (IAM) allows secure management of access to AWS services and resources through groups that contain users. This procedure targets the enumeration of managed policies attached to a specific IAM group, providing details on policy names, ARNs, and attachment information. In an attack scenario, this discovery technique can map out permissions for reconnaissance, enabling further actions like privilege escalation if overly permissive policies are found. It requires AWS credentials with permission to call the ListAttachedGroupPolicies API and operates in cloud environments where IAM is configured. Expected outcomes include a JSON list of attached policies, which can be parsed to assess access scopes such as read/write on S3 buckets or EC2 instances.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) configured in the environment or via AWS CLI profiles.
2. Permissions to call the `iam:ListAttachedGroupPolicies` API action.
3. AWS CLI installed and accessible (version 1.x or 2.x).
4. Network access to AWS endpoints (no VPC restrictions blocking IAM API calls).

## Defense

Defensive measures and detection strategies:

- Implement least privilege by ensuring IAM groups have only necessary policies attached and regularly audit attachments using AWS IAM Access Analyzer.
- Enable AWS CloudTrail logging for IAM API calls and monitor for unusual `ListAttachedGroupPolicies` invocations via Amazon GuardDuty or custom CloudWatch alarms.
- Use IAM policies to deny listing actions for non-administrative roles and enforce multi-factor authentication (MFA) for IAM management.

## Objectives

1. Identify all managed policies attached to a specific IAM group to understand granted permissions.
2. Map permissions for group members to detect potential over-privileging or escalation vectors.
3. Gather intelligence on AWS resource access for lateral movement or persistence planning.

## Instructions

### Step 1: Configure AWS CLI and Enumerate Group Policies

**Context**: Ensure AWS credentials are set up, then use the AWS CLI to query attached policies for the target group. This step retrieves policy details in JSON format, allowing analysis of permissions like those for S3, EC2, or other services.

**Command** ([[commands/aws-iam-list-attached-group-policies]]):
```bash
aws iam list-attached-group-policies --group-name $_GROUP_NAME
```

> This command calls the IAM API to list policies. Replace `$_GROUP_NAME` with the actual group name (e.g., "Admins"). If the group has no policies, it returns an empty list. Pipe output to `jq` for parsing if needed: `| jq '.AttachedPolicies[].PolicyName'`. Decision point: If no policies are returned, the group may use inline policies—consider enumerating users separately.

### Step 2: Parse and Analyze Output

**Context**: Review the JSON response to extract policy ARNs and names. This helps identify high-privilege policies (e.g., AdministratorAccess) for further exploitation.

**Command** ([[commands/aws-iam-list-attached-group-policies]]):
```bash
aws iam list-attached-group-policies --group-name $_GROUP_NAME | jq '.AttachedPolicies[] | {PolicyName: .PolicyName, PolicyArn: .PolicyArn}'
```

> The `jq` filter extracts key fields. Expected: Structured output showing policy details. If `jq` is unavailable, use Python or manual inspection. Verify success by checking for non-empty policy lists indicating group access levels.
