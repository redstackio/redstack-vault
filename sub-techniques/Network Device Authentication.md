---
id: 6dabed56-35b0-484a-9eb2-93c2b04b37d4
name: Network Device Authentication
type: sub-technique
mitre_id: T1556.004
mitre_url: null
created_at: '2023-04-06T00:31:27.228657+00:00'
updated_at: '2023-04-06T00:31:27.228657+00:00'
parent_technique: '[[Modify Authentication Process|T1556 - Modify Authentication Process]]'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Web Sockets Authentication Exploitation]]'
---

# Network Device Authentication

**MITRE ID**: T1556.004

**Parent Technique**: [[Modify Authentication Process|T1556 - Modify Authentication Process]]

This is a sub-technique of T1556 - Modify Authentication Process.

## Summary

Adversaries may use [Patch System Image](https://attack.mitre.org/techniques/T1601/001) to hard code a password in the operating system, thus bypassing of native authentication mechanisms for local accounts on network devices.

[Modify System Image](https://attack.mitre.org/techniques/T1601) may inc

## Description

Adversaries may use [Patch System Image](https://attack.mitre.org/techniques/T1601/001) to hard code a password in the operating system, thus bypassing of native authentication mechanisms for local accounts on network devices.

[Modify System Image](https://attack.mitre.org/techniques/T1601) may include implanted code to the operating system for network devices to provide access for adversaries using a specific password.  The modification includes a specific password which is implanted in the operating system image via the patch.  Upon authentication attempts, the inserted code will first check to see if the user input is the password. If so, access is granted. Otherwise, the implanted code will pass the credentials on for verification of potentially valid credentials.(Citation: Mandiant - Synful Knock)

## Tactics

This sub-technique is used in the following tactics:

- [[Credential Access|TA0006 - Credential Access]]
- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[Web Sockets Authentication Exploitation]]
