---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: 'curl -s https://owncloud.com/wp-json/wp/v2/users/'
tags:
  - recon
  - http
  - wordpress
type: command
output: >-
  A JSON array of user objects, e.g.,
  [{"id":1,"name":"admin","slug":"admin"},...]
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:11.083Z'
verified: false
validated: true
submitted: true
---
# curl-get-users

## Command

```bash
curl -s https://owncloud.com/wp-json/wp/v2/users/
```

## Description

This command uses curl to perform a silent GET request to the WordPress REST API users endpoint, enumerating all users who have published posts without authentication. Use it for initial reconnaissance on vulnerable WordPress sites.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode (suppress progress meter) | Yes |
| `https://owncloud.com/wp-json/wp/v2/users/` | Target API endpoint (replace with site URL) | Yes |

## Examples

### Basic Usage

```bash
curl -s https://example.com/wp-json/wp/v2/users/
```

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" https://owncloud.com/wp-json/wp/v2/users/ | jq '.[].name'
```

## Expected Output

JSON array of users: [{"id":1,"name":"admin","url":"","description":"","link":"https://owncloud.com/author/admin/","slug":"admin","avatar_urls":{"24":"https://...","48":"https://...","96":"https://..."},"meta":[],"_links":{"self":[{"href":"https://..."}],"collection":[{"href":"https://..."}]}}]

## Related

- [[commands/curl-get-user-id]]
- [[procedures/Enumerate-Users-via-WordPress-REST-API]]
