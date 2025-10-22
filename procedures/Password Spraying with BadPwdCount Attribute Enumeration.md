---
id: 3e3215ca-7896-4b3d-8c21-585b23780789
name: Password Spraying with BadPwdCount Attribute Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:04.377299+00:00'
updated_at: '2023-04-10T20:36:12.412324+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
- '[[Brute Force|T1110 - Brute Force]]'
tags:
- '[[Active Directory Attacks]]'
- '[[BadPwdCount attribute]]'
- '[[Password spraying]]'
commands:
- '[[crackmapexec ldap users enumeration]]'
---

# Password Spraying with BadPwdCount Attribute Enumeration

## Summary

Password spraying with BadPwdCount attribute enumeration is a common technique used by attackers to gain access to Active Directory user accounts. This attack involves guessing a small set of common passwords against a large number of Active Directory user accounts. By enumerating the BadPwdCount a

## Description

# Description

Password spraying with BadPwdCount attribute enumeration is a common technique used by attackers to gain access to Active Directory user accounts. This attack involves guessing a small set of common passwords against a large number of Active Directory user accounts. By enumerating the BadPwdCount attribute, attackers can determine which accounts have not had their password changed after a certain number of failed login attempts. This provides a list of potential targets that are more likely to have weak passwords.

Technical Explanation: Password spraying is a technique where attackers try a small set of common passwords against a large number of user accounts. This attack is often successful because many users choose weak passwords that are easy to guess. The BadPwdCount attribute is a counter that keeps track of the number of failed login attempts for a user account. By enumerating this attribute, attackers can determine which accounts have not had their password changed after a certain number of failed login attempts. This provides a list of potential targets that are more likely to have weak passwords. Attackers can then use this list to launch a password spraying attack against these accounts.

Business Value: Password spraying with BadPwdCount attribute enumeration can allow attackers to gain access to sensitive information and systems, which can result in data theft, financial loss, and reputational damage.

## Requirements

1. Access to Active Directory environment

1. Credentials with permission to enumerate BadPwdCount attribute

1. Password spraying tool or script

## Defense

1. Enforce strong password policies and require regular password changes

1. Monitor and limit the number of failed login attempts

1. Implement multi-factor authentication for user accounts

## Objectives

1. Gain access to user accounts with weak passwords

1. Compromise Active Directory systems and data

1. Steal sensitive information

# Instructions

1. The 'crackmapexec' command is used to enumerate LDAP users and Kerberos tickets on a remote host. The '-u' option specifies the username to be used for authentication, and the '-p' option specifies the password for the provided username. The '--kdcHost' option specifies the host to use as the Kerberos KDC. The '--users' option specifies to enumerate LDAP users. The output shows the LDAP server, port, domain controller, user, and some additional information like bad password count and password last set time.

**Code**: [[$ crackmapexec ldap 10.0.2.11 -u 'username' -p 'pa]]

> This command is useful for enumerating users and Kerberos tickets on a remote host. It can be used for reconnaissance purposes to gather information about a target network. The output of this command can be used to perform further attacks like password spraying, brute-forcing, or privilege escalation.

**Command** ([[crackmapexec ldap users enumeration]]):

```bash
$ crackmapexec ldap 10.0.2.11 -u 'username' -p 'password' --kdcHost 10.0.2.11 --users
```

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access|TA0006 - Credential Access]]
- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]
- [[Brute Force|T1110 - Brute Force]]

## Commands Used

- [[crackmapexec ldap users enumeration]]

## Tags

- [[Active Directory Attacks]]
- [[BadPwdCount attribute]]
- [[Password spraying]]
