---
id: 35f45ae4-7ad2-46d4-bc12-e58be7f64fb1
name: Elevate-Privileges-Using-Cobalt-Strike-Beacon-Runasadmin
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:16.627590+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Event Triggered Execution|T1546 - Event Triggered Execution]]'
  - '[[techniques/Process Injection|T1055 - Process Injection]]'
sub_techniques:
  - >-
    [[sub-techniques/Component Object Model Hijacking|T1546.015 - Component
    Object Model Hijacking]]
tags:
  - '[[tags/Cobalt Strike]]'
  - '[[tags/Elevate Kit]]'
  - '[[tags/Kits]]'
  - privilege-escalation
  - windows
commands:
  - '[[commands/beacon-runasadmin-list-exploits]]'
platforms:
  - Windows
tools:
  - '[[tools/Cobalt-Strike]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Elevate Privileges Using Cobalt Strike Beacon Runasadmin

## Summary

This procedure uses the Cobalt Strike Elevate Kit's 'runasadmin' Beacon command to list and execute privilege escalation exploits, allowing attackers to gain SYSTEM-level access on Windows targets by exploiting vulnerabilities like UAC bypasses and kernel flaws. It is effective for post-exploitation in red team engagements where initial low-privilege access via Beacon is established.

## Description

The Cobalt Strike Elevate Kit integrates with Beacon implants to facilitate privilege escalation through a suite of built-in exploits targeting Windows vulnerabilities. The 'runasadmin' command invokes the Elevators module, which lists available exploits such as kernel NULL pointer dereferences (e.g., CVE-2014-4113), WebDAV local escalations (e.g., CVE-2016-0051), and UAC bypass techniques like token duplication or schtasks.exe abuse. Once listed, an exploit is selected and executed to inject code into legitimate processes or trigger event-based execution, evading detection by running with elevated privileges. This approach is particularly useful in domain environments for lateral movement and persistence, but exploits may fail on patched systems (e.g., uac-token-duplication is fixed in Windows 10 RS5). The procedure assumes an active Beacon session on the target and focuses on Windows 7-10/Server editions.

## Requirements

1. Active Cobalt Strike Beacon implant with low-privilege access on the target Windows system (e.g., via initial access through phishing or exploit).
2. Cobalt Strike client and team server configured for command execution.
3. Target system vulnerabilities unpatched (e.g., pre-October 2018 for certain UAC bypasses).
4. Network connectivity between the C2 server and the Beacon for command relay.

## Defense

- Enable and monitor Windows Defender Exploit Guard and Credential Guard to block UAC bypasses and process injection.
- Regularly patch Windows systems (e.g., apply MS14-058, MS15-051, MS16-016 fixes) and disable unnecessary services like WMI event subscriptions.
- Implement application whitelisting (e.g., AppLocker) to prevent unauthorized executable execution and monitor for anomalous process spawning via EDR tools like Sysmon or CrowdStrike.
- Audit Beacon-like C2 traffic on high/restricted ports and enable PowerShell logging for script-based injections.

## Objectives

1. List available privilege escalation exploits compatible with the target system.
2. Execute a selected exploit to elevate the Beacon session to SYSTEM privileges.
3. Verify elevated access for further post-exploitation actions like data access or lateral movement.
4. Maintain stealth by avoiding detection through process injection and event triggers.

## Instructions

### Step 1: List Available Elevators

**Context**: Invoke the 'runasadmin' command in the Beacon console to display the list of available exploits in the Elevate Kit. This step identifies which elevators are viable based on the target's OS and patch level, allowing selection of the most appropriate one.

**Command** ([[commands/beacon-runasadmin-list-exploits]]):
```bash
beacon> runasadmin
```

> This command queries the Elevate Kit and outputs a table of exploits with descriptions. Review the list for compatibility; for example, kernel exploits like ms14-058 work on older Windows versions, while UAC bypasses like uac-token-duplication target modern systems.

### Step 2: Select and Execute an Exploit

**Context**: Choose an exploit from the list (e.g., 'uac-token-duplication' for UAC bypass via token manipulation) and execute it to escalate privileges. This injects the exploit payload, potentially using process hollowing or WMI triggers, to spawn an elevated Beacon or shell.

**Instructions**: In the Beacon console, use the 'execute' subcommand with the exploit name. Monitor for success indicators like a new elevated session spawning.

For example, to execute the UAC token duplication exploit:
```bash
beacon> runasadmin execute uac-token-duplication
```

> If successful, the exploit duplicates a high-integrity token and runs the payload as SYSTEM. On failure (e.g., patched system), try alternatives like 'uac-schtasks' which abuses scheduled tasks for silent cleanup execution. Verify elevation by checking the new session's integrity level.

### Step 3: Verify Elevated Privileges

**Context**: Confirm the escalation by executing a privilege check command in the new session, ensuring access to protected resources like the SYSTEM registry hive or service controls.

**Instructions**: In the elevated Beacon session, run a command to query privileges or access a high-privilege resource.

For example:
```bash
beacon> whoami /priv
```

> Expected output should show 'nt authority\system' with enabled privileges like SeDebugPrivilege. If not elevated, retry with another exploit or diagnose via error logs.
