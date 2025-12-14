---
id: uuid-sqlmap-enum
data: sqlmap -r r.txt --level=2 --risk=2 --dbs
tags:
  - sqli
  - enumeration
  - automation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.908Z'
verified: false
validated: true
submitted: true
---
# sqlmap-database-enumeration

## Command

```bash
sqlmap -r r.txt --level=2 --risk=2 --dbs
```

## Description

Runs sqlmap to detect SQL injection from a request file, identify the DBMS, and enumerate database names using time-based techniques.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r | Load HTTP request from file | Yes |
| --level=2 | Test more injection points and payloads | No |
| --risk=2 | Include riskier payloads that may affect database | No |
| --dbs | Enumerate DBMS databases | Yes |

## Examples

### Basic Usage

```bash
sqlmap -r r.txt --dbs
```

### Advanced Usage

With higher risk for thorough testing:

```bash
sqlmap -r r.txt --level=2 --risk=2 --dbs
```

## Expected Output

Output includes: [INFO] the back-end DBMS is MySQL >= 5.0.12, followed by a list of databases like ['information_schema', 'atavist_db'].

## Related

- [[commands/sqlmap-detect-only]] (hypothetical for detection phase)
