---
id: b5deba00-ca85-49f4-99f5-1e7f1960f6a3
name: AWS-S3-Bucket-ACL-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.999424+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Getting information about a specific bucket]]'
commands:
  - '[[commands/aws-s3api-get-bucket-acl]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-S3-Bucket-ACL-Enumeration

## Summary

This procedure retrieves the Access Control List (ACL) for a specified AWS S3 bucket using the AWS CLI, allowing attackers to identify permissions granted to users and groups. It is useful in cloud discovery phases to map access rights and identify misconfigurations that could enable further unauthorized access or data exfiltration.

## Description

In an attack scenario, enumerating S3 bucket ACLs helps discover overly permissive settings, such as public read/write access or grants to unintended principals. This technique targets AWS environments where credentials with S3 read permissions are compromised. The procedure outputs a JSON structure detailing the bucket owner, grantees (AWS accounts, users, or groups), and their permissions (READ, WRITE, FULL_CONTROL). It requires authenticated access to the S3 service and is typically executed after initial credential acquisition. Expected outcomes include visibility into bucket security posture, which can inform lateral movement or persistence strategies in cloud infrastructures.

## Requirements

1. Valid AWS credentials with at least 's3:GetBucketAcl' permission on the target bucket.
2. AWS CLI installed and configured with the credentials (via 'aws configure' or environment variables).
3. Network access to AWS endpoints (no VPC restrictions blocking S3 API calls).
4. Knowledge of the target S3 bucket name.

## Defense

- Implement least privilege access: Use IAM policies to restrict 's3:GetBucketAcl' to necessary roles only.
- Enable S3 access logging and monitor CloudTrail for API calls to 'GetBucketAcl' from unusual sources.
- Use bucket policies and ACLs to deny unauthorized enumeration, and regularly audit permissions with tools like AWS Config.
- Rotate credentials frequently and use MFA for IAM users with S3 access.

## Objectives

1. Retrieve and analyze the ACL permissions for a specific S3 bucket to identify misconfigurations.
2. Gather intelligence on bucket ownership and grantee access for potential exploitation.
3. Validate assumptions about bucket security in reconnaissance or post-compromise phases.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure your AWS credentials are active and have the necessary permissions before attempting enumeration. This prevents errors due to misconfiguration.

Run the AWS CLI version check and test basic S3 access if needed.

> Use [[commands/aws-configure-list]] or simply proceed if already set up.

### Step 2: Retrieve S3 Bucket ACL

**Context**: Execute the core enumeration command to fetch the ACL details. This step directly accomplishes the objective by querying the S3 API for permission grants.

**Command** ([[commands/aws-s3api-get-bucket-acl]]):
```bash
aws s3api get-bucket-acl --bucket $_BUCKET_NAME
```

> This command queries the S3 service for the ACL of the specified bucket. Replace $_BUCKET_NAME with the actual bucket name (e.g., 'my-sensitive-bucket'). The output is a JSON object; pipe to 'jq' for readability if available (e.g., | jq '.'). If successful, it reveals grantees and permissions without errors. Decision point: If access denied, the credentials lack permission—escalation or alternative creds may be needed.
