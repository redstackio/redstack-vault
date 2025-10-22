---
id: 8f760a76-770e-457a-bced-af697ad9d274
name: Windows Sticky Keys Persistence
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:28.137378+00:00'
updated_at: '2023-04-10T20:37:22.430181+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Accessibility Features|T1015 - Accessibility Features]]'
tags:
- '[[Binary Replacement]]'
- '[[Binary Replacement on Windows XP+]]'
- '[[Elevated]]'
- '[[Windows - Persistence]]'
---

# Windows Sticky Keys Persistence

## Summary

Sticky Keys Persistence is a technique used by attackers to maintain access to a compromised system. This technique involves replacing the sethc.exe binary with cmd.exe, which allows an attacker to execute commands with elevated privileges by pressing the shift key five times. This technique is eff

## Description

# Description

Sticky Keys Persistence is a technique used by attackers to maintain access to a compromised system. This technique involves replacing the sethc.exe binary with cmd.exe, which allows an attacker to execute commands with elevated privileges by pressing the shift key five times. This technique is effective because it is a built-in feature of Windows and does not require any additional tools or software to be installed.

From a technical perspective, this technique works by replacing the Sticky Keys binary (sethc.exe) with the Command Prompt binary (cmd.exe) in the Windows system directory. When the shift key is pressed five times, Windows launches the Command Prompt with elevated privileges, allowing the attacker to execute commands as the system user.

The business value of this technique is that it allows an attacker to maintain persistent access to a compromised system, even if the user changes their password or the system is rebooted.

## Requirements

1. Access to the target system

1. Ability to replace system binaries

## Defense

1. Disable the Sticky Keys feature on all systems to prevent attackers from using this technique

1. Monitor system binaries for changes or modifications

1. Implement strong password policies to make it more difficult for attackers to gain access to systems

## Objectives

1. Maintain persistent access to a compromised system

1. Execute commands with elevated privileges

# Instructions

1. This module exploits a feature in Windows Sticky Keys that allows you to reset the user password without knowing their current password.

**Code**: [[use post/windows/manage/sticky_keys]]

> The Sticky Keys feature can be activated by pressing the shift key five times in a row. This module replaces the Sticky Keys executable (sethc.exe) with a command prompt (cmd.exe) executable, which is executed when Sticky Keys is activated on the login screen. This allows an attacker to gain access to a Windows machine without knowing the user's password.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Accessibility Features|T1015 - Accessibility Features]]

## Tags

- [[Binary Replacement]]
- [[Binary Replacement on Windows XP+]]
- [[Elevated]]
- [[Windows - Persistence]]
