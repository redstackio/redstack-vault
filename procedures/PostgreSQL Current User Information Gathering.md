---
id: c8c6ec7c-f586-43e7-b569-4a7609af72ed
name: PostgreSQL Current User Information Gathering
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.456901+00:00'
updated_at: '2023-04-10T20:23:19.527470+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[PostgreSQL Current User]]'
- '[[PostgreSQL injection]]'
commands:
- '[[Get current user]]'
- '[[Get current username]]'
- '[[Get session user]]'
- '[[List all PostgreSQL users]]'
- '[[List all users]]'
---

# PostgreSQL Current User Information Gathering

## Summary

The PostgreSQL Current User Information Gathering procedure is used to gather information about the current user on a PostgreSQL database through SQL injection. This technique can be used to determine the level of access a user has to the database and potentially escalate privileges. This procedure

## Description

# Description

The PostgreSQL Current User Information Gathering procedure is used to gather information about the current user on a PostgreSQL database through SQL injection. This technique can be used to determine the level of access a user has to the database and potentially escalate privileges. This procedure involves injecting SQL code into the PostgreSQL database to extract information about the current user. Once the information is obtained, an attacker can use it to plan further attacks on the database.

 

## Requirements

1. Access to the PostgreSQL database

1. Knowledge of SQL injection techniques

 

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Use parameterized queries to prevent SQL injection attacks

1. Limit user privileges to reduce the impact of a successful attack

 

## Objectives

1. To gather information about the current user on a PostgreSQL database

1. To determine the level of access a user has to the database

1. To potentially escalate privileges

 

# Instructions

1. To retrieve user information in PostgreSQL, use one of the following commands:

1. SELECT user; - Returns the name of the current database user.
2. SELECT current_user; - Returns the name of the current database user.
3. SELECT session_user; - Returns the name of the user that owns the current session.
4. SELECT usename FROM pg_user; - Returns a list of all users in the PostgreSQL cluster.
5. SELECT getpgusername(); - Returns the name of the current database user.

 



**Code**: [[SELECT user;
SELECT current_user;
SELECT session_u]]



> The commands listed above are used to retrieve information about users in a PostgreSQL database. The first three commands return the name of the current user or the user that owns the current session. The fourth command returns a list of all users in the PostgreSQL cluster. The fifth command returns the name of the current database user. These commands can be useful for troubleshooting and auditing purposes.



**Command** ([[List all users]]):

```bash
SELECT user;
```





**Command** ([[Get current user]]):

```bash
SELECT current_user;
```





**Command** ([[Get session user]]):

```bash
SELECT session_user;
```





**Command** ([[List all PostgreSQL users]]):

```bash
SELECT usename FROM pg_user;
```





**Command** ([[Get current username]]):

```bash
SELECT getpgusername();
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[Get current user]]
- [[Get current username]]
- [[Get session user]]
- [[List all PostgreSQL users]]
- [[List all users]]

## Tags

- [[PostgreSQL Current User]]
- [[PostgreSQL injection]]


