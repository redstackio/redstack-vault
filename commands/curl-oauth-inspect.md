---
id: cmd-uuid-002
data: >-
  curl -v -X GET
  "https://graph.facebook.com/oauth/authorize?client_id=410312912374011&display=popup&redirect_uri=https%3A%2F%2Ffacebookstore.shopifyapps.com%2Fauthenticated&response_type=code&scope=manage_pages+email&state=c2f449f2df5ee64df6173702846bce72e3a57319"
  > response.html
tags:
  - oauth
  - curl
  - inspect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.841Z'
verified: false
validated: true
submitted: true
---
# curl-oauth-inspect

## Command

```bash
curl -v -X GET "https://graph.facebook.com/oauth/authorize?client_id=410312912374011&display=popup&redirect_uri=https%3A%2F%2Ffacebookstore.shopifyapps.com%2Fauthenticated&response_type=code&scope=manage_pages+email&state=c2f449f2df5ee64df6173702846bce72e3a57319" > response.html
```

## Description

Verbose curl to inspect and save the OAuth authorization response for analysis of fixed state.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | Yes |
| `> response.html` | Save to file | Yes |

## Examples

### Basic Usage

```bash
curl -v -X GET "https://graph.facebook.com/oauth/authorize?..." > response.html
```

## Expected Output

Verbose logs and saved HTML file showing request headers, response body with state parameter.

## Related

- [[Related Procedure: Initiate-OAuth-Authorization-Request]]
