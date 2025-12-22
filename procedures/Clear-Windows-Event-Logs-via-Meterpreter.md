---
id: eca72344-c803-4a09-98e8-31ef20343991
name: Clear-Windows-Event-Logs-via-Meterpreter
type: procedure
verified: true
submitted: true
created_at: '2019-12-18T18:42:07.362540+00:00'
updated_at: '2023-05-25T19:59:14.495209+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/audit]]'
  - defense-evasion
  - log-clearing
commands:
  - '[[commands/metasploit-clear-event-logs]]'
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Clear-Windows-Event-Logs-via-Meterpreter

## Summary

This procedure uses a Meterpreter session within the Metasploit Framework to clear Windows event logs, helping to evade detection by removing traces of attacker activity from the Application, System, and Security logs. It is particularly useful in post-exploitation scenarios where maintaining stealth is critical, though it may trigger alerts in monitored environments.

## Description

Clearing event logs is a common defense evasion technique after gaining access to a Windows system. Using Meterpreter's built-in 'clearev' command, this procedure wipes records from key event log categories without needing additional tools or direct file manipulation, which could leave further artifacts. The technique targets the Windows Event Log service and is effective on systems running Windows Vista and later. However, many security tools and SIEM systems monitor for log clearing events, so this should be used judiciously in stealthy operations. It maps to MITRE ATT&CK technique T1070 for indicator removal on host.

## Requirements

1. An active Meterpreter session on the target Windows system (achieved via exploitation and payload delivery using Metasploit).
2. Metasploit Framework installed on the attacker's machine (Kali Linux recommended).
3. Administrative privileges on the target, as log clearing typically requires elevated access.
4. Network connectivity between attacker and target for maintaining the session.

## Defense

Defensive measures and detection strategies:

- Enable advanced auditing for logon events and object access to detect unauthorized log modifications.
- Use tools like Sysmon or Windows Event Forwarding to create immutable copies of logs before they can be cleared.
- Monitor for Meterpreter processes or unusual network connections indicative of C2 communication.
- Implement SIEM rules to alert on event log clearing attempts, such as Event ID 1102 in Security logs.

## Objectives

1. Remove attacker footprints from Windows event logs to evade forensic analysis.
2. Maintain operational stealth during post-exploitation activities.
3. Minimize detection risk from log-based monitoring tools.

## Instructions

### Step 1: Establish and Verify Meterpreter Session

**Context**: Ensure you have an active Meterpreter session on the target Windows machine. This is a prerequisite, as the log clearing command operates within the session.

If not already established, use Metasploit to exploit the target and deliver the Meterpreter payload. Once connected, verify the session with basic commands like 'sysinfo' or 'getuid' to confirm elevated privileges.

**Expected Output**: Confirmation of session details, such as OS version and user context, indicating successful access.

### Step 2: Execute Log Clearing Command

**Context**: From within the Meterpreter shell, run the 'clearev' command to wipe the primary event logs. This step removes entries from Application, System, and Security logs, effectively hiding prior actions like logons or process creations.

**Command** ([[commands/metasploit-clear-event-logs]]):
```metasploit
clearev
```

> The command iterates through the logs, displaying the number of records wiped for each category. It requires no additional parameters and operates silently on the target without generating new log entries in most cases.

**Expected Output**:
```
meterpreter > clearev
[*] Wiping 1919 records from Application...
[*] Wiping 1406 records from System...
[*] Wiping 7980 records from Security...
```

This output confirms the number of entries removed from each log type. Success is indicated by the completion of wiping without errors.
