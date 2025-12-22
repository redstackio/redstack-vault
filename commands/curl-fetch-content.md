---
id: c4g5h6i7-j8k9-0124-ghij-7890123456
data: 'curl https://subdomain.mozaws.net'
tags:
  - web
  - fetch
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:51:10.614Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-content

## Command

```bash
curl https://subdomain.mozaws.net
```

## Description

Fetches the full content from the subdomain to verify uploaded arbitrary content is served correctly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://subdomain.mozaws.net` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl https://subdomain.mozaws.net
```

### Advanced Usage

```bash
curl -s https://subdomain.mozaws.net | grep "Phishing"
```

## Expected Output

HTML or content body, e.g., '<h1>Fake Mozilla Login</h1>'.

## Related

- [[Related Procedure|procedures/Host-Arbitrary-Content-on-Taken-Over-Subdomain]]
