---
id: 54ef9e6e-6414-4870-8f3c-2b46c38c8cd3
name: Nested Impersonation Attack
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.094259+00:00'
updated_at: '2023-04-10T20:36:46.063156+00:00'
tags:
- '[[Exploiting Nested Impersonation]]'
- '[[Manual SQL Server Queries]]'
- '[[MSSQL Server]]'
commands:
- '[[Check if user is sysadmin]]'
- '[[Execute as sa and check if user is sysadmin]]'
- '[[Execute as stduser and get current user]]'
- '[[Get current user]]'
- '[[Get current user]]'
- '[[Get original login]]'
---

# Nested Impersonation Attack

## Summary

A nested impersonation attack is a technique used by attackers to escalate privileges and gain access to sensitive data by exploiting the trust relationship between different SQL Server instances. This attack involves the use of a compromised account with elevated privileges to impersonate other ac

## Description

# Description

A nested impersonation attack is a technique used by attackers to escalate privileges and gain access to sensitive data by exploiting the trust relationship between different SQL Server instances. This attack involves the use of a compromised account with elevated privileges to impersonate other accounts with even higher privileges, allowing the attacker to move laterally through the network and gain access to sensitive data.

To execute this attack, the attacker first needs to gain access to a SQL Server instance with a compromised account. They can then use this account to impersonate other accounts with higher privileges, such as the SQL Server Agent account, and gain access to sensitive data. This attack can be difficult to detect as the attacker is using legitimate credentials and is not creating any new processes or connections.

The business value of this attack is that it can allow attackers to gain access to sensitive data and intellectual property, which can be used for financial gain or to gain a competitive advantage in the market.

## Requirements

1. Access to a compromised account with elevated privileges

1. Access to a SQL Server instance

## Defense

1. Implement the principle of least privilege to limit the privileges of user accounts

1. Implement multi-factor authentication to prevent unauthorized access to user accounts

1. Monitor and analyze logs for suspicious activity, such as multiple failed login attempts or unusual access patterns

## Objectives

1. Escalate privileges to gain access to sensitive data

1. Move laterally through the network

1. Access data that is not normally accessible with the compromised account

# Instructions

1. The above SQL commands are used for user authentication and authorization. The SELECT SYSTEM_USER command returns the name of the current user. The IS_SRVROLEMEMBER('sysadmin') command returns 1 if the current user is a member of the sysadmin server role, otherwise it returns 0. The EXECUTE AS LOGIN = 'stduser' command switches the context of the current session to the specified login. The EXECUTE AS LOGIN = 'sa' command switches the context of the current session back to the original login. The SELECT ORIGINAL_LOGIN() command returns the name of the original login that connected to the server.

**Code**: [[SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadm]]

> The purpose of these commands is to ensure that only authorized users are able to access the data and perform certain actions on the database. The SELECT SYSTEM_USER and SELECT ORIGINAL_LOGIN() commands are used to check the current user and the original login respectively. The IS_SRVROLEMEMBER('sysadmin') command is used to check if the current user is a member of the sysadmin server role, which has full control over the server. The EXECUTE AS LOGIN command is used to switch the context of the current session to a different login, which can be useful for testing or troubleshooting purposes. It is important to ensure that only authorized users are granted the sysadmin server role and that the EXECUTE AS LOGIN command is used judiciously to prevent unauthorized access to the system.

**Command** ([[Get current user]]):

```bash
SELECT SYSTEM_USER
```

**Command** ([[Check if user is sysadmin]]):

```bash
SELECT IS_SRVROLEMEMBER('sysadmin')
```

**Command** ([[Execute as stduser and get current user]]):

```bash
EXECUTE AS LOGIN = 'stduser'
SELECT SYSTEM_USER
```

**Command** ([[Execute as sa and check if user is sysadmin]]):

```bash
EXECUTE AS LOGIN = 'sa'
SELECT IS_SRVROLEMEMBER('sysadmin')
```

**Command** ([[Get original login]]):

```bash
SELECT ORIGINAL_LOGIN()
```

**Command** ([[Get current user]]):

```bash
SELECT SYSTEM_USER
```

## Commands Used

- [[Check if user is sysadmin]]
- [[Execute as sa and check if user is sysadmin]]
- [[Execute as stduser and get current user]]
- [[Get current user]]
- [[Get current user]]
- [[Get original login]]

## Tags

- [[Exploiting Nested Impersonation]]
- [[Manual SQL Server Queries]]
- [[MSSQL Server]]
