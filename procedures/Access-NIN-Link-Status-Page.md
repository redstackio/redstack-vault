---
id: proc-uuid-2
tags:
  - web-interaction
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:35.674Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Access-NIN-Link-Status-Page

## Summary

This procedure simulates legitimate user interaction by clicking the 'Check your NIN Link Status' button on the MTN NIN homepage, loading the vulnerable page whose source code exposes administrative paths.

## Description

The MTN NIN linking site uses WordPress, and user interactions like button clicks load dynamic content. This step targets the status check feature, which inadvertently includes references to admin endpoints in its HTML. It requires no inputs beyond the click, making it low-risk for detection, but it positions the attacker to inspect client-side code for misconfigurations leading to improper access controls.

## Requirements

1. Active session from previous navigation to https://nin.mtn.ng/
2. Functional web browser
3. No credentials or additional network access

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove admin path references in client-side code
- Monitor for repeated interactions with specific endpoints
- Employ content security policies (CSP) to limit source inspection impacts

## Objectives

1. Load the NIN status page to access its HTML structure
2. Mimic user behavior to avoid suspicion
3. Prepare for source code analysis

## Instructions

### Step 1: Locate the Button

**Context**: Identify the entry point for status checking on the homepage.

Scan the page for the 'Check your NIN Link Status' button, typically prominent.

> The button should be visible and clickable upon hover.

### Step 2: Click and Load Page

**Context**: Trigger the page load to reveal embedded vulnerabilities.

Click the button to navigate.

> Expected: Transition to a form or status interface without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-interaction
- recon
