---
id: e13bbed2-4d21-4adc-9303-9eebc98188c4
name: golden-gmsa-query-specific-gmsa
type: command
executor: bash
data: GoldenGMSA.exe gmsainfo --sid $_GMSA_SID
output: null
created_at: '2023-04-06T03:56:04.615368+00:00'
updated_at: '2023-04-10T20:25:56.697280+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - enumeration
verified: true
validated: true
---

# golden-gmsa-query-specific-gmsa

## Command

```bash
GoldenGMSA.exe gmsainfo --sid $_GMSA_SID
```

## Description

Queries details for a specific GMSA using its Security Identifier (SID). This is useful for targeted reconnaissance before password computation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --sid | SID of the target GMSA (e.g., S-1-5-21-1437000690-1664695696-1586295871-1112) | Yes |
| gmsainfo | Subcommand for GMSA info | Yes |

## Examples

### Basic Usage

```bash
GoldenGMSA.exe gmsainfo --sid S-1-5-21-1437000690-1664695696-1586295871-1112
```

## Expected Output

Details for the specified GMSA:
```
GMSA Name: target-gmsa
SID: S-1-5-21-...
Attributes: ...
```

## Related

- [[procedures/Forging-Golden-GMSA]]
- [[tools/GoldenGMSA]]
