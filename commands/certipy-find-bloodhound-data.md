---
id: 61e8b405-1960-4519-be24-cbdc4f1e91a0
name: certipy-find-bloodhound-data
type: command
executor: bash
data: 'certipy find ''$_DOMAIN/$_USERNAME:$_PASSWORD@$_DC'' -bloodhound'
output: null
created_at: '2023-04-06T03:56:02.119115+00:00'
updated_at: '2023-10-10T20:26:14.196507+00:00'
platforms:
  - Linux
tags:
  - recon
  - ad
verified: true
validated: true
---

# certipy-find-bloodhound-data

## Command

```bash
certipy find '$_DOMAIN/$_USERNAME:$_PASSWORD@$_DC' -bloodhound
```

## Description

Searches Active Directory for certificate-related objects exportable to BloodHound format, identifying relationships for attack path analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain (e.g., corp.local) | Yes |
| $_USERNAME | Username for auth | Yes |
| $_PASSWORD | Password for auth | Yes |
| $_DC | Domain controller FQDN (e.g., dc.corp.local) | Yes |
| -bloodhound | Output in BloodHound JSON format | Yes |

## Examples

### Basic Usage

```bash
certipy find 'corp.local/john:Passw0rd@dc.corp.local' -bloodhound
```

### Advanced Usage

```bash
certipy find 'corp.local/john:Passw0rd@dc.corp.local' -bloodhound -output-dir ./output
```

## Expected Output

JSON files (nodes.json, edges.json) listing AD objects like users, computers, and cert templates with relationships.

## Related

- [[procedures/Active-Directory-Reconnaissance-with-BloodHound-and-Certipy]]
- [[tools/Certipy]]
