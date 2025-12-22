---
id: 3afcc5f4-82e6-4a1c-b44b-a6edcbf2a774
name: curl-retrieve-ec2-user-data-imdsv2
type: command
executor: bash
data: >-
  TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H
  "X-aws-ec2-metadata-token-ttl-seconds: 21600") && curl -H
  "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/user-data/
output: null
created_at: '2023-04-06T03:56:13.398773+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - AWS
  - Linux
tags:
  - cloud-metadata
  - aws-imds
verified: true
validated: true
---

# curl-retrieve-ec2-user-data-imdsv2

## Command

```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600") && curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/user-data/
```

## Description

This command fetches a session token from IMDSv2 and uses it to securely retrieve EC2 user data. Essential for instances in IMDSv2-required mode to access metadata without exposing it to unauthenticated requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -X PUT | HTTP method for token request | Yes |
| http://169.254.169.254/latest/api/token | IMDS token endpoint | Yes |
| X-aws-ec2-metadata-token-ttl-seconds: 21600 | Token TTL in seconds (max 21600) | Yes |
| $TOKEN | Captured session token | Yes (auto-generated) |
| -v | Verbose output for debugging | No |
| http://169.254.169.254/latest/user-data/ | User data endpoint | Yes |

## Examples

### Basic Usage

```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600") && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/user-data/
```

### Reuse Token for Multiple Queries

```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/iam/security-credentials/
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/user-data/
```

## Expected Output

Token request: 201 Created with token string. User data request: 200 OK with raw data (e.g., script content). Verbose shows headers like < HTTP/1.1 200 OK. Errors: 401 for invalid token, 403 for IMDS blocked.

## Related

- [[procedures/Retrieve-AWS-EC2-User-Data-via-Instance-Metadata-Service]]
- [[codes/curl-retrieve-ec2-user-data-imdsv1]]
