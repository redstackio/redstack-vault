---
id: new-uuid-1-for-token
name: retrieve-aws-ec2-metadata-token
type: command
executor: bash
data: >-
  TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H
  "X-aws-ec2-metadata-token-ttl-seconds: 21600")
output: null
created_at: '2023-04-06T03:56:13.368549+00:00'
updated_at: '2023-04-10T20:19:58.621084+00:00'
platforms:
  - AWS
  - Linux
tags:
  - aws-metadata
  - cloud
verified: true
validated: true
---

# retrieve-aws-ec2-metadata-token

## Command

```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
```

## Description

This command requests a session token from the AWS IMDSv2 endpoint, which is required to access instance metadata securely. The token is stored in the TOKEN environment variable for use in subsequent queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://169.254.169.254/latest/api/token` | Fixed IMDSv2 token endpoint URL | Yes |
| `-X PUT` | HTTP method for token request | Yes |
| `-H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` | Header specifying token TTL (6 hours) | Yes |

## Examples

### Basic Usage

```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
echo $TOKEN
```

### Advanced Usage

Use a shorter TTL for testing:

```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 60")
```

## Expected Output

A long alphanumeric token string, e.g.,

```
AQAAACA... (truncated for security)
```

If the request fails, output may be empty or an error like "Connection refused" if IMDSv2 is not enabled.

## Related

- [[procedures/Retrieve-AWS-EC2-Instance-Metadata-Keys]]
- [[commands/query-aws-ec2-metadata-with-token]]
