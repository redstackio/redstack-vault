---
id: 82b17d6c-00f8-47e7-a8cf-82448c825a31
name: Abusing Active Directory ACLs/ACEs to Retrieve LAPS Passwords
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.934873+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[techniques/Unsecured Credentials/.005 - Credentials in Registry]]'
tags:
  - abusing-active-directory-acls-aces
  - active-directory-attacks
  - read-laps-password
commands:
  - '[[commands/bloodyad-get-object-attributes-for-laps-password]]'
tools:
  - '[[tools/BloodHound]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Abusing Active Directory ACLs/ACEs to Retrieve LAPS Passwords

## Summary

This procedure demonstrates how to abuse Active Directory Access Control Lists (ACLs) and Access Control Entries (ACEs) to gain unauthorized access to Local Administrator Password Solution (LAPS) passwords stored in AD attributes. By modifying permissions on the ms-Mcs-AdmPwd attribute, an attacker with limited privileges can read local admin passwords for domain-joined computers, enabling lateral movement and privilege escalation.

## Description

LAPS is a Microsoft solution that manages local administrator passwords for domain-joined systems by randomly generating and storing them in the ms-Mcs-AdmPwd attribute in Active Directory. By default, access to this attribute is restricted, but misconfigurations in AD ACLs—such as overly permissive ACEs or improper delegation—can allow attackers to query or modify these permissions. This procedure focuses on identifying and exploiting such misconfigurations to retrieve LAPS passwords without needing domain admin rights. It is typically used in post-compromise scenarios where the attacker has domain user credentials and aims to access local admin accounts on target machines. The technique relies on tools like PowerShell Active Directory module or Python-based AD interrogation scripts to enumerate and extract the attributes.

## Requirements

1. Domain user credentials with read access to AD objects and potential ability to modify ACLs (e.g., via delegated permissions).
2. Access to a domain-joined system or network segment with AD connectivity (e.g., via LDAP over port 389/636).
3. Installed tools: Active Directory PowerShell module (for enumeration) and BloodHound or bloodyAD.py (for attribute querying).
4. Knowledge of the target computer's name (e.g., LAPS_PC$) and the LAPS schema extensions in the domain.

## Defense

- Regularly audit AD ACLs and ACEs using tools like BloodHound or AD auditing scripts to identify permissive permissions on sensitive attributes like ms-Mcs-AdmPwd.
- Implement least privilege principles by restricting write access to LAPS attributes to only necessary groups (e.g., Domain Admins) and monitor for unauthorized changes via Event ID 5136 (Directory Service Changes).
- Enable LAPS auditing and integrate with SIEM for alerts on LAPS attribute reads; use Group Policy to enforce strict password rotation and limit delegation.

## Objectives

1. Identify domain-joined computers with expired or retrievable LAPS passwords.
2. Exploit AD ACL misconfigurations to read the ms-Mcs-AdmPwd attribute.
3. Obtain local administrator credentials for lateral movement to target systems.

## Instructions

### Step 1: Enumerate Computers with LAPS Passwords

**Context**: Begin by querying Active Directory for computers that have LAPS passwords set, focusing on those with expired passwords to prioritize high-value targets. This step uses PowerShell to filter AD objects based on the ms-Mcs-AdmPwdExpirationTime attribute, revealing systems ready for password retrieval.

**Code** ([[codes/enumerate-computers-with-expired-laps-passwords]]):

```powershell
Get-ADComputer -Filter {ms-Mcs-AdmPwdExpirationTime -like '*'} -Properties 'ms-Mcs-AdmPwd','ms-Mcs-AdmPwdExpirationTime'
```

> This command retrieves a list of computers with non-null expiration times, including the password (if accessible) and expiration details. Run it from a domain-joined machine with the Active Directory module imported. If ACLs block direct password access, proceed to abuse them in the next step. Expected output includes computer names, passwords (if permitted), and timestamps.

### Step 2: Retrieve LAPS Password via Attribute Query

**Context**: If direct access is blocked, abuse AD ACLs by ensuring your credentials have read permissions on the ms-Mcs-AdmPwd attribute for the target computer object. Use a tool like bloodyAD.py to query the specific attributes without triggering broader alerts.

**Command** ([[commands/bloodyad-get-object-attributes-for-laps-password]]):

```bash
bloodyAD.py -u john.doe -d bloody -p Password512 --host 192.168.10.2 getObjectAttributes LAPS_PC$ ms-Mcs-AdmPwd,ms-Mcs-AdmPwdExpirationTime
```

> Replace placeholders with actual username (-u), domain (-d), password (-p), DC host (--host), computer name (LAPS_PC$), and attributes. This queries the AD object for the LAPS password and expiration. If successful, it outputs the plaintext password, confirming ACL abuse. If permission denied, investigate and modify ACEs using tools like PowerView for escalation.
