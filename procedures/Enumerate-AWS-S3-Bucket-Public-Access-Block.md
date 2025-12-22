---
id: a3c3334e-7012-419a-8b4d-930666f3f351
name: Enumerate-AWS-S3-Bucket-Public-Access-Block
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.044162+00:00'
updated_at: '2023-04-10T20:20:12.197015+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Cloud-Service-Dashboard|T1538 - Cloud Service Dashboard]]'
  - '[[techniques/Cloud-Service-Discovery|T1526 - Cloud Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Cloud-AWS]]'
  - '[[tags/Enumeration]]'
  - '[[tags/S3-Bucket-Public-Access]]'
commands:
  - '[[commands/aws-s3api-get-public-access-block]]'
platforms:
  - AWS
  - Cloud
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# Enumerate-AWS-S3-Bucket-Public-Access-Block

## Summary

This procedure checks the Public Access Block configuration for a specific AWS S3 bucket to determine if public access is restricted, helping identify potential data exposure risks in cloud environments.

## Description

In AWS, S3 buckets can be configured for public access, which may lead to unintended data leaks if not properly secured. The Public Access Block feature provides four settings to block public access at the bucket or account level: BlockPublicAcls, IgnorePublicAcls, BlockPublicPolicy, and RestrictPublicBuckets. This procedure uses the AWS CLI to query the configuration for a given bucket, returning a JSON response that indicates whether these blocks are enabled. This is useful in reconnaissance phases to assess if a bucket is vulnerable to public enumeration or access without authentication. The technique aligns with cloud service discovery by inspecting infrastructure configurations via authorized API calls.

## Requirements

1. Valid AWS credentials (access key and secret key) with at least `s3:GetPublicAccessBlock` permissions on the target bucket.
2. AWS CLI installed and configured with the appropriate profile (e.g., via `aws configure`).
3. Network access to AWS endpoints (no VPC restrictions blocking API calls).

## Defense

- Enable Public Access Block at the account level via AWS Organizations or IAM policies to prevent public bucket configurations.
- Monitor S3 access logs and CloudTrail for API calls to `GetPublicAccessBlock` from unauthorized sources.
- Implement least-privilege IAM policies to restrict `s3:GetPublicAccessBlock` to trusted roles only.

## Objectives

1. Retrieve the Public Access Block settings for a specified S3 bucket.
2. Identify if the bucket allows public access, enabling further reconnaissance or exploitation planning.
3. Validate bucket security posture without attempting direct access.

## Instructions

### Step 1: Verify AWS CLI Configuration

**Context**: Ensure your AWS credentials are set up correctly to authenticate API requests. This step prevents authentication errors during the enumeration.

Run `aws sts get-caller-identity` to confirm your identity and permissions.

**Expected Output**: JSON response showing your AWS account, user ARN, and account ID, confirming successful authentication.

### Step 2: Query Public Access Block Configuration

**Context**: Use the AWS S3 API to fetch the Public Access Block details for the target bucket. This reveals if public access is blocked, allowing assessment of exposure risks.

**Command** ([[commands/aws-s3api-get-public-access-block]]):

```bash
aws s3api get-public-access-block --bucket $_BUCKET_NAME
```

> This command queries the S3 API for the bucket's Public Access Block settings. Replace `$_BUCKET_NAME` with the actual bucket name (e.g., `my-exposed-bucket`). The response is a JSON object under `PublicAccessBlockConfiguration` with fields like `BlockPublicAcls`, `IgnorePublicAcls`, etc., each set to `true` (enabled/blocked) or `false` (disabled/allowed).

**Expected Output**:

```json
{
    "PublicAccessBlockConfiguration": {
        "BlockPublicAcls": true,
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": false,
        "RestrictPublicBuckets": true
    }
}
```

If all blocks are `true`, the bucket is fully protected from public access. Partial or false values indicate potential vulnerabilities.
