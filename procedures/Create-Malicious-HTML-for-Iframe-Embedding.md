---
tags:
  - clickjacking
  - iframe
  - html
type: procedure
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
updated_at: '2025-12-14T17:28:05.429Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: cf4190ad-7341-475a-a116-1cafeaf75abd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Malicious-HTML-for-Iframe-Embedding

## Summary

This procedure creates a malicious HTML page that embeds the Nextcloud login page in an iframe, using sandbox attributes to allow scripts, forms, and popups for effective clickjacking.

## Description

Clickjacking relies on framing the target in an invisible or overlaid iframe on a malicious site. This step involves authoring an HTML file with an <iframe> tag sourcing the vulnerable login URL, setting dimensions (e.g., 600x400), and sandbox attributes (allow-modals, allow-scripts, allow-forms, allow-popups, allow-same-origin) to bypass restrictions and enable user interactions like login submissions. The outcome is a functional malicious page that can trick users into actions, leading to credential theft or phishing. Requires a text editor; no server hosting needed for local testing.

## Requirements

1. Text editor (e.g., VS Code, Notepad++)
2. Knowledge of basic HTML
3. Verified vulnerable target URL from prior reconnaissance

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP frame-ancestors 'none'
- Scan for and block suspicious iframe sources in proxy logs
- Educate users on phishing indicators and use browser extensions to detect overlays

## Objectives

1. Construct a framable malicious page
2. Enable interactive elements within the iframe
3. Prepare for overlay-based user deception

## Instructions

### Step 1: Author the HTML File

**Context**: Create the base structure for the malicious page.

Open a text editor and create a new file named malicious.html with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Fake Page</title>
</head>
<body>
    <iframe src="https://portal.nextcloud.com/login.php" sandbox="allow-modals allow-scripts allow-forms allow-popups allow-same-origin" width="600" height="400"></iframe>
</body>
</html>
```

> This embeds the login page; sandbox allows necessary permissions without full origin relaxation.

### Step 2: Customize for Overlay

**Context**: Add invisible overlay elements to hijack clicks (optional for basic test).

Enhance the body with transparent divs positioned over the iframe for click interception.

> Example: Add <div style="position:absolute; top:0; left:0; width:600px; height:400px; opacity:0.1; z-index:10;"></div> to simulate overlay.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- clickjacking
- iframe
- exploitation
