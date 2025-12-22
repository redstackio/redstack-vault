---
id: 07eea62c-a51d-4ff7-9fba-297ebea7c7ce
name: Enumerate-Installed-Antivirus-Products-Windows
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.749497+00:00'
updated_at: '2023-04-10T20:37:53.508273+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Bypass User Account Control|T1088 - Bypass User Account
    Control]]
  - >-
    [[techniques/Security Software Discovery|T1063 - Security Software
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Antivirus Enumeration]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/wmic-query-antivirus-products]]'
platforms:
  - Windows
tools: []
validated: true
---

# Enumerate-Installed-Antivirus-Products-Windows

## Summary

This procedure uses Windows Management Instrumentation Command-line (WMIC) to query the system's Security Center for details on installed antivirus products. It reveals the names and configurations of AV software, which can help identify potential bypass opportunities or misconfigurations for privilege escalation during red team engagements or penetration testing.

## Description

Antivirus enumeration involves querying the Windows Security Center namespace to discover installed endpoint protection software. This technique is part of the discovery phase in an attack, allowing attackers to assess the target's defenses. By identifying the specific AV product (e.g., Windows Defender, McAfee, Symantec), an operator can research known vulnerabilities, weak configurations, or evasion methods. For instance, outdated AV versions might have exploitable flaws, or misconfigured real-time scanning could be bypassed. This is particularly useful in privilege escalation scenarios where AV blocks execution of payloads. The query works on local or remote systems with appropriate WMI access, but requires command-line privileges on the target. Success provides a list of AV display names, which can be cross-referenced with vulnerability databases like CVE or exploit frameworks.

## Requirements

1. Command-line access to the target Windows system (local or remote via WMI).
2. Administrative privileges may be needed for remote queries (/Node parameter).
3. Windows OS with WMI enabled (default on modern versions like Windows 10/11 or Server 2016+).
4. No additional tools required; WMIC is built-in to Windows.

## Defense

- Ensure antivirus software is properly configured, up-to-date, and monitored for queries or unusual WMI activity.
- Limit user privileges to prevent unauthorized command-line access and WMI queries.
- Implement network segmentation and WMI filtering to restrict remote access.
- Enable Windows Event Logging for WMI (Event ID 5857 for AV-related queries) and monitor for anomalous enumeration attempts.

## Objectives

1. Identify installed antivirus products to uncover potential vulnerabilities for exploitation.
2. Detect misconfigurations in AV that could enable privilege escalation or payload execution.
3. Gather intelligence on the target's security posture to inform subsequent evasion tactics.

## Instructions

### Step 1: Query Installed Antivirus Products

**Context**: Use WMIC to retrieve the display names of all antivirus products registered in the Security Center. This step works locally by default but can target remote systems. Run this from an elevated command prompt to ensure access; for remote execution, specify the target computer name to avoid authentication issues.

**Command** ([[commands/wmic-query-antivirus-products]]):
```cmd
WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntivirusProduct Get displayName
```

> This command queries the WMI SecurityCenter2 namespace for the 'displayName' property of all AntivirusProduct instances. Replace 'localhost' with a remote hostname or IP if targeting another machine. If no AV is installed or registered, it returns an empty list. Verify success by checking for recognizable AV names like 'Windows Defender Antivirus'. If the query fails (e.g., access denied), escalate privileges or confirm WMI connectivity.

### Step 2: Interpret and Validate Results

**Context**: Review the output to identify the AV product and version. Cross-reference with known exploits or bypass techniques. If multiple products are listed, note any conflicts or disabled ones that could be leveraged.

**Command** ([[commands/wmic-query-antivirus-products]]):
```cmd
WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntivirusProduct Get displayName,productState /format:table
```

> This variation includes 'productState' to show AV status (e.g., enabled/disabled). Expected output includes a table with names and states. Use this to confirm if AV is active, which impacts escalation strategies like injecting into trusted processes.
