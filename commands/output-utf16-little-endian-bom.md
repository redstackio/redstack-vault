---
id: 7b024ac1-d04f-4055-aab2-61e544c6e51c
name: output-utf16-little-endian-bom
type: command
executor: bash
data: printf '\xFF\xFE'
output: FFFE
created_at: '2023-04-06T03:56:43.117520+00:00'
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

# output-utf16-little-endian-bom

## Command

```bash
printf '\xFF\xFE'
```

## Description

Outputs the BOM bytes for UTF-16 Little Endian. Prepend to UTF-16 encoded XSS payloads for filter bypass testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed output | Yes |

## Examples

### Basic Usage

```bash
printf '\xFF\xFE'
```

## Expected Output

Raw bytes: FF FE.

## Related

- [[procedures/Bypassing-XSS-Filters-Using-UTF-BOM-Character]]
- [[commands/output-utf16-xss-payload]]
