---
id: cmd-strings-search-001
data: strings firmware.bin | grep -i 'wpa_supplicant\|root\|password'
tags:
  - reverse-engineering
  - firmware
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.660Z'
verified: false
validated: true
submitted: true
---
# strings-search

## Command

```bash
strings firmware.bin | grep -i 'wpa_supplicant\|root\|password'
```

## Description

This command extracts printable strings from a binary firmware file and filters for keywords related to WiFi configs and credentials, useful for quickly spotting hardcoded passwords in embedded device firmware.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `firmware.bin` | Path to the firmware binary file | Yes |
| `-i` | Case-insensitive grep matching | No |
| `'wpa_supplicant\|root\|password'` | Regex pattern for relevant strings | Yes |

## Examples

### Basic Usage

```bash
strings firmware.bin | grep -i password
```

### Advanced Usage

```bash
strings -n 8 firmware.bin | grep -i 'root\|pass' > creds.txt
```

## Expected Output

Lines of text from the binary, such as:

wpa_supplicant.conf:root_pass=miura123

## Related

- [[Related Procedure|procedures/Analyze-Embedded-Device-Firmware-for-Credentials]]
