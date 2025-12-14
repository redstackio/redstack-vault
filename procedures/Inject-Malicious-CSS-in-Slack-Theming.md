---
id: proc-slack-css-injection-001
tags:
  - css-injection
  - slack
  - macos
  - payload
type: procedure
tools:
  - '[[tools/CSS-Keylogging]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-13T23:52:33.514Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Disable or Modify Tools]]'
---
# Inject-Malicious-CSS-in-Slack-Theming

## Summary

This procedure injects a malicious CSS payload into Slack's Column Background field on macOS, exploiting lack of validation to hide the entire app interface and demonstrate potential for data exfiltration.

## Description

The vulnerability stems from un-sanitized CSS input in the custom theming feature, allowing closure of existing styles and injection of rules like `html {display:none;}`. This renders the app unusable. Advanced use could leverage CSS selectors for keylogging messages, referencing techniques from CSS-Keylogging tool. Targets macOS Slack client; effect applies immediately to the DOM.

## Requirements

1. Custom theming enabled in Slack
2. Access to Column Background field
3. Basic knowledge of CSS syntax

## Defense

Defensive measures and detection strategies:

- Validate and whitelist CSS properties in theming inputs
- Escape or strip user CSS to prevent rule injection
- Monitor for DOM manipulation via browser dev tools or app logs
- Patch Slack to version post-vulnerability disclosure

## Objectives

1. Apply malicious CSS to impair app functionality
2. Achieve persistence of the disablement
3. Explore exfiltration via CSS attribute selectors for key capture

## Instructions

### Step 1: Prepare Payload

**Context**: Craft CSS to close prior rules and hide content.

Use payload: `#FFFFFF;} html {display:none;}` where `#FFFFFF;` mimics a color, `}` closes the style, and the new rule hides HTML.

> For exfiltration, extend with selectors targeting input fields, e.g., using `:focus` for keylogging simulation.

### Step 2: Enter and Apply

**Context**: Input the payload into the vulnerable field.

In Column Background, paste the payload and click Apply or Save.

> CSS injects into the app's stylesheet, immediately hiding content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Disable or Modify Tools]] Disable or Modify Tools

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/CSS-Keylogging]]

## Tags

- [[css-injection]]
- [[slack]]
- [[macos]]
