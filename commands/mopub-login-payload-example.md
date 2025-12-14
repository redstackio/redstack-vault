---
data: '{"username":"TARGET@exmple.com","password":"HACKEDP@SS"}'
tags:
  - brute-force
  - login
type: command
executor: bash
platforms:
  - Web
id: b31f828e-2462-418a-ae3c-5a0bb97b0a94
created_at: '2025-12-14T17:30:26.724Z'
updated_at: '2025-12-14T17:30:26.724Z'
verified: false
validated: true
submitted: true
---
# mopub-login-payload-example

## Command

```bash
# Example payload for curl --data-binary
{"username":"TARGET@exmple.com","password":"HACKEDP@SS"}
```

## Description

This JSON payload demonstrates the body format for POST requests to the MoPub login endpoint to test authentication with a target username and guessed password.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| username | Target email address for login | Yes |
| password | Guessed or candidate password | Yes |

## Examples

### Basic Usage

```bash
curl ... --data-binary '{"username":"alert.wids@gmail.com","password":"test123"}'
```

### Advanced Usage

Incorporate into loops with variable passwords from a file.

## Expected Output

HTTP 204 on success (valid credentials); 400/401 on failure.

## Related

- [[commands/mopub-rate-limit-test-curl-loop]]
- [[procedures/Test-IP-Based-Rate-Limiting-on-MoPub-Login]]
