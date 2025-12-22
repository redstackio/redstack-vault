---
id: 57b3a931-e2ba-4714-b818-1996175dd1b3
name: Certipy-AD-Recon-Command-Sequence
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:02.119007+00:00'
updated_at: '2023-10-10T20:26:14.194807+00:00'
platforms:
  - Linux
tags:
  - recon
  - ad
  - cert
validated: true
---

# Certipy-AD-Recon-Command-Sequence

## Code

```bash
certipy find 'corp.local/john:Passw0rd@dc.corp.local' -bloodhound
certipy find 'corp.local/john:Passw0rd@dc.corp.local' -old-bloodhound
certipy find 'corp.local/john:Passw0rd@dc.corp.local' -vulnerable -hide-admins -username user@domain -password Password123
```

## Description

Sequence of Certipy commands to perform AD certificate reconnaissance, generating BloodHound-compatible data and identifying vulnerabilities.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| corp.local | Domain name | corp.local |
| john | Username | john |
| Passw0rd | Password | Passw0rd |
| dc.corp.local | DC FQDN | dc.corp.local |
| user@domain | Override username | user@corp.local |
| Password123 | Override password | Password123 |

## Usage

Run sequentially in a Python environment with Certipy to collect cert data for BloodHound import during AD recon.

## Detection

- Anomalous LDAP queries to AD CS
- Python processes with Certipy imports
- Outbound connections to DC on port 636

## Related

- [[procedures/Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[tools/Certipy]]
