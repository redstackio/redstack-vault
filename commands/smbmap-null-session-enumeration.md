---
id: 4df3bf34-9145-471f-a853-f4dee53a62d0
type: command
executor: bash
data: smbmap -H $_TARGET_IP
output: null
created_at: '2023-04-06T03:56:03.237938+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - discovery
  - smb
verified: true
validated: true
---

# smbmap-null-session-enumeration

## Command

```bash
smbmap -H $_TARGET_IP
```

## Description

Enumerates SMB shares on a target using a null session (no credentials). Ideal for initial reconnaissance to identify open shares without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H | Target IP address | Yes |
| $_TARGET_IP | IP of the Windows host (e.g., 10.10.10.10) | Yes |

## Examples

### Basic Usage

```bash
smbmap -H 10.10.10.10
```

### Advanced Usage

Combine with other flags for more detail, but this is null session only.

## Expected Output

```
[+] Finding open SMB ports....
[+] IP: 10.10.10.10:445 Name: TARGETHOST                                 
    Disk                                                    10.10.10.10 IPC$                     [Public IPC]           IPC                 (rw)           
    Disk                                                    10.10.10.10 C$                       [Default share]       Remote Admin        (ro)           
    Disk                                                    10.10.10.10 ADMIN$                   [Remote Admin]        Remote Admin        (ro)           
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/SMBMap]]
