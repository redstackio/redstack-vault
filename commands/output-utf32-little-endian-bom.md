---
id: 5d0a14ac-6c7f-47e0-a4a9-fccea320c574
name: output-utf32-little-endian-bom
type: command
executor: bash
data: printf '\xFF\xFE\x00\x00'
output: FFFE0000
created_at: '2023-04-06T03:56:43.117686+00:00'
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

# output-utf32-little-endian-bom

## Command

```bash
printf '\xFF\xFE\x00\x00'
```

## Description

Outputs UTF-32 Little Endian BOM for payload prefixing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | Yes |

## Examples

### Basic Usage

```bash
printf '\xFF\xFE\x00\x00'
```

## Expected Output

Bytes: FF FE 00 00.

## Related

- [[procedures/Bypassing-XSS-Filters-Using-UTF-BOM-Character]]
- [[commands/output-utf32-xss-payload]]
