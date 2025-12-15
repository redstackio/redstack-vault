---
id: proc-uuid-1
tags:
  - client-side-bypass
  - html-manipulation
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
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
updated_at: '2025-12-14T17:29:20.024Z'
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
# Manipulate Client-Side HTML to Reveal Hidden Vote Controls

## Summary

This procedure involves using browser developer tools to tamper with client-side HTML and JavaScript on the HackerOne Hacktivity page, removing disabled attributes and modifying JSON flags to expose hidden vote functionality that is not intended for public use.

## Description

In the context of HackerOne's unreleased Vote feature for Hacktivity reports, the functionality is hidden behind client-side controls like disabled form elements and JSON boolean flags set to false. By inspecting and editing the page source in real-time, an attacker can enable these controls, allowing access to vote buttons. This bypasses the intended restrictions without any server-side enforcement, enabling further exploitation. Prerequisites include access to the public Hacktivity page and basic knowledge of browser dev tools.

## Requirements

1. Access to a modern web browser with developer tools (e.g., Chrome DevTools)
2. Public access to https://hackerone.com/hacktivity
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement server-side feature flags to hide unreleased endpoints entirely (e.g., return 404 for unauthorized access)
- Monitor for anomalous client-side modifications via client-side integrity checks (e.g., Content Security Policy)
- Log and alert on unexpected requests to beta endpoints

## Objectives

1. Expose hidden UI elements for vote functionality
2. Enable JSON request modifications to simulate authorized voting
3. Prepare for unauthorized request sending

## Instructions

### Step 1: Inspect and Edit HTML Elements

**Context**: Open the Hacktivity report page and use developer tools to locate and modify disabled controls.

Right-click on the page, select "Inspect Element," navigate to vote-related form elements, and remove the 'disabled' attribute from buttons or inputs.

> This makes the vote button clickable, revealing the hidden feature.

### Step 2: Modify JavaScript JSON Requests

**Context**: Intercept or edit JavaScript code that sends JSON with vote flags.

In the Console tab of dev tools, locate scripts setting vote flags to false, and override them to true, or edit the request payload directly.

> Expected output: Vote buttons appear enabled, and preparatory requests can be triggered.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[client-side-bypass]]
- [[html-manipulation]]
