---
id: fe5d5fef-d6bb-4967-83f0-71300fd43c29
name: Query-LDAP-and-Enumerate-Base-DN-with-Nmap
type: procedure
verified: true
submitted: true
created_at: '2020-03-17T22:45:52.428344+00:00'
updated_at: '2023-05-25T19:57:51.161999+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Domain Trust Discovery]]'
sub_techniques: []
tags:
  - active-directory
  - enumeration
commands:
  - '[[commands/nmap-ldap-enumeration-with-scripts]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Query-LDAP-and-Enumerate-Base-DN-with-Nmap

## Summary

Use Nmap to perform anonymous LDAP queries against a domain controller to enumerate the base distinguished name (DN) and basic directory structure, aiding in AD reconnaissance.

## Description

LDAP enumeration via anonymous bind reveals the domain's base DN (e.g., dc=example,dc=com) and OUs without credentials, providing foundational info for user enumeration and Kerberos attacks in AD environments.

## Requirements

- Target with open LDAP port (389)
- Nmap with NSE scripts enabled
- Network connectivity

## Defense

- Disable anonymous LDAP binds on domain controllers
- Monitor LDAP queries in event logs (Event ID 2886/2887/2888)
- Use LDAPS (636) with TLS enforcement

## Objectives

1. Extract base DN for domain targeting
2. Identify OUs and basic structure
3. Confirm anonymous access level

## Instructions

### Step 1: Run LDAP Search Script

**Context**: Probe the LDAP service anonymously to pull directory info.

**Command** ([[commands/nmap-ldap-enumeration-with-scripts]]):
```bash
nmap -p 389 --script ldap-search $_TARGET_IP
```

> The script performs an anonymous bind and searches for base objects. If successful, it outputs the DN and attributes; if bind fails, consider authenticated access.

### Step 2: Parse Output for DN

**Context**: Extract the root DN from results for use in tools like GetNPUsers.

Look for 'Context: dc=domain,dc=com' in output.

**Expected Output**: Sample: | ldap-search: | Context: dc=example,dc=com | dn: dc=example,dc=com.
