---
data: >-
  curl -X POST https://target-site.com/forgot-password -d
  "userName=victim_username" -s
tags:
  - reset
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.452Z'
id: 7237c646-6290-429a-9bba-51999294811a
verified: false
validated: true
submitted: true
---
# curl-password-reset

## Command

```bash
curl -X POST https://target-site.com/forgot-password \
  -d "userName=victim_username" \
  -s
```

## Description

Triggers password reset for victim, sending link to recovery email.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d "userName=..."` | Victim username | Yes |

## Examples

### Basic Usage

As above.

## Expected Output

Server acknowledgment; check email for link.

## Related

- [[Related Procedure: Request-Password-Reset-Using-Added-Recovery-Email]]
