---
id: 61aa1952-16cd-47e9-8850-fd44eb4acd53
name: PostgreSQL Password Hash Retrieval
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.521362+00:00'
updated_at: '2023-04-10T20:23:12.814965+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[PostgreSQL injection]]'
- '[[PostgreSQL List Password Hashes]]'
commands:
- '[[Extract user credentials from pg_shadow table]]'
---

# PostgreSQL Password Hash Retrieval

## Summary

PostgreSQL injection is a technique used to exploit vulnerabilities in web applications that use PostgreSQL databases. This specific procedure aims to retrieve password hashes from the pg_shadow table in the PostgreSQL database. The attacker can then use these hashes to perform offline password cra

## Description

# Description

PostgreSQL injection is a technique used to exploit vulnerabilities in web applications that use PostgreSQL databases. This specific procedure aims to retrieve password hashes from the pg_shadow table in the PostgreSQL database. The attacker can then use these hashes to perform offline password cracking attacks to obtain the plaintext passwords. This technique can be used to gain access to sensitive data such as customer information or financial records.

To retrieve the password hashes, the attacker uses SQL injection to execute a SELECT statement on the pg_shadow table. The attacker can then extract the password hashes from the result set and use them for further attacks. This technique requires a good understanding of SQL and the PostgreSQL database schema.

The business value of this procedure is the ability to obtain sensitive information that can be used for further attacks or sold on the black market.

## Requirements

1. Access to the web application that uses a PostgreSQL database.

1. Knowledge of SQL and the PostgreSQL database schema.

## Defense

1. Implement input validation and sanitization to prevent SQL injection attacks.

1. Use strong and unique passwords that are resistant to offline cracking attacks.

1. Implement multi-factor authentication to prevent unauthorized access even if passwords are compromised.

## Objectives

1. Retrieve password hashes from the pg_shadow table in the PostgreSQL database.

1. Use the retrieved password hashes for offline password cracking attacks.

# Instructions

1. This command retrieves the usernames and hashed passwords from the pg_shadow table in PostgreSQL. The pg_shadow table stores password-protected user account information for the PostgreSQL database cluster.

**Code**: [[SELECT usename, passwd FROM pg_shadow]]

> The 'usename' column contains the username and the 'passwd' column contains the hashed password. This command can be useful for database administrators to verify user passwords or for security auditing purposes. It is important to note that the passwords are hashed and cannot be retrieved in plain text.

**Command** ([[Extract user credentials from pg_shadow table]]):

```bash
SELECT usename, passwd FROM pg_shadow
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Extract user credentials from pg_shadow table]]

## Tags

- [[PostgreSQL injection]]
- [[PostgreSQL List Password Hashes]]
