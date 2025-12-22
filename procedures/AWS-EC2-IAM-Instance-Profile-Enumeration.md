---
id: 54149739-f9b8-4a7a-9b80-95ae0d42c8d3
name: AWS-EC2-IAM-Instance-Profile-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.298595+00:00'
updated_at: '2023-04-10T20:20:19.423372+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Dashboard|T1538 - Cloud Service Dashboard]]'
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Listing roles of an instance]]'
commands:
  - '[[commands/aws-ec2-describe-iam-instance-profile-associations]]'
tools:
  - '[[tools/AWS-CLI]]'
platforms:
  - AWS
  - Cloud
validated: true
---

# AWS-EC2-IAM-Instance-Profile-Enumeration

## Summary

This procedure enumerates the IAM roles attached to AWS EC2 instances using the AWS CLI, providing insight into the permissions granted to applications running on those instances. It helps attackers identify overly permissive roles for further exploitation in the AWS environment, while defenders can use it to audit and remediate access controls.

## Description

AWS EC2 instances often use IAM instance profiles to attach roles that grant permissions to services like S3, RDS, or Lambda without embedding long-term credentials in the application code. Enumerating these profiles reveals the scope of access an instance has, such as read/write to buckets or administrative privileges on other resources. This technique leverages the AWS metadata service or CLI queries to list associations without requiring direct instance access, assuming the attacker has valid AWS credentials with EC2 describe permissions. In a red team scenario, this discovery aids in planning lateral movement or privilege escalation; for blue teams, it highlights misconfigurations like broad role policies. The procedure focuses on the `describe-iam-instance-profile-associations` API call, which returns details on instance-profile links, including ARNs and states.

## Requirements

1. Valid AWS credentials (access key and secret key) with at least `ec2:DescribeIamInstanceProfileAssociations` permission.
2. AWS CLI installed and configured with the target account's credentials via `aws configure`.
3. Network access to AWS APIs (no direct EC2 instance access needed).
4. Knowledge of target instance IDs or association IDs for targeted enumeration.

## Defense

- Restrict access to the AWS IAM and EC2 services to only authorized users and roles using IAM policies.
- Implement the principle of least privilege by assigning minimal permissions to EC2 instance roles and regularly auditing them with AWS IAM Access Analyzer.
- Monitor AWS CloudTrail logs for API calls like `DescribeIamInstanceProfileAssociations`, setting up alerts for unusual queries from compromised credentials.
- Enable AWS Config rules to detect and notify on instances with attached profiles that exceed defined permission boundaries.

## Objectives

1. Identify the IAM roles and instance profiles attached to specific EC2 instances.
2. Gain insight into the permissions and access levels the instance has to other AWS services.
3. Assess potential attack paths based on discovered role privileges for further exploitation or remediation.

## Instructions

### Step 1: Configure AWS CLI and Verify Credentials

**Context**: Ensure the AWS CLI is set up with credentials that have the necessary EC2 permissions. This step verifies authentication before querying instance profiles.

**Command** ([[commands/aws-ec2-describe-iam-instance-profile-associations]]):
Use the AWS CLI to test basic access, but the main command is prepared here.

First, run `aws sts get-caller-identity` to confirm credentials:

```bash
aws sts get-caller-identity
```

> This command authenticates and returns the account ID, user ARN, and session details. If it fails with an access denied error, update credentials or permissions.

### Step 2: Enumerate IAM Instance Profile Associations

**Context**: Query the AWS EC2 API to list associations between instances and IAM profiles. Specify instance IDs to target specific EC2 instances; without them, it lists all associations in the region.

**Command** ([[commands/aws-ec2-describe-iam-instance-profile-associations]]):
```bash
aws ec2 describe-iam-instance-profile-associations --instance-ids $_INSTANCE_ID
```

> Replace `$_INSTANCE_ID` with the target EC2 instance ID (e.g., i-1234567890abcdef0). This retrieves JSON output showing association IDs, instance IDs, IAM instance profile ARNs, and association states (e.g., "associated"). If multiple instances, use comma-separated IDs or omit for all. Decision point: If no associations return, the instance may not have a profile attached—proceed to check metadata service on the instance if accessible.

### Step 3: Parse and Analyze Output for Role Details

**Context**: Review the JSON response to extract role ARNs and states. Use jq for parsing if needed, or manually inspect for privilege indicators like admin roles.

**Command** ([[commands/aws-ec2-describe-iam-instance-profile-associations]]):
Pipe the output to jq for filtering:

```bash
aws ec2 describe-iam-instance-profile-associations --instance-ids $_INSTANCE_ID | jq '.IamInstanceProfileAssociations[] | {InstanceId: .InstanceId, Arn: .IamInstanceProfile.Arn, State: .State}'
```

> Expected: Filtered JSON with instance ID, profile ARN (e.g., arn:aws:iam::123456789012:instance-profile/MyRole), and state. If the ARN indicates a high-privilege role (e.g., containing "admin"), flag for escalation potential. Success: Associations listed without API errors.
