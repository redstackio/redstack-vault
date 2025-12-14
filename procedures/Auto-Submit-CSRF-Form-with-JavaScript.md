---
id: 123e4567-e89b-12d3-a456-426614174002
name: Auto-Submit-CSRF-Form-with-JavaScript
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:03.805Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - csrf
  - javascript
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Auto-Submit-CSRF-Form-with-JavaScript

## Summary

Enhance the malicious CSRF form with JavaScript to automatically submit upon page load, ensuring the attack executes without requiring victim interaction.

## Description

To make the CSRF effective in a drive-by scenario, the form must submit immediately when the victim loads the page. This procedure adds a script that triggers the form submission on DOM load, leveraging the browser's same-origin policy bypass for cross-site requests. This relies on the absence of CSRF protections like tokens or origin checks on the Localize.io endpoint.

## Requirements

1. Existing HTML form from previous procedure
2. Basic JavaScript knowledge
3. Browser developer tools for testing

## Defense

Defensive measures and detection strategies:

- Enforce Content-Security-Policy (CSP) to block inline scripts
- Log and alert on rapid settings changes from unexpected origins
- Use frame-busting or X-Frame-Options to prevent embedding

## Objectives

1. Automate CSRF execution for stealth
2. Confirm auto-submission works cross-origin
3. Integrate with delivery mechanism

## Instructions

### Step 1: Add JavaScript to Form

**Context**: Insert script to submit the form on page load.

Edit the HTML to include:

```html
<script>
  window.onload = function() {
    document.forms[0].submit();
  }
</script>
```

Place this before the closing </body> tag.

> This script waits for the page to load and submits the first form. Test by loading the page; the request should fire immediately.

### Step 2: Test Auto-Submission

**Context**: Verify the request is sent without clicks.

Open the updated HTML in an authenticated browser session. Monitor network tab for POST to /pages/settings.

> Expected: Automatic POST with settings data; no manual input needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[JavaScript]]
