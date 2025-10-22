---
id: 940d0525-2434-487b-bc5b-b40e57cbad53
name: Kerberos Pre-Auth Bruteforcing with Kerbrute
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.229151+00:00'
updated_at: '2023-04-10T20:26:23.708098+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
techniques:
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Active Directory Attacks]]'
- '[[Kerberos pre-auth bruteforcing]]'
- '[[Password spraying]]'
commands:
- '[[Enumerate passwords]]'
- '[[Enumerate usernames]]'
---

# Kerberos Pre-Auth Bruteforcing with Kerbrute

## Summary

Kerberos pre-auth bruteforcing is a technique used to obtain valid user credentials by guessing the password of a user account. Kerbrute is a powerful tool that can be used to automate this process. An attacker can use this technique to gain access to sensitive information and systems within an org

## Description

# Description

Kerberos pre-auth bruteforcing is a technique used to obtain valid user credentials by guessing the password of a user account. Kerbrute is a powerful tool that can be used to automate this process. An attacker can use this technique to gain access to sensitive information and systems within an organization.

Kerberos is a network authentication protocol used by Active Directory to authenticate users and computers. Kerberos pre-authentication is a mechanism used to verify the user's identity before the actual authentication process begins. By default, Kerberos pre-authentication is enabled in Active Directory, which means that an attacker needs to guess the password of a user account before they can authenticate to the domain.

Using Kerbrute, an attacker can automate the process of guessing passwords for user accounts. This tool can also be used to perform password spraying attacks, where a list of common passwords is tried against a large number of user accounts.

## Requirements

1. Access to the target network

1. Valid domain user or computer account credentials

1. Kerbrute tool installed on the attacker's machine

## Defense

1. Enforce strong password policies and multi-factor authentication to prevent password guessing attacks

1. Monitor for failed login attempts and alert on suspicious activity

1. Disable Kerberos pre-authentication for service accounts and other non-user accounts where possible

## Objectives

1. Obtain valid user credentials through Kerberos pre-auth bruteforcing

1. Gain access to sensitive information and systems within an organization

# Instructions

1. Kerbrute is a network service brute-forcing tool that can help you identify valid user accounts on a domain. The tool supports Kerberos-based authentication and can be used to test the strength of user passwords. Kerbrute can be used to perform password spraying attacks or brute-force attacks against a domain. The tool can also be used to enumerate valid usernames on a domain. 

**Code**: [[kerbrute]]

> To use Kerbrute, you will need to provide the tool with a list of usernames and a list of passwords. The tool will then attempt to authenticate each username using each password until it finds a valid combination. Kerbrute supports various authentication methods, including Kerberos, NTLM, and LDAP. You can also use the tool to perform other tasks, such as DNS enumeration and service scanning. Kerbrute is a powerful tool that should be used with caution, as it can potentially cause account lockouts or other security issues if used improperly.

**Command** ([[Enumerate usernames]]):

```bash
kerbrute userenum --dc CONTROLLER.local -d CONTROLLER.local /path/to/userlist.txt
```

**Command** ([[Enumerate passwords]]):

```bash
kerbrute bruteforce --dc CONTROLLER.local -d CONTROLLER.local user1 /path/to/passwordlist.txt
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]

### Techniques

- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[Enumerate passwords]]
- [[Enumerate usernames]]

## Tags

- [[Active Directory Attacks]]
- [[Kerberos pre-auth bruteforcing]]
- [[Password spraying]]
