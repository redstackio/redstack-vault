---
id: b49b273e-b79b-4323-b46d-e3adc8a06279
name: AMSI Session and Context Disablement
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.958553+00:00'
updated_at: '2023-04-10T20:36:15.456354+00:00'
tags:
- '[[Forcing an error]]'
---

# AMSI Session and Context Disablement

## Summary

The AMSI (Antimalware Scan Interface) is a Windows feature that allows applications to integrate with antimalware products on the system. It is designed to detect malicious code and stop it from running. However, attackers can disable AMSI to bypass detection and execute their malicious code. One w

## Description

# Description

The AMSI (Antimalware Scan Interface) is a Windows feature that allows applications to integrate with antimalware products on the system. It is designed to detect malicious code and stop it from running. However, attackers can disable AMSI to bypass detection and execute their malicious code. One way to do this is by disabling the AMSI session and context. This can be achieved by using the 'Disable AMSI Session and Context' command. By doing so, an attacker can evade detection and execute their code without being detected by the antimalware software on the system.

In technical terms, the AMSI session and context are used by applications to communicate with the AMSI provider. By disabling the session and context, the provider is effectively turned off, allowing malicious code to run without being detected.

The business value of this technique is that it allows attackers to bypass security measures and execute their code without being detected, potentially leading to data theft, system compromise, and other malicious activities.

## Requirements

1. Access to the system

1. Privileges to disable AMSI

1. Ability to execute commands on the system

## Defense

1. Ensure that antimalware software is up to date and configured correctly

1. Monitor for suspicious activity and anomalies on the system

1. Implement least privilege access to limit the ability to disable AMSI

## Objectives

1. Disable AMSI to bypass antimalware detection

1. Execute malicious code without being detected

# Instructions

1. This command disables AMSI (Antimalware Scan Interface) session and context by allocating a block of memory and setting the amsiSession and amsiContext fields to null. This can be useful in avoiding detection by antivirus software that relies on AMSI to scan PowerShell code.

**Code**: [[$mem = [System.Runtime.InteropServices.Marshal]::A]]

> This command has no arguments.

## Tags

- [[Forcing an error]]
