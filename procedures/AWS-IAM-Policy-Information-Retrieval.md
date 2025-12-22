---
id: 3a361207-6eeb-4937-a163-8043d40ec9d6
name: AWS-IAM-Policy-Information-Retrieval
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.739566+00:00'
updated_at: '2023-04-10T20:20:09.051857+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Accessing more credentials]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Persistence & Backdooring]]'
  - '[[tags/Retrieving information about an specific policy]]'
commands:
  - '[[commands/aws-iam-get-policy]]'
  - '[[commands/aws-iam-get-policy-version]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-IAM-Policy-Information-Retrieval

## Summary

This procedure retrieves metadata and the full policy document for a specific IAM policy in an AWS account using the AWS CLI. It enables discovery of permissions granted by the policy, helping attackers map access rights, identify overly permissive configurations, and plan privilege escalation in a compromised AWS environment.

## Description

IAM policies in AWS define permissions for identities like users, groups, and roles. Once an attacker has obtained AWS credentials (e.g., via initial access or credential dumping), retrieving policy information allows them to understand the scope of permissions, such as access to S3 buckets, EC2 instances, or other services. This discovery technique reveals potential abuse vectors, like service roles with excessive rights. The procedure uses standard IAM API calls via AWS CLI, assuming the credentials have iam:GetPolicy and iam:GetPolicyVersion permissions. It targets managed or inline policies by ARN and is applicable in post-exploitation scenarios within AWS.

## Requirements

1. Valid AWS credentials configured in the environment (e.g., via AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY) with at least iam:GetPolicy and iam:GetPolicyVersion permissions.
2. AWS CLI version 2 installed and accessible in the PATH.
3. The ARN of the target IAM policy (e.g., arn:aws:iam::123456789012:policy/MyPolicy).
4. Network access to AWS IAM endpoints (typically over HTTPS on port 443).

## Defense

- Enforce least privilege by regularly auditing IAM policies with tools like IAM Access Analyzer.
- Enable AWS CloudTrail logging for IAM API calls to detect unauthorized GetPolicy or GetPolicyVersion requests.
- Implement credential rotation and monitor for anomalous API activity using Amazon GuardDuty.
- Use AWS Organizations SCPs to restrict IAM actions across accounts.

## Objectives

1. Retrieve metadata for a specific IAM policy to confirm its existence and attachment details.
2. Extract the policy document to analyze granted permissions and identify escalation paths.
3. Understand the AWS environment's access controls for further exploitation planning.

## Instructions

### Step 1: Retrieve IAM Policy Metadata

**Context**: First, query the IAM service to get basic metadata about the policy, including its default version ID. This step verifies the policy exists and provides the version needed for retrieving the full document. It helps in scoping the policy's attachments and update history without exposing the full permissions yet.

**Command** ([[commands/aws-iam-get-policy]]):
```bash
aws iam get-policy --policy-arn $_POLICY_ARN
```

> Run this command with the target policy ARN substituted for $_POLICY_ARN. If the policy exists and credentials are sufficient, it returns JSON metadata. Use the "DefaultVersionId" from the output in the next step. If access is denied, credentials lack iam:GetPolicy permission.

Expected Output:
```json
{
    "Policy": {
        "PolicyName": "MyPolicy",
        "PolicyId": "ANPAJKWEXAMPLE",
        "Arn": "arn:aws:iam::123456789012:policy/MyPolicy",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 1,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "Description": "Sample policy description",
        "CreateDate": "2015-03-09T18:43:32.752Z",
        "UpdateDate": "2015-03-09T18:43:32.752Z"
    }
}
```

### Step 2: Retrieve the Full Policy Document

**Context**: Using the version ID from Step 1, fetch the actual policy document, which is a JSON structure detailing the permissions (e.g., Allow/Deny statements for actions like s3:GetObject). Analyze this for broad permissions like "*" actions or access to sensitive resources, which could enable lateral movement or data exfiltration.

**Command** ([[commands/aws-iam-get-policy-version]]):
```bash
aws iam get-policy-version --policy-arn $_POLICY_ARN --version-id $_VERSION_ID
```

> Substitute $_POLICY_ARN with the policy ARN and $_VERSION_ID with the default version (e.g., "v1") from Step 1. This returns the policy's JSON document. If the version doesn't exist, check the metadata again. Parse the output to map permissions to MITRE techniques like privilege escalation (TA0004).

Expected Output:
```json
{
    "PolicyVersion": {
        "Document": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::my-bucket/*"
                }
            ]
        },
        "VersionId": "v1",
        "IsDefaultVersion": true,
        "CreateDate": "2015-03-09T18:43:32.752Z"
    }
}
```
