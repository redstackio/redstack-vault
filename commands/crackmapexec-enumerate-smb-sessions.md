---
type: command
executor: bash
data: cme smb $_TARGET_SUBNET -u $_USERNAME -p $_PASSWORD --sessions
output: null
created_at: '2023-04-06T03:56:04Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - enumeration
  - smb
verified: true
validated: true
---

# crackmapexec-enumerate-smb-sessions

## Command

```bash
cme smb $_TARGET_SUBNET -u $_USERNAME -p $_PASSWORD --sessions
```

## Description

This command uses CrackMapExec to authenticate via SMB to hosts in a subnet and enumerate active sessions, revealing logged-in users for each machine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_SUBNET | Target network range (e.g., 10.10.10.0/24) | Yes |
| -u $_USERNAME | Domain username for authentication | Yes |
| -p $_PASSWORD | Password for the username | Yes |
| --sessions | Flag to enumerate SMB sessions | Yes |

## Examples

### Basic Usage

```bash
cme smb 10.10.10.0/24 -u Administrator -p 'P@ssw0rd' --sessions
```

### Advanced Usage

```bash
cme smb 10.10.10.0/24 -u lowpriv -p 'weakpass' --sessions --continue-on-success
```

## Expected Output

```
SMB         10.10.10.10    445    WIN-8OJFTLMU1IG  [+] Enumerated sessions
SMB         10.10.10.10    445    WIN-8OJFTLMU1IG  \\10.10.10.10            User:Administrator
```
Lists IP, hostname, and user sessions per host.

## Related

- [[procedures/Active-Directory-User-Enumeration]]
- [[tools/CrackMapExec]]
