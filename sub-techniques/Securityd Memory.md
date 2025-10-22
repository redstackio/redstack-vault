---
id: 5e0f4f7a-9d0e-4cf0-baf0-30f6744e729b
name: Securityd Memory
type: sub-technique
mitre_id: T1555.002
mitre_url: null
created_at: '2023-04-06T00:31:25.643925+00:00'
updated_at: '2023-04-06T00:31:25.643925+00:00'
parent_technique: '[[Credentials from Password Stores|T1555 - Credentials from Password
  Stores]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[Stealing Chrome Cookies and Credentials with Mimikatz]]'
- '[[Windows DPAPI Credential Retrieval with Mimikatz]]'
- '[[Windows DPAPI Credential Theft]]'
---

# Securityd Memory

**MITRE ID**: T1555.002

**Parent Technique**: [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]

This is a sub-technique of T1555 - Credentials from Password Stores.

## Summary

An adversary may obtain root access (allowing them to read securityd’s memory), then they can scan through memory to find the correct sequence of keys in relatively few tries to decrypt the user’s logon keychain. This provides the adversary with all the plaintext passwords for users, WiFi, mail, bro

## Description

An adversary may obtain root access (allowing them to read securityd’s memory), then they can scan through memory to find the correct sequence of keys in relatively few tries to decrypt the user’s logon keychain. This provides the adversary with all the plaintext passwords for users, WiFi, mail, browsers, certificates, secure notes, etc.(Citation: OS X Keychain)(Citation: OSX Keydnap malware)

In OS X prior to El Capitan, users with root access can read plaintext keychain passwords of logged-in users because Apple’s keychain implementation allows these credentials to be cached so that users are not repeatedly prompted for passwords.(Citation: OS X Keychain)(Citation: External to DA, the OS X Way) Apple’s securityd utility takes the user’s logon password, encrypts it with PBKDF2, and stores this master key in memory. Apple also uses a set of keys and algorithms to encrypt the user’s password, but once the master key is found, an adversary need only iterate over the other values to unlock the final password.(Citation: OS X Keychain)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures

There are 3 procedures using this sub-technique:

- [[Stealing Chrome Cookies and Credentials with Mimikatz]]
- [[Windows DPAPI Credential Retrieval with Mimikatz]]
- [[Windows DPAPI Credential Theft]]
