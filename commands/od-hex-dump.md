---
id: cmd-od-hex-dump
data: od -tx1 ./test000
tags:
  - file-analysis
  - hex-dump
type: command
output: 20000000 30 ff ff ff ff ff ff ff ff ff ff ff ff 30000015
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.414Z'
verified: false
validated: true
submitted: true
---
# od-hex-dump

## Command

```bash
od -tx1 ./test000
```

## Description

Dumps the contents of a binary file in hexadecimal format, one byte per line, useful for inspecting malicious LZMA files to identify crafted headers causing memory issues in libxml2.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-tx1` | Hexadecimal output, one byte per line | Yes |
| `./test000` | Path to the input file | Yes |

## Examples

### Basic Usage

```bash
od -tx1 ./test000
```

### Advanced Usage

```bash
od -tx1 -A x ./test000 | head -20
```

## Expected Output

Hex dump like "20000000 30 ff ff ff ff ff ff ff ff ff ff ff ff 30000015", revealing LZMA header manipulations such as large dictionary sizes.

## Related

- [[Related Procedure|procedures/Inspect-Malicious-LZMA-File]]
