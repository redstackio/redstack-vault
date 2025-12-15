---
data: ln -s $TARGET/dags/poc.py example_bash_operator.py.log
tags:
  - symlink
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.465Z'
id: 60a0c04e-0c13-4098-bed8-8a6787a4966e
verified: false
validated: true
submitted: true
---
# ln-symlink-to-dag

## Command

```bash
ln -s $TARGET/dags/poc.py example_bash_operator.py.log
```

## Description

Creates a symbolic link from the log file name to the target DAG file, allowing log writes to affect the DAG.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Create symbolic link | Yes |
| `$TARGET/dags/poc.py` | Target DAG path | Yes |
| `example_bash_operator.py.log` | Link name | Yes |

## Examples

### Basic Usage

```bash
ln -s /home/airflow/dags/poc.py example_bash_operator.py.log
```

### Verify Link

```bash
ls -l example_bash_operator.py.log  # Shows lrwxrwxrwx -> /home/airflow/dags/poc.py
```

## Expected Output

No output if successful.

## Related

- [[commands/rm-log-file]]
