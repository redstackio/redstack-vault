---
data: 'java -classpath ''.:./runtime/*'' QueryHive ████████:10000 "SELECT 1"'
tags:
  - java
  - query
type: command
executor: bash
platforms:
  - Linux
id: 01de1c0e-76c6-4702-8879-c46eb2d105fd
created_at: '2025-12-13T09:00:27.736Z'
updated_at: '2025-12-13T09:00:27.736Z'
verified: false
validated: true
submitted: true
---
# java-queryhive-select

## Command

```bash
java -classpath '.:./runtime/*' QueryHive ████████:10000 "SELECT 1"
```

## Description

Executes simple query against Hive database using Java POC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-classpath '.:./runtime/*'` | Includes runtime dependencies | Yes |
| `████████:10000` | Hive server address | Yes |
| `"SELECT 1"` | SQL query | Yes |

## Examples

### Basic Usage

```bash
java -classpath '.:./runtime/*' QueryHive ████████:10000 "SELECT 1"
```

## Expected Output

Result of SELECT 1

## Related

- [[procedures/Reproduce-Exploitation-with-Custom-Java-POC]]
