---
data: >-
  curl "https://api.hackerone.com/v1/hackers/payments/payouts" -X GET -u
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
updated_at: '2025-12-14T17:32:48.454Z'
id: 289a9aa4-43b1-4ed7-8ebf-0bc9f64788ae
verified: false
validated: true
submitted: true
---
# curl-hackerone-fetch-payouts

## Command

```bash
curl "https://api.hackerone.com/v1/hackers/payments/payouts" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

## Description

Fetches payout history for the banned account using unrevoked token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Auth credentials | Yes |
| URL | Payouts endpoint | Yes |
| `-H` | JSON header | Yes |

## Examples

### Basic Usage

```bash
curl "https://api.hackerone.com/v1/hackers/payments/payouts" -X GET -u "mrtst:XXXXXXXXXXXXXXXXXXXX=" -H 'Accept: application/json'
```

## Expected Output

JSON array of payouts with transaction details.

## Related

- [[commands/curl-hackerone-fetch-earnings]]
- [[procedures/Exploit-HackerOne-API-with-Old-Token]]
