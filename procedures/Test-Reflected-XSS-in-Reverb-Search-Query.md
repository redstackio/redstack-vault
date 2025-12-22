---
tags:
  - xss
  - reflected
  - web
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
id: bba6b50b-55c2-4fbb-ba7a-ffa659f17f48
created_at: '2025-12-14T03:47:18.348Z'
updated_at: '2025-12-14T03:47:18.348Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Reflected-XSS-in-Reverb-Search-Query

## Summary

This procedure tests for reflected XSS in Reverb.com's marketplace search by injecting HTML tags into the query parameter and observing if they render unsanitized, enabling further payload crafting for phishing.

## Description

The Reverb search functionality echoes user input from the 'query' parameter directly into the HTML without proper escaping, allowing attackers to inject tags and attributes. This is a reflected XSS variant, triggered per search, suitable for targeted phishing via shared malicious links. Prerequisites include basic web access; no authentication needed. Outcomes include confirmation of vulnerability and basis for advanced exploits like UI spoofing.

## Requirements

1. Web browser with URL bar access
2. Knowledge of HTML and URL encoding
3. Access to Reverb.com marketplace

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to block inline scripts
- Sanitize all user inputs with HTML entity encoding on output
- Monitor for anomalous search queries containing HTML tags

## Objectives

1. Verify unsanitized HTML rendering in search results
2. Identify injectable attributes like class for styling
3. Establish foundation for phishing payload development

## Instructions

### Step 1: Inject Basic HTML Test

**Context**: Start with a simple tag to check if HTML renders without escaping.

Navigate to: https://reverb.com/marketplace?query=%3Ca%20href%3D%22http://example.com%22%3ETest%20Link%3C/a%3E

> This injects <a href="http://example.com">Test Link</a>. If it appears as a clickable link in results, XSS is confirmed.

### Step 2: Test with Site-Specific Classes

**Context**: Confirm attribute injection using Reverb's CSS classes for realistic rendering.

Use: https://reverb.com/marketplace?query=%3Ca%20href%3D%22http://badwebsite.com%22%3E%3Cspan%20class%3D%22btn%20button%20button--orange%20button--wide%22%3EXSS%3C/a%3E%3C/span%3E

> Observe if the span renders as an orange button styled like Reverb elements, indicating class attribute bypass.

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
- [[reflected-xss]]
