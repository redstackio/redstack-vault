---
tags:
  - xss
  - testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 02f30d9f-2f53-4718-ad5a-fa6309780628
created_at: '2025-12-14T03:47:12.604Z'
updated_at: '2025-12-14T03:47:12.604Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Initial-XSS-Payload

## Summary

This procedure tests a basic reflected XSS payload on a redirect endpoint to confirm if post-fix validation blocks javascript: injections, as seen in the Semrush vulnerability.

## Description

The attack scenario involves crafting a URL with a newline-injected javascript: payload to attempt code execution in the victim's browser. In a web environment like Semrush, this verifies the fix from report #311330. Prerequisites: Public access to the endpoint. Expected outcomes: Payload failure, confirming the need for bypass techniques.

## Requirements

1. Web browser with developer tools
2. URL encoding knowledge
3. Target URL: https://www.semrush.com/redirect

## Defense

Defensive measures and detection strategies:

- Sanitize URL parameters to block javascript: schemes
- Log and monitor anomalous URL patterns
- Employ CSP headers to restrict script execution

## Objectives

1. Verify basic XSS blocking
2. Identify validation strengths
3. Prepare for advanced bypasses

## Instructions

### Step 1: Craft Basic Payload

**Context**: Build a standard XSS payload using a newline to break out of validation.

Construct the URL: https://www.semrush.com/redirect?url=javascript://%0aalert(document.cookie).

> Expected: Browser visits the URL; no alert triggers due to fix.

### Step 2: Execute and Observe

**Context**: Visit the crafted URL to test execution.

Open the URL in a browser and check console for errors or blocked scripts.

> Expected: Redirect occurs without JavaScript execution; payload sanitized.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-testing]]
