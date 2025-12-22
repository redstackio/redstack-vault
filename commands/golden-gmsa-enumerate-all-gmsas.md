---
id: 27b77957-e3ed-4a43-8dc9-47f7229d4600
name: golden-gmsa-enumerate-all-gmsas
type: command
executor: bash
data: GoldenGMSA.exe gmsainfo
output: null
created_at: '2023-04-06T03:56:04.615293+00:00'
updated_at: '2023-04-10T20:25:56.697280+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - enumeration
verified: true
validated: true
---

# golden-gmsa-enumerate-all-gmsas

## Command

```bash
GoldenGMSA.exe gmsainfo
```

## Description

This command enumerates all Group Managed Service Accounts (GMSAs) in the Active Directory domain, listing their SIDs and other attributes. Use it during reconnaissance to identify service accounts for potential forging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| gmsainfo | Subcommand to enumerate GMSAs | Yes |

## Examples

### Basic Usage

```bash
GoldenGMSA.exe gmsainfo
```

Enumerates all GMSAs accessible via LDAP.

## Expected Output

A list of GMSAs with details like:
```
GMSA Name: svc-example
SID: S-1-5-21-...-1112
Managed Password ID: AQAA...
```

Success is indicated by a populated list without LDAP errors.

## Related

- [[procedures/Forging-Golden-GMSA]]
- [[tools/GoldenGMSA]]
