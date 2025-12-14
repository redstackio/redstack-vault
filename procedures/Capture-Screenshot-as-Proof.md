---
id: proc-capture-screenshot-proof
tags:
  - clickjacking
  - proof-capture
  - documentation
type: procedure
tools:
  - '[[tools/Browser-Unspecified]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:04.831Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Screenshot-as-Proof

## Summary

This procedure documents the successful iframe embedding by capturing a screenshot of the browser window showing the target site (e.g., Yelp) loaded within the PoC iframe.

## Description

Screenshots serve as irrefutable evidence in vulnerability reports, capturing the exact state of the exploit. This step follows verification and uses built-in browser or OS tools. Outcomes include a visual artifact demonstrating the vulnerability, crucial for disclosure platforms like HackerOne.

## Requirements

1. Web browser with PoC loaded
2. Screenshot tool (built-in or external)
3. Image saving capability

## Defense

Defensive measures and detection strategies:

- N/A (documentation step)
- Monitor report submissions for early detection

## Objectives

1. Create visual evidence
2. Preserve state for reporting
3. Support vulnerability validation

## Instructions

### Step 1: Prepare View

**Context**: Ensure iframe is fully loaded.

With the PoC open and Yelp rendered, adjust window to show the iframe clearly.

> No commands; visual preparation.

### Step 2: Take Screenshot

**Context**: Capture the browser content.

Use browser shortcut (e.g., Ctrl+Shift+S in Chrome) or OS tool (e.g., Snipping Tool) to screenshot the iframe area.

> Expected output: PNG/JPG file showing embedded Yelp. Success if iframe and content are visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Unspecified]]

## Tags

- [[clickjacking]]
- [[documentation]]
