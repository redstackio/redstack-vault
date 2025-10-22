---
id: 114b4015-81e3-41ee-8b2f-83628ccd0a79
name: Password Managers
type: sub-technique
mitre_id: T1555.005
mitre_url: null
created_at: '2023-04-06T00:31:25.846692+00:00'
updated_at: '2023-04-06T00:31:25.846692+00:00'
parent_technique: '[[Credentials from Password Stores|T1555 - Credentials from Password
  Stores]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
---

# Password Managers

**MITRE ID**: T1555.005

**Parent Technique**: [[Credentials from Password Stores|T1555 - Credentials from Password Stores]]

This is a sub-technique of T1555 - Credentials from Password Stores.

## Summary

Adversaries may acquire user credentials from third-party password managers.(Citation: ise Password Manager February 2019) Password managers are applications designed to store user credentials, normally in an encrypted database. Credentials are typically accessible after a user provides a master pas

## Description

Adversaries may acquire user credentials from third-party password managers.(Citation: ise Password Manager February 2019) Password managers are applications designed to store user credentials, normally in an encrypted database. Credentials are typically accessible after a user provides a master password that unlocks the database. After the database is unlocked, these credentials may be copied to memory. These databases can be stored as files on disk.(Citation: ise Password Manager February 2019)

Adversaries may acquire user credentials from password managers by extracting the master password and/or plain-text credentials from memory.(Citation: FoxIT Wocao December 2019)(Citation: Github KeeThief) Adversaries may extract credentials from memory via [Exploitation for Credential Access](https://attack.mitre.org/techniques/T1212).(Citation: NVD CVE-2019-3610)
 Adversaries may also try brute forcing via [Password Guessing](https://attack.mitre.org/techniques/T1110/001) to obtain the master password of a password manager.(Citation: Cyberreason Anchor December 2019)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]
