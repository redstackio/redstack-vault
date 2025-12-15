---
data: >-
  Link Google account via https://www.yelp.com/profile_sharing, intercept POST
  to /google_connect/register in Burp Suite to capture id_token
tags:
  - oauth
  - token
type: command
output: >-
  id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjYwODNkZDU5ODE2NzNmNjYxZmRlOWRhZTY0NmI2ZjAzODBhMDE0NWMiLCJ0eXAiOiJKV1QifQ...
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.333Z'
id: 51f4b78a-ab65-4d15-94b8-809a24351635
verified: false
validated: true
submitted: true
---
# Generate ID Token

## Command

Link Google via profile_sharing and intercept in Burp.

```http
POST /google_connect/register
id_token=eyJhbGciOiJSUzI1NiIs...&csrftok=...
```

## Description

Generates a Google id_token by completing OAuth flow on attacker's account; capture for use in ATO payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /profile_sharing | Endpoint to initiate linking | Yes |

## Examples

### Basic Usage

Browse to /profile_sharing, authorize Google, intercept POST.

## Expected Output

JWT id_token in POST body.

## Related

- [[commands/deploy-ato-payload]]
- [[procedures/Perform-Account-Takeover-via-Google-Linking]]
