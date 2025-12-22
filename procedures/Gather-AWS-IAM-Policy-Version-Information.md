---
id: de07cfab-8454-4c59-bc4b-2b14c3d11d5e
name: Gather-AWS-IAM-Policy-Version-Information
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:13.486198+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Discovery]]'
  - '[[tags/IAM]]'
  - '[[tags/Privilege Escalation]]'
commands:
  - '[[commands/aws-iam-get-policy-version]]'
  - '[[commands/curl-retrieve-ec2-instance-id]]'
platforms:
  - AWS
tools: []
validated: true
---

# Gather-AWS-IAM-Policy-Version-Information

## Summary

This procedure retrieves detailed information about a specific version of an AWS IAM policy, including its permissions and document contents. It is useful for discovering privilege escalation opportunities by analyzing policy attachments and permissions associated with IAM roles or users, particularly in cloud environments where over-privileged policies may exist.

## Description

In AWS environments, IAM policies define permissions for users, groups, and roles. Gathering information on a specific policy version allows attackers or red teamers to understand the scope of access granted, such as EC2 instance management or S3 bucket access, which can reveal paths for lateral movement or escalation. This procedure uses the AWS CLI to query policy details and, if operating from within an EC2 instance, retrieves the instance ID via metadata service for contextual awareness, such as identifying the current instance's profile attachments. The technique aligns with cloud service discovery by enumerating configuration details without direct console access, assuming valid credentials with iam:GetPolicyVersion permission.

## Requirements

1. Valid AWS credentials with at least iam:GetPolicyVersion permission.
2. AWS CLI installed and configured with the target account's access keys or role.
3. Knowledge of the target IAM policy ARN and version ID (obtainable via prior enumeration like aws iam list-policies).
4. If retrieving EC2 instance ID, execution must occur from within a running EC2 instance with instance metadata access enabled.

## Defense

- Implement least privilege principles by regularly auditing and minimizing IAM policy permissions.
- Enable AWS CloudTrail for logging IAM API calls, including GetPolicyVersion, to detect unauthorized discovery attempts.
- Use IAM Access Analyzer to identify and alert on unexpected policy access patterns.
- Restrict metadata service access on EC2 instances using Instance Metadata Service Version 2 (IMDSv2) to prevent unauthorized instance information retrieval.

## Objectives

1. Retrieve and analyze the JSON document of a specific IAM policy version to identify granted permissions.
2. Understand potential privilege escalation vectors, such as overly permissive actions like iam:AttachRolePolicy.
3. Gather contextual instance information if operating within EC2 to map policy attachments to resources.

## Instructions

### Step 1: Retrieve IAM Policy Version Details

**Context**: This step queries AWS for the specified policy version, returning its document, creation date, and status. Use this to inspect permissions for exploitation opportunities, such as identifying admin-level actions.

**Command** ([[commands/aws-iam-get-policy-version]]):
```bash
aws iam get-policy-version --policy-arn arn:aws:iam::123456789012:policy/MyPolicy --version-id v1
```

> Replace the policy ARN and version ID with target values. The command outputs a JSON response with the policy document under 'PolicyVersion.Document', detailing statements, actions, and resources. If the version is the default, it includes an 'IsDefaultVersion' flag.

### Step 2: Retrieve Current EC2 Instance ID for Contextual Mapping

**Context**: If executing from an EC2 instance, obtain the instance ID to correlate with IAM role attachments or policy scoping. This helps determine if the current instance's profile grants access to the queried policy's permissions.

**Command** ([[commands/curl-retrieve-ec2-instance-id]]):
```bash
curl http://169.254.169.254/latest/meta-data/instance-id
```

> This queries the EC2 instance metadata service (IMDS). Success returns a string like 'i-1234567890abcdef0'. Use this ID with commands like aws ec2 describe-instances to check attached roles and policies. Failure indicates no metadata access or non-EC2 environment.
