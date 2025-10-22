---
id: 61994f5e-8250-4396-b1cb-e6bd1f4a7302
name: SSH
type: sub-technique
mitre_id: T1021.004
mitre_url: null
created_at: '2023-04-06T00:31:25.811974+00:00'
updated_at: '2023-04-06T00:31:25.811974+00:00'
parent_technique: '[[Remote Services|T1021 - Remote Services]]'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
---

# SSH

**MITRE ID**: T1021.004

**Parent Technique**: [[Remote Services|T1021 - Remote Services]]

This is a sub-technique of T1021 - Remote Services.

## Summary

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log into remote machines using Secure Shell (SSH). The adversary may then perform actions as the logged-on user.

SSH is a protocol that allows authorized users to open remote shells on other computers. Many Linux and

## Description

Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to log into remote machines using Secure Shell (SSH). The adversary may then perform actions as the logged-on user.

SSH is a protocol that allows authorized users to open remote shells on other computers. Many Linux and macOS versions come with SSH installed by default, although typically disabled until the user enables it. The SSH server can be configured to use standard password authentication or public-private keypairs in lieu of or in addition to a password. In this authentication scenario, the user’s public key must be in a special file on the computer running the server that lists which keypairs are allowed to login as that user.

## Tactics

This sub-technique is used in the following tactics:

- [[Lateral Movement|TA0008 - Lateral Movement]]
