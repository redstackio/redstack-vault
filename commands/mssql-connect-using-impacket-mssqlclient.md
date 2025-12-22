---
id: new-uuid-for-this
name: mssql-connect-using-impacket-mssqlclient
type: command
executor: bash
data: 'python mssqlclient.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_MSSQL_IP -port $_PORT'
output: null
created_at: '2023-04-06T03:56:33.953478+00:00'
updated_at: '2023-04-10T20:22:46.090384+00:00'
platforms:
  - Linux
tags:
  - mssql
  - connection
  - impacket
verified: true
validated: true
---

# mssql-connect-using-impacket-mssqlclient

## Command

```bash
python mssqlclient.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_MSSQL_IP -port $_PORT
```

## Description

Connects to an MSSQL server using Impacket's mssqlclient.py, supporting NTLM and domain authentication for interactive SQL sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain for Windows auth (e.g., WORKGROUP) | Yes if domain-joined |
| $_USERNAME | Username (e.g., Administrator) | Yes |
| $_PASSWORD | Password | Yes |
| $_MSSQL_IP | Target IP | Yes |
| -port $_PORT | MSSQL port (default 1433) | No |

## Examples

### Basic Usage

```bash
python mssqlclient.py WORKGROUP/Administrator:password@192.168.1.100 -port 1433
```

## Expected Output

Connection success with prompt:

```
[+] Connecting to 192.168.1.100:1433...
[*] Authenticated!
SQL> 
```

## Related

- [[procedures/MSSQL-Command-Execution-via-xp-cmdshell]]
- [[commands/mssql-connect-using-sqsh]]
