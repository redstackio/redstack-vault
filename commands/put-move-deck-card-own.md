---
data: >-
  curl -X PUT 'https://nextcloud.example.com/apps/deck/cards/13' -H
  'Content-Type: application/json' -H 'OCS-APIRequest: true' -H 'Cookie:
  nc_username=attacker; nc_token=session_token' -d
  '{"title":"SOME_TEST","description":"","stackId":2,"type":"plain","lastModified":1588755341,"lastEditor":null,"createdAt":1588755341,"labels":null,"assignedUsers":null,"attachments":null,"attachmentCount":null,"owner":"attacker","order":999,"archived":false,"duedate":null,"deletedAt":0,"commentsUnread":0,"id":13,"overdue":0}'
tags:
  - api
  - nextcloud
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.806Z'
id: 6d8776f4-0ece-445e-8004-b3dff2077acb
verified: false
validated: true
submitted: true
---
# put-move-deck-card-own

## Command

```bash
curl -X PUT 'https://nextcloud.example.com/apps/deck/cards/13' \
  -H 'Content-Type: application/json' \
  -H 'OCS-APIRequest: true' \
  -H 'Cookie: nc_username=attacker; nc_token=session_token' \
  -d '{"title":"SOME_TEST","description":"","stackId":2,"type":"plain","lastModified":1588755341,"lastEditor":null,"createdAt":1588755341,"labels":null,"assignedUsers":null,"attachments":null,"attachmentCount":null,"owner":"attacker","order":999,"archived":false,"duedate":null,"deletedAt":0,"commentsUnread":0,"id":13,"overdue":0}'
```

## Description

Moves a Deck card to a stack within the user's own decks via API. Captures structure for interception.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Card ID (e.g., 13) | Yes |
| stackId | Target stack ID (e.g., 2) | Yes |
| lastModified | Unix timestamp | Yes |
| owner | Card owner username | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT 'https://nextcloud.example.com/apps/deck/cards/13' -H 'Content-Type: application/json' -H 'OCS-APIRequest: true' -H 'Cookie: nc_username=attacker; nc_token=session_token' -d '{"stackId":2,...}'
```

## Expected Output

200 OK with updated card JSON.

## Related

- [[commands/put-move-deck-card-target]]
