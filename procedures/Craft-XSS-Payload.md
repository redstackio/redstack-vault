---
tags:
  - xss
  - payload
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/test-xss-payload]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 711eddaf-fa5f-4853-b7b8-044bdf887a13
created_at: '2025-12-13T22:26:40.935Z'
updated_at: '2025-12-13T22:26:40.935Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft XSS Payload

## Summary

This procedure details the creation of a JavaScript payload for injection into vulnerable parameters to achieve reflected XSS.

## Description

Payloads are crafted to bypass basic filters and execute arbitrary code. For the Pangle 'redirect' parameter, a simple alert script demonstrates the vulnerability. This assumes the parameter has been identified as reflective.

## Requirements
1. Identified vulnerable parameter
2. Knowledge of JavaScript syntax
3. HTTP client for testing

## Defense

Defensive measures and detection strategies:
- Sanitize inputs with HTML encoding
- Monitor logs for suspicious script patterns

## Objectives
1. Create executable payload
2. Test injection without execution
3. Ensure payload integrity

## Instructions

### Step 1: Build Payload

**Context**: Construct a basic script tag with alert.

Use '<script>alert("XSS")</script>' as the payload string.

### Step 2: Inject into URL

**Context**: Append the payload to the parameter.

Execute [[commands/test-xss-payload]]:

```bash
curl "https://example.pangle-endpoint.com?redirect=<script>alert(\"XSS\")</script>"
```

> Verify the payload is reflected in the response.

## MITRE ATT&CK Mapping

### Tactics
- [[Execution]]

### Techniques
- [[JavaScript]]

### Sub-Techniques

## Commands Used
- [[commands/test-xss-payload]]

## Tools Used
- [[tools/Browser-Developer-Tools]]

## Tags
- [[xss]]
- [[payload]]
