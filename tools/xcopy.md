---
id: e1b94341-3698-4c40-8731-357dd3355ecd
name: xcopy
type: tool
verified: true
created_at: '2020-03-04T22:55:06.385887+00:00'
updated_at: '2023-05-30T19:57:13.757876+00:00'
commands:
  - '[[commands/xcopy-download-files-from-remote-smb]]'
platforms:
  - Windows
tags:
  - file-system
  - file-transfer
url: >-
  https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy
validated: true
---

# xcopy

**Status**: ✓ Verified

## Overview

Xcopy is a built-in Windows command-line tool for copying files and directory trees. It extends the basic 'copy' command with advanced options for handling remote shares, file attributes, encrypted files, and recursive operations, making it suitable for file transfer in security testing scenarios like lateral movement or data staging.

## Description

Xcopy supports copying files between local directories, network shares (including SMB), and even across systems. Key capabilities include preserving file attributes, timestamps, and permissions; handling long path names; and options for excluding files or copying based on date/time. In offensive security, it's often used for quick file exfiltration over SMB without needing external tools, though it requires valid credentials or null session access for remote operations.

## Features

- Feature 1: Recursive copying of directories and subdirectories (/s or /e flags)
- Feature 2: Support for remote SMB shares (\server\share syntax)
- Feature 3: Attribute preservation (read-only, hidden, system files) and exclusion patterns
- Feature 4: Overwrite control (/y to suppress prompts) and verification (/v flag)

## Installation

### Requirements

- Windows OS (XP or later; built-in on modern versions)
- Administrative privileges not required for local use, but needed for some remote operations

### Install Commands

Xcopy is pre-installed on all Windows systems. No installation required.

For verification:

```cmd
xcopy /?
```

## Basic Usage

```cmd
xcopy /?
```

This displays the help menu with all available options.

### Common Options

| Option | Description |
|--------|-------------|
| /s | Copies directories and subdirectories, excluding empty ones |
| /e | Copies directories and subdirectories, including empty ones |
| /y | Suppresses prompting to confirm overwriting files |
| /v | Verifies each file after copying |
| /c | Continues copying even if errors occur |
| /q | Quiet mode; suppresses file names during copy |

## Examples

### Example 1: Basic Usage

Copy all files from a local source to a destination:

```cmd
xcopy C:\source C:\destination /s /e
```

### Example 2: Advanced Usage

Download files from a remote SMB share (requires network access):

```cmd
xcopy \\remote-server\share\*.* C:\local\ /s /e /y
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[SMB-Windows Admin Shares]] Remote Services: SMB/Windows Admin Shares
- [[Exfiltration Over Unencrypted Non-C2 Protocol]] Exfiltration Over Alternative Protocol: SharePoint

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor Command Prompt or PowerShell logs for 'xcopy' invocations, especially with UNC paths (\\server\share)
- Detection method 2: Network traffic analysis for SMB (port 445) file transfers from unexpected sources
- Detection method 3: File system auditing for unusual copies to/from admin shares or staged directories
- Detection method 4: Sysmon Event ID 1 (Process Creation) filtering for xcopy.exe with suspicious arguments

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/robocopy]]
- [[tools/smbclient]]

## References

- Official Microsoft documentation: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1021/002/
