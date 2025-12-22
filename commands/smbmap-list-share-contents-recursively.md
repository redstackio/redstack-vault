---
type: command
executor: bash
data: smbmap -u $_USERNAME -p $_PASSWORD -R $_SHARE_NAME -H $_TARGET_IP
platforms:
  - Linux
  - Windows
tags:
  - enumeration
  - smb
verified: true
validated: true
---

# smbmap-list-share-contents-recursively

## Command

```bash
smbmap -u $_USERNAME -p $_PASSWORD -R $_SHARE_NAME -H $_TARGET_IP
```

## Description

This command uses SMBMap to authenticate to a target SMB server and recursively list the contents of a specific share, displaying directories, files, permissions, sizes, and modification times. It's useful for mapping out share structures during reconnaissance or identifying sensitive files for download. Requires valid credentials unless the share allows guest access (omit -u/-p for NULL sessions).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Username for SMB authentication (e.g., 'bob') | Yes (for authenticated access) |
| $_PASSWORD | Password or NTLM hash for the user | Yes (for authenticated access) |
| $_SHARE_NAME | Name of the SMB share to enumerate (e.g., 'temp') | Yes |
| $_TARGET_IP | IP address or hostname of the target SMB server | Yes |
| -u | Flag to specify username | Built-in |
| -p | Flag to specify password/hash | Built-in |
| -R | Flag for recursive directory listing | Built-in |
| -H | Flag to specify target host | Built-in |

## Examples

### Basic Usage

```bash
smbmap -u bob -p secretpass -R temp -H 10.10.10.10
```

### Advanced Usage

For NULL session (anonymous):

```bash
smbmap -R IPC$ -H 10.10.10.10
```

(IPC$ is a common null session share for enumeration.)

## Expected Output

```
[+] Finding open SMB ports....  
[+] User SMB session established on 10.10.10.10...
[+] IP: 10.10.10.10:445 Name: 10.10.10.14
        Disk                                                    Permissions 
        ----                                                    ----------- 
        msfadmin                                                READ ONLY 
        .\                                                                                  
        dr--r--r--                0 Thu Sep 12 14:30:21 2019    . 
        dw--w--w--                0 Fri Apr 16 02:16:01 2010    ..
        dr--r--r--                0 Tue Apr 27 23:44:16 2010    vulnerable 
        -r--r--r--                4 Sun May 20 14:22:31 2012    .rhosts 
        dr--r--r--                0 Mon May 17 21:43:17 2010    .ssh
        dw--w--w--                0 Sat Apr 17 14:10:59 2010    .
        dr--r--r--                0 Sat Apr 17 14:10:59 2010    ..
        -w--w--w--                0 Sat Apr 17 14:10:59 2010    cpu_localhost_0
```

Success is indicated by the listing of share contents without authentication errors. Empty or permission-denied outputs suggest access issues.

## Related

- [[tools/SMBMap]] (parent tool)
- [[Related Procedure]] (if applicable, e.g., SMB share enumeration procedure)
