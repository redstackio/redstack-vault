---
id: 4eff9751-b999-40e5-8cbc-9eafaa949d7f
name: Enumerate-Windows-for-Privilege-Escalation-JAWS
type: procedure
verified: true
submitted: false
created_at: '2019-11-26T19:36:52.606652+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
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
  - '[[tags/data exposure]]'
  - '[[tags/Misconfiguration]]'
  - '[[tags/Service Attacks]]'
commands:
  - '[[commands/jaws-enumerate-for-privilege-escalation]]'
platforms:
  - Windows
tools:
  - '[[tools/jaws]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Enumerate-Windows-for-Privilege-Escalation-JAWS

## Summary

This procedure uses JAWS (Just Another [Enumeration] Script), a PowerShell-based enumeration tool, to systematically scan a Windows system for potential privilege escalation vectors. It collects information on user accounts, services, file permissions, processes, network configurations, and other system details that could reveal misconfigurations or weak points allowing escalation from a low-privileged account to higher privileges, such as administrator or SYSTEM.

## Description

JAWS automates the discovery of common privilege escalation opportunities on Windows environments by running a series of native PowerShell commands and queries. It is particularly useful in post-exploitation scenarios where an attacker has initial foothold access but needs to identify paths to elevate privileges. The script outputs results to a file for offline analysis, covering MITRE ATT&CK techniques like account discovery, permission groups discovery, and system service discovery. This procedure assumes execution on a compromised Windows host with PowerShell available, typically via a reverse shell or interactive session. Expected outcomes include identification of weak services, writable files in privileged directories, unquoted service paths, and other exploitable configurations.

## Requirements

1. PowerShell execution policy set to allow script execution (e.g., Unrestricted or Bypass).
2. Local or remote access to the target Windows system with at least user-level privileges.
3. Ability to download and transfer the JAWS script to the target (e.g., via SMB, HTTP, or existing shell).
4. Sufficient disk space on the target for output file generation (typically a few MB).
5. [[tools/jaws]] script downloaded from its GitHub repository.

## Defense

Defensive measures and detection strategies:

- Enable PowerShell logging (Module, ScriptBlock, and Transcription) to capture script imports and executions.
- Implement application whitelisting (e.g., AppLocker or WDAC) to block unsigned scripts like JAWS.
- Monitor for anomalous file downloads or transfers to sensitive systems using EDR tools.
- Regularly audit service configurations, file permissions, and scheduled tasks to remediate common escalation vectors identified by JAWS.
- Use integrity monitoring to detect changes to system files and binaries.

## Objectives

1. Collect comprehensive system enumeration data to identify privilege escalation opportunities.
2. Generate an output file with categorized findings for analysis.
3. Validate the presence of exploitable misconfigurations without alerting defenders.

## Instructions

### Step 1: Download and Transfer JAWS Script

**Context**: Obtain the JAWS enumeration script from its official repository and transfer it to the target Windows system. This ensures local execution to avoid network dependencies and reduce detection risk.

Download the script using a browser or curl on your attack machine:

```bash
curl -O https://raw.githubusercontent.com/411Hall/JAWS/master/jaws-enum.ps1
```

Transfer the file to the target via your established access method (e.g., SMB copy if domain access, or upload via web shell). Place it in a temporary directory like C:\temp\.

**Expected Output**: jaws-enum.ps1 file present on the target at the specified path.

### Step 2: Set PowerShell Execution Policy

**Context**: Ensure PowerShell can import and run the unsigned JAWS module by temporarily bypassing execution restrictions. This step is necessary if the default policy blocks scripts.

Execute the following in your PowerShell session:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

**Expected Output**: No errors; policy changed for the current process.

### Step 3: Import and Run JAWS Module

**Context**: Load the JAWS module and execute the enumeration, directing output to a file for later review. This step performs the core discovery across multiple system areas.

**Command** ([[commands/jaws-enumerate-for-privilege-escalation]]):

```powershell
Import-Module .\jaws-enum.ps1 -OutputFileName C:\temp\jaws-output.txt
```

> This command imports the JAWS module from the current directory and runs the enumeration, saving results to the specified output file. The script will query accounts, services, processes, network settings, and permissions, producing a detailed log.

**Expected Output**: A text file (e.g., jaws-output.txt) generated with sections on Hotfixes, Users, Groups, Policies, Services, Autos, Tasks, Processes, and more. Look for indicators like 'Unquoted Service Path', 'Weak Service Permissions', or 'Writable SYSTEM Files'.

### Step 4: Review Output for Escalation Vectors

**Context**: Analyze the generated output file to identify actionable privilege escalation paths, such as exploitable services or misconfigured permissions.

Transfer the output file back to your attack machine if needed (e.g., via SMB or base64 encoding in the shell). Manually review sections like Services and File Permissions for vulnerabilities.

**Expected Output**: Identification of at least one potential escalation vector, such as a service running as SYSTEM with weak ACLs.

### Step 5: Clean Up

**Context**: Remove traces of the script and output to maintain operational security and avoid detection.

Delete the files:

```powershell
Remove-Item .\jaws-enum.ps1 -Force
Remove-Item C:\temp\jaws-output.txt -Force
Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope Process
```

**Expected Output**: Files removed without errors; execution policy reset.
