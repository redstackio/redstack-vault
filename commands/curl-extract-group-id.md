---
data: >-
  curl -X GET 'https://example.line.endpoint/account/info' -H 'User-Agent:
  Mozilla/5.0'
tags:
  - web
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: b0344351-33d8-4544-9ec8-0d240e9ae5b7
created_at: '2025-12-11T06:10:22.395Z'
updated_at: '2025-12-11T06:10:22.395Z'
verified: false
validated: true
submitted: true
---
# curl-extract-group-id

## Command

```bash
curl -X GET 'https://example.line.endpoint/account/info' -H 'User-Agent: Mozilla/5.0'
```

## Description

This command uses curl to query LINE endpoints and extract group IDs from responses, useful for IDOR setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies GET method | Yes |
| `URL` | Target endpoint | Yes |
| `-H 'User-Agent'` | Mimics browser | No |

## Examples

### Basic Usage

```bash
curl -X GET 'https://example.line.endpoint/account/info' -H 'User-Agent: Mozilla/5.0'
```

### Advanced Usage

```bash
curl -X GET 'https://example.line.endpoint/account/info' -H 'User-Agent: Mozilla/5.0' -o output.json
```

## Expected Output

JSON response containing group IDs, e.g., {"group_id": "abc123"}

## Related

- [[commands/curl-craft-admin-request]]
- [[procedures/Discover-and-Extract-Group-IDs-from-LINE-Accounts]]
