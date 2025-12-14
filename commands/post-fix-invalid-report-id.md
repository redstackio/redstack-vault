---
id: cmd-007
data: 'curl -X GET "https://hackerone.com/reports/1.458239753714584e+55.json"'
tags:
  - verification
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:30.155Z'
verified: false
validated: true
submitted: true
---
# post-fix-invalid-report-id

## Command

```bash
curl -X GET "https://hackerone.com/reports/1.458239753714584e+55.json"
```

## Description

Tests post-fix behavior with non-integer report_id to verify validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Path | Non-integer ID | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://hackerone.com/reports/nonint.json"
```

## Expected Output

404 Not Found, confirming integer validation fix.

## Related

- [[commands/normal-bugs-request]]
- [[procedures/Observe-Normal-Bugs-Endpoint-Behavior]]
