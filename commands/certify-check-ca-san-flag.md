---
type: command
executor: powershell
data: Certify.exe cas
tags:
  - adcs
  - enumeration
platforms:
  - Windows
verified: true
validated: true
---

# certify-check-ca-san-flag

## Command

```powershell
Certify.exe cas
```

## Description

This command uses Certify.exe to enumerate accessible Certificate Authorities in the domain and check their configuration flags, specifically identifying if the EDITF_ATTRIBUTESUBJECTALTNAME2 (UserSpecifiedSAN) flag is enabled. It is used to assess AD CS misconfigurations that allow arbitrary SAN requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| cas | Enumerates Certificate Authorities and their settings | Yes (built-in flag) |

## Examples

### Basic Usage

```powershell
Certify.exe cas
```

### Advanced Usage

Run from a domain-joined machine with user credentials:
```powershell
Certify.exe cas /quiet
```

## Expected Output

```
[*] Action: Enumerating Certificate Authorities

Certificate Authorities:

CA Name: domain-DC-CA
DNS Hostname: dc.domain.local
Forest: domain.local
Config String: dc.domain.local\domain-DC-CA
...
EDITF_ATTRIBUTESUBJECTALTNAME2: Enabled  <-- Key indicator
```

## Related

- [[procedures/Request-Alternative-Name-Certificate-via-AD-CS]]
- [[tools/Certify]]
