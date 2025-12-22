---
id: 36206460-5693-4536-b12c-71351f7a302e
name: certipy-find-old-bloodhound-data
type: command
executor: bash
data: 'certipy find ''$_DOMAIN/$_USERNAME:$_PASSWORD@$_DC'' -old-bloodhound'
output: null
created_at: '2023-04-06T03:56:02.119156+00:00'
updated_at: '2023-10-10T20:26:14.196507+00:00'
platforms:
  - Linux
tags:
  - recon
  - ad
verified: true
validated: true
---

# certipy-find-old-bloodhound-data

## Command

```bash
certipy find '$_DOMAIN/$_USERNAME:$_PASSWORD@$_DC' -old-bloodhound
```

## Description

Identifies outdated certificates in AD that may be exploitable, outputting in BloodHound format for relationship mapping.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain | Yes |
| $_USERNAME | Auth username | Yes |
| $_PASSWORD | Auth password | Yes |
| $_DC | Domain controller | Yes |
| -old-bloodhound | Flag for legacy cert search in BH format | Yes |

## Examples

### Basic Usage

```bash
certipy find 'corp.local/john:Passw0rd@dc.corp.local' -old-bloodhound
```

## Expected Output

List of old certs with details like issue date, template, and linked objects in JSON.

## Related

- [[procedures/Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[tools/Certipy]]
