---
id: ca24626f-c625-494c-a97f-76454d06f2f5
name: SQL Injection - Admin Password Change
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.652019+00:00'
updated_at: '2023-04-10T20:24:24.058840+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[Insert Statement - ON DUPLICATE KEY UPDATE]]'
- '[[SQL Injection]]'
commands:
- '[[Inject Payload]]'
---

# SQL Injection - Admin Password Change

## Summary

This attack involves exploiting a vulnerability in a web application's SQL database to change the admin password. By injecting SQL code into the web application's input fields, an attacker can modify the SQL query to include an 'ON DUPLICATE KEY UPDATE' statement. This statement allows the attacker

## Description

# Description

This attack involves exploiting a vulnerability in a web application's SQL database to change the admin password. By injecting SQL code into the web application's input fields, an attacker can modify the SQL query to include an 'ON DUPLICATE KEY UPDATE' statement. This statement allows the attacker to update the admin password by inserting a new value into the database. This attack can lead to complete control of the web application and potentially the underlying server.

 

## Requirements

1. Access to the web application's input fields

1. Knowledge of SQL injection techniques

 

## Defense

1. Use parameterized SQL queries to prevent SQL injection attacks

1. Implement input validation to prevent malicious input

1. Limit database privileges to prevent attackers from modifying sensitive data

 

## Objectives

1. Gain access to the web application's admin account

1. Take control of the web application

 

# Instructions

1. Use the provided MySQL injection payload to change the admin password. Replace 'bcrypt_hash_of_your_password_input' with the desired password input that you want to set for the admin account.

 



**Code**: [[Inject using payload:
  attacker_dummy@example.com]]



> The provided MySQL injection attack allows an attacker to change the admin password by using the ON DUPLICATE KEY UPDATE keyword. This keyword tells MySQL to update the `password` column of the already existing row to the provided password hash. By injecting the provided payload, the attacker can insert a new row for their own account and update the password of the admin account in the same query. After this, the attacker can authenticate with the admin account and the new password to gain unauthorized access.



**Command** ([[Inject Payload]]):

```bash
INSERT INTO users (email, password) VALUES ("attacker_dummy@example.com", "bcrypt_hash_of_qwerty"), ("admin@example.com", "bcrypt_hash_of_qwerty") ON DUPLICATE KEY UPDATE password="bcrypt_hash_of_qwerty" -- ", "bcrypt_hash_of_your_password_input");
```



## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Inject Payload]]

## Tags

- [[Insert Statement - ON DUPLICATE KEY UPDATE]]
- [[SQL Injection]]


