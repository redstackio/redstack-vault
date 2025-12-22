---
id: cmd-curl-profile-attacker-001
data: >-
  curl -X POST https://target.com/EditUserProfile/Save -H "Cookie:
  .AspNetCore.Antiforgery.w=...; TS014b77bb=..." -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "Email=attacker@gmail.com&PositionTitleIds=10&Title=Pentester&FirstName=attacking&MiddleName=test&LastName=wearehackerone&PhoneNumber=&LanguageId=&Password=&ConfirmPassword=&userId=123464&passChange=true&PersonProfileId=0&CitizenshipId=101&__RequestVerificationToken=CSRF_TOKEN_HERE"
tags:
  - web
  - post
  - profile
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.643Z'
verified: false
validated: true
submitted: true
---
# curl-profile-update-attacker

## Command

```bash
curl -X POST https://target.com/EditUserProfile/Save \
  -H "Cookie: .AspNetCore.Antiforgery.w=...; TS014b77bb=..." \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "Email=attacker@gmail.com&PositionTitleIds=10&Title=Pentester&FirstName=attacking&MiddleName=test&LastName=wearehackerone&PhoneNumber=&LanguageId=&Password=&ConfirmPassword=&userId=123464&passChange=true&PersonProfileId=0&CitizenshipId=101&__RequestVerificationToken=CSRF_TOKEN_HERE"
```

## Description

Sends a POST request to update the attacker's profile, useful for intercepting and analyzing the userId parameter in Burp Suite or via curl for scripting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Cookie: ..."` | Session and CSRF cookies | Yes |
| `-d "..."` | Form data including userId and email | Yes |
| `userId` | Attacker's ID (e.g., 123464) | Yes |
| `__RequestVerificationToken` | CSRF token from form | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/EditUserProfile/Save -H "Cookie: ..." -d "Email=attacker@gmail.com&userId=123464&__RequestVerificationToken=..."
```

### Advanced Usage

Include full parameters for complete update:

```bash
curl -X POST https://target.com/EditUserProfile/Save -H "Cookie: ..." -H "Referer: https://target.com/MyAccount/EditUserProfile" -d "Email=attacker@gmail.com&userId=123464&Title=Pentester&..."
```

## Expected Output

HTTP 200 OK with success message or redirect to profile page; profile updated if valid.

## Related

- [[Related Procedure: Intercept-and-Analyze-Profile-Update-Request]]
