---
id: af9684d2-0eef-454c-8612-cb8ed4126960
name: meterpreter-getsystem-privilege-escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.371881+00:00'
updated_at: '2023-04-10T20:25:01.583917+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
  - >-
    [[techniques/Bypass User Account Control|T1088 - Bypass User Account
    Control]]
sub_techniques: []
tags:
  - get-system
  - metasploit
  - meterpreter-basic
commands:
  - '[[commands/meterpreter-getsystem-elevate-to-system]]'
  - '[[commands/meterpreter-getuid-check-user-context]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit]]'
validated: true
---

# meterpreter-getsystem-privilege-escalation

## Summary

This procedure uses the Meterpreter payload within the Metasploit framework to escalate privileges from a standard user session to SYSTEM-level access on a compromised Windows system. It leverages techniques like named pipe impersonation to achieve elevation without dropping additional files, enabling further post-exploitation activities such as persistence, data exfiltration, or lateral movement.

## Description

Meterpreter is an advanced post-exploitation payload in Metasploit that provides a dynamic environment for interacting with compromised hosts. The 'getsystem' command attempts multiple privilege escalation methods, starting with in-memory techniques like named pipe impersonation, token manipulation, and UAC bypass, to elevate the session to NT AUTHORITY\SYSTEM. This is particularly effective on Windows systems where the initial access might be at a limited user level. Once elevated, the attacker can perform administrative actions. The procedure assumes an active Meterpreter session and focuses on verification of the escalation. It maps to MITRE ATT&CK for privilege escalation and defense evasion in post-exploitation scenarios.

## Requirements

1. An active Meterpreter session on the target Windows system (e.g., obtained via exploit or phishing).
2. Metasploit Framework installed on the attacker's machine (Kali Linux or equivalent).
3. Network connectivity between attacker and target for the session to remain active.
4. Initial access at least at user level; administrative privileges not required for escalation attempt.

## Defense

Defensive measures and detection strategies:

- Implement application whitelisting and restrict execution of unsigned binaries or scripts to prevent initial payload delivery.
- Enable Windows Defender Exploit Guard and UAC to block common escalation vectors like named pipe impersonation.
- Monitor for suspicious process injections or token manipulations using Sysmon (Event IDs 10, 12) and Windows Event Logs (ID 4688 for process creation).
- Use endpoint detection tools to alert on Meterpreter-like network patterns, such as beaconing over common ports.
- Regularly audit privileged accounts and limit service account usage to reduce escalation impact.

## Objectives

1. Escalate the Meterpreter session privileges to NT AUTHORITY\SYSTEM.
2. Verify the new privilege level to confirm successful escalation.
3. Enable administrative access for subsequent post-exploitation tasks like persistence or credential dumping.

## Instructions

### Step 1: Elevate Privileges Using Getsystem

**Context**: Within the active Meterpreter session, execute the getsystem command to attempt privilege escalation. Meterpreter tries several techniques automatically, such as named pipe impersonation (Technique 1), which creates an in-memory admin token without disk writes. This step is performed immediately after gaining initial shell access to maximize the window for escalation before detection.

**Command** ([[commands/meterpreter-getsystem-elevate-to-system]]):
```bash
getsystem
```

> The command runs silently and attempts escalation methods in order. If successful via named pipe impersonation, it will output a confirmation message indicating the technique used. Failure may occur if the system has strong mitigations like Credential Guard enabled; in such cases, retry or pivot to alternative escalation procedures.

### Step 2: Verify Escalation with Getuid

**Context**: After getsystem completes, check the current user context to confirm elevation to SYSTEM. This step validates success and provides awareness of the privilege level for planning next actions, such as running administrative commands or migrating to a more stable process.

**Command** ([[commands/meterpreter-getuid-check-user-context]]):
```bash
getuid
```

> The command returns the current username. Success is indicated by 'NT AUTHORITY\SYSTEM', confirming full administrative control. If it shows a lower privilege (e.g., 'NT AUTHORITY\LOCAL SERVICE'), the escalation failed, and alternative techniques like token impersonation may be needed.
