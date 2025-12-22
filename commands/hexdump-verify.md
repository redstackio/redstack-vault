---
id: cmd-uuid-003
name: hexdump-verify
type: command
executor: bash
data: hexdump -C xss.zip | head -5
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.813Z'
platforms:
  - Linux
tags:
  - verify
  - hex
verified: false
validated: true
submitted: true
---

# hexdump-verify

## Command

```bash
hexdump -C xss.zip | head -5
```

## Description

Dumps the first 5 lines of hex and ASCII for a binary file to verify structure like ZIP header and HTML payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -C | Canonical hex+ASCII format | Yes |
| xss.zip | Input file | Yes |
| | head -5 | Limit lines | No |

## Examples

### Basic Usage

```bash
hexdump -C file.bin
```

### Advanced Usage

Full dump: ```bash
hexdump -C xss.zip > dump.txt
```

## Expected Output

00000000  50 4b 03 04 14 00 06 00  08 08 00 00 00 21 00 00  |PK............!|
... showing PK and <html>.

## Related

- [[commands/create-malicious-zip-html]]
