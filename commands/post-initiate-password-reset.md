---
data: >-
  curl -X POST https://helpdesk.bistudio.com/api/system/verification-codes -H
  "Content-Type: application/json" -d '{"username":"admin"}'
tags:
  - api
  - password-reset
type: command
executor: bash
platforms:
  - Web
id: 7e23a55f-8c07-4186-acf1-5507c50de8a2
created_at: '2025-12-14T17:33:12.390Z'
updated_at: '2025-12-14T17:33:12.390Z'
verified: false
validated: true
submitted: true
---
# post-initiate-password-reset

## Command

```bash
curl -X POST https://helpdesk.bistudio.com/api/system/verification-codes -H "Content-Type: application/json" -d '{"username":"admin"}'
```

## Description

Initiates the password reset by requesting an SMS token for the specified username on the Bistudio helpdesk API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `username` | Target staff username (e.g., 'admin') | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://helpdesk.bistudio.com/api/system/verification-codes -H "Content-Type: application/json" -d '{"username":"admin"}'
```

### Advanced Usage

```bash
curl -X POST https://helpdesk.bistudio.com/api/system/verification-codes -H "Content-Type: application/json" -H "X-XSRF-TOKEN: tokenvalue" -d '{"username":"admin"}'
```

## Expected Output

JSON response indicating success or error; SMS token sent to phone if valid username.

## Related

- [[Related Procedure]]
