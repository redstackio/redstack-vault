---
id: e72d5b2b-824f-4cfc-8b5d-8539b416bdcc
name: Windows Defender Disabler
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.686015+00:00'
updated_at: '2023-04-10T20:37:26.792144+00:00'
tags:
- '[[Disable Antivirus and Security]]'
- '[[Disable Windows Defender]]'
- '[[Windows - Persistence]]'
---

# Windows Defender Disabler

## Summary

The Windows Defender Disabler is a tool used to disable Windows Defender on a target system. This tool can be used by an attacker to avoid detection by the target's anti-virus and security software. By disabling Windows Defender, the attacker can execute malicious code on the target system without 

## Description

# Description

The Windows Defender Disabler is a tool used to disable Windows Defender on a target system. This tool can be used by an attacker to avoid detection by the target's anti-virus and security software. By disabling Windows Defender, the attacker can execute malicious code on the target system without being detected. This tool can be used in conjunction with other attack techniques to achieve persistence on the target system.

Technical Explanation: The tool uses a Windows PowerShell script to disable Windows Defender by modifying the registry keys that control Windows Defender's behavior. This script can be run manually or can be executed remotely using a command and control (C2) framework. 

Business Value: By disabling Windows Defender, an attacker can avoid detection by the target's anti-virus and security software. This can allow the attacker to execute malicious code on the target system without being detected, which can lead to data theft, system compromise, and other malicious activities. 

## Requirements

1. Local administrator access to the target system

1. PowerShell access on the target system

## Defense

1. Ensure that Windows Defender is enabled and up-to-date on all systems

1. Implement network segmentation to limit lateral movement in case of a compromise

1. Monitor for registry changes related to Windows Defender and other security software

## Objectives

1. Disable Windows Defender on the target system

1. Avoid detection by the target's anti-virus and security software

1. Execute malicious code on the target system without being detected

# Instructions

1. This command disables Windows Defender and all its components. It includes disabling real-time monitoring, IOAV protection, script scanning, and AMSI. It also excludes some processes and locations from scanning. Additionally, it removes all definitions and signatures and disables the Windows Defender Security Center and Real Time Protection.

**Code**: [[# Disable Defender
sc config WinDefend start= disa]]

> The command is written in PowerShell and is used to disable Windows Defender on a Windows machine. It includes multiple commands to disable different components of Windows Defender. The 'Set-MpPreference' command is used to disable real-time monitoring, IOAV protection, script scanning, and AMSI. The 'Add-MpPreference' command is used to exclude some processes and locations from scanning. The 'reg' command is used to disable the Windows Defender Security Center and Real Time Protection. The 'MpCmdRun.exe' command is used to remove all definitions and signatures.

## Tags

- [[Disable Antivirus and Security]]
- [[Disable Windows Defender]]
- [[Windows - Persistence]]
