---
type: procedure
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/BadPwdCount attribute]]'
  - '[[tags/Password spraying]]'
commands:
  - '[[commands/crackmapexec-ldap-users-enumeration]]'
platforms:
  - Windows
tools:
  - '[[tools/CrackMapExec]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Password-Spraying-with-BadPwdCount-Attribute-Enumeration

## Summary

This procedure uses CrackMapExec to enumerate Active Directory user accounts via LDAP queries, focusing on the BadPwdCount attribute to identify accounts with multiple failed login attempts. These accounts are prime targets for password spraying attacks, where common passwords are tested against many users to avoid account lockouts while discovering valid credentials.

## Description

Password spraying is an effective credential access technique in Active Directory environments, where attackers test a limited set of common passwords (e.g., 'Password123', seasonal variants) against numerous user accounts. To optimize targeting, attackers first enumerate the BadPwdCount attribute, which tracks failed authentication attempts for each user. Accounts with elevated BadPwdCount values but no recent password changes (via pwdLastSet) indicate potential weak passwords or reuse. This procedure authenticates to a domain controller using provided credentials and queries LDAP for user details, outputting badpwdcount and last set times. It targets Windows Active Directory domains and requires network access to a domain controller. Success enables follow-on brute force or spraying to compromise accounts, potentially leading to lateral movement or privilege escalation.

## Requirements

1. Network access to the Active Directory domain controller (typically over LDAP port 389 or LDAPS 636).
2. Valid domain credentials with permissions to query LDAP user attributes (e.g., domain user or service account).
3. CrackMapExec tool installed on the attacker's machine (Python-based, supports Windows/Linux).

## Defense

- Enforce strong password policies, including complexity requirements, regular rotations, and bans on common passwords.
- Implement account lockout thresholds after a low number of failed attempts (e.g., 5-10) to prevent spraying.
- Enable multi-factor authentication (MFA) for all accounts to add a secondary verification layer.
- Monitor LDAP queries for anomalous enumeration patterns using tools like Windows Event Logs (Event ID 4625 for failed logons) or SIEM rules.
- Restrict LDAP access via network segmentation and just-in-time permissions.

## Objectives

1. Enumerate Active Directory user accounts and their BadPwdCount values to identify high-risk targets.
2. Gather pwdLastSet information to prioritize accounts unlikely to have been rotated recently.
3. Prepare a targeted list for password spraying to achieve credential access without triggering lockouts.

## Instructions

### Step 1: Authenticate and Enumerate LDAP Users with BadPwdCount

**Context**: Authenticate to the domain controller using provided credentials and query LDAP for all user accounts. The --users flag triggers enumeration, revealing usernames, badpwdcount (failed attempts), and pwdLastSet (last password change). Filter results manually for accounts with badpwdcount > 0 and stale pwdLastSet to build a spraying target list. This step assumes CrackMapExec is installed; if errors occur (e.g., authentication failure), verify credentials and network connectivity.

**Command** ([[commands/crackmapexec-ldap-users-enumeration]]):

```bash
crackmapexec ldap $_TARGET_DC -u '$_USERNAME' -p '$_PASSWORD' --kdcHost $_TARGET_DC --users
```

> Run this command from a machine with network access to the DC. Replace placeholders with actual values. The output lists users; high badpwdcount indicates repeated failures, making these ideal for spraying common passwords next. If no users appear, check permissions or firewall rules. Export output to a file (e.g., add > users.txt) for parsing.

**Expected Output**:

```
LDAP         10.0.2.11       389    dc01       Guest           [normal] badpwdcount: 0 pwdLastSet: <never>
LDAP         10.0.2.11       389    dc01       krbtgt          [normal] badpwdcount: 0 pwdLastSet: <never>
LDAP         10.0.2.11       389    dc01       Administrator   [normal] badpwdcount: 5 pwdLastSet: 2023-01-15
```

**Success Indicators**:
- Output displays multiple user entries with badpwdcount and pwdLastSet fields.
- No authentication errors (e.g., 'STATUS_LOGON_FAILURE'); credentials are valid for LDAP queries.
