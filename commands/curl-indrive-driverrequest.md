---
id: c1d2e3f4-g5h6-7891-cdef-5678901234
data: >-
  curl
  "https://terra-akamai.indriverapp.com/api/driverrequest?cid=5957&locale=en_US&job_id=338f72ff-f3c1-4da0-af15-5d1aa720146b&phone=██████████&token=████████&v=7&stream_id=1682279074257167&order_id=██████&client_id=█████████&shield_session_id=██████████&type=indriver&price=63&period=3&geo_arrival_time=1&distance=5&longitude=85.3249627&latitude=27.7390611&sn=1"
tags:
  - indrive
  - api-bid
type: command
output: null
executor: bash
platforms:
  - Web API
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.841Z'
verified: false
validated: true
submitted: true
---
# curl-indrive-driverrequest

## Command

```bash
curl "https://terra-akamai.indriverapp.com/api/driverrequest?cid=5957&locale=en_US&job_id=338f72ff-f3c1-4da0-af15-5d1aa720146b&phone=██████████&token=████████&v=7&stream_id=1682279074257167&order_id=██████&client_id=█████████&shield_session_id=██████████&type=indriver&price=63&period=3&geo_arrival_time=1&distance=5&longitude=85.3249627&latitude=27.7390611&sn=1"
```

## Description

Sends a driver bid request to the inDrive API to respond to a passenger ride order, generating tender_id and order_id. Use for initial bid submission or price inflation by modifying the price parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cid` | Client ID (5957) | Yes |
| `locale` | Language (en_US) | Yes |
| `job_id` | Passenger job UUID | Yes |
| `phone` | Driver phone (redacted) | Yes |
| `token` | Auth token (redacted) | Yes |
| `v` | API version (7) | Yes |
| `stream_id` | Session ID (timestamp) | Yes |
| `order_id` | Order ID (redacted) | Yes |
| `client_id` | Client session (redacted) | Yes |
| `shield_session_id` | Security session (redacted) | Yes |
| `type` | Type (indriver) | Yes |
| `price` | Bid price (modifiable for inflation) | Yes |
| `period` | Time period (3) | Yes |
| `geo_arrival_time` | Arrival factor (1) | Yes |
| `distance` | Distance (5) | Yes |
| `longitude` | Long (85.3249627) | Yes |
| `latitude` | Lat (27.7390611) | Yes |
| `sn` | Sequence (1) | Yes |

## Examples

### Basic Usage

```bash
curl "https://terra-akamai.indriverapp.com/api/driverrequest?...&price=63"
```

### Advanced Usage (Inflated Price)

```bash
curl "https://terra-akamai.indriverapp.com/api/driverrequest?...&price=1000"
```

## Expected Output

JSON with success status, tender_id, and order_id (e.g., {"status":"ok","tender_id":"abc123"}). Errors for invalid auth or params.

## Related

- [[commands/curl-indrive-settenderstatus]]
- [[procedures/Submit-inDrive-Driver-Request-for-Tender-ID]]
