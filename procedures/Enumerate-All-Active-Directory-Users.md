---
id: 6d10cb1d-08a9-4d01-811a-33e5fbfc385c
name: Enumerate-All-Active-Directory-Users
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T19:07:19.064482+00:00'
updated_at: '2023-05-25T19:58:16.378137+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - active-directory
  - network
  - service-attacks
commands:
  - '[[commands/getadusers-enumerate-active-directory-users]]'
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Enumerate-All-Active-Directory-Users

## Summary

This procedure authenticates to a domain controller to list all AD users, including details like last logon, aiding in targeting high-value accounts.

## Description

With valid domain creds, query LDAP via Impacket to dump user info. Helps identify service accounts (SPNs) for Kerberoasting or admins for targeting.

## Requirements

- Domain credentials
- Domain controller IP
- Impacket installed

## Defense

- Limit LDAP queries with ACLs
- Enable AD logging (Event ID 4662)
- Use protected users group to restrict enumeration

## Objectives

1. Authenticate to DC
2. Retrieve user list
3. Identify targets

## Instructions

### Step 1: Query AD Users

**Context**: Use -all for comprehensive details.

**Command** ([[commands/getadusers-enumerate-active-directory-users]]):
```bash
GetADUsers.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -all
```

> Outputs table; filter for SPN-enabled users.

### Step 2: Analyze Output

**Context**: Save and grep for interesting users.

GetADUsers.py ... -all -o users.csv; grep -i 'service' users.csv.

> Success if full list obtained.
