---
tags:
  - xss
  - execution
  - impact
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: dc20dcee-d987-44c7-946c-1e8cf414efc5
created_at: '2025-12-14T03:15:35.883Z'
updated_at: '2025-12-14T03:15:35.883Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-Stored-XSS-Execution

## Summary

This procedure verifies the stored XSS by viewing the order details, triggering JavaScript execution in the attacker's chosen context, such as an admin panel.

## Description

After submission, accessing the order confirmation or admin order details page reflects the stored payload, executing it on load or interaction. The proof-of-concept `prompt(0)` alert fires in multiple locations (up to 5), confirming breakout and execution. Alternative payloads like ` onmouseover = " prompt(0)` test event-based triggers. This step highlights the impact on authenticated users viewing orders, enabling further attacks like credential theft.

## Requirements

1. Successful order submission with payload
2. Access to view order details (self or simulated admin)
3. Browser capable of executing JS

## Defense

Defensive measures and detection strategies:

- Output encode all user data in templates (e.g., htmlspecialchars in PHP)
- Deploy browser-based protections like XSS auditors
- Monitor for JS errors or unexpected prompts in user sessions

## Objectives

1. Confirm payload execution on page render
2. Demonstrate impact through alert or console logs
3. Simulate real-world exploitation for credential access

## Instructions

### Step 1: Access Order Confirmation or Details

**Context**: Load the page where stored data is reflected.

Navigate to the order confirmation page post-submission or admin order view.

> Payload executes automatically if on load; check for alert in 5 reflection points.

### Step 2: Test Interaction Triggers

**Context**: Verify event-based execution if onload fails.

Hover over affected elements with payload like ` onmouseover = " prompt(0)`.

> Prompt appears on mouseover, confirming stored and executable state.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
