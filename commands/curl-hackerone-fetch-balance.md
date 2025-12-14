---
data: >-
  curl "https://api.hackerone.com/v1/hackers/payments/balance" -X GET -u
  "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
tags:
  - api
  - hackerone
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.470Z'
id: 04f8a505-c6a5-4d04-9191-56eeadfb4c61
verified: false
validated: true
submitted: true
---
# curl-hackerone-fetch-balance

## Command

```bash
curl "https://api.hackerone.com/v1/hackers/payments/balance" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

## Description

Fetches the current payment balance for the authenticated HackerOne user using a persistent token from a banned account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Basic auth with username:token | Yes |
| URL | Balance endpoint | Yes |
| `-H 'Accept: application/json'` | JSON format | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.hackerone.com/v1/hackers/payments/balance" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

### Advanced Usage

With output to file: ```bash
curl "https://api.hackerone.com/v1/hackers/payments/balance" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json' > balance.json
```

## Expected Output

JSON object with balance amount and currency.

## Related

- [[commands/curl-hackerone-fetch-reports]]
- [[procedures/Exploit-HackerOne-API-with-Old-Token]]
