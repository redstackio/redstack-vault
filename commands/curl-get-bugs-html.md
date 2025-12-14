---
id: cmd-curl-bugs-html
data: >-
  curl -X GET https://hackerone.com/bugs.html -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H
  "User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:60.0) Gecko/20100101
  Firefox/60.0" -v
tags:
  - web
  - content-type
  - testing
type: command
output: 'HTTP/1.1 200 OK Content-Type: text/html; charset=utf-8'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.866Z'
verified: false
validated: true
submitted: true
---
# curl-get-bugs-html

## Command

```bash
curl -X GET https://hackerone.com/bugs.html -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:60.0) Gecko/20100101 Firefox/60.0" -v
```

## Description

This command requests /bugs.html with HTML Accept header, demonstrating a content-type logic flaw where .html extension causes HTML response instead of expected JSON for AJAX, leading to broken pages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET | Yes |
| `https://hackerone.com/bugs.html` | Path with .html extension | Yes |
| `-H "Accept: ..."` | Requests HTML content-type | Yes |
| `-H "User-Agent: ..."` | Browser simulation | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://hackerone.com/bugs.html -H "Accept: text/html"
```

### Advanced Usage

Add Referer for AJAX simulation: -H "Referer: https://hackerone.com/bugs.html"

## Expected Output

HTML content (200 OK, Content-Type: text/html), which breaks JSON-dependent AJAX loads.

## Related

- [[Related Procedure: None - Separate Logic Flaw]]
