---
type: procedure
description: >-
  Exfiltrate sensitive text data from a publicly accessible AWS S3 bucket using
  direct HTTP requests.
verified: true
submitted: false
created_at: '2023-04-06T03:56:11Z'
updated_at: '2023-04-10T20:20:27Z'
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques: []
tags:
  - '[[tags/Cloud - AWS]]'
  - '[[tags/Data Exfiltration]]'
  - '[[tags/Public Access]]'
commands:
  - '[[commands/curl-download-s3-object]]'
platforms:
  - AWS
tools: []
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
---

# AWS S3 Secret Text Retrieval - Public Access Data Exfiltration

## Summary

This procedure demonstrates how to exfiltrate sensitive text files, such as passwords or API keys, from a publicly accessible AWS S3 bucket. By constructing the direct HTTPS URL to the object and downloading it via standard HTTP tools, an attacker can retrieve data without authentication, blending with normal web traffic.

## Description

Publicly accessible S3 buckets expose objects to anyone with the URL, often due to misconfigurations in bucket policies. This technique targets text-based secrets stored in such buckets, allowing attackers to download files containing credentials or other sensitive information. Once obtained, these secrets can enable further attacks like privilege escalation or lateral movement within the AWS environment. The procedure uses simple HTTP GET requests, making it stealthy and requiring no AWS credentials. It applies to any region where the bucket is hosted and assumes the attacker knows the bucket name and object path, which could be discovered via reconnaissance.

## Requirements

1. Knowledge of the target S3 bucket name and the path to the secret text object (e.g., via prior enumeration).
2. Internet access to reach the AWS S3 endpoint.
3. A tool like curl installed on the attacker's machine (standard on most Linux distributions).
4. No AWS credentials needed, as the bucket must be publicly readable.

## Defense

- Implement strict bucket policies to prevent public access; use private buckets with IAM controls.
- Enable S3 server access logging and monitor CloudTrail for unusual GET Object requests from unknown IPs.
- Regularly audit bucket permissions using tools like AWS Config or Prowler to identify public exposures.
- Use S3 Block Public Access settings at the account and bucket levels.

## Objectives

1. Download sensitive text data from a public S3 bucket without authentication.
2. Capture and analyze the exfiltrated data for usable secrets.
3. Maintain stealth by mimicking legitimate web traffic.

## Instructions

### Step 1: Construct the S3 Object URL

**Context**: Build the direct HTTPS URL to the target object in the public bucket. S3 objects are accessible via REST API endpoints if the bucket ACL allows public reads. Replace placeholders with the actual bucket name, region (optional if default), and object key.

**Command** ([[commands/curl-download-s3-object]]):
```bash
curl "https://$_BUCKET_NAME.s3.$_REGION.amazonaws.com/$_OBJECT_KEY" -o $_OUTPUT_FILE
```

> This command fetches the object content. The URL format ensures compatibility with S3's virtual-hosted style. If the region is not specified, S3 defaults to us-east-1, but including it avoids redirects.

### Step 2: Download and Verify the File

**Context**: Execute the download and inspect the content to confirm it contains the expected secrets. Save the output to a local file for offline analysis.

**Command** ([[commands/curl-download-s3-object]]):
```bash
curl "https://example-bucket.s3.us-east-1.amazonaws.com/secrets.txt" -o secrets.txt
cat secrets.txt
```

> Run the curl command to retrieve the file. Then use `cat` or a text editor to view the content. If the bucket is public, the response will be 200 OK with the file body; otherwise, expect 403 Forbidden.

### Step 3: Handle Potential Variations

**Context**: If the direct URL fails due to path-style access or redirects, adjust the URL format or use AWS CLI for testing (though not required for public access). Decision point: If curl returns a redirect, follow it manually or use `-L` flag.

**Command** ([[commands/curl-download-s3-object]]):
```bash
curl -L "http://$_BUCKET_NAME.s3.amazonaws.com/$_OBJECT_KEY" -o $_OUTPUT_FILE
```

> The `-L` flag follows redirects. Verify success by checking the file size and content match expected secret format (e.g., plaintext API keys).
