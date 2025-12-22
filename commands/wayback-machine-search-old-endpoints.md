---
type: command
executor: bash
data: >-
  curl -sX GET
  "http://web.archive.org/cdx/search/cdx?url=$_TARGET_DOMAIN&output=text&fl=original&collapse=urlkey&matchType=prefix"
output: null
platforms:
  - Linux
tags:
  - reconnaissance
  - historical-analysis
verified: true
validated: true
---

# Wayback Machine Search Old Endpoints

## Command

```bash
curl -sX GET "http://web.archive.org/cdx/search/cdx?url=$_TARGET_DOMAIN&output=text&fl=original&collapse=urlkey&matchType=prefix"
```

## Description

This command queries the Wayback Machine's CDX API to retrieve archived URLs for a target domain, helping identify forgotten endpoints, JS files, or old pages that may reveal vulnerabilities or configs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DOMAIN | Target domain (e.g., example.com) | Yes |
| -s | Silent mode (no progress bar) | Built-in |
| -X GET | HTTP GET method | Built-in |
| url=... | Filters by domain prefix | Yes |
| output=text | Text format output | Built-in |
| fl=original | Returns original URLs | Built-in |
| collapse=urlkey | Deduplicates by URL key | Built-in |
| matchType=prefix | Matches domain prefix | Built-in |

## Examples

### Basic Usage

```bash
curl -sX GET "http://web.archive.org/cdx/search/cdx?url=example.com&output=text&fl=original&collapse=urlkey&matchType=prefix"
```

### Advanced Usage (Filter JS)

```bash
curl -sX GET "http://web.archive.org/cdx/search/cdx?url=example.com&output=text&fl=original&collapse=urlkey&matchType=prefix" | grep '\.js'
```

## Expected Output

List of archived URLs:

```
http://example.com/
http://example.com/old/admin.php
http://example.com/js/config.js
```

## Related

- [[procedures/passive-reconnaissance-information-gathering]]
