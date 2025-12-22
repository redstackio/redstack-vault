---
id: new-uuid-1
name: aws-configure-set-credentials
type: command
executor: bash
data: >-
  aws configure set aws_access_key_id $_ACCESS_KEY_ID && aws configure set
  aws_secret_access_key $_SECRET_ACCESS_KEY && aws configure set default.region
  $_REGION
output: null
created_at: '2023-04-06T03:56:13.964126+00:00'
updated_at: '2023-04-10T20:19:50.628379+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - aws
  - configuration
verified: true
validated: true
---

# aws-configure-set-credentials

## Command

```bash
aws configure set aws_access_key_id $_ACCESS_KEY_ID && aws configure set aws_secret_access_key $_SECRET_ACCESS_KEY && aws configure set default.region $_REGION
```

## Description

Configures AWS CLI credentials and default region for authenticated API calls. Use this before executing AWS commands with stolen or compromised keys.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ACCESS_KEY_ID | AWS access key ID (e.g., AKIAIOSFODNN7EXAMPLE) | Yes |
| $_SECRET_ACCESS_KEY | AWS secret access key | Yes |
| $_REGION | AWS region (e.g., us-east-1) | Yes |

## Examples

### Basic Usage

```bash
aws configure set aws_access_key_id AKIAIOSFODNN7EXAMPLE && aws configure set aws_secret_access_key wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY && aws configure set default.region us-east-1
```

### Advanced Usage

Combine with profile: `aws configure set profile.myprofile.aws_access_key_id $_ACCESS_KEY_ID`

## Expected Output

No output on success; errors if invalid credentials. Verify with `aws sts get-caller-identity` showing UserId and Account.

## Related

- [[commands/aws-rds-describe-db-instances]]
- [[procedures/List-AWS-RDS-DB-Instances-for-Exfiltration]]
