---
data: >-
  curl -X POST 'https://target.com/█████████' -H 'Content-Type:
  application/json' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"member_id":
  "YOUR_ID"}'
tags:
  - web
  - post
  - recon
type: command
output: |-
  HTTP/1.1 200 OK
  {"status": "success"}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-05T12:00:00Z'
updated_at: '2025-12-14T17:33:24.283Z'
id: 02522f18-5629-4177-a4f0-ec91270896fd
verified: false
validated: true
submitted: true
---
# curl-identify-post-endpoint

## Command

```bash
curl -X POST 'https://target.com/█████████' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"member_id": "YOUR_ID"}'
```

## Description

This command sends a POST request to probe a potential IDOR endpoint, verifying it processes the member_id parameter for the authenticated user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `'https://target.com/█████████'` | Target endpoint URL | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON body type | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header | Yes |
| `-d '{"member_id": "YOUR_ID"}'` | Request body with member_id | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/█████████' -H 'Content-Type: application/json' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"member_id": "123"}'
```

### Advanced Usage

```bash
curl -v -X POST 'https://target.com/█████████' -H 'Content-Type: application/json' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"member_id": "123", "action": "view"}'
```

## Expected Output

A 200 OK response with JSON confirming successful processing, such as {"status": "success", "data": {...}}.

## Related

- [[Related Procedure|procedures/Identify-Vulnerable-POST-Endpoint-for-IDOR]]
