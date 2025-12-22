---
tags:
  - xss
  - recon
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/test-xss-payload]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: ab3703ba-ba63-4ced-bffb-fbb0757b7a06
created_at: '2025-12-13T22:26:40.931Z'
updated_at: '2025-12-13T22:26:40.931Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Parameter

## Summary

This procedure involves testing web parameters for reflection of user input without proper HTML escaping, a common precursor to identifying reflected XSS vulnerabilities.

## Description

In this context, the 'redirect' parameter in the Pangle endpoint reflects user-supplied data back into the response without encoding, allowing potential injection of scripts. This is typically discovered by submitting test inputs and inspecting the output. The target is a web-based endpoint, and success leads to opportunities for payload injection.

## Requirements
1. Access to the target URL
2. Web browser or HTTP client like curl
3. Basic understanding of HTTP requests

## Defense

Defensive measures and detection strategies:
- Implement output encoding for all reflected user inputs
- Use web application firewalls (WAF) to detect script injections

## Objectives
1. Confirm parameter reflection
2. Identify lack of sanitization
3. Prepare for payload crafting

## Instructions

### Step 1: Test Parameter Reflection

**Context**: Send a benign test string to the parameter and check the response.

Execute [[commands/test-xss-payload]]:

```bash
curl "https://example.pangle-endpoint.com?redirect=test"
```

> This command fetches the endpoint and checks if 'test' appears unencoded in the response.

### Step 2: Inspect Response

**Context**: Use browser tools to verify if the input is directly inserted into HTML.

Open the URL in a browser and use developer tools to examine the source.

> Look for the test string in the DOM without escaping.

## MITRE ATT&CK Mapping

### Tactics
- [[Initial Access]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/test-xss-payload]]

## Tools Used
- [[tools/Browser-Developer-Tools]]

## Tags
- [[xss]]
- [[recon]]
