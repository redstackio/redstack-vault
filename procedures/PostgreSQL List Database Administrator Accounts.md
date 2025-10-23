---
id: c50eaf9b-094a-4236-b017-a2fe8bfdf199
name: PostgreSQL List Database Administrator Accounts
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.549012+00:00'
updated_at: '2023-04-10T20:23:21.402353+00:00'
tags:
- '[[PostgreSQL injection]]'
- '[[PostgreSQL List Database Administrator Accounts]]'
commands:
- '[[List all superusers]]'
---

# PostgreSQL List Database Administrator Accounts

## Summary

This procedure involves exploiting a vulnerability in PostgreSQL to list the database administrator accounts. The attacker can use a technique called SQL injection to execute arbitrary SQL commands and obtain sensitive information. By using the 'List Superusers' command, the attacker can obtain a l

## Description

# Description

This procedure involves exploiting a vulnerability in PostgreSQL to list the database administrator accounts. The attacker can use a technique called SQL injection to execute arbitrary SQL commands and obtain sensitive information. By using the 'List Superusers' command, the attacker can obtain a list of all superusers in the database, which includes the database administrator accounts.

From a technical perspective, the attacker would need to identify a vulnerable parameter in the application that interacts with the database. They would then craft a malicious SQL query that would be executed by the database. This query would include the 'List Superusers' command to obtain the list of administrator accounts.

The business value of this procedure is that it allows an attacker to gain access to sensitive information and potentially take control of the database. This can lead to data theft, data modification, and disruptions to business operations.

 

## Requirements

1. Access to a vulnerable web application that interacts with a PostgreSQL database

1. Knowledge of SQL injection techniques

1. Access to a tool for crafting and executing SQL queries

 

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks

1. Implement least privilege access controls to limit the permissions of database users

1. Monitor database logs for suspicious activity

 

## Objectives

1. Obtain a list of all superusers in the database

1. Identify potential targets for further exploitation

 

# Instructions

1. This command lists all the superusers in the PostgreSQL database.

 



**Code**: [[SELECT usename FROM pg_user WHERE usesuper IS TRUE]]



> The 'SELECT' statement is used to retrieve data from the 'pg_user' table. The 'WHERE' clause filters the results to only include users that have the 'usesuper' attribute set to 'TRUE', which indicates that they are superusers. The 'usename' field is selected to display the names of the superusers. This command can be useful for identifying the users who have the ability to perform certain actions that regular users cannot.



**Command** ([[List all superusers]]):

```bash
SELECT usename FROM pg_user WHERE usesuper IS TRUE
```



## Commands Used

- [[List all superusers]]

## Tags

- [[PostgreSQL injection]]
- [[PostgreSQL List Database Administrator Accounts]]


