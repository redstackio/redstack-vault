---
tags:
  - xss
  - bypass
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
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 27a817b1-b064-4b3e-82a9-8f67133cf986
created_at: '2025-12-11T06:10:28.408Z'
updated_at: '2025-12-11T06:10:28.408Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1189]]'
---
# Bypass Filtering with HTML Entities

## Summary

This procedure crafts a payload using HTML entities like &lt; and &gt; to bypass filtering of literal angle brackets, enabling the injection of a script tag for XSS exploitation.

## Description

The vulnerability allows entities to decode into executable HTML, turning "/>&lt;script>alert(1)&lt;/script>"/ into a functional script tag. This targets Imgur's input sanitization flaws, with the outcome being a payload ready for storage.

## Requirements

1. Knowledge of HTML entities.
2. Text editor for crafting payloads.
3. Imgur account access.

## Defense

Defensive measures and detection strategies:

- Sanitize inputs by decoding entities before filtering.
- Use content security policy (CSP) to restrict script execution.

## Objectives

1. Create a bypass payload.
2. Ensure it renders as valid JavaScript.
3. Prepare for injection in the next step.

## Instructions

### Step 1: Craft Payload

**Context**: Replace angle brackets with entities.

Construct the payload: "/>&lt;script>alert(1)&lt;/script>"/.

> This should decode to "/><script>alert(1)</script>"/ in HTML.

### Step 2: Validate Locally

**Context**: Test the payload in a local HTML file to confirm decoding.

Create a test HTML page and insert the payload to verify alert execution.

> Ensure the script runs without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xss]]
- [[bypass]]
