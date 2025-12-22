---
id: 20aaaf83-5964-4d1b-8c88-ff9b8fa8a6d0
name: output-utf16-big-endian-bom
type: command
executor: bash
data: printf '\xFE\xFF'
output: FEFF
created_at: '2023-04-06T03:56:43.117491+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - xss
  - bypass
  - unicode
verified: true
validated: true
---

# output-utf16-big-endian-bom

## Command

```bash
printf '\xFE\xFF'
```

## Description

This command outputs the Byte Order Mark (BOM) bytes for UTF-16 Big Endian encoding. Use this as a prefix for XSS payloads to potentially bypass filters that do not handle Unicode BOM correctly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; outputs fixed bytes | Yes |

## Examples

### Basic Usage

```bash
printf '\xFE\xFF'
```

Outputs raw bytes equivalent to hex FE FF.

### Piping to File

```bash
printf '\xFE\xFF' > bom_prefix.bin
```

## Expected Output

Raw binary output: the two bytes FE FF (displays as garbled or hex in terminals).

## Related

- [[procedures/Bypassing-XSS-Filters-Using-UTF-BOM-Character]]
- [[commands/output-utf16-xss-payload]]
