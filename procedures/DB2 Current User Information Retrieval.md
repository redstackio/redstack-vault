---
id: 17f8e2a1-90f8-4ee2-a0e7-1bd581948121
name: DB2 Current User Information Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:32.599155+00:00'
updated_at: '2023-04-10T20:21:57.597075+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Query Registry|T1012 - Query Registry]]'
tags:
- '[[Current User]]'
- '[[DB2 Cheatsheet]]'
- '[[DB2 Injection]]'
---

# DB2 Current User Information Retrieval

## Summary

This procedure involves the retrieval of the current user information from a DB2 database through SQL injection. By exploiting vulnerabilities in the application that interacts with the database, an attacker can inject malicious SQL code that retrieves information about the current user. This infor

## Description

# Description

This procedure involves the retrieval of the current user information from a DB2 database through SQL injection. By exploiting vulnerabilities in the application that interacts with the database, an attacker can inject malicious SQL code that retrieves information about the current user. This information can include the username, privileges, and other sensitive data. From a technical perspective, this attack involves crafting SQL queries that exploit vulnerabilities in the application's input validation and sanitization mechanisms. The business value of this attack is that it can provide an attacker with valuable information that can be used to further compromise the system or steal sensitive data.

 

## Requirements

1. Access to the application that interacts with the DB2 database

1. Knowledge of SQL injection techniques

 

## Defense

1. Implement input validation and sanitization mechanisms to prevent SQL injection attacks

1. Use prepared statements or parameterized queries to mitigate the risk of SQL injection attacks

1. Regularly update and patch the application and database to address known vulnerabilities

 

## Objectives

1. Retrieve current user information from a DB2 database

1. Gain insight into the privileges and access levels of the current user

 

# Instructions

1. This command retrieves information about the currently logged in user. There are three different commands that are executed in this query. The first command retrieves the name of the current user. The second command retrieves the name of the current session user. The third command retrieves the name of the current system user.

 



**Code**: [[select user from sysibm.sysdummy1
select session_u]]



> The 'user' command retrieves the name of the current user. The 'session_user' command retrieves the name of the current session user. The 'system_user' command retrieves the name of the current system user. These commands are useful for identifying the user who is currently logged in to the system and for auditing purposes.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Query Registry|T1012 - Query Registry]]

## Tags

- [[Current User]]
- [[DB2 Cheatsheet]]
- [[DB2 Injection]]


