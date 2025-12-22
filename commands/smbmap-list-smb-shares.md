---
id: 0071c284-e546-4b48-be33-69e446d29b33
name: smbmap-list-smb-shares
type: command
executor: bash
data: smbmap -u '$_USERNAME' -p '$_PASSWORD' -H $_TARGET_IP
output: >-
  root@kali:~# smbmap -u 'bob' -p 's3cr3t' -H 10.10.10.10

  [+] Finding open SMB ports....

  [+] User SMB session establishd on 10.10.10.10...

  [+] IP: 10.10.10.10:445 Name:
  10.10.10.10                                       
          Disk                                                    Permissions
          ----                                                    -----------
          print$                                                  NO ACCESS
          opt                                                     NO ACCESS
          IPC$                                                    NO ACCESS
          ADMIN$                                                  NO ACCESS
created_at: '2019-09-18T01:44:02.132073+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - enumeration
verified: true
validated: true
---

# smbmap-list-smb-shares

## Command

```bash
smbmap -u '$_USERNAME' -p '$_PASSWORD' -H $_TARGET_IP
```

## Description

Enumerates SMB shares and their permissions using SMBMap.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H $_TARGET_IP | Target host IP | Yes |
| -u '$_USERNAME' | Username | No |
| -p '$_PASSWORD' | Password | No |

## Examples

### Basic

```bash
smbmap -H 10.10.10.10
```

## Expected Output

Disk list with permissions.

## Related

- [[procedures/List-Available-SMB-Shares]]
