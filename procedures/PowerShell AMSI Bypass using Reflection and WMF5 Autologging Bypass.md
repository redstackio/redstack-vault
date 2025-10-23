---
id: 8bd1a2fd-5fee-4118-98db-0f4e528522f9
name: PowerShell AMSI Bypass using Reflection and WMF5 Autologging Bypass
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.164763+00:00'
updated_at: '2023-04-10T20:36:17.266638+00:00'
tags:
- '[[Other interesting AMSI bypass]]'
- '[[Using Matt Graebers Reflection method with WMF5 autologging bypass]]'
---

# PowerShell AMSI Bypass using Reflection and WMF5 Autologging Bypass

## Summary

This procedure is a PowerShell script that leverages Matt Graeber's Reflection method and WMF5 Autologging Bypass to bypass the Anti-Malware Scan Interface (AMSI) protection. The script is designed to evade detection and execute malicious code without being detected by anti-virus or anti-malware so

## Description

# Description

This procedure is a PowerShell script that leverages Matt Graeber's Reflection method and WMF5 Autologging Bypass to bypass the Anti-Malware Scan Interface (AMSI) protection. The script is designed to evade detection and execute malicious code without being detected by anti-virus or anti-malware software. The script can be used by attackers to gain access to sensitive data, steal credentials, and execute other malicious activities.

Technical Explanation: The script uses the Reflection method to load the Microsoft.Management.Infrastructure.dll and the System.Management.Automation.dll, which are required for the WMF5 Autologging Bypass. The script then uses the Autologging Bypass to disable AMSI protection and execute the malicious code. The script is designed to evade detection by using obfuscation techniques and packing the code.

Business Value: This procedure allows attackers to evade detection and execute malicious code on a target system. This can result in the loss of sensitive data, intellectual property, and financial loss.

 

## Requirements

1. Authenticated access to the target system

1. PowerShell version 5 or later

 

## Defense

1. Ensure that anti-virus and anti-malware software is up-to-date and configured to detect PowerShell-based attacks

1. Implement network segmentation to limit lateral movement of attackers

1. Monitor for suspicious PowerShell activity on the network and endpoint devices

 

## Objectives

1. Bypass AMSI protection and execute malicious code on a target system

 

# Instructions

1. To bypass AMSI using PowerShell, copy and paste the code from the data field into a PowerShell script. Then, run the script as administrator. This will disable AMSI in PowerShell.

 



**Code**: [[$A="5492868772801748688168747280728187173688878280]]



> The code in the data field obtains the reference to the `System.Management.Automation.AmsiUtils` class in the PowerShell runtime. It then retrieves the `amsiInitFailed` field of the class and sets its value to `$true`, which disables AMSI in PowerShell. This technique can be used to bypass AMSI in PowerShell and execute malicious code.

## Tags

- [[Other interesting AMSI bypass]]
- [[Using Matt Graebers Reflection method with WMF5 autologging bypass]]


