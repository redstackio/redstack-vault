---
id: 85478aa6-d1f7-488a-9402-e8f63f39a5e1
name: Windows-JuicyPotatoNG-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.273922+00:00'
updated_at: '2023-04-10T20:37:34.765115+00:00'
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access-Token-Manipulation|T1134 - Access Token Manipulation]]'
sub_techniques: []
tags:
  - '[[tags/EoP - Impersonation Privileges]]'
  - '[[tags/JuicyPotatoNG]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/juicy-potato-ng-execute-command-as-system]]'
platforms:
  - Windows
tools:
  - '[[tools/juicy-potato-ng]]'
validated: true
---

# Windows-JuicyPotatoNG-Privilege-Escalation

## Summary

This procedure uses JuicyPotatoNG to escalate privileges on a Windows system by exploiting COM object hijacking to impersonate the NT AUTHORITY\SYSTEM user, allowing execution of commands with SYSTEM-level access. It is effective on unpatched Windows systems vulnerable to token manipulation techniques, enabling attackers to bypass user-level restrictions for further post-exploitation activities like data access or malware deployment.

## Description

JuicyPotatoNG is an advanced iteration of the JuicyPotato exploit, targeting vulnerabilities in Windows COM (Component Object Model) interfaces to perform local privilege escalation. By creating and manipulating COM objects, the tool impersonates privileged tokens, such as those belonging to the SYSTEM account, to execute arbitrary commands with elevated privileges. This technique is particularly useful in scenarios where an attacker has initial low-privilege shell access (e.g., via phishing or initial exploit) and needs to escalate to SYSTEM for deeper system control. It maps to MITRE ATT&CK technique T1134 (Access Token Manipulation) under the Privilege Escalation and Defense Evasion tactics. The procedure assumes the target is a vulnerable Windows version (e.g., Windows 7-10 pre-patches) and requires the JuicyPotatoNG binary to be present on the system. Success grants full administrative control, but detection can occur through anomalous process creation or token changes.

## Requirements

1. Local administrator or user-level access to the target Windows system (non-SYSTEM initial privileges).
2. JuicyPotatoNG executable (JuicyPotatoNG.exe) downloaded and placed on the target system, typically in a writable directory like C:\temp.
3. Target system must be vulnerable to COM hijacking (unpatched Windows 7, 8, 10, or Server editions prior to relevant security updates).
4. Command prompt or PowerShell access for execution.

## Defense

- Apply the latest Windows security patches, particularly those addressing COM and token manipulation vulnerabilities (e.g., MS17-017 and subsequent updates).
- Implement principle of least privilege by restricting user accounts from unnecessary local logons and monitoring for anomalous privilege changes.
- Deploy endpoint detection and response (EDR) tools to monitor for suspicious process executions involving JuicyPotatoNG.exe or unexpected SYSTEM token usage.
- Enable Windows Defender Application Control (WDAC) or AppLocker to block unsigned executables like JuicyPotatoNG.
- Audit logs for Event ID 4672 (privilege assignments) and 4688 (process creation) to detect escalation attempts.

## Objectives

1. Escalate from user-level privileges to NT AUTHORITY\SYSTEM on a Windows host.
2. Execute arbitrary commands with elevated privileges to access sensitive data or deploy persistence mechanisms.
3. Verify successful escalation through output indicating SYSTEM context.

## Instructions

### Step 1: Prepare the Environment

**Context**: Ensure the JuicyPotatoNG tool is available on the target system and verify initial privileges to confirm escalation is needed. This step sets up the necessary files and checks the current user context to avoid unnecessary execution.

Use [[commands/whoami-check-current-user]] to verify current privileges:

```cmd
whoami /priv
```

> This command lists current privileges. If NT AUTHORITY\SYSTEM is not listed with full rights, proceed to escalation. Expected output includes a table of privileges like SeDebugPrivilege, confirming low-privilege state.

Download JuicyPotatoNG if not present (e.g., via PowerShell from a controlled source) and place it in a temporary directory like C:\temp\JuicyPotatoNG.exe.

### Step 2: Execute Privilege Escalation

**Context**: Run the JuicyPotatoNG tool to hijack a COM object and impersonate a SYSTEM token, then execute a test command to validate the escalation. This is the core step where token manipulation occurs, targeting all available tokens (-t *) for maximum compatibility.

Use [[tools/juicy-potato-ng]] and execute [[commands/juicy-potato-ng-execute-command-as-system]] to perform the escalation:

```cmd
JuicyPotatoNG.exe -t * -p "C:\Windows\System32\cmd.exe" -a "/c whoami" > C:\juicypotatong.txt
```

> The -t * flag targets all available tokens for impersonation. -p specifies the program to run elevated (cmd.exe). -a provides arguments to the program (/c whoami to check the escalated user). Output is redirected to a file for review without alerting monitoring tools. If successful, the file will contain 'nt authority\system', indicating privilege escalation. If it fails (e.g., due to patches), the output will show the original user context or an error like 'No token found'.

### Step 3: Verify and Clean Up

**Context**: Review the output file to confirm SYSTEM access and remove artifacts to maintain stealth. This step ensures the escalation worked and minimizes forensic evidence.

Check the output file:

```cmd
type C:\juicypotatong.txt
```

> Expected output: 'nt authority\system' confirming success. If not, review system logs for errors (e.g., Event Viewer under Security) and retry with different tokens if needed.

Delete the output file and tool for cleanup:

```cmd
del C:\juicypotatong.txt & del C:\temp\JuicyPotatoNG.exe
```

> This removes evidence. Success is indicated by no file remnants and no new alerts in monitoring tools.
