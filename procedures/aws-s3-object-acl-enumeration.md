---
id: 39632370-6cb9-4871-8f9d-9b6eb7f12bde
name: aws-s3-object-acl-enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.093733+00:00'
updated_at: '2023-04-10T20:20:21.121110+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Getting ACL information about specific object]]'
commands:
  - '[[commands/aws-s3api-get-object-acl]]'
platforms:
  - AWS
tools: []
validated: true
---

# aws-s3-object-acl-enumeration

## Summary

This procedure enumerates the Access Control List (ACL) for a specific object in an AWS S3 bucket using the AWS CLI. It reveals the owner of the object and the permissions granted to various AWS accounts or groups, helping attackers identify misconfigurations that could allow unauthorized access to sensitive data.

## Description

In cloud environments, S3 buckets often store sensitive information like configuration files, backups, or application data. Attackers with valid AWS credentials can query object ACLs to discover which principals (users, roles, or groups) have read, write, or full control permissions. This information aids in planning data exfiltration, privilege escalation, or lateral movement by targeting over-privileged accounts. The procedure requires s3:GetObjectAcl permission on the target bucket and object. It is particularly useful in reconnaissance phases to map access controls without altering the environment.

## Requirements

1. Valid AWS credentials configured in the environment (e.g., via AWS CLI profile) with at least s3:GetObjectAcl permission on the target S3 bucket and object.
2. AWS CLI installed and accessible (version 1.x or 2.x).
3. Knowledge of the target S3 bucket name and the specific object key (path).

## Defense

- Implement least privilege access by restricting s3:GetObjectAcl permissions to only necessary roles and users.
- Enable S3 bucket logging and monitor CloudTrail for API calls to get-object-acl, alerting on anomalous access patterns.
- Use S3 bucket policies and ACLs to deny public or unintended access, and regularly audit permissions with tools like AWS IAM Access Analyzer.

## Objectives

1. Retrieve the ACL details for a specific S3 object to identify granted permissions.
2. Discover principals with access to potentially sensitive data in the bucket.
3. Assess misconfigurations that could enable unauthorized data access or exfiltration.

## Instructions

### Step 1: Retrieve Object ACL

**Context**: Use the AWS CLI to query the ACL of the target object. This step assumes AWS credentials are already configured (e.g., via `aws configure`). Replace placeholders with actual bucket and object details to fetch the permissions list.

**Command** ([[commands/aws-s3api-get-object-acl]]):
```bash
aws s3api get-object-acl --bucket $_BUCKET_NAME --key $_OBJECT_KEY
```

> This command returns JSON output detailing the object's owner (ID and display name) and a list of grants. Each grant specifies the grantee type (e.g., CanonicalUser, Group), grantee ID or URI, and permissions (READ, WRITE, FULL_CONTROL). Success is indicated by a 200 OK response without permission errors. If the object does not exist or access is denied, an error like AccessDenied will appear.
