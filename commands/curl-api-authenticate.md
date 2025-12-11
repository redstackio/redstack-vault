---
id: 537275bc-480f-4b08-bc30-ad7806bf9a9c
name: curl-api-authenticate
type: command
executor: bash
data: >-
  curl -u username: --cert leaked_certificate.pem
  https://code.uberinternal.com/api endpoint
output: null
created_at: '2025-12-11T06:10:15.524Z'
updated_at: '2025-12-11T06:10:15.524Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - api
  - authentication
verified: false
validated: true
submitted: true
---

# curl-api-authenticate

## Command

```bash
curl -u username: --cert leaked_certificate.pem https://code.uberinternal.com/api endpoint
```

## Description

Authenticates to an API endpoint using basic auth and a client certificate, ideal for exploiting leaked credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u username:` | Basic auth username (password blank if not needed) | Yes |
| `--cert file.pem` | Path to certificate file | Yes |
| `url` | API endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -u username: --cert cert.pem https://api.example.com
```

### Advanced Usage

```bash
curl -u username: --cert cert.pem --key key.pem https://api.example.com
```

## Expected Output

API response data if authentication succeeds, such as JSON output from the endpoint.

## Related

- [[procedures/Access-Phabricator-API-Using-Leaked-Credentials]]
