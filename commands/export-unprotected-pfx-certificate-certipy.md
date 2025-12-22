---
id: 332af589-5e5f-411c-997e-4243c0483f89
name: export-unprotected-pfx-certificate-certipy
type: command
executor: python
data: >-
  certipy cert -export -pfx $_PFX_PATH -password $_PFX_PASSWORD -out
  $_OUTPUT_PFX
output: null
created_at: '2023-04-06T03:56:06.176894+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - adcs
  - export
verified: true
validated: true
---

# export-unprotected-pfx-certificate-certipy

## Command

```python
certipy cert -export -pfx $_PFX_PATH -password $_PFX_PASSWORD -out $_OUTPUT_PFX
```

## Description

Exports a PFX certificate without password protection using Certipy, facilitating its use in PKINIT tools by removing encryption on the private key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -pfx | Input PFX file path | Yes |
| -password | Password for the input PFX | Yes |
| -out | Output file path for unprotected PFX | Yes |
| -export | Export mode flag | Yes |

## Examples

### Basic Usage

```python
certipy cert -export -pfx protected.pfx -password Pass123 -out unprotected.pfx
```

## Expected Output

Exported certificate to unprotected.pfx
Private key exported without password.

No errors in ASN.1 parsing.

## Related

- [[procedures/Pass-The-Certificate-Attack]]
