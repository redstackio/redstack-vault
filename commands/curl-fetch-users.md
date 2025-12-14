---
data: 'curl -s https://sifchain.finance/wp-json/wp/v2/users/'
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.837Z'
id: ba79c524-2fe3-42c5-8c29-ba2735c38404
verified: false
validated: true
submitted: true
---
# curl-fetch-users

## Command

```bash
curl -s https://sifchain.finance/wp-json/wp/v2/users/
```

## Description

This command uses curl to fetch the WordPress REST API users endpoint, retrieving a JSON list of all users without authentication. It is used in reconnaissance to enumerate accounts on vulnerable WordPress sites.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | No |
| URL | The target endpoint, e.g., https://target.com/wp-json/wp/v2/users/ | Yes |

## Examples

### Basic Usage

```bash
curl https://sifchain.finance/wp-json/wp/v2/users/
```

### Advanced Usage

```bash
curl -s https://sifchain.finance/wp-json/wp/v2/users/ | jq '.[].slug'
```

## Expected Output

A JSON array of user objects, such as:

```json
[
  {"id":1,"name":"Admin","slug":"admin","description":"","link":"https://sifchain.finance/author/admin/"},
  {"id":2,"name":"Employee","slug":"employee1","description":"Sifchain staff","link":"https://sifchain.finance/author/employee1/"}
]
```

Success is indicated by the presence of user data; failure returns an empty array or error if protected.

## Related

- [[Related Procedure: Enumerate-WordPress-Users-via-REST-API]]
