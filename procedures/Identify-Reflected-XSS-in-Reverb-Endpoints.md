---
tags:
  - xss
  - recon
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:47:12.621Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 4e55013b-2adb-4480-bb57-63c3db29e797
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Reflected XSS in Reverb Endpoints

## Summary

This procedure involves manual exploration of Reverb.com's sandbox environment to identify query parameters in dashboard pages that reflect user input as unsanitized HTML, enabling potential XSS attacks. It builds on prior vulnerability fixes to uncover similar issues in buying and selling sections.

## Description

In the context of web application security testing, this step targets authenticated pages like /my/buying/orders where query parameters are rendered directly into HTML without escaping. The attacker, having knowledge of a previously fixed XSS (e.g., report #351376), systematically tests endpoints for reflection points. Successful identification allows progression to payload crafting, ultimately leading to phishing via spoofed content. Prerequisites include a Reverb account for accessing dashboard pages and basic HTML knowledge.

## Requirements

1. Access to a web browser with network inspection capabilities (e.g., Chrome DevTools).
2. Valid login to sandbox.reverb.com to reach /my/ endpoints.
3. Awareness of prior vulnerability reports for targeted exploration.

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict inline HTML rendering.
- Sanitize all user inputs in query parameters using HTML entity encoding.
- Monitor for anomalous query strings in access logs that contain HTML tags.

## Objectives

1. Locate vulnerable query parameters in Reverb dashboard pages.
2. Confirm lack of sanitization for HTML tags and classes.
3. Establish foundation for XSS exploitation.

## Instructions

### Step 1: Review Prior Vulnerabilities

**Context**: Start by noting fixed issues to guide exploration, such as a previous XSS in report #351376, then focus on related endpoints.

No specific command; manually review HackerOne reports or internal notes.

> Expected: List of candidate pages like /my/buying/orders.

### Step 2: Test Endpoints for Reflection

**Context**: Append simple test inputs to query parameters and inspect rendered output.

Navigate to https://sandbox.reverb.com/my/buying/orders?query=<test> and use browser dev tools to check if <test> appears as a tag in the DOM.

> Repeat for /my/selling/listings and /my/selling/orders. Expected: Direct HTML insertion without escaping.

### Step 3: Validate Unsanitized Classes

**Context**: Test class attributes to confirm arbitrary styling injection.

Use ?query=<span class="test-class">test</span> and inspect CSS application.

> Expected: Custom class renders without blocking, indicating full HTML control.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[recon]]
- [[web-vuln]]
