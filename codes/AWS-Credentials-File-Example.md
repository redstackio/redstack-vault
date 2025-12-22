---
id: e7fb2714-6341-4454-92b7-b6dcd1510f72
name: AWS-Credentials-File-Example
type: code
language: ini
verified: true
created_at: '2019-10-10T18:18:30.585971+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - credentials
  - config
validated: true
---

# AWS-Credentials-File-Example

## Code

```ini
# ~/.aws/credentials
[hacker]
aws_access_key_id = AKIA<REDACTED>SX65
aws_secret_access_key = pODU9<REDACTED>K4qW
```

## Description

This code snippet configures the AWS CLI credentials file with a named profile ('hacker') for use in red team operations. It stores access key ID and secret access key, enabling authenticated API calls without passing credentials inline.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| aws_access_key_id | AWS IAM access key ID | AKIAIOSFODNN7EXAMPLE |
| aws_secret_access_key | AWS IAM secret access key | wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY |

## Usage

Place this in ~/.aws/credentials and reference the 'hacker' profile in commands (e.g., --profile hacker). Use for Terraform or AWS CLI operations provisioning S3 resources. Generate keys via IAM console with minimal permissions for opsec.

## Detection

- Scan for ~/.aws/credentials files in compromised systems.
- Monitor IAM access key creation and usage patterns in CloudTrail.
- Alert on API calls from unusual profiles or IPs.

## Related

- [[procedures/Provision-AWS-S3-Website-and-Upload-Payload]]
- [[tools/aws-cli]]
