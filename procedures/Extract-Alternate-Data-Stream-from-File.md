---
id: 6d8de39e-862e-41b3-85b5-61ffb92a8f50
name: Extract-Alternate-Data-Stream-from-File
type: procedure
verified: true
submitted: false
created_at: '2019-11-22T18:04:45.451961+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/NTFS File Attributes|T1096 - NTFS File Attributes]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/File System]]'
  - '[[tags/Obfuscation]]'
commands:
  - '[[commands/powershell-extract-ads-from-file]]'
  - '[[commands/cmd-list-directory-with-ads]]'
  - '[[commands/cmd-more-extract-ads-from-file]]'
tools: []
validated: true
---

# Extract-Alternate-Data-Stream-from-File

## Summary

This procedure extracts data hidden in Alternate Data Streams (ADS) attached to NTFS files, a technique used for obfuscating payloads or sensitive information since ADS are not visible in standard file explorers or listings. It is useful in post-exploitation scenarios to retrieve steganographically hidden data without alerting basic file monitoring tools.

## Description

Alternate Data Streams (ADS) are a feature of the NTFS file system (version 3.1 and later) that allow multiple data streams to be associated with a single file. The primary stream is the visible file content, while additional streams can store hidden data without affecting the apparent file size or name. This makes ADS an effective method for hiding malicious payloads, configuration files, or credentials during defense evasion. Attackers might embed scripts or keys in ADS to bypass antivirus scans that focus on main file contents. This procedure covers identifying and extracting ADS using both Command Prompt and PowerShell, assuming local access to the target Windows system. It requires NTFS-formatted drives and appropriate read permissions on the target file.

## Requirements

1. Local access to a Windows system with NTFS file system.
2. Read permissions on the target file containing the ADS.
3. Command Prompt or PowerShell available (standard on Windows).
4. Knowledge of the ADS name if not enumerating first.

## Defense

Defensive measures and detection strategies:

- Enable file integrity monitoring tools like Sysmon to log file access and attribute changes on NTFS streams.
- Use antivirus solutions with ADS scanning capabilities (e.g., Windows Defender with real-time protection).
- Implement application whitelisting to restrict execution of hidden payloads extracted from ADS.
- Regularly audit files in sensitive directories for unexpected streams using tools like Streams.exe from Sysinternals.

## Objectives

1. Identify the presence of hidden ADS in a target file or directory.
2. Extract the contents of a specific ADS for analysis or execution.
3. Verify successful extraction without corrupting the original file.

## Instructions

### Step 1: Enumerate Directory for ADS

**Context**: Before extraction, verify if the target file or directory contains any ADS streams, as they are not shown in standard listings. This step lists all files and reveals any attached streams.

**Command** ([[commands/cmd-list-directory-with-ads]]):
```command_prompt
dir /R $_TARGET_PATH
```

> This command recursively lists directory contents including ADS. The `/R` switch enables ADS display. Look for entries like `filename:streamname:$DATA` indicating a stream. Replace `$_TARGET_PATH` with the directory or file path (e.g., `C:\temp`). This step confirms the ADS existence and name, preventing errors in extraction.

### Step 2: Extract ADS Using Command Prompt (More Command)

**Context**: If the ADS name is known (e.g., from Step 1), use the `more` command to pipe and display the stream contents directly. This is a lightweight method without needing additional tools.

**Command** ([[commands/cmd-more-extract-ads-from-file]]):
```command_prompt
more < $_FILE:$_ADS
```

> The `more` command reads the stream specified by `$_FILE:$_ADS` (e.g., `normal.txt:secret`). It outputs the hidden data to the console. This is useful for quick inspection of text-based payloads like keys or scripts. If the stream is binary, output may appear garbled; redirect to a file for saving (e.g., `more < file:stream > output.txt`).

### Step 3: Extract ADS Using PowerShell

**Context**: For more flexible handling, especially with larger or structured data, use PowerShell's `Get-Content` cmdlet to retrieve the ADS contents. This method supports scripting and easier output manipulation.

**Command** ([[commands/powershell-extract-ads-from-file]]):
```powershell
Get-Content -Path $_FILE -Stream $_ADS
```

> Specify the file path and stream name with `-Path` and `-Stream` parameters (e.g., `normal.txt` and `secret`). This cmdlet reads the stream as text and displays it. Success is indicated by the output matching expected content, such as a private key or script. Pipe to `Out-File` to save if needed (e.g., `Get-Content ... | Out-File extracted.txt`).
