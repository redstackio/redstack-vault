---
data: 'until [ -f $TARGET/dags/poc.py ]; do sleep 1; done'
tags:
  - wait
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.462Z'
id: a2eacf4f-312a-4876-b6da-051a75dd3fa1
verified: false
validated: true
submitted: true
---
# wait-for-poc-file

## Command

```bash
until [ -f $TARGET/dags/poc.py ]; do sleep 1; done
```

## Description

Loops until the target poc.py file exists, sleeping 1 second between checks, ensuring it's ready for writing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Test file existence | Yes |
| `$TARGET/dags/poc.py` | File to check | Yes |
| `sleep 1` | 1-second pause | Yes |

## Examples

### Basic Usage

```bash
until [ -f /home/airflow/dags/poc.py ]; do sleep 1; done
echo "File ready"
```

## Expected Output

No output; exits loop when file exists.

## Related

- [[commands/ln-symlink-to-dag]]
