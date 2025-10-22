---
id: c0808b8a-8d9a-4788-a7ef-09ea43f3cc7f
name: SSH Hijacking
type: sub-technique
mitre_id: T1563.001
mitre_url: null
created_at: '2023-04-06T00:31:26.070282+00:00'
updated_at: '2023-04-06T00:31:26.070282+00:00'
parent_technique: '[[Remote Service Session Hijacking|T1563 - Remote Service Session
  Hijacking]]'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
---

# SSH Hijacking

**MITRE ID**: T1563.001

**Parent Technique**: [[Remote Service Session Hijacking|T1563 - Remote Service Session Hijacking]]

This is a sub-technique of T1563 - Remote Service Session Hijacking.

## Summary

Adversaries may hijack a legitimate user's SSH session to move laterally within an environment. Secure Shell (SSH) is a standard means of remote access on Linux and macOS systems. It allows a user to connect to another system via an encrypted tunnel, commonly authenticating through a password, certi

## Description

Adversaries may hijack a legitimate user's SSH session to move laterally within an environment. Secure Shell (SSH) is a standard means of remote access on Linux and macOS systems. It allows a user to connect to another system via an encrypted tunnel, commonly authenticating through a password, certificate or the use of an asymmetric encryption key pair.

In order to move laterally from a compromised host, adversaries may take advantage of trust relationships established with other systems via public key authentication in active SSH sessions by hijacking an existing connection to another system. This may occur through compromising the SSH agent itself or by having access to the agent's socket. If an adversary is able to obtain root access, then hijacking SSH sessions is likely trivial.(Citation: Slideshare Abusing SSH)(Citation: SSHjack Blackhat)(Citation: Clockwork SSH Agent Hijacking)(Citation: Breach Post-mortem SSH Hijack)

[SSH Hijacking](https://attack.mitre.org/techniques/T1563/001) differs from use of [SSH](https://attack.mitre.org/techniques/T1021/004) because it hijacks an existing SSH session rather than creating a new session using [Valid Accounts](https://attack.mitre.org/techniques/T1078).

## Tactics

This sub-technique is used in the following tactics:

- [[Lateral Movement|TA0008 - Lateral Movement]]
