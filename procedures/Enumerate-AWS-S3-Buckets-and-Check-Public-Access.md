---
id: 895f3c46-7c03-4a33-b825-35c5d298ea74
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T04:25:34.663717+00:00'
updated_at: '2023-05-25T20:07:44.584676+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Cloud Service Discovery]]'
sub_techniques: []
tags:
  - AWS
  - Cloud
  - Reconnaissance
  - S3
platforms:
  - Cloud
commands:
  - '[[commands/aws-s3-list-buckets]]'
  - '[[commands/aws-s3-list-bucket-contents]]'
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-AWS-S3-Buckets-and-Check-Public-Access

## Summary

This procedure uses the AWS CLI to enumerate S3 buckets accessible via IAM credentials and checks the contents of specific buckets to identify public access. It is useful for reconnaissance in cloud environments to discover potentially exposed storage resources owned by the target organization or misconfigured public buckets.

## Description

In AWS environments, attackers with compromised IAM credentials can query S3 services to list buckets and their contents. This technique leverages the AWS API to perform discovery without needing direct ownership of the buckets. If a bucket is publicly accessible, the IAM key can retrieve its contents even if the key belongs to a different account. This is commonly used in initial reconnaissance to identify sensitive data exposure, such as configuration files, backups, or credentials. The procedure assumes valid IAM credentials are configured in the AWS CLI and focuses on the us-east-1 region by default, but can be adapted for others. Success depends on the permissions granted to the IAM role or user.

## Requirements

1. AWS CLI installed and configured with IAM access key and secret key (via `aws configure`).
2. IAM permissions allowing `s3:ListBuckets` and `s3:ListBucket` actions.
3. Network access to AWS endpoints (no VPC restrictions blocking API calls).
4. Target bucket names for content enumeration (can be guessed or brute-forced separately).

## Defense

Defensive measures and detection strategies:

- Implement least-privilege IAM policies to restrict `s3:ListBuckets` and `s3:ListBucket` actions to necessary roles only.
- Enable S3 bucket logging and AWS CloudTrail to monitor API calls for unusual enumeration patterns.
- Use bucket policies to deny public access and require authentication for all operations.
- Set up AWS GuardDuty to detect anomalous S3 access from unfamiliar IAM principals.

## Objectives

1. Identify all S3 buckets accessible to the current IAM credentials.
2. Verify if specific buckets allow public read access by attempting to list their contents.
3. Gather intelligence on exposed data for further exploitation or reporting.

## Instructions

### Step 1: List Accessible S3 Buckets

**Context**: This step enumerates all S3 buckets that the configured IAM credentials have permission to list. It provides an overview of the attacker's scope within the AWS account and can reveal buckets owned by the target or accessible due to cross-account policies.

**Command** ([[commands/aws-s3-list-buckets]]):
```bash
aws s3 ls
```

> This command queries the S3 service for a list of buckets. Run it after configuring credentials to ensure the IAM key has the necessary permissions. If no buckets are listed, the credentials lack `s3:ListBuckets` access.

### Step 2: List Contents of a Specific Bucket

**Context**: Once potential bucket names are identified (from Step 1 or external sources like DNS enumeration), attempt to list the contents of a specific bucket. If the bucket is public, this will succeed even without ownership, indicating a misconfiguration. Use this to probe for sensitive files.

**Command** ([[commands/aws-s3-list-bucket-contents]]):
```bash
aws s3 ls s3://$_BUCKET_NAME --region $_REGION
```

> Replace $_BUCKET_NAME with the target bucket (e.g., "example-bucket") and $_REGION with the AWS region (e.g., "us-east-1"). A successful response lists objects; an access denied error indicates private status. For brute-forcing, script multiple invocations with a wordlist of potential bucket names.
