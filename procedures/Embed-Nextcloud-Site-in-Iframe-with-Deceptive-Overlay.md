---
tags:
  - clickjacking
  - iframe
  - overlay
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
updated_at: '2025-12-14T17:28:04.442Z'
skill_level: novice
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 1de5774f-9cb9-4b0d-b3b5-c1268923aa66
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Embed-Nextcloud-Site-in-Iframe-with-Deceptive-Overlay

## Summary

This procedure embeds nextcloud.com in an iframe within the HTML file and adds an overlay with deceptive elements to trick users into clicking on hidden site features.

## Description

The core of the clickjacking exploit relies on framing nextcloud.com without restrictions, as confirmed by the absence of X-Frame-Options in its HTTP headers. An iframe of size 500x500 pixels is used to load the site, with a semi-transparent overlay div containing a visible button (e.g., "Click and go!") positioned to align with interactive elements like buttons or forms on the Nextcloud page. When a user clicks the overlay, it triggers actions on the framed site, potentially leading to form submissions or logins. This step assumes the basic HTML file from the previous procedure and targets a web browser environment.

## Requirements

1. The clickjack.html file created in prior steps
2. Knowledge of basic HTML, CSS for positioning
3. Access to inspect nextcloud.com elements (e.g., via browser dev tools)

## Defense

Defensive measures and detection strategies:

- Set X-Frame-Options: DENY or SAMEORIGIN in server responses
- Use frame-ancestors in CSP to block unauthorized framing
- Educate users on phishing risks and verify site authenticity

## Objectives

1. Successfully frame nextcloud.com in an iframe
2. Create a deceptive overlay that misleads user clicks
3. Align overlay elements with vulnerable site interactions for maximum impact

## Instructions

### Step 1: Insert Iframe into HTML Body

**Context**: Add the iframe element to load nextcloud.com, exploiting the lack of frame protection.

Edit clickjack.html and insert within the <body>:

```html
<iframe src="https://nextcloud.com" width="500" height="500" style="position: absolute; top: 0; left: 0; opacity: 0.5;"></iframe>
```

> This embeds the site with partial opacity for testing; adjust opacity to 0 for stealth in real attacks. Save and verify syntax.

### Step 2: Add Deceptive Overlay

**Context**: Overlay a div with a button that aligns with a target element on nextcloud.com, such as a login button.

Append to the <body>:

```html
<div style="position: absolute; top: 200px; left: 200px; width: 100px; height: 30px; background: transparent;">
    <button style="position: absolute; top: 0; left: 0;">Click and go!</button>
</div>
```

> Position the button to overlap a clickable element on the framed site (e.g., via trial and error in browser). The transparent div ensures the iframe is clickable underneath.

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
- [[iframe]]
- [[web]]
