---
id: ddf5236d-026f-478f-9792-e15667ad819d
name: Password Cracking
type: sub-technique
mitre_id: T1110.002
mitre_url: null
created_at: '2023-04-06T00:31:25.680691+00:00'
updated_at: '2023-04-06T00:31:25.680691+00:00'
parent_technique: '[[Brute Force|T1110 - Brute Force]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[JWT Token Creation and Verification]]'
- '[[NTLM Hash Cracking with Hashcat]]'
---

# Password Cracking

**MITRE ID**: T1110.002

**Parent Technique**: [[Brute Force|T1110 - Brute Force]]

This is a sub-technique of T1110 - Brute Force.

## Summary

Adversaries may use password cracking to attempt to recover usable credentials, such as plaintext passwords, when credential material such as password hashes are obtained. [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) can be used to obtain password hashes, this may only get an a

## Description

Adversaries may use password cracking to attempt to recover usable credentials, such as plaintext passwords, when credential material such as password hashes are obtained. [OS Credential Dumping](https://attack.mitre.org/techniques/T1003) can be used to obtain password hashes, this may only get an adversary so far when [Pass the Hash](https://attack.mitre.org/techniques/T1550/002) is not an option. Further,  adversaries may leverage [Data from Configuration Repository](https://attack.mitre.org/techniques/T1602) in order to obtain hashed credentials for network devices.(Citation: US-CERT-TA18-106A) 

Techniques to systematically guess the passwords used to compute hashes are available, or the adversary may use a pre-computed rainbow table to crack hashes. Cracking hashes is usually done on adversary-controlled systems outside of the target network.(Citation: Wikipedia Password cracking) The resulting plaintext password resulting from a successfully cracked hash may be used to log into systems, resources, and services in which the account has access.

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 2 procedures using this sub-technique:

- [[JWT Token Creation and Verification]]
- [[NTLM Hash Cracking with Hashcat]]
