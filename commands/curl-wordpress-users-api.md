---
data: 'curl https://target.com/wp-json/wp/v2/users/'
tags:
  - reconnaissance
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 2e5aacf4-0539-4002-8017-636bb1c37347
created_at: '2025-12-14T17:25:18.103Z'
updated_at: '2025-12-14T17:25:18.103Z'
verified: false
validated: true
submitted: true
---
# curl-wordpress-users-api

## Command

```bash
curl https://target.com/wp-json/wp/v2/users/
```

## Description

This command uses curl to perform a GET request against the WordPress REST API users endpoint, retrieving a JSON list of all site users without authentication. It is ideal for quick reconnaissance on misconfigured WordPress sites to enumerate accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://target.com/wp-json/wp/v2/users/` | The target URL for the REST API endpoint; replace target.com with the actual domain | Yes |
| `-s` (silent) | Suppress progress meter; optional for cleaner output | No |
| `-o output.json` | Save response to file | No |

## Examples

### Basic Usage

```bash
curl https://nordvpn.com/wp-json/wp/v2/users/
```

### Advanced Usage

```bash
curl -s https://nordvpn.com/?rest_route=/wp/v2/users/ | jq '.'
```

### With Pagination Handling

```bash
curl https://target.com/wp-json/wp/v2/users/?page=1 | jq '."
```

## Expected Output

A JSON array of user objects, such as:

[
  {
    "id": 1,
    "name": "Admin User",
    "slug": "admin",
    "description": "Site administrator",
    "avatar_urls": {
      "24": "https://secure.gravatar.com/avatar/..."
    }
  }
]

If successful, no errors; empty array or 403 indicates protection.

## Related

- [[Related Procedure: Enumerate-WordPress-Users-via-REST-API]]
