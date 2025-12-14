---
id: cmd-create-png-001
data: >-
  echo -e
  '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x16\x1d\xb3\x00\x00\x00\x00IEND\xaeB`\x82'>
  test.png
tags:
  - file-generation
  - png
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.573Z'
verified: false
validated: true
submitted: true
---
# create-minimal-png

## Command

```bash
echo -e '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x16\x1d\xb3\x00\x00\x00\x00IEND\xaeB`\x82'> test.png
```

## Description

Generates a minimal 1x1 pixel PNG file using echo to output binary PNG structure, useful for testing file uploads without external tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Enables backslash escape interpretation for hex bytes | Yes |
| `> test.png` | Redirects output to the file test.png | Yes |

## Examples

### Basic Usage

```bash
echo -e '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x16\x1d\xb3\x00\x00\x00\x00IEND\xaeB`\x82'> test.png
```

### Advanced Usage

To create a different filename, change the redirect: `... > myimage.png`

## Expected Output

A valid 1x1 PNG file (test.png) of approximately 50 bytes. Command produces no stdout; verify with `file test.png` showing "PNG image data".

## Related

- [[Related Procedure|procedures/Create-Minimal-Test-PNG-Image]]
