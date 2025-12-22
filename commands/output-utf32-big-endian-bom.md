---
id: 8fbd1cc7-2548-49e1-8459-4622f5749a6c
name: output-utf32-big-endian-bom
type: command
executor: bash
data: printf '\x00\x00\xFE\xFF'
output: 0000FEFF
created_at: '2023-04-06T03:56:43.117663+00:00'
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

# output-utf32-big-endian-bom

## Command

```bash
printf '\x00\x00\xFE\xFF'
```

## Description

Outputs BOM for UTF-32 Big Endian to prefix 32-bit encoded XSS payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed bytes | Yes |

## Examples

### Basic Usage

```bash
printf '\x00\x00\xFE\xFF'
```

## Expected Output

Raw bytes: 00 00 FE FF.

## Related

- [[procedures/Bypassing-XSS-Filters-Using-UTF-BOM-Character]]
- [[commands/output-utf32-xss-payload]]
