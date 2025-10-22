---
id: a348e0eb-fdb7-4db5-bb13-8d2ca0da0e1d
name: LSA Secrets
type: sub-technique
mitre_id: T1003.004
mitre_url: null
created_at: '2023-04-06T00:31:25.698924+00:00'
updated_at: '2023-04-06T00:31:25.698924+00:00'
parent_technique: '[[Credential Dumping|T1003 - Credential Dumping]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Dumping AD Domain Credentials using Windows Domain Hashdump, Invoke-NinjaCopy,
  and CrackMapExec]]'
---

# LSA Secrets

**MITRE ID**: T1003.004

**Parent Technique**: [[Credential Dumping|T1003 - Credential Dumping]]

This is a sub-technique of T1003 - Credential Dumping.

## Summary

Adversaries with SYSTEM access to a host may attempt to access Local Security Authority (LSA) secrets, which can contain a variety of different credential materials, such as credentials for service accounts.(Citation: Passcape LSA Secrets)(Citation: Microsoft AD Admin Tier Model)(Citation: Tilbury W

## Description

Adversaries with SYSTEM access to a host may attempt to access Local Security Authority (LSA) secrets, which can contain a variety of different credential materials, such as credentials for service accounts.(Citation: Passcape LSA Secrets)(Citation: Microsoft AD Admin Tier Model)(Citation: Tilbury Windows Credentials) LSA secrets are stored in the registry at <code>HKEY_LOCAL_MACHINE\SECURITY\Policy\Secrets</code>. LSA secrets can also be dumped from memory.(Citation: ired Dumping LSA Secrets)

[Reg](https://attack.mitre.org/software/S0075) can be used to extract from the Registry. [Mimikatz](https://attack.mitre.org/software/S0002) can be used to extract secrets from memory.(Citation: ired Dumping LSA Secrets)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Dumping AD Domain Credentials using Windows Domain Hashdump, Invoke-NinjaCopy, and CrackMapExec]]
