---
tags:
  - xss
  - web
  - parameter-identification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 9754cfc9-f576-4802-92c1-8fc694a68c0a
created_at: '2025-12-11T06:10:17.185Z'
updated_at: '2025-12-11T06:10:17.185Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Identify Vulnerable Hash Parameter in Slack

## Summary

This procedure involves inspecting Slack's web pages to identify the 'cvo_sid1' parameter in the location hash, which is vulnerable to XSS due to lack of sanitization in live.js when calling convertro code.

## Description

The attack targets public-facing Slack pages where the hash parameter is processed without escaping, allowing injection of malicious 'typ' values. This is useful for reconnaissance in web vulnerability assessments, leading to potential XSS exploits. Expected outcome is confirmation of the vulnerability for further exploitation.

## Requirements

1. Access to a web browser with developer tools.
2. Target URL: https://slack.com/is.
3. Basic knowledge of JavaScript and web inspection.

## Defense

Defensive measures and detection strategies:

- Implement input sanitization for hash parameters in JavaScript.
- Monitor for unusual hash manipulations in web logs.

## Objectives

1. Locate and confirm the vulnerable parameter.
2. Understand its role in generating unsanitized JavaScript.
3. Prepare for payload crafting.

## Instructions

### Step 1: Inspect Page Source

**Context**: Use browser tools to analyze the hash usage.

Open developer tools and navigate to the network or sources tab to find live.js and its handling of 'cvo_sid1'.

> Expect to see the parameter passed to convertro without sanitization.

### Step 2: Test Parameter Manipulation

**Context**: Manually alter the hash to observe behavior.

Append a test value to the URL hash and reload to confirm it affects JavaScript generation.

> Look for opportunities to inject via 'typ' without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss
- web
