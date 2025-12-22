---
data: '# Use OAuth to sign'
tags:
  - oauth
  - signing
type: command
executor: bash
platforms:
  - Web
id: 3e63e96d-ec4d-4644-8219-f9bcaa551e10
created_at: '2025-12-13T23:56:20.093Z'
updated_at: '2025-12-13T23:56:20.093Z'
verified: false
validated: true
submitted: true
---
# Sign OAuth Request

## Command

```bash
# oauth-sign --token <token> --url <file-url>
```

## Description

Sign a request with OAuth token to make uploaded files accessible to others.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--token` | OAuth token | Yes |
| `--url` | File URL to sign | Yes |

## Examples

### Basic Usage

```bash
oauth-sign --token abc123 --url https://ton.twitter.com/file.test
```

## Expected Output

Signed URL for sharing.

## Related

- [[procedures/Inject-XSS-Payload-via-Modified-Upload]]
