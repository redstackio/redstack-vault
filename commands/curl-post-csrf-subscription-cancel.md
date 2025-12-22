---
data: >-
  curl -X POST 'https://akismet.com/api/subscription/1/cancel' -H 'Cookie:
  session=abc123' -d ''
tags:
  - csrf
  - web
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.493Z'
id: 40baccd5-92f9-4035-aa1d-7a4d8fe58f89
verified: false
validated: true
submitted: true
---
# curl-post-csrf-subscription-cancel

## Command

```bash
curl -X POST 'https://akismet.com/api/subscription/1/cancel' -H 'Cookie: session=abc123' -d ''
```

## Description

Forwards a POST request to cancel a subscription, testing the CSRF vulnerability in Akismet's API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Method | Yes |
| `https://akismet.com/api/subscription/1/cancel` | Cancellation endpoint | Yes |
| `-H 'Cookie: session=abc123'` | Authentication cookie | Yes |
| `-d ''` | Request body | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://akismet.com/api/subscription/1/cancel' -H 'Cookie: session=abc123' -d ''
```

### Advanced Usage

```bash
curl -X POST 'https://akismet.com/api/subscription/1/cancel' -H 'Cookie: session=abc123' -v
```

## Expected Output

Success message or redirect post-cancellation.

## Related

- [[Related Procedure]]
