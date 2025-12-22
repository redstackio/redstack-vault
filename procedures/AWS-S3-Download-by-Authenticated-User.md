---
id: 9ef03344-339d-4d68-b6ad-25a131dc2def
name: AWS-S3-Download-by-Authenticated-User
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.138841+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques:
  - >-
    [[sub-techniques/Exfiltration Over Unencrypted Non-C2 Protocol|T1048.003 -
    Exfiltration Over Unencrypted Non-C2 Protocol]]
tags:
  - '[[tags/Authenticated User]]'
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Data Exfiltration]]'
commands:
  - '[[commands/aws-s3api-get-object]]'
platforms:
  - AWS
tools:
  - '[[tools/AWS-CLI]]'
validated: true
---

# AWS-S3-Download-by-Authenticated-User

## Summary

This procedure enables an authenticated user to download objects from an Amazon S3 bucket using the AWS CLI, facilitating data exfiltration from a compromised AWS account. It leverages legitimate AWS APIs to retrieve sensitive files such as customer data, credentials, or intellectual property stored in S3, often over HTTPS to blend with normal traffic.

## Description

In a typical attack scenario, an attacker with valid AWS credentials (e.g., obtained via phishing or credential dumping) targets S3 buckets containing valuable data. The procedure abuses AWS's S3 service for exfiltration, downloading objects to the attacker's local machine without triggering obvious alerts if access policies are lax. This is particularly effective in cloud environments where S3 is used for storage, and detection relies on monitoring unusual data transfers. The technique requires no additional privileges beyond read access to the bucket and uses the AWS CLI for authentication via access keys or IAM roles. Potential outcomes include data theft leading to financial loss or regulatory violations for the victim organization.

## Requirements

1. Valid AWS credentials (access key ID and secret access key) with read permissions on the target S3 bucket.
2. Network access to AWS endpoints (typically over HTTPS on port 443).
3. AWS CLI installed and configured on the attacker's machine with the target profile.
4. Knowledge of the S3 bucket name and object key (path) to download.

## Defense

- Implement least-privilege IAM policies to restrict S3 read access to only necessary users and roles.
- Enable AWS CloudTrail logging for S3 API calls and monitor for anomalous downloads (e.g., large data volumes or unusual IP sources).
- Use S3 bucket policies to deny downloads from untrusted networks and enable server-side encryption with KMS for data at rest.
- Integrate Amazon GuardDuty or third-party tools to detect exfiltration patterns in S3 access logs.

## Objectives

1. Authenticate to AWS using compromised credentials and access S3 resources.
2. Download specific objects from the target bucket to the local system.
3. Verify the integrity of downloaded data without alerting monitoring systems.

## Instructions

### Step 1: Configure AWS CLI and Authenticate

**Context**: Ensure the AWS CLI is set up with the compromised credentials to authenticate requests. This step prepares the environment for secure API calls to S3.

Use [[tools/AWS-CLI]] to configure credentials if not already done:

```bash
aws configure set aws_access_key_id $_ACCESS_KEY_ID
aws configure set aws_secret_access_key $_SECRET_ACCESS_KEY
aws configure set default.region $_REGION
```

> This sets the access key, secret key, and default region (e.g., us-east-1). Expected output is a confirmation message or no output if successful. Verify with `aws sts get-caller-identity` to confirm authentication.

### Step 2: Download the S3 Object

**Context**: Execute the download using the S3 API to retrieve the target object. This step accomplishes the exfiltration by transferring the file locally while maintaining HTTPS encryption.

**Command** ([[commands/aws-s3api-get-object]]):

```bash
aws s3api get-object --bucket $_BUCKET_NAME --key $_OBJECT_KEY $_LOCAL_FILE_PATH
```

> Replace placeholders with actual values (e.g., bucket 'my-sensitive-data', key 'secrets.txt', local path './downloaded-secrets.txt'). This command authenticates via the configured credentials and downloads the object. Expected output includes metadata like ETag and LastModified, followed by the file saved locally. Verify success by checking the file size and contents match the S3 object.
