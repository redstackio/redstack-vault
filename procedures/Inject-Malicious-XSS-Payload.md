---
id: proc-inject-xss-payload
tags:
  - xss
  - payload-injection
  - web-exploit
type: procedure
tools: []
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
updated_at: '2025-12-14T03:16:08.239Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-XSS-Payload

## Summary

This procedure details the injection of a malicious JavaScript payload into a vulnerable stored input parameter, such as q_13787 in the DoD web application, to persist executable code for later victim execution.

## Description

In a stored XSS attack, the payload is submitted via a form or API and saved without sanitization, then rendered in HTML for other users. Here, the payload "'><svg onload=confirm(666)>" (URL-encoded as %22%27%3e%3csvg%2fonload%3dconfirm(666)%3e) closes any attribute or tag and loads an SVG with onload JavaScript. This targets the DoD app, leading to execution on view. Prerequisites: Confirmed vulnerable parameter. Outcomes: Stored payload ready for triggering.

## Requirements

1. Access to submit data via the vulnerable parameter
2. Knowledge of payload encoding to bypass basic filters
3. Browser or scripting tool for submission

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs with libraries like DOMPurify
- Escape outputs using context-aware encoding (e.g., htmlspecialchars)
- Rate-limit submissions and scan for script patterns in stored data

## Objectives

1. Successfully store a JavaScript payload without detection
2. Ensure payload survives storage and retrieval
3. Prepare for execution in victim contexts

## Instructions

### Step 1: Prepare Payload

**Context**: Craft a payload that evades common filters and executes reliably.

Use the encoded payload: %22%27%3e%3csvg%2fonload%3dconfirm(666)%3e. This uses SVG for broad browser support.

**Expected Output**: Valid encoded string ready for submission.

### Step 2: Submit via Parameter

**Context**: Inject into the target input field.

In the DoD app form, set q_13787 to the encoded payload and submit. Use dev tools to modify if needed.

**Expected Output**: Successful form submission without errors.

### Step 3: Verify Storage

**Context**: Check if payload is persisted intact.

Query or view the stored data endpoint to inspect the raw value of q_13787.

**Expected Output**: Payload present without alteration or encoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[JavaScript]]
