---
data: >-
  # In Burp Suite: Monitor responses for 200 OK or 500 instead of
  {'message':'Unverified request'}
tags:
  - burp
  - response
type: command
executor: bash
platforms:
  - Web
id: 800a0d3e-5dbf-460d-b3e7-1cb1132a1abb
created_at: '2025-12-13T09:01:17.577Z'
updated_at: '2025-12-13T09:01:17.577Z'
verified: false
validated: true
submitted: true
---
# Observe Smuggling Response

## Command

```bash
# In Burp Suite: Monitor responses for 200 OK or 500 instead of {'message':'Unverified request'}
```

## Description

Monitors HTTP responses in Burp Suite to detect signs of successful request smuggling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Manual observation | No |

## Examples

### Basic Usage

```bash
# Check response code and body
```

## Expected Output

Unexpected status codes like 200 OK or 500 confirming smuggling.

## Related

- [[commands/run-turbo-intruder-script]]
- [[procedures/Exploit-HTTP-Request-Smuggling-CL-TE]]
