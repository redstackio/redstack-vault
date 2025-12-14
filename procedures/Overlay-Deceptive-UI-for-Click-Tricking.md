---
id: proc-overlay-ui-001
tags:
  - clickjacking
  - css-overlay
  - ui-deception
  - web
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
updated_at: '2025-12-14T17:28:12.856Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Overlay-Deceptive-UI-for-Click-Tricking

## Summary

This procedure modifies the malicious HTML to overlay semi-transparent iframes with fake UI elements like buttons and text, tricking users into clicking on hidden site elements to perform unintended actions such as form submissions or credential entry.

## Description

Building on iframe embedding, CSS is used to position deceptive elements over the target site. The iframe's opacity is reduced to show underlying content subtly, while higher z-index fake buttons align with sensitive site controls. This exploits user trust on the attacker's page, leading to account takeover or phishing on https://topechelon.com/.

## Requirements

1. Existing HTML file from embedding step
2. Basic CSS knowledge for positioning
3. Browser developer tools for alignment testing

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP to block inline styles/scripts
- User education on suspicious overlays
- Browser extensions like NoScript to detect framing

## Objectives

1. Create visual deception for click hijacking
2. Align fake elements with target site controls
3. Test propagation of clicks to iframe

## Instructions

### Step 1: Add CSS Styles to HTML

**Context**: Apply styles to make iframe semi-transparent and position overlays.

No command; edit the HTML.

```html
<style>
.iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0.6; z-index: 99; }
.deceptive-btn { position: absolute; top: 200px; left: 300px; z-index: 100; padding: 10px; background: #4CAF50; color: white; }
</style>
<iframe src="https://topechelon.com/" class="iframe" frameborder="0"></iframe>
<button class="deceptive-btn">Click to Login</button>
```

> Adjust positions to align with target login button; test clicks.

### Step 2: Test Click Propagation

**Context**: Ensure clicks on fake elements trigger real site actions.

No command; manual interaction.

> Click the overlay button; it should submit a form or navigate in the iframe.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ui-manipulation]]
- [[css-exploitation]]
