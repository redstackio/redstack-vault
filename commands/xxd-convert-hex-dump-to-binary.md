---
id: 72d514b3-35d8-4732-ab46-b9105b060e12
name: xxd-convert-hex-dump-to-binary
type: command
executor: bash
data: xxd -ps -r $_INPUT > $_OUTPUT
output: xxd -ps -r dump > dump.decoded
created_at: '2019-11-25T19:19:33.877757+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - convert
  - hex
verified: true
validated: true
---

# xxd-convert-hex-dump-to-binary

## Command

```bash
xxd -ps -r $_INPUT > $_OUTPUT
```

## Description

Converts a plain hex dump file back to binary format using xxd's reverse mode. This is useful for decoding hex-encoded data, such as payloads or keys extracted during security assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT | Input file containing plain-style hex data | Yes |
| $_OUTPUT | Output file for the resulting binary data | Yes |
| -ps | Specifies plain style (continuous hex digits without offsets) for input | Built-in |
| -r | Reverse operation: converts hex dump back to binary | Built-in |

## Examples

### Basic Usage

```bash
xxd -ps -r hexdump.txt > binary.key
```

### Advanced Usage

```bash
xxd -ps -r hexdump.txt | openssl rsa -in - -check
```

## Expected Output

The command produces a binary file at $_OUTPUT with no stdout output unless an error occurs. Verify success by checking the file size and contents match the expected binary format.

## Related

- [[tools/xxd]]
