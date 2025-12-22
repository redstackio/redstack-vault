---
id: 90c77397-f697-4324-b6c0-583909689187
name: upgrade-windows-meterpreter-x32-to-x64
type: procedure
verified: true
submitted: true
created_at: '2019-11-14T01:00:13.652758+00:00'
updated_at: '2023-05-25T20:00:05.354793+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Process Injection|T1055 - Process Injection]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/injection]]'
  - '[[tags/known-vulnerability]]'
commands:
  - '[[commands/metasploit-background-current-session]]'
  - '[[commands/meterpreter-list-running-processes]]'
  - '[[commands/meterpreter-migrate-to-process]]'
  - '[[commands/metasploit-use-payload-inject-module]]'
  - '[[commands/metasploit-set-session-id]]'
  - '[[commands/metasploit-run-payload-inject]]'
tools: []
validated: true
---

# Upgrade Windows Meterpreter x32 Shell to x64

## Summary

This procedure upgrades a 32-bit Meterpreter session to a 64-bit architecture on a Windows target, enabling access to full PowerShell features and avoiding limitations of the x86 environment. It is useful during post-exploitation when initial access was gained via a 32-bit payload but the target system is 64-bit, allowing attackers to evade detection and expand capabilities.

## Description

On 64-bit Windows systems, running a 32-bit Meterpreter session restricts access to certain features, such as full 64-bit PowerShell modules and processes. This procedure outlines two methods to migrate the session: using the Metasploit 'payload_inject' module to inject a 64-bit payload into a new process, or directly migrating the existing session to a stable 64-bit process using the 'migrate' command. Both approaches leverage process injection to maintain persistence while switching architectures, mapping to MITRE ATT&CK's Process Injection technique for defense evasion and potential privilege escalation if targeting a higher-privileged process.

## Requirements

1. Active 32-bit Meterpreter session on a 64-bit Windows target (e.g., via initial exploit like EternalBlue).
2. Metasploit Framework installed and running on the attacker's machine (Kali Linux recommended).
3. Network connectivity between attacker and target for reverse shell callbacks.
4. Basic knowledge of process architectures (x86 vs x64) to identify suitable migration targets.

## Defense

- Enable process creation monitoring via Windows Event Logs (Event ID 4688) to detect unexpected process injections.
- Use application whitelisting tools like AppLocker or WDAC to block unsigned or suspicious process migrations.
- Monitor for anomalous Meterpreter-like network traffic using EDR solutions (e.g., unusual SMB or HTTP beacons).
- Implement PowerShell Constrained Language Mode to limit script execution in 64-bit contexts post-migration.

## Objectives

1. Switch from 32-bit to 64-bit Meterpreter session to unlock full system capabilities.
2. Maintain session persistence without dropping the connection.
3. Evade detection by injecting into legitimate system processes.
4. Enable advanced post-exploitation like 64-bit PowerShell Empire or Cobalt Strike beacons.

## Instructions

This procedure provides two alternative approaches. Choose based on session stability and target environment; the payload_inject method is more reliable for unstable sessions.

### Approach 1: Using Metasploit Payload Inject Module

**Context**: This method backgrounds the current session, loads a Metasploit module to inject a 64-bit Meterpreter payload into a new process (e.g., notepad.exe), and establishes a fresh 64-bit session. It is ideal for upgrading architecture without relying on existing process stability.

#### Step 1: Background the Current Meterpreter Session

**Context**: Suspend the active 32-bit session to allow loading the migration module without interference.

**Command** ([[commands/metasploit-background-current-session]]):
```metasploit
bg
```

> This command backgrounds the session, returning control to the Metasploit console. Verify the session ID (e.g., session 1) for later use.

#### Step 2: Load the Payload Inject Module

**Context**: Select the exploit module designed for local payload injection to prepare for 64-bit migration.

**Command** ([[commands/metasploit-use-payload-inject-module]]):
```metasploit
use exploit/windows/local/payload_inject
```

> Loads the module into the Metasploit console. Confirm with 'show options' to ensure compatibility with Windows targets.

#### Step 3: Set the Target Session ID

**Context**: Specify the backgrounded 32-bit session as the source for injection.

**Command** ([[commands/metasploit-set-session-id]]):
```metasploit
set session $_SESSION_ID
```

> Replace $_SESSION_ID with the actual ID (e.g., 1). This links the module to the existing session for migration.

#### Step 4: Execute the Payload Injection

**Context**: Run the module to launch a 64-bit process and inject the upgraded payload, creating a new Meterpreter session.

**Command** ([[commands/metasploit-run-payload-inject]]):
```metasploit
run
```

> The module starts a reverse TCP handler, launches a temporary process like notepad.exe, injects the 64-bit payload, and opens a new session. Interact with the new session using 'sessions -i <new_id>'.

### Approach 2: Using the Migrate Command

**Context**: This direct method lists running processes, identifies a stable 64-bit one (e.g., explorer.exe or svchost.exe), and migrates the session into it. Use this for quick upgrades when the current session is stable.

#### Step 1: List Running Processes

**Context**: Enumerate processes to find a suitable 64-bit target (look for 'x64' in the Arch column; prefer system-started processes for reliability).

**Command** ([[commands/meterpreter-list-running-processes]]):
```metasploit
ps
```

> Displays a table of PIDs, names, architectures, and paths. Note the PID of a 64-bit process with similar or higher privileges (e.g., PID 1234 for svchost.exe x64).

#### Step 2: Migrate to the Selected 64-Bit Process

**Context**: Inject the Meterpreter payload into the chosen 64-bit process to upgrade the session architecture.

**Command** ([[commands/meterpreter-migrate-to-process]]):
```metasploit
migrate $_PID
```

> Replace $_PID with the target PID (e.g., 1234). The migration injects the payload and switches the session; verify architecture with 'ps' post-migration.
