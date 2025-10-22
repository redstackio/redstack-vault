---
id: 5d8933df-6b1c-43b1-9a9f-7d948f2466e0
name: SQL Injection Authentication Bypass with Raw MD5 and SHA1 Hashes
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:36.581692+00:00'
updated_at: '2023-04-10T20:24:18.431926+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]'
tags:
- '[[Authentication Bypass (Raw MD5 SHA1)]]'
- '[[SQL Injection]]'
commands:
- '[[Boolean true]]'
- '[[Calculate MD5 and SHA1 hash values]]'
---

# SQL Injection Authentication Bypass with Raw MD5 and SHA1 Hashes

## Summary

This procedure involves using SQL injection techniques to bypass authentication mechanisms that rely on raw MD5 or SHA1 hashes. An attacker can use the 'Query Admin Password with MD5 Hash' command to retrieve the hashed password, and then use 'Hashing Functions' to generate the same hash for a pass

## Description

# Description

This procedure involves using SQL injection techniques to bypass authentication mechanisms that rely on raw MD5 or SHA1 hashes. An attacker can use the 'Query Admin Password with MD5 Hash' command to retrieve the hashed password, and then use 'Hashing Functions' to generate the same hash for a password of their choice. The attacker can then use the 'SQL Injection Attack' and 'Comma Separated String Injection' commands to bypass the authentication mechanism and gain access to the system. This attack can be devastating as it allows the attacker to gain access to sensitive data and systems.

## Requirements

1. Access to a vulnerable web application

1. Knowledge of SQL injection techniques

1. Ability to generate MD5 or SHA1 hashes

## Defense

1. Use strong password hashing algorithms such as bcrypt or scrypt

1. Implement multi-factor authentication mechanisms

1. Regularly audit and monitor web application logs for suspicious activity

## Objectives

1. Bypass authentication mechanisms that rely on raw MD5 or SHA1 hashes

1. Gain access to sensitive data and systems

# Instructions

1. This command queries the admin table for a matching password hash that has been generated using the MD5 algorithm.

**Code**: [["SELECT * FROM admin WHERE pass = '".md5($password]]

> The command takes in a password as an argument, and then generates an MD5 hash of that password. It then queries the admin table to find a matching password hash. If a match is found, the query returns all the columns of that row from the admin table. This command is useful for authenticating users in a web application.

2. When accepting user input that may contain commas, ensure that the input is properly sanitized and validated. If the input is used in a comma-separated list, consider using a different delimiter or properly escaping the comma character.

**Code**: [[true]]

> An attacker can exploit this vulnerability by injecting a comma-separated string that can be interpreted as multiple values. This can lead to various attacks such as privilege escalation, SQL injection, and command injection.

**Command** ([[Boolean true]]):

```bash
true
```

3. The SQL Injection Attack command is used to exploit vulnerabilities in a target application's database. The attacker inserts malicious SQL statements into an entry field that is then executed by the application's database. This can result in unauthorized access, manipulation, or deletion of data within the database.

**Code**: [[' or 'SOMETHING]]

> The argument ' or 'SOMETHING' is a common example of a SQL injection attack. The single quote character is used to terminate a string in SQL, so by adding an additional statement after the closing quote, the attacker can add their own SQL code to the original query. This can allow the attacker to bypass authentication, view sensitive data, or modify the database in unintended ways. It is important for developers to sanitize user input and use prepared statements to prevent SQL injection attacks.

4. The md5() function calculates the MD5 hash of a string. The first argument is the string to be hashed and the second argument is a boolean value, which indicates whether the output should be in binary format or not. The sha1() function is similar, but it calculates the SHA-1 hash of the string.

**Code**: [[md5("ffifdyop", true) = 'or'6�]��!r,��b
sha1("3fD]]

> The MD5 and SHA-1 hashing functions are commonly used for data encryption and security purposes. The md5() function returns a 32-character hexadecimal number, while the sha1() function returns a 40-character hexadecimal number. The second argument of both functions is optional and defaults to false, which means that the output will be in hexadecimal format. If the second argument is set to true, the output will be in binary format.

**Command** ([[Calculate MD5 and SHA1 hash values]]):

```bash
md5("ffifdyop", true) = 'or'6�]��!r,��b
sha1("3fDf ", true) = Q�u'='�@�[�t�- o��_-!
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Exploitation for Credential Access|T1212 - Exploitation for Credential Access]]

## Commands Used

- [[Boolean true]]
- [[Calculate MD5 and SHA1 hash values]]

## Tags

- [[Authentication Bypass (Raw MD5 SHA1)]]
- [[SQL Injection]]
