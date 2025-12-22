---
id: 396b262e-d50e-4ea5-9e54-8d5dfee7ee5e
name: List-Contents-of-Misconfigured-AWS-S3-Bucket
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:10.593484+00:00'
updated_at: '2023-04-10T20:20:36.861164+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/Cloud-Service-Discovery|T1526 - Cloud Service Discovery]]'
  - '[[techniques/Data-from-Cloud-Storage|T1530 - Data from Cloud Storage]]'
sub_techniques: []
tags:
  - '[[tags/5. Exploitation Scenario]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Listing a restricted resource (Example S3)]]'
  - aws
  - s3
  - misconfiguration
commands:
  - '[[commands/aws-s3-list-bucket-contents]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/aws-cli]]'
validated: true
---

# List-Contents-of-Misconfigured-AWS-S3-Bucket

## Summary

This procedure exploits misconfigured access controls on an AWS S3 bucket to list its contents, potentially exposing sensitive data such as customer records, intellectual property, or configuration files. It assumes the attacker has obtained limited AWS credentials or is targeting a publicly accessible bucket, allowing enumeration without full privileges.

## Description

Misconfigured S3 buckets often have overly permissive ACLs or bucket policies that allow unauthorized listing and access to objects. An attacker can identify such buckets through reconnaissance (e.g., guessing common names like 'company-backup') and then use AWS CLI to list contents if anonymous access is permitted or if compromised credentials grant read permissions. This technique is part of broader cloud discovery and data exfiltration campaigns, enabling further attacks like downloading files for analysis or ransom. In a realistic scenario, this might follow subdomain enumeration or credential dumping from a compromised AWS IAM user. Success depends on the bucket's policy; if private, additional privilege escalation may be needed.

## Requirements

1. AWS CLI installed and accessible (see [[tools/aws-cli]] for setup).
2. Valid AWS credentials (e.g., access key and secret key) with s3:ListBucket permissions, or targeting a public bucket where no credentials are needed.
3. Internet access to reach AWS APIs.
4. Knowledge of potential bucket names (e.g., from reconnaissance or wordlists).

## Defense

- Implement least-privilege IAM policies and block public access on S3 buckets using bucket policies and ACLs.
- Enable AWS CloudTrail logging for S3 API calls to detect anomalous listing attempts.
- Use AWS Config rules to audit and remediate misconfigurations regularly.
- Segment network access with VPC endpoints to limit S3 exposure.

## Objectives

1. Enumerate objects within a target S3 bucket to identify sensitive data.
2. Confirm misconfiguration by successfully listing contents without expected errors.
3. Collect metadata on files (sizes, modification dates) for further exfiltration planning.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure AWS credentials are set up correctly to authenticate API calls. This step confirms access to AWS services and avoids authentication errors during listing.

If using a specific profile, configure it via `aws configure --profile example_profile`. For public buckets, omit credentials or use anonymous access.

**Expected Output**: Successful configuration with no errors; test with `aws sts get-caller-identity --profile example_profile` to verify identity.

### Step 2: Identify and Target the S3 Bucket

**Context**: Specify the bucket name to attempt listing. For exploitation, use guessed or enumerated bucket names (e.g., from tools like S3Scanner). This step focuses on the misconfigured resource.

Use a wordlist or known names to select $_BUCKET_NAME. If public, no profile needed.

**Expected Output**: Bucket name ready for querying; no prior output, but proceed to listing.

### Step 3: List Bucket Contents

**Context**: Execute the listing command to retrieve object metadata. This reveals the exploit success if contents are accessible despite restrictions, providing insight into stored data.

**Command** ([[commands/aws-s3-list-bucket-contents]]):
```bash
aws s3 ls s3://$_BUCKET_NAME/ --profile $_PROFILE --recursive
```

> This command lists all objects in the specified bucket recursively, including sizes and last modified dates. The --recursive flag ensures subdirectories are included. If the bucket is public or credentials allow, it succeeds; otherwise, expect 'AccessDenied'.

**Expected Output**: A list of objects, e.g.,
```
2023-01-15 10:30:00     1234 config.json
2023-02-20 14:45:00   56789 customer-data.csv
PRE sensitive/backup.tar.gz
```

If empty or denied: `An error occurred (AccessDenied) when calling the ListObjectsV2 operation: Access Denied`.
