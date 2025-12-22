---
id: 69b954c2-c5c2-4734-9756-b96bbcd7b337
name: Embed-Alternate-Data-Stream-in-File
type: procedure
verified: true
submitted: true
created_at: '2019-11-22T17:24:23.178077+00:00'
updated_at: '2023-05-25T20:02:53.961708+00:00'
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
  - '[[commands/powershell-add-content-to-ads]]'
  - '[[commands/cmd-type-to-ads]]'
tools: []
validated: true
---

# Embed-Alternate-Data-Stream-in-File

## Summary

This procedure demonstrates how to embed an alternate data stream (ADS) into a file using NTFS file attributes on Windows systems. ADS allows attaching hidden data to a file without altering its visible size or content, providing a simple obfuscation method for hiding payloads, scripts, or sensitive information within innocuous cover files.

## Description

Alternate Data Streams (ADS) is a feature of the NTFS file system introduced in Windows NT 3.1, enabling multiple data streams to be associated with a single file. The primary stream is the visible file content, while additional streams can store hidden data. This technique is useful for evading basic file inspection tools, as ADS are not displayed by default in Windows Explorer, command-line listings (like dir), or reflected in file properties. Attackers can use ADS to hide malicious executables, configuration files, or stolen data within legitimate-looking files such as images or documents. Detection requires specific tools like streams.exe or PowerShell cmdlets. This procedure covers embedding via both Command Prompt and PowerShell, assuming local file system access on an NTFS volume.

## Requirements

1. Windows operating system with NTFS file system (Windows 7 or later recommended).
2. Local write access to the target directory and cover file.
3. The embedded file or data to hide (e.g., a text file, script, or binary).
4. No administrative privileges required for basic embedding, but elevated access may be needed for system-protected files.

## Defense

Defensive measures and detection strategies:

- Use tools like Sysinternals Streams (streams.exe) to enumerate ADS on files and directories.
- Enable file integrity monitoring (FIM) solutions to detect unexpected file modifications.
- Implement antivirus/EDR solutions that scan for ADS (e.g., Windows Defender with real-time protection).
- Regularly audit file systems with PowerShell scripts to list all streams: Get-Item -Path file.txt -Stream *.

## Objectives

1. Hide data within a cover file using ADS to evade casual inspection.
2. Verify the embedding without revealing the hidden stream in standard views.
3. Provide a method for obfuscation in post-exploitation scenarios, such as hiding payloads.
4. Expected outcome: Hidden data accessible only via explicit stream queries, maintaining the cover file's integrity.

## Instructions

### Step 1: Prepare Files

**Context**: Identify or create the cover file (the visible host file) and the embedded content (the data or file to hide). Ensure both are in an accessible NTFS directory. This step sets up the environment without performing the embedding.

No command required for preparation, but verify file existence:

```powershell
Test-Path -Path "$_COVER_FILE"
Test-Path -Path "$_EMBEDDED_FILE"
```

> This returns True if files exist, ensuring prerequisites are met before proceeding.

### Step 2: Embed Using PowerShell

**Context**: Use PowerShell's Add-Content cmdlet to attach the embedded data as a named stream to the cover file. This method allows direct content addition or file import, ideal for scripting environments.

**Command** ([[commands/powershell-add-content-to-ads]]):

```powershell
Add-Content -Path $_COVER_FILE -Value (Get-Content $_EMBEDDED_FILE) -Stream $_STREAM_NAME -Encoding UTF8
```

> This command reads the content of the embedded file and appends it to the specified stream in the cover file. Use -Value for direct text or pipe Get-Content for files. Expected output: No visible response if successful; verify with Step 4.

### Step 3: Embed Using Command Prompt

**Context**: For non-PowerShell environments, use the type command in cmd.exe to redirect the embedded file's content into a named ADS on the cover file. This is a lightweight method without needing scripting.

**Command** ([[commands/cmd-type-to-ads]]):

```cmd
type $_EMBEDDED_FILE > $_COVER_FILE:$_STREAM_NAME
```

> This redirects the entire embedded file into the ADS named $_STREAM_NAME. The cover file remains unchanged in size and appearance. Expected output: No console output; the command completes silently on success.

### Step 4: Verify Embedding

**Context**: Confirm the ADS was created by listing streams on the cover file. This step ensures the procedure succeeded and the data is hidden but retrievable.

Use PowerShell to list streams:

```powershell
Get-Item -Path $_COVER_FILE -Stream *
```

> Expected output: Displays the primary stream and the new ADS stream with length. For example:
>
>    PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\path\cover.txt:stream
>    Stream        : stream
>    FileName      : cover.txt
>
> If the stream appears, embedding is successful. To extract: Get-Content -Path $_COVER_FILE -Stream $_STREAM_NAME.
