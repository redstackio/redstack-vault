---
id: 98a926fc-f02a-4e79-bb0b-1b0d3c261ff4
name: Metasploit Enum SMB Shares
type: command
executor: msfconsole
data: use scanner/smb/smb_enumshares; set RHOSTS $_TARGET_IP; run
output: null
created_at: '2023-04-06T03:56:03.529861+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - discovery
  - smb
verified: true
validated: true
---

# Metasploit Enum SMB Shares

## Command

```msfconsole
use scanner/smb/smb_enumshares; set RHOSTS $_TARGET_IP; run
```

## Description

This Metasploit module enumerates SMB shares on a remote Windows host, useful for discovering accessible resources like SYSVOL in Active Directory environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| RHOSTS ($_TARGET_IP) | Target IP address or range | Yes |
| SMBUser | Username for authentication (optional) | No |
| SMBPass | Password for authentication (optional) | No |

## Examples

### Basic Usage

```msfconsole
use scanner/smb/smb_enumshares; set RHOSTS 192.168.1.10; run
```

### With Credentials

```msfconsole
use scanner/smb/smb_enumshares; set RHOSTS 192.168.1.10; set SMBUser domain\\user; set SMBPass password; run
```

## Expected Output

[+] 192.168.1.10:445 - SMB - Share: ADMIN$, Type: Disk, Comment: Remote Admin  
[+] 192.168.1.10:445 - SMB - Share: C$, Type: Disk, Comment: Default share  
[+] 192.168.1.10:445 - SMB - Share: SYSVOL, Type: Disk, Comment: 

## Related

- [[procedures/Automated-Password-Extraction-from-SYSVOL-and-Group-Policy-Preferences]]
- [[tools/Metasploit-Framework]]
