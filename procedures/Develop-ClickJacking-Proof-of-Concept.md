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
updated_at: '2025-12-14T17:28:04.576Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 36c9f94d-72b1-4867-8d6e-ce60953135e8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Develop-ClickJacking-Proof-of-Concept

## Summary

This procedure creates a proof-of-concept (PoC) HTML page that embeds a vulnerable site in an iframe and overlays it with decoy elements to demonstrate ClickJacking. It simulates how attackers can trick users into interacting with hidden page elements, such as buttons or forms on the Yelp homepage.

## Description

The PoC uses absolute positioning to place a transparent or hidden iframe over visible content, inducing clicks or keystrokes on the underlying legitimate site. For Yelp, this could lead to unintended actions like writing reviews or submitting searches. The approach requires only HTML/CSS; outcomes include a demo showing potential for credential theft or action hijacking. Prerequisites: Text editor and browser.

## Requirements

1. Text editor (e.g., VS Code, Notepad++)
2. Web browser for testing
3. Basic understanding of HTML and CSS positioning

## Defense

Defensive measures and detection strategies:

- Enforce frame-busting JavaScript to detect and break out of iframes
- Deploy browser extensions or policies to warn on suspicious overlays
- Log and alert on unusual user interactions via client-side monitoring

## Objectives

1. Build an interactive PoC overlaying the target site
2. Demonstrate click or input hijacking potential
3. Validate exploitability for reporting

## Instructions

### Step 1: Set Up Base HTML Structure

**Context**: Create the skeleton with an iframe for the target site.

In a file named clickjacking-poc.html, add:

```html
<!DOCTYPE html>
<html>
<head><title>ClickJacking PoC</title></head>
<body style="margin:0;">
<div id="overlay" style="position:absolute; top:0; left:0; width:500px; height:500px; background:rgba(255,0,0,0.1); z-index:1;">
Click here to win a prize!
</div>
<iframe id="target" src="https://www.yelp.com/" width="500" height="500" style="position:absolute; top:0; left:0; z-index:0; opacity:0.5;"></iframe>
</body>
</html>
```

> The overlay is semi-transparent for demo; in real attacks, make it fully opaque or hidden.

### Step 2: Position Elements for Hijacking

**Context**: Align the overlay to target specific elements like buttons on the embedded page.

Adjust CSS to position the overlay over a vulnerable element, e.g., a login button. Test by loading the file.

> Users clicking the overlay interact with the hidden iframe, e.g., submitting a form on Yelp.

### Step 3: Test Interaction Simulation

**Context**: Verify the PoC by simulating user actions.

Open in browser, click the overlay, and check if actions propagate to the iframe (e.g., via DevTools).

> Successful test shows clicks/keystrokes hijacked to the Yelp page.

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
