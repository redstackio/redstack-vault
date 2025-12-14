---
data: cd $TARGET/logs/scheduler/latest/native_dags/example_dags
tags:
  - navigation
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.475Z'
id: 7a361b7d-1c9b-4811-beaa-e1d95fbf92d8
verified: false
validated: true
submitted: true
---
# cd-to-scheduler-logs

## Command

```bash
cd $TARGET/logs/scheduler/latest/native_dags/example_dags
```

## Description

Changes the current working directory to the Airflow scheduler's log subdirectory, where exploitable world-writable logs are located.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$TARGET` | Base Airflow home path (e.g., /home/airflow) | Yes |

## Examples

### Basic Usage

```bash
export TARGET=/home/airflow
cd $TARGET/logs/scheduler/latest/native_dags/example_dags
```

### Verify

```bash
pwd  # Outputs /home/airflow/logs/scheduler/latest/native_dags/example_dags
```

## Expected Output

No output; directory changed.

## Related

- [[commands/umask-0]]
