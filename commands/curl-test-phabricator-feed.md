---
id: cmd-uuid-1
data: >-
  curl -X POST 'https://phabricator.example.com/api/feed.publish' -H
  'Content-Type: application/x-www-form-urlencoded' -d
  'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-self","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-self"}'
tags:
  - api-test
  - phabricator
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.065Z'
verified: false
validated: true
submitted: true
---
# curl-test-phabricator-feed

## Command

```bash
curl -X POST 'https://phabricator.example.com/api/feed.publish' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-self","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-self"}'
```

## Description

Tests the Phabricator feed.publish API with a basic legitimate payload to verify endpoint functionality and parameter acceptance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for API call | Yes |
| `-H 'Content-Type: ...'` | Sets form-encoded content | Yes |
| `-d '...'` | Payload with token, type, and data | Yes |
| `token` | Conduit API token | Yes |
| `type` | Story type (PhabricatorTokenGivenFeedStory) | Yes |
| `data` | JSON with PHIDs | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://phabricator.example.com/api/feed.publish' -H 'Content-Type: application/x-www-form-urlencoded' -d 'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-self","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-self"}'
```

### Advanced Usage

```bash
curl -X POST 'https://phabricator.example.com/api/feed.publish' -H 'Content-Type: application/x-www-form-urlencoded' -d 'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"invalid","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"invalid"}'
```

## Expected Output

JSON response like {"result":{"story":{"id":"123","phid":"PHID-..."}}} on success, or error details on failure.

## Related

- [[Related Procedure]]
