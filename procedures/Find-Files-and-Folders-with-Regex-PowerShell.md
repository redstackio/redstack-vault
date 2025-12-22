---
id: d36c250a-f406-4320-8854-4b3988febb26
name: Find-Files-and-Folders-with-Regex-PowerShell
type: procedure
verified: true
submitted: true
created_at: '2020-04-24T18:25:00.614353+00:00'
updated_at: '2023-05-25T19:59:03.472098+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/Enumeration]]'
commands:
  - '[[commands/get-childitem-regex-search-powershell]]'
tools: []
validated: true
---

# Find-Files-and-Folders-with-Regex-PowerShell

## Summary

This procedure uses native PowerShell cmdlets to recursively search for files and folders matching a specified regular expression pattern in their names. It emulates the functionality of Unix-like 'find' commands on Windows systems, enabling attackers or security testers to discover sensitive files, configurations, or directories during reconnaissance or post-exploitation phases.

## Description

In offensive security operations, discovering files and directories is a key step for identifying valuable assets like credentials, scripts, or backups. PowerShell's Get-ChildItem cmdlet, combined with Where-Object filtering, allows for flexible regex-based searches across the file system. This approach is stealthy as it leverages built-in Windows tools, avoiding the need for external binaries that might trigger alerts. It is particularly useful in environments where administrative privileges are not required for read access, though deeper searches may need elevated permissions to traverse protected directories. The procedure supports case-insensitive matching by default and can be scoped to specific paths to reduce noise and execution time.

## Requirements

1. PowerShell execution policy allowing script execution (e.g., not Restricted).
2. Read access to the target directories (local user privileges suffice for user-accessible paths; elevated for system-wide searches).
3. Windows operating system (PowerShell 3.0 or later recommended for performance).
4. A defined regex pattern to match file or folder names (e.g., for sensitive keywords like 'password' or 'secret').

## Defense

Defensive measures include file system auditing via Windows Event Logs (Event ID 4663 for file access), restricting PowerShell execution through AppLocker or constrained language mode, and monitoring for anomalous Get-ChildItem usage via Sysmon or EDR tools. Detection can focus on regex patterns targeting sensitive terms or recursive searches from unusual starting points.

## Objectives

1. Identify files or folders whose names match a regex pattern for potential sensitive data discovery.
2. Gather intelligence on file system structure without external tools.
3. Verify search results for actionable items like configuration files or logs.

## Instructions

### Step 1: Define Search Parameters

**Context**: Before executing the search, determine the starting directory and regex pattern to ensure targeted and efficient discovery. This prevents scanning the entire drive unnecessarily, which could be time-consuming or detectable.

Choose a starting path (e.g., C:\Users or the current directory) and craft a regex pattern. For example, to find files starting with 'secret', use '^secret.*'. Test the regex in a simple PowerShell one-liner if needed.

### Step 2: Execute Recursive Regex Search

**Context**: Run the core search command to enumerate items matching the regex. This step performs the actual discovery, filtering results in-memory for performance.

**Command** ([[commands/get-childitem-regex-search-powershell]]):
```powershell
Get-ChildItem -Path $_START_PATH -Recurse | Where-Object { $_.Name -Match $_REGEX }
```

> This command starts from the specified path, recurses through subdirectories, and filters items where the name matches the regex. Use -ErrorAction SilentlyContinue to suppress access denied errors on protected folders. Expected output includes a list of matching files/folders with details like path, size, and last modified time. If no matches, it returns empty; pipe to Format-Table for better readability.

### Step 3: Review and Export Results

**Context**: Analyze the output to identify relevant items and export for further investigation or exfiltration. This step ensures results are actionable and documented.

Review the listed items for sensitivity (e.g., .txt files with credential hints). Export to a file using | Export-Csv -Path results.csv or | Out-File results.txt. If results are voluminous, add | Select-Object FullName, Length, LastWriteTime for concise output.

**Expected Output**: A table of matching items, e.g.:

```
    Directory: C:\Users\Bob\Desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        4/24/2020  11:23 AM              0 secretdocument.txt
```
