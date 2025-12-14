---
id: 123e4567-e89b-12d3-a456-426614174002
name: twitter-dm-show-retrieve
type: command
executor: bash
data: >-
  curl -X GET "https://api.twitter.com/1.1/direct_messages/show.json?id=[DM-ID]"
  -H "Authorization: Bearer YOUR_API_TOKEN"
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.693Z'
platforms:
  - Web
  - API
tags:
  - api
  - twitter
  - retrieval
verified: false
validated: true
submitted: true
---

# twitter-dm-show-retrieve

## Command

```bash
curl -X GET "https://api.twitter.com/1.1/direct_messages/show.json?id=[DM-ID]" -H "Authorization: Bearer YOUR_API_TOKEN"
```

## Description

This command retrieves a specific direct message from Twitter's API v1.1 using its unique ID, useful for verifying access in IDOR testing. Requires OAuth authentication with DM read permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `id` | Unique DM identifier (e.g., 578631102144741376) | Yes |
| `Authorization` | Bearer token for API auth | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.twitter.com/1.1/direct_messages/show.json?id=578631102144741376" -H "Authorization: Bearer YOUR_TOKEN"
```

### Advanced Usage

```bash
curl -X GET "https://api.twitter.com/1.1/direct_messages/show.json?id=578631102144741376&include_entities=true" -H "Authorization: Bearer YOUR_TOKEN"
```

## Expected Output

JSON object with DM details: {"id": "578631102144741376", "sender_id": "...", "text": "Message content", ...}. In vuln case, returns even deleted content.

## Related

- [[commands/twitter-dm-show-retrieve-deleted]]
- [[procedures/Exploit-IDOR-in-Twitter-DM-API]]
