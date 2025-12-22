---
tags:
  - xss
  - reflected-xss
  - bypass
  - javascript-injection
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/access-xss-poc-url]]'
  - '[[commands/access-backtick-xss-poc-url]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 74e93d3d-5f1f-4695-83b4-a87860afa09d
created_at: '2025-12-11T06:10:28.652Z'
updated_at: '2025-12-11T06:10:28.652Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Bypass Partial XSS Fix with Backticks

## Summary

This procedure bypasses an initial fix for a reflected XSS vulnerability by using backticks to close strings in JavaScript context, allowing continued injection and execution of arbitrary code.

## Description

After an initial remediation that escaped quotes but not backticks, this bypass exploits the oversight by crafting a payload with backticks (%60) to close the string and inject an alert. This demonstrates the importance of comprehensive escaping in JavaScript contexts and can lead to the same impacts as the original vulnerability, such as cookie theft or phishing.

## Requirements

1. Access to a web browser like [[tools/Firefox]]
2. Network connectivity to the target Glassdoor URL post-initial fix
3. Understanding of JavaScript string delimiters

## Defense

Defensive measures and detection strategies:

- Escape all potential string delimiters including backticks in JavaScript
- Regularly retest fixes with varied payloads
- Implement WAF rules to detect encoded JavaScript injections

## Objectives

1. Prove insufficiency of initial fix
2. Execute arbitrary JavaScript post-remediation
3. Highlight need for thorough vulnerability patching

## Instructions

### Step 1: Craft and Access Bypass POC URL

**Context**: Retest with a new payload using backticks to demonstrate persisting vulnerability.

**Command** ([[commands/access-xss-poc-url]]):
```bash
# Use browser to visit:
https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=%60%2balert/**/(1)%2b%60
```

> This uses backticks to close the string in JavaScript context and execute alert(1). Expect an alert box to appear if the bypass is successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/access-xss-poc-url]]

## Tools Used

- [[tools/Firefox]]

## Tags

- [[commands/access-xss-poc-url]]
- [[bypass]]
