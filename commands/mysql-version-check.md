---
id: 38c84c73-526f-4226-b45a-0e1ac12472e4
name: mysql-version-check
type: command
executor: bash
data: mysql --version
output: null
created_at: '2023-04-06T03:56:34.912644+00:00'
updated_at: '2023-04-10T20:22:50.539408+00:00'
platforms:
  - Linux
tags:
  - database
  - version
verified: true
validated: true
---

# mysql-version-check

## Command

```bash
mysql --version
```

## Description

This command checks the installed MySQL client version from the command line, helping verify compatibility for SQL injection testing environments (requires MySQL >=4.1).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| mysql | MySQL client executable | Built-in |
| --version | Display version information | Yes |

## Examples

### Basic Usage

```bash
mysql --version
```

## Expected Output

mysql  Ver 14.14 Distrib 5.7.44, for Linux (x86_64) using  EditLine wrapper

## Related

- [[procedures/MySQL-Union-Based-Injection-to-Extract-Column-Names]]
