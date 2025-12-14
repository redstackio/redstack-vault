---
id: cmd-binwalk-extract-001
data: binwalk -e firmware.bin
tags:
  - firmware
  - extraction
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.656Z'
verified: false
validated: true
submitted: true
---
# binwalk-extract

## Command

```bash
binwalk -e firmware.bin
```

## Description

This command scans a firmware binary for embedded files and extracts them to a directory, aiding in the analysis of packed configurations in devices like Miura EMV readers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Extract mode: automatically unpack identified files | Yes |
| `firmware.bin` | Input firmware file | Yes |

## Examples

### Basic Usage

```bash
binwalk -e firmware.bin
```

### Advanced Usage

```bash
binwalk --dd='.*' firmware.bin
```

## Expected Output

Creation of an _extracted directory with unpacked files, e.g., ./sqfs-root/wpa_supplicant.conf containing credentials.

## Related

- [[Related Procedure|procedures/Analyze-Embedded-Device-Firmware-for-Credentials]]
