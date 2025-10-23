---
id: 8a0ce905-886e-4cd0-b263-e3f868c1c29d
name: Query LDAP and Enumerate the Base DN (ldapsearch)
type: procedure
verified: false
submitted: false
created_at: '2019-12-15T22:33:38.252261+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Account Discovery|T1087 - Account Discovery]]'
platforms:
- Linux
- Windows
tags:
- '[[data exposure]]'
- '[[Network]]'
commands:
- '[[Query LDAP Root DSE with Anonymous Bind]]'
- '[[Query the Base DN with Anonymous Bind]]'
---

# Query LDAP and Enumerate the Base DN (ldapsearch)

## Summary

Connect to LDAP with anonymous bind and enumerate the root DSA-specific Entry (DSE), then use the result to enumerate the base DN. 

## Description

# Description

Connect to LDAP with anonymous bind and enumerate the root DSA-specific Entry (DSE), then use the result to enumerate the base DN.



# Instructions

1. Enumerate the root DSE object





**Command** ([[Query LDAP Root DSE with Anonymous Bind]]):

```bash
ldapsearch -x -h $_TARGET_IP -s base
```



A successful query will return the "rootDomainNamingContext", which lists the domain's domain components (DC). eg: "dc=corporatehq,dc=com"  = "corporatehq.com"



2. Enumerate the base object using the "rootDomainNamingContext" from step 1.





**Command** ([[Query the Base DN with Anonymous Bind]]):

```bash
ldapsearch -x -h $_TARGET_IP -b 'dc=$_ENTRY1,dc=$_ENTRY2'
```



Tip: Append " | grep sAMAccountName" to the previous command to only show account names.



## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Account Discovery|T1087 - Account Discovery]]

## Commands Used

- [[Query LDAP Root DSE with Anonymous Bind]]
- [[Query the Base DN with Anonymous Bind]]

## Tags

- [[data exposure]]
- [[Network]]


