---
id: cb235d74-a267-4c57-83a9-5b66c9601de2
name: guidtool-inspect-version1-guid
type: command
executor: bash
data: guidtool -i $_GUID
output: null
created_at: '2023-04-06T03:55:59.812940+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - discovery
  - guid
verified: true
validated: true
---

# guidtool-inspect-version1-guid

## Command

```bash
guidtool -i $_GUID
```

## Description

This command uses `guidtool` to inspect a version 1 GUID, extracting its timestamp, MAC address, node ID, and clock sequence for system fingerprinting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Flag to enable inspection mode | Yes |
| $_GUID | The version 1 GUID to analyze (e.g., 95f6e264-bb00-11ec-8833-00155d01ef00) | Yes |

## Examples

### Basic Usage

```bash
guidtool -i 95f6e264-bb00-11ec-8833-00155d01ef00
```

### Advanced Usage

Use with a GUID from target logs:

```bash
guidtool -i a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

## Expected Output

```
UUID version: 1
UUID time: 2022-04-13 08:06:13.202186
UUID timestamp: 138691299732021860
UUID node: 91754721024
UUID MAC address: 00:15:5d:01:ef:00
UUID clock sequence: 2099
```

The output confirms the GUID version and reveals system-specific details like the MAC address.

## Related

- [[procedures/Enumerate-GUID-UUID-for-System-Fingerprinting]]
- [[commands/guidtool-attack-version1-guid-with-timestamp-and-clock-sequence]]
