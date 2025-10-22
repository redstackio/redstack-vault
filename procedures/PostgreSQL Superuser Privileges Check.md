---
id: 522e4e4a-1179-4c9a-b378-ddfe0ce73e86
name: PostgreSQL Superuser Privileges Check
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.603271+00:00'
updated_at: '2023-04-10T20:23:22.107218+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
tags:
- '[[PostgreSQL Check if Current User is Superuser]]'
- '[[PostgreSQL injection]]'
commands:
- '[[Check Current User Superuser Privileges]]'
- '[[Check Superuser Privileges]]'
- '[[Check Superuser Status of Current User]]'
---

# PostgreSQL Superuser Privileges Check

## Summary

The PostgreSQL Superuser Privileges Check procedure is used to determine if the current user has superuser privileges within the PostgreSQL database. This procedure takes advantage of a vulnerability in the PostgreSQL database that allows for SQL injection attacks. By exploiting this vulnerability,

## Description

# Description

The PostgreSQL Superuser Privileges Check procedure is used to determine if the current user has superuser privileges within the PostgreSQL database. This procedure takes advantage of a vulnerability in the PostgreSQL database that allows for SQL injection attacks. By exploiting this vulnerability, an attacker can gain access to sensitive information or execute arbitrary code within the database. This procedure can be used by an attacker as part of a larger attack campaign to gain access to the target's network or steal sensitive data.

To perform this procedure, the attacker must have access to the target's network and be able to send SQL queries to the PostgreSQL database. The attacker can use a variety of tools to execute this procedure, including SQL injection tools and custom scripts.

This procedure is valuable to attackers because it allows them to determine if the current user has superuser privileges within the PostgreSQL database. If the current user has superuser privileges, the attacker can use these privileges to execute arbitrary code within the database, steal sensitive data, or gain access to the target's network.

## Requirements

1. Access to the target's network

1. Ability to send SQL queries to the PostgreSQL database

## Defense

1. Implement input validation to prevent SQL injection attacks

1. Limit user privileges within the PostgreSQL database

1. Regularly update and patch the PostgreSQL database to address known vulnerabilities

## Objectives

1. Determine if the current user has superuser privileges within the PostgreSQL database

# Instructions

1. To check if a user has superuser privileges, run the following commands:

1. SHOW is_superuser;
This command will display whether the current user is a superuser or not.

2. SELECT current_setting('is_superuser');
This command will return the value of the is_superuser setting, which is 'on' for superusers and 'off' for regular users.

3. SELECT usesuper FROM pg_user WHERE usename = CURRENT_USER;
This command will return whether the current user has the usesuper attribute set to 'true' or 'false'. If it's 'true', then the user has superuser privileges.

**Code**: [[SHOW is_superuser; 
SELECT current_setting('is_sup]]

> The above commands can be used to determine whether a user has superuser privileges in a PostgreSQL database. Superuser privileges allow a user to perform any operation on the database, including creating and deleting databases and users, and modifying system settings. It's important to ensure that only trusted users have superuser privileges, as they can potentially cause damage to the database if they make a mistake.

**Command** ([[Check Superuser Privileges]]):

```bash
SHOW is_superuser;
```

**Command** ([[Check Current User Superuser Privileges]]):

```bash
SELECT current_setting('is_superuser');
```

**Command** ([[Check Superuser Status of Current User]]):

```bash
SELECT usesuper FROM pg_user WHERE usename = CURRENT_USER;
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]

## Commands Used

- [[Check Current User Superuser Privileges]]
- [[Check Superuser Privileges]]
- [[Check Superuser Status of Current User]]

## Tags

- [[PostgreSQL Check if Current User is Superuser]]
- [[PostgreSQL injection]]
