---
tags:
  - clickjacking
  - browser-verification
  - framing-test
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
updated_at: '2025-12-14T17:28:12.668Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 4693f69a-c801-46be-bd7c-054628f88644
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Verify-Clickjacking-by-Loading-HTML-in-Browser

## Summary

This procedure tests the clickjacking vulnerability by opening the crafted HTML frameset in a browser, confirming that Semrush pages load without frame protection.

## Description

Loading the HTML file in a compatible browser like Firefox v56 or Google Chrome reveals if the Semrush pages can be embedded cross-origin. Without X-Frame-Options, the pages render fully, allowing attackers to overlay transparent elements for tricking user interactions, such as clicking on login buttons or form submissions invisibly.

## Requirements

1. Firefox v56 or Google Chrome installed
2. The frameset.html file from previous procedure
3. Stable internet connection

## Defense

Defensive measures and detection strategies:

- Enforce strict framing policies via headers
- Browser extensions or WAF rules to detect anomalous framing attempts
- Log and alert on cross-origin iframe loads

## Objectives

1. Confirm pages load in frames without denial
2. Observe interactive elements for potential exploitation
3. Document the vulnerability for reporting

## Instructions

### Step 1: Open HTML File in Browser

**Context**: Launch the browser and load the local HTML to simulate the attack.

Double-click frameset.html or use File > Open in the browser menu to load it.

> The Semrush pages should appear in the frameset columns without any error messages like "Refused to display in a frame".

### Step 2: Interact and Validate

**Context**: Test if the framed content is clickable and functional.

Click on elements within the frames, such as navigation links on Semrush pages, to ensure they respond normally.

> Expected: Full interactivity, no blocking, demonstrating frameable vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[browser-test]]
- [[ui-redressing]]
