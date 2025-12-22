---
id: c06117f5-6877-4f7b-8d11-befb305db0f2
name: Loot-Passwords-from-Alternate-Data-Stream
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.351701+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
  - '[[techniques/Credentials In Files|T1552.001 - Credentials In Files]]'
sub_techniques: []
tags:
  - eop-looting-passwords
  - password-in-ads
  - windows-privilege-escalation
commands:
  - '[[commands/powershell-get-item-list-all-streams]]'
  - '[[commands/powershell-get-content-ads-stream]]'
platforms:
  - Windows
tools: []
validated: true
---

# Loot-Passwords-from-Alternate-Data-Stream

## Summary

This procedure demonstrates how to loot hidden credentials or passwords stored in Alternate Data Streams (ADS) of NTFS files using built-in PowerShell commands. ADS allows attackers to hide data within files without altering the primary file content, enabling stealthy storage of sensitive information like passwords that can be retrieved later for privilege escalation or persistence.

## Description

Alternate Data Streams are a feature of the NTFS file system that permits attaching additional data streams to files, often used by attackers to conceal payloads or credentials. In a post-exploitation scenario on a Windows system, an attacker with sufficient file access can enumerate and extract these streams to recover stored passwords. This technique is particularly useful in privilege escalation chains where credentials are hidden in common files like documents or executables. The procedure assumes the target file exists and contains an ADS with sensitive data; it does not cover creating ADS but focuses on detection and extraction. Success depends on file permissions; administrative privileges may be required for protected system files.

## Requirements

1. Access to a Windows system with NTFS file system.
2. PowerShell execution privileges (typically available in user context, but admin for system files).
3. Read access to the target file containing the ADS.
4. Knowledge of the potential file path where ADS might be hidden (e.g., user documents, system directories).

## Defense

- Monitor file system changes and ADS creation using tools like Sysmon (Event ID 11 for file creation with streams).
- Implement least privilege access to files to prevent unauthorized reading of streams.
- Regularly audit files for hidden streams using tools like Streams.exe from Sysinternals.
- Enable PowerShell logging (Module, Script Block) to detect suspicious Get-Item and Get-Content usage on sensitive files.

## Objectives

1. Enumerate all streams associated with a target file to identify hidden data.
2. Extract the content from a specific ADS to retrieve embedded passwords or credentials.
3. Use recovered credentials for further actions like privilege escalation or lateral movement.

## Instructions

### Step 1: Enumerate All Streams in the Target File

**Context**: Begin by listing all alternate data streams attached to the target file to discover hidden ones that may contain passwords. This step reveals the names of streams without extracting their content, helping identify potential targets like a 'password' or 'flag' stream.

**Command** ([[commands/powershell-get-item-list-all-streams]]):
```powershell
Get-Item -Path flag.txt -Stream *
```

> This command retrieves the target file object and displays all associated streams. Replace 'flag.txt' with the actual file path. The output will list the primary stream and any ADS, such as ':Flag:$DATA'. If no ADS exist, only the main file will show.

### Step 2: Extract Content from the Specific ADS

**Context**: Once streams are identified, extract the content from the suspected ADS containing the password. This reveals the hidden data, which could be plaintext credentials for use in authentication or escalation.

**Command** ([[commands/powershell-get-content-ads-stream]]):
```powershell
Get-Content -Path flag.txt -Stream Flag
```

> This command reads the content of the named stream ('Flag' in this example). The output will display the stream's data, such as a password string. Verify the stream name from Step 1; if the password is not in plaintext, it may require further cracking or decoding.
