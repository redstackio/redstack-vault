---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567895
data: >-
  http://web.archive.org/cdx/search/cdx?url=app.pullrequest.com/*&output=text&fl=original&collapse=urlkey
tags:
  - reconnaissance
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.068Z'
verified: false
validated: true
submitted: true
---
# wayback-machine-cdx-query

## Command

```bash
http://web.archive.org/cdx/search/cdx?url=app.pullrequest.com/*&output=text&fl=original&collapse=urlkey
```

## Description

This command queries the Wayback Machine's CDX API to retrieve a list of archived original URLs for a given domain, useful for discovering historical endpoints during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Base URL pattern to search (e.g., app.pullrequest.com/*) | Yes |
| output | Output format (text for line-separated results) | Yes |
| fl | Fields to return (original for URL only) | Yes |
| collapse | Collapse duplicates by urlkey | Yes |

## Examples

### Basic Usage

```bash
http://web.archive.org/cdx/search/cdx?url=example.com/*&output=text&fl=original&collapse=urlkey
```

### Advanced Usage

```bash
http://web.archive.org/cdx/search/cdx?url=app.pullrequest.com/reviews/*&output=json&fl=original,timestamp&collapse=urlkey
```

## Expected Output

A text list of original archived URLs, one per line, e.g.,
https://app.pullrequest.com/reviews/ratings/6eaa6b75-b958-4530-ba46-0d00cbe74e0b/false

## Related

- [[procedures/Discover-Archived-Endpoints-with-Wayback-Machine]]
