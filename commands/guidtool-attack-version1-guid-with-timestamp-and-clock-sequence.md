---
id: a802ef77-7b02-4dba-a9dc-50bd4c7e1d2c
name: guidtool-attack-version1-guid-with-timestamp-and-clock-sequence
type: command
executor: bash
data: guidtool $_GUID -t '$_TIMESTAMP' -p $_CLOCK_SEQUENCE
output: null
created_at: '2023-04-06T03:55:59.813000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - discovery
  - guid
verified: true
validated: true
---

# guidtool-attack-version1-guid-with-timestamp-and-clock-sequence

## Command

```bash
guidtool $_GUID -t '$_TIMESTAMP' -p $_CLOCK_SEQUENCE
```

## Description

This command manipulates a version 1 GUID by applying a custom timestamp and clock sequence, useful for testing GUID validation or forging identifiers in attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_GUID | The target version 1 GUID to modify | Yes |
| -t | Flag to specify custom timestamp | Yes |
| '$_TIMESTAMP' | Timestamp in 'YYYY-MM-DD HH:MM:SS' format (e.g., '2021-11-17 18:03:17') | Yes |
| -p | Flag to specify clock sequence | Yes |
| $_CLOCK_SEQUENCE | Numeric clock sequence value (e.g., 10000) | Yes |

## Examples

### Basic Usage

```bash
guidtool 1b2d78d0-47cf-11ec-8d62-0ff591f2a37c -t '2021-11-17 18:03:17' -p 10000
```

### Advanced Usage

Test with a different sequence:

```bash
guidtool a1b2c3d4-e5f6-7890-abcd-ef1234567890 -t '2023-01-01 12:00:00' -p 5000
```

## Expected Output

The command generates a modified GUID based on the inputs, with no explicit output shown in samples, but success is a valid new GUID string without errors.

## Related

- [[procedures/Enumerate-GUID-UUID-for-System-Fingerprinting]]
- [[commands/guidtool-inspect-version1-guid]]
