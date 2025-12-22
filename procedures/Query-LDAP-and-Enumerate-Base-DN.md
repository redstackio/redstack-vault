---
id: 8a0ce905-886e-4cd0-b263-e3f868c1c29d
name: Query-LDAP-and-Enumerate-Base-DN
type: procedure
verified: true
submitted: true
created_at: '2019-12-15T22:33:38.252261+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
platforms:
  - Linux
  - Windows
tags:
  - data-exposure
  - network
commands:
  - '[[commands/ldapsearch-query-root-dse-anonymous]]'
  - '[[commands/ldapsearch-query-base-dn-anonymous]]'
tools:
  - '[[tools/OpenLDAP-Utils]]'
validated: true
---

# Query-LDAP-and-Enumerate-Base-DN

## Summary

This procedure uses anonymous LDAP binds to query the root DSE for domain structure and then enumerates the base DN to discover user accounts, providing a foundation for targeted credential attacks in Active Directory environments.

## Description

LDAP enumeration is a discovery technique that leverages anonymous access (common in misconfigured Windows domains) to map the directory structure. The root DSE query reveals the naming context (e.g., DC=example,DC=com), while the base DN query lists objects like users. This is useful in reconnaissance phases to identify valid usernames for brute force without alerting defenders. It targets LDAP servers on port 389 and assumes no authentication is required for basic queries.

## Requirements

- Network access to target's LDAP port (TCP/389)
- ldapsearch tool installed (from OpenLDAP)
- Target IP address
- No credentials needed for anonymous bind

## Defense

- Disable anonymous LDAP binds via Group Policy (Network access: Do not allow anonymous enumeration of SAM accounts)
- Monitor LDAP logs for anonymous queries (Event ID 2886/2887/2888 in Windows Security logs)
- Implement LDAP signing and channel binding to prevent anonymous access

## Objectives

- Retrieve domain naming context from root DSE
- Enumerate sAMAccountNames for user discovery
- Identify domain components for further queries

## Instructions

### Step 1: Query Root DSE for Domain Context

**Context**: This step connects anonymously to LDAP and retrieves the root DSE, which contains the rootDomainNamingContext needed for subsequent queries. It confirms LDAP accessibility.

**Command** ([[commands/ldapsearch-query-root-dse-anonymous]]):
```bash
ldapsearch -x -h $_TARGET_IP -s base
```

> The -x flag enables simple authentication (anonymous), -h specifies the host, and -s base limits to the root object. Success is indicated by the presence of rootDomainNamingContext (e.g., DC=example,DC=com). If bound fails, the server may require authentication.

### Step 2: Query Base DN for User Enumeration

**Context**: Using the naming context from Step 1, query the subtree to list domain objects, focusing on users via sAMAccountName. This reveals potential targets for brute force.

**Command** ([[commands/ldapsearch-query-base-dn-anonymous]]):
```bash
ldapsearch -x -h $_TARGET_IP -b 'dc=$_ENTRY1,dc=$_ENTRY2' | grep sAMAccountName
```

> Replace $_ENTRY1 and $_ENTRY2 with domain components (e.g., example,com). The grep filters for usernames. Expected: Lines like sAMAccountName: user1. Pipe to a file for later use if needed.
