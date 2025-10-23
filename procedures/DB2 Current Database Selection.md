---
id: a61fcfb4-4044-4418-9826-f65cab39c725
name: DB2 Current Database Selection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.726585+00:00'
updated_at: '2023-04-10T20:21:59.021854+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]'
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Current Database]]'
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
commands:
- '[[Select current server]]'
---

# DB2 Current Database Selection

## Summary

The DB2 Current Database Selection procedure is used to obtain information about the current database in use. This information can be used to identify the type of database and version, as well as to determine the level of access that an attacker has to the database. The technical explanation of thi

## Description

# Description

The DB2 Current Database Selection procedure is used to obtain information about the current database in use. This information can be used to identify the type of database and version, as well as to determine the level of access that an attacker has to the database. The technical explanation of this procedure involves injecting SQL commands into the database through user input fields or other vulnerabilities to extract the current database information. The business value of this procedure is that it allows an attacker to gain a better understanding of the target's infrastructure and potentially identify other vulnerabilities to exploit.

 

## Requirements

1. Access to a vulnerable application or system with user input fields or other vulnerabilities that can be exploited to inject SQL commands

 

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Enforce the principle of least privilege to limit access to the database

1. Monitor the database for suspicious activity and unauthorized access attempts

 

## Objectives

1. Obtain information about the current database in use

1. Identify the type of database and version

1. Determine the level of access that an attacker has to the database

 

# Instructions

1. To select the current server, execute the provided SQL statement. This command returns the name of the server that you are currently connected to.

 



**Code**: [[select current server from sysibm.sysdummy1]]



> This command is useful in a multi-server environment where you may have connections to multiple servers. The output of this command can be used to verify that you are connected to the correct server before executing any further commands.



**Command** ([[Select current server]]):

```bash
select current server from sysibm.sysdummy1
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation for Defense Evasion|T1211 - Exploitation for Defense Evasion]]
- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Select current server]]

## Tags

- [[Current Database]]
- [[DB2 Cheatsheet]]
- [[DB2 Injection]]


