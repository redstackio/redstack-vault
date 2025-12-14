---
id: proc-discover-open-redirect-anomaly
name: Discover-Open-Redirect-Anomaly
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.283Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - open-redirect
  - anomaly-detection
  - web-testing
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Discover-Open-Redirect-Anomaly

## Summary

This procedure involves testing GET parameters on web applications to detect anomalies in redirect handling, specifically identifying cases where malformed inputs like ">cofee" trigger unexpected redirects due to insufficient validation.

## Description

In the context of Starbucks websites, this step uncovers flaws in input processing where modifying parameters leads to chained or improper redirects. It serves as the entry point for discovering open redirect vulnerabilities, allowing attackers to probe for weak URL handling without prior knowledge of exact flaws. Expected outcomes include observing redirects to unintended locations, setting the stage for payload refinement.

## Requirements

1. Access to a web browser with developer tools
2. Publicly accessible target URL (e.g., shop.starbucks.de)
3. Basic understanding of HTTP GET requests

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation to block malformed parameters
- Log and monitor unusual redirect patterns in web server access logs
- Use Content Security Policy (CSP) to restrict navigation

## Objectives

1. Identify input handling weaknesses in redirect logic
2. Confirm anomaly as a potential vulnerability entry point
3. Gather data for crafting targeted payloads

## Instructions

### Step 1: Modify GET Parameter

**Context**: Append anomalous characters to a standard parameter to test stripping and redirect behavior.

Navigate to the target site and alter a parameter like ?prefn1=>cofee in the URL bar or via developer tools.

> Load the modified URL in the browser and inspect the network response for redirect status (e.g., 302) to a strange path.

### Step 2: Analyze Response

**Context**: Examine the redirect destination to confirm unexpected behavior.

Check the Location header in the browser's network tab.

> If the redirect points to an invalid or external-like path post-stripping, the anomaly is confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[anomaly-detection]]
