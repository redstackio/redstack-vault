---
id: cmd-curl-test-001
data: 'curl "https://lichess.org/game/export/[GAME_ID]?players=test" -v'
tags:
  - http
  - test
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.673Z'
verified: false
validated: true
submitted: true
---
# curl-endpoint-test

## Command

```bash
curl "https://lichess.org/game/export/[GAME_ID]?players=test" -v
```

## Description

This command tests Lichess API endpoints for acceptance of the 'players' parameter, helping identify SSRF vectors by checking if queries are processed without errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[GAME_ID]` | Valid game ID | Yes |
| `?players=test` | Test value for parameter | Yes |
| `-v` | Verbose mode | No |

## Examples

### Basic Usage

```bash
curl "https://lichess.org/api/games/user/magnuscarlsen?players=test" -v
```

### Advanced Usage

```bash
curl "https://lichess.org/api/games/export/_ids?players=test" -v
```

## Expected Output

Successful response (200 OK) with API data, indicating parameter is accepted and passed to backend.

## Related

- [[Related Procedure: Identify-Vulnerable-Lichess-API-Endpoints]]
