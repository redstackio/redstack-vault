---
tags:
  - impact
  - ui-redressing
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 321cd03a-c1e1-4586-be6b-3064448e9dd7
created_at: '2025-12-14T17:28:12.646Z'
updated_at: '2025-12-14T17:28:12.646Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate-Clickjacking-Impact

## Summary

This procedure simulates the real-world effects of clickjacking by overlaying invisible or transparent iframes to hijack user interactions, potentially leading to account takeover, deletion, or password changes on the framed site.

## Description

Once framed, attackers can position fake UI elements over sensitive controls in the iframe, tricking users into clicking them. For Lemlist, this could target user management pages to add malicious users or delete accounts. The demonstration uses opacity and positioning in HTML/CSS to hide the iframe while capturing clicks or keystrokes. Limited to local contexts, but illustrates scalable phishing attacks.

## Requirements

1. Existing PoC HTML from prior procedure
2. Browser for testing interactions
3. Understanding of CSS positioning for overlays

## Defense

Defensive measures and detection strategies:

- Add X-Frame-Options: DENY to block all framing
- Implement JavaScript frame-busting code as fallback
- Educate users on phishing; monitor for unusual account actions via logs

## Objectives

1. Hijack clicks to perform unintended actions
2. Capture potential keystrokes in forms
3. Highlight risks like account takeover

## Instructions

### Step 1: Modify PoC for Overlay

**Context**: Add transparent or invisible elements to simulate trickery.

Edit poc.html to include an overlay div. Example addition:

```html
<div style="position: relative;">
    <iframe id="target" src="https://app.lemlist.com/teams/tea_sgYr5dZr478x4FQ9K/settings/user/usr_Z3GZ4DDHLLyLyZHj5/users" style="opacity: 0.3; position: absolute; top: 0; left: 0; height: 550px; width: 700px;"></iframe>
    <div style="position: absolute; top: 200px; left: 300px; z-index: 1;">
        <button onclick="document.getElementById('target').contentWindow.postMessage({action: 'click'}, '*');">Fake Delete Button</button>
    </div>
</div>
```

Adjust positions to align with real buttons (e.g., delete user).

### Step 2: Test Interaction Hijacking

**Context**: Simulate user clicks and observe propagation to the iframe.

Reload the PoC in browser. Click the fake button and check if it triggers the corresponding action in the partially visible iframe (e.g., a confirmation dialog for deletion).

> For keystroke capture, add input fields overlaying login forms and log inputs via JavaScript.

### Step 3: Document Potential Impacts

**Context**: Explain and capture evidence of risks.

Note scenarios: Overlay on password change form to steal credentials, or on add-user button for takeover. Attach screenshots of aligned elements.

**Expected Output**: Fake clicks result in real actions within the iframe, demonstrating hijack potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Impact]]
- [[account-takeover]]
