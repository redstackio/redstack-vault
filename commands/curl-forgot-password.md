---
id: c3f4g5h6-i7j8-9013-efgh-789012345678
data: >-
  curl -X POST https://target/api/v1/forgotPassword -H "Content-Type:
  application/json" -d '{"email": "$TARGET_EMAIL"}'
tags:
  - api
  - reset-trigger
type: command
output: Success message for email sent.
executor: bash
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:33:24.536Z'
verified: false
validated: true
submitted: true
---
# curl-forgot-password

## Command

```bash
curl -X POST https://target/api/v1/forgotPassword -H "Content-Type: application/json" -d '{"email": "$TARGET_EMAIL"}'
```

## Description

Triggers a password reset email in Rocket.Chat anonymously.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d '{"email": "$TARGET_EMAIL"}'` | Target email | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target/api/v1/forgotPassword -H "Content-Type: application/json" -d '{"email": "target@example.com"}'
```

## Expected Output

JSON: {"success": true, "message": "Email sent"}

## Related

- [[commands/curl-reset-password]]
