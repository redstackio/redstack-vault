---
tags:
  - phishing
  - browser-ui
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:41.771Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: db4d8648-74d6-46a0-9871-b009a16d2b28
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Open-Brave-Shield-Panel

## Summary

This procedure accesses the Brave Shield panel in the iOS app while on a malicious site, positioning for the domain display vulnerability exploitation.

## Description

Brave Shield is a privacy feature that blocks trackers and ads, accessible via an icon in the address bar. In vulnerable versions on iOS, opening this panel on an IDN homograph site does not properly handle punycode decoding, leading to the next step's deception. This manual UI interaction requires no technical tools and assumes the user is already on the spoofed site. Expected outcome: Panel opens without alerting the user to the domain's true nature.

## Requirements

1. Brave iOS app open on the malicious domain.
2. User interaction capability (tap gestures).
3. Vulnerable Brave version lacking IDN fixes.

## Defense

Defensive measures and detection strategies:

- Update Brave to versions with IDN homograph protections.
- Use browser audits to check for UI inconsistencies in security panels.
- Implement user training on verifying domains in all browser components, not just the address bar.

## Objectives

1. Trigger the Shield panel UI to expose the vulnerability.
2. Maintain user deception by avoiding any visual warnings.
3. Enable observation of the misdisplay in the subsequent step.

## Instructions

### Step 1: Locate Shield Icon

**Context**: Identify the entry point for the Shield interface on the current page.

While on the site (e.g., https://www.xn--80ak6aa92e.com/), look for the lion shield icon in the address bar.

> Confirm the icon is present and tappable; it should not be disabled.

### Step 2: Tap to Open Panel

**Context**: Activate the panel to load site details, including the flawed domain display.

Tap the Shield icon.

> The panel slides in, showing options like trackers blocked, but the domain field is key for the exploit.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[browser-ui]]
