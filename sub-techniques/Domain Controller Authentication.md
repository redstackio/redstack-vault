---
id: 3ce533e1-d727-4174-a15b-3fa52d3574ad
name: Domain Controller Authentication
type: sub-technique
mitre_id: T1556.001
mitre_url: null
created_at: '2023-04-06T00:31:27.013363+00:00'
updated_at: '2023-04-06T00:31:27.013363+00:00'
parent_technique: '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Detect-Secrets-in-Git-Repositories-with-Gitleaks]]'
- '[[Insecure-Docker-Registry-Pentest]]'
- '[[jwt-signature-key-confusion-attack-rs256-to-hs256-cve-2016-5431]]'
- '[[ntlm-reflection-smb-relay-attack]]'
- '[[Shadow-Credentials-for-Windows-Hello]]'
- '[[Web-Sockets-Authentication-Exploitation]]'
---

# Domain Controller Authentication

**MITRE ID**: T1556.001

**Parent Technique**: [[Modify Authentication Process|T1556 - Modify Authentication Process]]

This is a sub-technique of T1556 - Modify Authentication Process.

## Summary

Adversaries may patch the authentication process on a domain controller to bypass the typical authentication mechanisms and enable access to accounts. 

Malware may be used to inject false credentials into the authentication process on a domain controller with the intent of creating a backdoor used 

## Description

Adversaries may patch the authentication process on a domain controller to bypass the typical authentication mechanisms and enable access to accounts. 

Malware may be used to inject false credentials into the authentication process on a domain controller with the intent of creating a backdoor used to access any user’s account and/or credentials (ex: [Skeleton Key](https://attack.mitre.org/software/S0007)). Skeleton key works through a patch on an enterprise domain controller authentication process (LSASS) with credentials that adversaries may use to bypass the standard authentication system. Once patched, an adversary can use the injected password to successfully authenticate as any domain user account (until the the skeleton key is erased from memory by a reboot of the domain controller). Authenticated access may enable unfettered access to hosts and/or resources within single-factor authentication environments.(Citation: Dell Skeleton)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

## Related Procedures

There are 6 procedures using this sub-technique:

- [[Detect-Secrets-in-Git-Repositories-with-Gitleaks]]
- [[Insecure-Docker-Registry-Pentest]]
- [[jwt-signature-key-confusion-attack-rs256-to-hs256-cve-2016-5431]]
- [[ntlm-reflection-smb-relay-attack]]
- [[Shadow-Credentials-for-Windows-Hello]]
- [[Web-Sockets-Authentication-Exploitation]]
