---
id: 3dddb617-bd25-4195-9be3-672c2efb9de5
name: Security Account Manager
type: sub-technique
mitre_id: T1003.002
mitre_url: null
created_at: '2023-04-06T00:31:25.599533+00:00'
updated_at: '2023-04-06T00:31:25.599533+00:00'
parent_technique: '[[Credential Dumping|T1003 - Credential Dumping]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Automated Password Extraction from SYSVOL and Group Policy Preferences]]'
- '[[Azure AD Connect - Password Extraction via AD Sync Account DCSync]]'
- '[[Dumping AD Domain Credentials using Windows Domain Hashdump, Invoke-NinjaCopy,
  and CrackMapExec]]'
- '[[NTDS Reversible Encryption Dumping]]'
---

# Security Account Manager

**MITRE ID**: T1003.002

**Parent Technique**: [[Credential Dumping|T1003 - Credential Dumping]]

This is a sub-technique of T1003 - Credential Dumping.

## Summary

Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either through in-memory techniques or through the Windows Registry where the SAM database is stored. The SAM is a database file that contains local accounts for the host, typically those found wi

## Description

Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either through in-memory techniques or through the Windows Registry where the SAM database is stored. The SAM is a database file that contains local accounts for the host, typically those found with the <code>net user</code> command. Enumerating the SAM database requires SYSTEM level access.

A number of tools can be used to retrieve the SAM file through in-memory techniques:

* pwdumpx.exe
* [gsecdump](https://attack.mitre.org/software/S0008)
* [Mimikatz](https://attack.mitre.org/software/S0002)
* secretsdump.py

Alternatively, the SAM can be extracted from the Registry with Reg:

* <code>reg save HKLM\sam sam</code>
* <code>reg save HKLM\system system</code>

Creddump7 can then be used to process the SAM database locally to retrieve hashes.(Citation: GitHub Creddump7)

Notes: 

* RID 500 account is the local, built-in administrator.
* RID 501 is the guest account.
* User accounts start with a RID of 1,000+.

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 4 procedures using this sub-technique:

- [[Automated Password Extraction from SYSVOL and Group Policy Preferences]]
- [[Azure AD Connect - Password Extraction via AD Sync Account DCSync]]
- [[Dumping AD Domain Credentials using Windows Domain Hashdump, Invoke-NinjaCopy, and CrackMapExec]]
- [[NTDS Reversible Encryption Dumping]]
