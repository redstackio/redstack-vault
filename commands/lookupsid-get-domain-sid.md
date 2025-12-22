---
id: 54e7239c-8dfd-4cbb-a807-0dc883882543
name: lookupsid-get-domain-sid
type: command
executor: bash
data: 'lookupsid.py ''$_DOMAIN/$_USERNAME:$_PASSWORD''@$_TARGET_IP'
output: >-
  root@kali:~# lookupsid.py 'bank.local/bsmith:hunter2'@10.10.10.5

  Impacket v0.9.22.dev1+20200428.191254.96c7a512 - Copyright 2020 SecureAuth
  Corporation


  [*] Brute forcing SIDs at 10.10.10.5

  [*] StringBinding ncacn_np:10.10.10.5[\pipe\lsarpc]

  [*] Domain SID is: S-1-5-21-2291914956-2855975875-54887866952

  ...

  ...
created_at: '2020-06-24T05:08:26.191958+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - active-directory
  - discovery
verified: true
validated: true
---

# lookupsid-get-domain-sid

## Command

```bash
lookupsid.py '$_DOMAIN/$_USERNAME:$_PASSWORD'@$_TARGET_IP
```

## Description

This command uses Impacket's lookupsid.py to brute-force and retrieve the domain SID from a Windows domain controller via the LSARPC pipe, requiring valid domain credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name (e.g., bank.local) | Yes |
| $_USERNAME | Domain username | Yes |
| $_PASSWORD | Domain password | Yes |
| $_TARGET_IP | Domain controller IP address | Yes |

## Examples

### Basic Usage

```bash
lookupsid.py 'bank.local/bsmith:hunter2'@10.10.10.5
```

### Advanced Usage

Use with proxychains for pivoting:
```bash
proxychains lookupsid.py 'domain/user:pass'@192.168.1.10
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# lookupsid.py 'bank.local/bsmith:hunter2'@10.10.10.5
Impacket v0.9.22.dev1+20200428.191254.96c7a512 - Copyright 2020 SecureAuth Corporation

[*] Brute forcing SIDs at 10.10.10.5
[*] StringBinding ncacn_np:10.10.10.5[\pipe\lsarpc]
[*] Domain SID is: S-1-5-21-2291914956-2855975875-54887866952
...
...
```

Look for the "Domain SID is:" line to extract the value.

## Related

- [[procedures/Create-Golden-Ticket-and-Launch-Windows-SYSTEM-Shell-from-Linux]]
