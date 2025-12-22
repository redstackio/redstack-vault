---
id: 99de6c16-d5d9-4f00-b441-5fb614331344
name: Clear-Windows-Event-Logs-for-Evasion
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.722906+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Indicator-Removal-on-Host|T1070 - Indicator Removal on Host]]'
sub_techniques:
  - >-
    [[sub-techniques/Clear-Windows-Event-Logs|T1070.001 - Clear Windows Event
    Logs]]
tags:
  - '[[tags/Clear-System-and-Security-Logs]]'
  - '[[tags/Disable-Antivirus-and-Security]]'
  - '[[tags/Windows-Persistence]]'
commands:
  - '[[commands/clear-windows-event-logs-wevtutil]]'
platforms:
  - Windows
tools: []
validated: true
---

# Clear-Windows-Event-Logs-for-Evasion

## Summary

This procedure clears the System and Security event logs on a Windows system to remove indicators of compromise, evading detection by antivirus and security monitoring tools. It uses the built-in wevtutil utility to erase log entries, helping attackers cover their tracks after initial access or during persistence operations.

## Description

Clearing event logs is a common defense evasion technique used post-exploitation to hinder forensic analysis and real-time detection. On Windows systems, event logs such as System and Security record activities like process creation, network connections, and authentication events, which can reveal attacker actions. By executing commands to clear these logs, an attacker with administrative privileges can erase evidence of their presence, making it harder for defenders to reconstruct the attack timeline. This procedure is particularly useful in scenarios where the attacker has obtained local admin rights via privilege escalation and wants to maintain stealth before exfiltrating data or establishing persistence. Note that clearing logs may itself generate an event in other logs or SIEM systems if monitored, so it should be used judiciously.

## Requirements

1. Administrative privileges on the target Windows system (local or domain admin).
2. Access to Command Prompt or PowerShell executed with elevated rights.
3. No additional tools required, as wevtutil is built into Windows (Vista and later).

## Defense

- Implement SIEM or centralized logging to forward event logs off-host before they can be cleared.
- Monitor for wevtutil.exe executions, especially 'cl' (clear) commands via process auditing or EDR tools.
- Enable protected event logging (via Group Policy) to prevent clearing of critical logs.
- Regularly backup event logs to secure, remote locations and alert on anomalous log sizes or clearing attempts.

## Objectives

1. Remove traces of attacker activities from System and Security event logs to evade detection.
2. Prevent security analysts from identifying the attack vector or timeline.
3. Maintain undetected access to the target for further operations like data exfiltration or lateral movement.

## Instructions

### Step 1: Verify Elevated Privileges

**Context**: Ensure you have administrative access, as clearing event logs requires elevated privileges. Without this, the commands will fail with access denied errors.

Run the following in an elevated Command Prompt to confirm:

```cmd
whoami /priv
```

> This displays your privileges; look for SeSecurityPrivilege and SeBackupPrivilege enabled. If not, escalate privileges first using another procedure like [[procedures/Exploit-Unpatched-Kernel-Vulnerability]].

### Step 2: Clear System Event Log

**Context**: The System log records service starts, driver loads, and system events that might log tool executions or network activity. Clearing it removes these indicators.

**Command** ([[commands/clear-windows-event-logs-wevtutil]]):

```cmd
wevtutil cl System
```

> This command uses wevtutil to clear the System log. It will prompt for confirmation unless run silently. Expected output: "Log cleared successfully." Verify by checking Event Viewer; the System log should be empty or reset.

### Step 3: Clear Security Event Log

**Context**: The Security log captures authentication, privilege use, and process audits, often key to detecting lateral movement or persistence. Clearing it erases login attempts and policy changes.

**Command** ([[commands/clear-windows-event-logs-wevtutil]]):

```cmd
wevtutil cl Security
```

> Similar to Step 2, this clears the Security log. Expected output: "Log cleared successfully." In Event Viewer, the Security log should show no recent entries. If auditing is enabled, this action might log in the remaining log—clear in quick succession.

### Step 4: Verify Log Clearance

**Context**: Confirm the logs are cleared to ensure the procedure succeeded and no residual indicators remain.

Open Event Viewer (eventvwr.msc) and navigate to Windows Logs > System and Security. Alternatively, query log counts:

```cmd
wevtutil gl System /c:1
wevtutil gl Security /c:1
```

> Expected output: Record count of 0 or very low (new events only). If counts are high, repeat the clearance or check for errors like insufficient privileges.
