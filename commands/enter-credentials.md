---
id: b214727f-540a-44f5-aff0-422121180ccb
name: enter-credentials
type: command
executor: bash
data: >-
  curl -X POST "$_TARGET_URL/login" -d "username=$_USERNAME&password=$_PASSWORD"
  -v
output: null
created_at: '2023-04-06T03:56:31.692733+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - phishing
  - web
verified: true
validated: true
---

# enter-credentials

## Command

```bash
curl -X POST "$_TARGET_URL/login" -d "username=$_USERNAME&password=$_PASSWORD" -v
```

## Description

Simulates entering credentials on a login endpoint, useful for testing post-redirect authentication in phishing scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Login endpoint | Yes |
| $_USERNAME | Test username | Yes |
| $_PASSWORD | Test password | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://famous-website.tld/login" -d "username=test&password=test123" -v
```

## Expected Output

HTTP/1.1 200 OK with session cookie or redirect to dashboard.

## Related

- [[procedures/Open-URL-Redirection-Exploitation]]
- [[commands/submit-signup-form]]
