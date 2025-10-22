---
id: 3d2d1111-5c1f-4a9c-9668-af50dbba7fca
name: NTDS
type: sub-technique
mitre_id: T1003.003
mitre_url: null
created_at: '2023-04-06T00:31:27.152898+00:00'
updated_at: '2023-04-06T00:31:27.152898+00:00'
parent_technique: '[[Credential Dumping|T1003 - Credential Dumping]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Dumping AD Domain Credentials using Windows Domain Hashdump, Invoke-NinjaCopy,
  and CrackMapExec]]'
---

# NTDS

**MITRE ID**: T1003.003

**Parent Technique**: [[Credential Dumping|T1003 - Credential Dumping]]

This is a sub-technique of T1003 - Credential Dumping.

## Summary

Adversaries may attempt to access or create a copy of the Active Directory domain database in order to steal credential information, as well as obtain other information about domain members such as devices, users, and access rights. By default, the NTDS file (NTDS.dit) is located in <code>%SystemRoo

## Description

Adversaries may attempt to access or create a copy of the Active Directory domain database in order to steal credential information, as well as obtain other information about domain members such as devices, users, and access rights. By default, the NTDS file (NTDS.dit) is located in <code>%SystemRoot%\NTDS\Ntds.dit</code> of a domain controller.(Citation: Wikipedia Active Directory)

In addition to looking for NTDS files on active Domain Controllers, adversaries may search for backups that contain the same or similar information.(Citation: Metcalf 2015)

The following tools and techniques can be used to enumerate the NTDS file and the contents of the entire Active Directory hashes.

* Volume Shadow Copy
* secretsdump.py
* Using the in-built Windows tool, ntdsutil.exe
* Invoke-NinjaCopy

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Dumping AD Domain Credentials using Windows Domain Hashdump, Invoke-NinjaCopy, and CrackMapExec]]
