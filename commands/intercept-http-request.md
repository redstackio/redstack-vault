---
data: '# Use proxy tool to intercept'
tags:
  - web
  - interception
type: command
executor: bash
platforms:
  - Web
id: 138f535c-d46f-44fb-90f3-d03a7802006e
created_at: '2025-12-13T23:56:20.112Z'
updated_at: '2025-12-13T23:56:20.112Z'
verified: false
validated: true
submitted: true
---
# Intercept HTTP Request

## Command

```bash
# Use Burp Suite or similar to intercept POST requests
```

## Description

This command represents intercepting an HTTP request using a proxy tool to allow modification before forwarding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `request` | The HTTP request to intercept | Yes |

## Examples

### Basic Usage

```bash
# In Burp: Set proxy and intercept upload request
```

## Expected Output

Captured request ready for editing.

## Related

- [[tools/Burp-Suite]]
- [[procedures/Bypass-File-Upload-Restrictions]]
