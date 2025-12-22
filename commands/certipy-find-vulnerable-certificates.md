---
id: 691163f9-b82d-45d2-9611-2cae64eb370d
name: certipy-find-vulnerable-certificates
type: command
executor: bash
data: >-
  certipy find '$_DOMAIN/$_USERNAME:$_PASSWORD@$_DC' -vulnerable -hide-admins
  -username $_USERNAME -password $_PASSWORD
output: null
created_at: '2023-04-06T03:56:02.119238+00:00'
updated_at: '2023-10-10T20:26:14.196507+00:00'
platforms:
  - Linux
tags:
  - recon
  - ad
  - cert
verified: true
validated: true
---

# certipy-find-vulnerable-certificates

## Command

```bash
certipy find '$_DOMAIN/$_USERNAME:$_PASSWORD@$_DC' -vulnerable -hide-admins -username $_USERNAME -password $_PASSWORD
```

## Description

Locates vulnerable certificates (e.g., ESC8) in AD CS, excluding admins for focused recon.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Domain name | Yes |
| $_USERNAME | Initial auth user | Yes |
| $_PASSWORD | Initial auth pass | Yes |
| $_DC | DC hostname | Yes |
| -vulnerable | Search for exploitable certs | Yes |
| -hide-admins | Exclude admin accounts | No |
| -username | Override username | No |
| -password | Override password | No |

## Examples

### Basic Usage

```bash
certipy find 'corp.local/john:Passw0rd@dc.corp.local' -vulnerable -hide-admins
```

## Expected Output

Table of vulnerable certs with templates, subjects, and potential attacks (e.g., "Vulnerable to ESC1").

## Related

- [[procedures/Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[tools/Certipy]]
