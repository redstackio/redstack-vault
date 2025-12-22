---
id: p-discover-xss-query-params
tags:
  - xss
  - discovery
  - query-params
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:24.949Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover Reflected XSS in Query Parameters

## Summary

This procedure involves testing query parameters on web endpoints to identify reflected XSS vulnerabilities, specifically where user input is echoed into HTML without proper sanitization, allowing attribute breakout in this case on data.gov's /local/ endpoint.

## Description

In the attack scenario, attackers manually inject test payloads into URL query parameters like 'q' and observe their reflection in the page source, particularly in dynamic elements like pagination links. The target environment is a PHP-based web application with insufficient input filtering. Expected outcomes include confirming reflection points and breakout potential, setting the stage for payload refinement. Prerequisites include browser access to the target site and basic knowledge of HTML/JS injection.

## Requirements

1. Internet access to the target site (e.g., data.gov)
2. Web browser for manual testing and source inspection
3. Understanding of URL encoding and HTML attributes

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict inline scripts
- Use proper output encoding (e.g., htmlspecialchars with ENT_QUOTES) for all user input in HTML
- Monitor for anomalous query parameters with multiple '&' via WAF logs

## Objectives

1. Identify reflection points in query parameters
2. Confirm single quote breakout from attributes
3. Establish baseline for payload testing

## Instructions

### Step 1: Test Basic Reflection

**Context**: Append simple payloads to query parameters to check for unsanitized reflection.

Navigate to https://www.data.gov/local/?q=test and inspect the page source for the 'test' string in <div class="pagination"> elements. Look for href attributes like href='/local/?q=test'.

> If reflected without escaping, proceed to breakout tests.

### Step 2: Trial-and-Error for Breakout

**Context**: Incrementally test payloads with '&' to find the threshold for reflection.

Test payloads like ?q=abc' (one '&'), then ?q=abc'&def (two), up to ?q=abc'&def'&ghi (three+). Observe if fewer than three '&' prevent breakout due to sanitization.

> Success: Payload with 3+ '&' reflects and breaks out of single-quoted href='...'

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- discovery
