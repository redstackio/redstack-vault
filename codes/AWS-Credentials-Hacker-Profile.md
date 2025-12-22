---
id: 678bec71-028f-47f5-94a4-7223c39c8ee3
type: code
language: ini
verified: true
created_at: '2020-03-17T05:47:43.527601+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - aws
  - credentials
  - cloud
validated: true
---

# AWS-Credentials-Hacker-Profile

## Code

```ini
# ~/.aws/credentials
[hacker]
aws_access_key_id = AKIA<REDACTED>SX65
aws_secret_access_key = pODU9<REDACTED>K4qW
```

## Description

Configuration snippet for the AWS CLI credentials file, defining a 'hacker' profile with access key ID and secret access key. This profile is used by Terraform and AWS CLI for authenticating API calls during infrastructure provisioning.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| aws_access_key_id | AWS IAM access key identifier | AKIAIOSFODNN7EXAMPLE |
| aws_secret_access_key | AWS IAM secret access key | wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY |

## Usage

Place this in ~/.aws/credentials on the hacker machine. Reference the profile in Terraform with `profile = "hacker"`. Test with `aws sts get-caller-identity --profile hacker`. Used in red team ops to stage cloud resources without exposing keys in scripts.

## Detection

- Monitor AWS CloudTrail for IAM access key usage patterns.
- Scan for exposed credentials in git repos or configs (e.g., via tools like TruffleHog).
- Alert on unusual API calls from new keys.

## Related

- [[procedures/Terraform-Create-Kali-Linux-EC2-Instance]]
- [[tools/aws-cli]]
