---
id: 638a6a72-c4f2-4c2f-9f79-50c3085aef4d
name: RustHound-AD-Data-Collection-Sequence
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:02.119313+00:00'
updated_at: '2023-10-10T20:26:14.194807+00:00'
platforms:
  - Windows
  - Linux
tags:
  - recon
  - ad
validated: true
---

# RustHound-AD-Data-Collection-Sequence

## Code

```bash
# Windows with GSSAPI session
rusthound.exe -d domain.local --ldapfqdn domain
# Windows/Linux simple bind connection username:password
rusthound.exe -d domain.local -u user@domain.local -p Password123 -o output -z
# Linux with username:password and ADCS module for @ly4k BloodHound version
rusthound -d domain.local -u 'user@domain.local' -p 'Password123' -o /tmp/adcs --adcs -z
```

## Description

Series of RustHound commands for collecting AD data via different auth methods, including ADCS support for enhanced BloodHound graphs.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| domain.local | Target domain | domain.local |
| user@domain.local | Username | user@domain.local |
| Password123 | Password | Password123 |
| output | Output directory | ./output |
| /tmp/adcs | ADCS output path | /tmp/adcs |

## Usage

Execute based on environment (GSSAPI for Windows sessions, simple bind for Linux) to gather data for BloodHound visualization.

## Detection

- Execution of rusthound.exe or rusthound binary
- LDAP over GSSAPI or simple bind spikes
- ZIP files with JSON exports in temp dirs

## Related

- [[procedures/Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[tools/RustHound]]
