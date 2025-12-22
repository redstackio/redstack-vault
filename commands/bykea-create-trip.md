---
data: "curl -X POST \"https://api.bykea.net/api/v1/trips/create\" -H \"User-Agent: BYKEA/1.0.169 (com.bykea.pk; build:21; iOS 15.8.0) Alamofire/1.0.169\" -H \"X-App-Version:1.0.169\" -d '{\"advertisement_id\":\"REDACTED\",\"token_id\":\"{{access_token}}\",\"pickup_info\":{\"lng\":67.883339799999931,\"lat\":29.5500097,\"address\":\"Ø³Ø¨Û\x8C, ØªØØµÛ\x8CÙ\x84 Ø³Ø¨Û\x8C, Ø¶Ù\x84Ø¹ Ø³Ø¨Û\x8C, Ø³Ø¨Û\x98 Ú\x88Ù\x88Û\x8CÚ\x98Ù\x86, Ø¨Ù\x84Ù\x88Ú\x86Ø³ØªØ§Ù\x86, 82000, Ù¾Ø§Ú©Ø³ØªØ§Ù\x86\"},\"trip\":{\"creator\":\"iOS\",\"service_code\":23,\"lng\":67.883339799999931,\"lat\":29.5500097,\"customer_bid\":75},\"dropoff_info\":{\"address\":\"Kurak, ØªØØµÛ\x8CÙ\x84 Ø³Ø¨Û\x8C, Ø¶Ù\x84Ø¹ Ø³Ø¨Û\x98, Ø³Ø¨Û\x98 Ú\x88Ù\x88Û\x98Ú\x98Ù\x86, Ø¨Ù\x84Ù\x88Ú\x86Ø³ØªØ§Ù\x86, Ù¾Ø§Ú©Ø³ØªØ§Ù\x86\",\"lat\":29.573396420702664,\"lng\":67.898040153086185},\"_id\":\"{{user_id}}\"}'"
tags:
  - api
  - create
type: command
output: >-
  {"code":200,"success":true,"message":"Trip creation
  successful","data":{"trip_id":"███████","trip_no":"PKX████████","passenger_id":"██████████","dt":"2024-02-15T13:49:44.841Z","link":"https://track.bykea.net/PKX██████","nc":true}}
executor: bash
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.823Z'
id: 51a39daa-743f-4dc9-8aa0-1ea75ea6e6d1
verified: false
validated: true
submitted: true
---
# bykea-create-trip

## Command

```bash
curl -X POST "https://api.bykea.net/api/v1/trips/create" \
  -H "User-Agent: BYKEA/1.0.169 (com.bykea.pk; build:21; iOS 15.8.0) Alamofire/1.0.169" \
  -H "X-App-Version:1.0.169" \
  -d '{"advertisement_id":"REDACTED","token_id":"{{access_token}}","pickup_info":{"lng":67.883339799999931,"lat":29.5500097,"address":"Ø³Ø¨Û, ØªØØµÛÙ Ø³Ø¨Û, Ø¶ÙØ¹ Ø³Ø¨Û, Ø³Ø¨Û ÚÙÛÚÙ, Ø¨ÙÙÚØ³ØªØ§Ù, 82000, Ù¾Ø§Ú©Ø³ØªØ§Ù"},"trip":{"creator":"iOS","service_code":23,"lng":67.883339799999931,"lat":29.5500097,"customer_bid":75},"dropoff_info":{"address":"Kurak, ØªØØµÛÙ Ø³Ø¨Û, Ø¶ÙØ¹ Ø³Ø¨Û, Ø³Ø¨Û ÚÙÛÚÙ, Ø¨ÙÙÚØ³ØªØ§Ù, Ù¾Ø§Ú©Ø³ØªØ§Ù","lat":29.573396420702664,"lng":67.898040153086185},"_id":"{{user_id}}"}'
```

## Description

Creates a new trip/booking in Bykea API as an authenticated user, generating IDs for later IDOR exploitation. Used in victim setup phase.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| token_id | User's access token for auth | Yes |
| _id | User's ID | Yes |
| customer_bid | Bid amount (e.g., 75) | Yes |
| service_code | Service type (23 for specific ride) | Yes |
| pickup_info | JSON with lat, lng, address | Yes |
| dropoff_info | JSON with lat, lng, address | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://api.bykea.net/api/v1/trips/create" -H "..." -d '{...}'
```

### Advanced Usage

Replace placeholders with actual values; adjust addresses for different locations.

## Expected Output

{"code":200,"success":true,"message":"Trip creation successful","data":{"trip_id":"███████","trip_no":"PKX████████","passenger_id":"██████████","dt":"2024-02-15T13:49:44.841Z","link":"https://track.bykea.net/PKX██████","nc":true}}

## Related

- [[procedures/Create-Victim-Booking]]
