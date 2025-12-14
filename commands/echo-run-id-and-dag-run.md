---
data: 'echo "run_id={{ run_id }} | dag_run={{ dag_run }}"'
tags:
  - airflow
  - templating
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.478Z'
id: 3e89f10d-c0f2-4b0b-b8e6-ea96d74e5f9e
verified: false
validated: true
submitted: true
---
# echo-run-id-and-dag-run

## Command

```bash
echo "run_id={{ run_id }} | dag_run={{ dag_run }}"
```

## Description

This Bash command, defined in Airflow's example_bash_operator.py BashOperator, echoes the run_id and dag_run values after Jinja templating. It is vulnerable to injection when run_id contains shell metacharacters like backticks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{{ run_id }}` | User-controlled run ID interpolated via Jinja | Yes |
| `{{ dag_run }}` | Reference to the current DAG run object | Yes |

## Examples

### Basic Usage

```bash
echo "run_id=manual | dag_run=<DagRun>"
```

### Advanced Usage (Injected)

```bash
echo "run_id=`touch /tmp/success` | dag_run=<DagRun>"
```

## Expected Output

Normal: Outputs "run_id=manual | dag_run=<DagRun manual @ ...>"
Injected: Executes the command inside backticks (e.g., creates /tmp/success) and echoes the substituted value.

## Related

- [[Related Procedure]]
