---
id: uuid-c3
data: 'java -classpath ''.:./runtime/*'' QueryHive IP:10000 "SELECT 1"'
tags:
  - test
  - connection
type: command
output: Result of SELECT 1 (value 1)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.608Z'
verified: false
validated: true
submitted: true
---
# java-queryhive-select1

## Command

```bash
java -classpath '.:./runtime/*' QueryHive IP:10000 "SELECT 1"
```

## Description

Runs the compiled QueryHive class to connect to Hive server and execute a test SQL query, verifying connectivity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -classpath '.:./runtime/*' | Includes current dir and JARs | Yes |
| IP:10000 | Hive server address | Yes |
| "SELECT 1" | Test query | Yes |

## Examples

### Basic Usage

```bash
java -classpath '.:./runtime/*' QueryHive IP:10000 "SELECT 1"
```

## Expected Output

Displays query result: 1, confirming successful connection.

## Related

- [[Related Procedure: Connect-to-Open-Apache-Hive-Database]]
