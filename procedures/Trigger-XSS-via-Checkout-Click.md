---
id: proc-starbucks-xss-trigger
tags:
  - xss
  - execution
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:21.131Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Checkout-Click

## Summary

This procedure triggers the injected XSS payload by clicking the 'Checkout' element, which uses jQuery to propagate the click to the injected 'checkoutButton' id, executing the malicious onclick handler.

## Description

The page's jQuery binds clicks on body or title elements to trigger #checkoutButton clicks. The injected link element becomes clickable, executing the confirm() or further phishing code upon interaction.

## Requirements

1. Page loaded with injected payload.
2. Firefox browser.
3. User interaction capability.

## Defense

Defensive measures and detection strategies:

- Sanitize reflected content in attributes.
- Disable or validate dynamic attribute additions.

## Objectives

1. Execute injected JavaScript.
2. Demonstrate control over page events.
3. Enable further exploitation.

## Instructions

### Step 1: Wait for Page Load

**Context**: Ensure DOM is ready and jQuery bindings are active.

Pause briefly after navigation.

> Expected output: Page fully rendered.

### Step 2: Click Checkout Element

**Context**: Interact to fire the onclick.

Click the 'Checkout' title or button.

> Expected output: JavaScript executes, e.g., alert pops up.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[Execution]]
