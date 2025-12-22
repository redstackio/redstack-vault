---
id: 6d10cb1d-08a9-4d01-811a-33e5fbfc385c
name: enumerate-active-directory-users-authenticated
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T19:07:19.064482+00:00'
updated_at: '2023-05-25T19:58:16.378137+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[T1087.002]] - Domain Account'
sub_techniques: []
tags:
  - active-directory
  - network
  - service-attacks
commands:
  - '[[commands/getadusers-enumerate-ad-users]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Enumerate Active Directory Users Authenticated

## Summary

Using valid domain credentials, this procedure queries the domain controller to list all AD users, including details like emails and logon times. It provides a user inventory for targeting in Kerberoasting or phishing.

## Description

Impacket's GetADUsers.py performs LDAP queries over SMB to enumerate users. With GPP-obtained creds, attackers gain a full directory dump, revealing privileged accounts (e.g., admins) and service principals for further attacks.

## Requirements

1. Valid domain username/password (from GPP)
2. Impacket suite installed (pip install impacket)
3. Domain controller IP
4. Port 445/389 open

## Defense

- Limit LDAP/SMB query rights; use protected users group
- Enable AD logging (Event ID 4662) and monitor for bulk queries
- Implement Just Enough Administration (JEA) for least privilege

## Objectives

1. Authenticate to DC with low-priv creds
2. Dump all user objects
3. Identify high-value targets (admins, SPNs)

## Instructions

### Step 1: Prepare Credentials

**Context**: Format creds as DOMAIN/USER:PASS.

No command; set $_DOMAIN, $_USERNAME, $_PASSWORD.

### Step 2: Query All Users

**Context**: Use -all flag for comprehensive details.

**Command** ([[commands/getadusers-enumerate-ad-users]]):
```bash
GetADUsers.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DC_IP -all
```

> Expected: Table with Name, Email, PasswordLastSet, LastLogon.

### Step 3: Filter and Analyze

**Context**: Grep for admins or SPN users.

```bash
GetADUsers.py ... | grep -i admin
```

> Identifies targets for Kerberoasting.
