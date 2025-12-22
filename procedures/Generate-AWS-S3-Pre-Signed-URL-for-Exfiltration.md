---
id: ced4d768-07a9-4341-be47-cc6322a7a77a
name: Generate-AWS-S3-Pre-Signed-URL-for-Exfiltration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:11.164875+00:00'
updated_at: '2023-04-10T20:20:44.956719+00:00'
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques: []
tags:
  - '[[tags/cloud-aws]]'
  - '[[tags/data-exfiltration]]'
  - '[[tags/time-based-url]]'
commands:
  - '[[commands/aws-s3-presign-object-url]]'
platforms:
  - AWS
  - Cloud
tools: []
validated: true
---

# Generate-AWS-S3-Pre-Signed-URL-for-Exfiltration

## Summary

This procedure demonstrates how to generate a time-limited pre-signed URL for an AWS S3 object using the AWS CLI, enabling temporary access to sensitive data for exfiltration purposes. The URL expires after a specified duration, allowing attackers with valid AWS credentials to bypass direct access restrictions and download objects without ongoing authentication.

## Description

In an attack scenario, adversaries who have compromised AWS credentials with S3 permissions can use pre-signed URLs to exfiltrate data from S3 buckets. This technique leverages AWS's built-in presigning feature, which embeds a cryptographic signature in the URL valid for a set time (e.g., seconds to hours). Once generated, the URL can be shared or used to download the object via standard HTTP clients like curl or a browser, evading network controls that monitor authenticated API calls. This is particularly useful in cloud environments where direct S3 access might be logged or restricted, but temporary URLs appear as normal web traffic. The target environment is AWS S3 buckets containing sensitive data, such as customer records or proprietary files. Expected outcomes include successful download of the object before expiration, potentially leading to data theft without immediate detection.

## Requirements

1. Valid AWS credentials (access key and secret key) with permissions to read the target S3 object and generate pre-signed URLs (e.g., s3:GetObject, s3:GetObjectUrl).
2. Access to an S3 bucket containing the target sensitive data object.
3. AWS CLI installed and configured on the attacker's system with the appropriate credentials (via `aws configure`).
4. Network connectivity to AWS endpoints (no VPC restrictions blocking S3 access).

## Defense

Defensive measures and detection strategies:

- Monitor S3 access logs and CloudTrail for unusual pre-signed URL generation or object downloads, focusing on short expiration times or anomalous IP sources.
- Implement least-privilege IAM policies to restrict pre-signing capabilities and limit S3 bucket permissions.
- Use AWS Config rules to alert on public or overly permissive S3 buckets, and enable S3 Block Public Access.
- Deploy network security controls like AWS WAF or VPC flow logs to detect and block exfiltration over alternative protocols (e.g., direct HTTPS to S3 endpoints).
- Shorten default expiration times for pre-signed URLs via policy enforcement and rotate credentials regularly.

## Objectives

1. Generate a temporary pre-signed URL to access and exfiltrate an S3 object without direct authentication.
2. Download the sensitive data using the URL before it expires to avoid detection.
3. Demonstrate evasion of standard API monitoring by mimicking legitimate web requests.

## Instructions

### Step 1: Configure AWS CLI and Verify Access

**Context**: Ensure the AWS CLI is set up with compromised credentials and test basic S3 access to confirm permissions before generating the pre-signed URL. This step verifies the environment and prevents errors during presigning.

**Command** ([[commands/aws-s3-presign-object-url]]):

First, list objects in the target bucket to identify the exfiltration target:

```bash
aws s3 ls s3://$_BUCKET_NAME/ --recursive
```

> This command lists all objects in the specified bucket. Expected output is a table of object keys, sizes, and last modified dates, confirming read access. If access is denied, adjust IAM permissions or credentials.

### Step 2: Generate Pre-Signed URL for the Target Object

**Context**: Use the AWS CLI to create a pre-signed URL for the specific S3 object, setting a short expiration time (e.g., 605000 seconds ≈ 7 days) to limit exposure while allowing time for exfiltration. This embeds a signature based on the credentials, granting temporary GET access.

**Command** ([[commands/aws-s3-presign-object-url]]):
```bash
aws s3 presign s3://$_BUCKET_NAME/$_OBJECT_KEY --expires-in $_EXPIRATION_SECONDS
```

> The command outputs a direct HTTPS URL to the object. For example: `https://$_BUCKET_NAME.s3.amazonaws.com/$_OBJECT_KEY?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=...&X-Amz-Signature=...&X-Amz-SignedHeaders=host&X-Amz-Expires=...&X-Amz-Date=...`. Success is indicated by the URL generation without errors; test by curling the URL to download the object.

### Step 3: Exfiltrate Data Using the Pre-Signed URL

**Context**: Download the object via the generated URL using a standard HTTP client. This step completes the exfiltration, treating the URL as a simple web resource to blend with normal traffic.

**Command**:
```bash
curl -o exfiltrated_data "$_PRESIGNED_URL"
```

> This downloads the object to a local file. Expected output is the file saved locally with the object's content. Verify by checking file size and contents match the S3 object. If the URL has expired, regenerate it.
