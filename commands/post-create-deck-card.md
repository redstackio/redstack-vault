---
data: >-
  curl -X POST 'https://nextcloud.example.com/apps/deck/cards' -H 'Content-Type:
  application/json' -H 'OCS-APIRequest: true' -H 'Cookie: nc_username=attacker;
  nc_token=session_token' -d '{"title":"SOME_TEST","stackId":1,"type":"plain"}'
tags:
  - api
  - nextcloud
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.809Z'
id: 812c6d7e-35cd-4fb6-97ad-d4d777c49c09
verified: false
validated: true
submitted: true
---
# post-create-deck-card

## Command

```bash
curl -X POST 'https://nextcloud.example.com/apps/deck/cards' \
  -H 'Content-Type: application/json' \
  -H 'OCS-APIRequest: true' \
  -H 'Cookie: nc_username=attacker; nc_token=session_token' \
  -d '{"title":"SOME_TEST","stackId":1,"type":"plain"}'
```

## Description

Creates a new plain card in Nextcloud Deck's specified stack using the API. Used to initialize a task for manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| title | Card title (e.g., SOME_TEST) | Yes |
| stackId | Destination stack ID (e.g., 1) | Yes |
| type | Card type (plain) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://nextcloud.example.com/apps/deck/cards' -H 'Content-Type: application/json' -H 'OCS-APIRequest: true' -H 'Cookie: nc_username=attacker; nc_token=session_token' -d '{"title":"Test Card","stackId":1,"type":"plain"}'
```

### Advanced Usage

Add more fields if needed, but minimal for exploitation.

## Expected Output

JSON response like {"ocs":{"meta":{"status":"ok","statuscode":200,...},"data":{"id":13,"title":"SOME_TEST",...}}}

## Related

- [[commands/put-move-deck-card-own]]
