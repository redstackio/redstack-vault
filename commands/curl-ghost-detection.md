---
id: cmd-uuid-1
data: >-
  curl -s
  "https://target.com/ghost/api/oembed/?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  | grep -i ghost
tags:
  - recon
  - fingerprinting
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.459Z'
verified: false
validated: true
submitted: true
---
# curl-ghost-detection

## Command

```bash
curl -s "https://target.com/ghost/api/oembed/?url=https://www.youtube.com/watch?v=dQw4w9WgXcQ" | grep -i ghost
```

## Description

This command probes a Ghost CMS oEmbed endpoint with a benign external URL to detect the platform via response content or errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, no progress meter | Yes |
| `url=` | External URL for oEmbed test | Yes |
| `grep -i ghost` | Filter for Ghost indicators | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://target.com/ghost/api/oembed/?url=https://example.com" | grep -i ghost
```

### Advanced Usage

```bash
curl -I https://target.com/ | grep -i "x-powered-by: ghost"
```

## Expected Output

JSON oEmbed response containing 'ghost' keywords or headers like 'X-Powered-By: Ghost' if the instance is detected.

## Related

- [[Related Procedure|procedures/Identify-Ghost-CMS-Instance]]
