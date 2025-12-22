---
tags:
  - xss
  - execution
  - proof-of-concept
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: c7eab4b6-7a4a-4b85-90b9-af15fe57e00d
created_at: '2025-12-11T06:06:04.863Z'
updated_at: '2025-12-11T06:06:04.863Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Demonstrate XSS Execution

## Summary

This procedure demonstrates the execution of an injected XSS payload in the victim's browser, loading and running arbitrary JavaScript.

## Description

After injection, the stored payload is viewed in a browser, where the normalized script tag loads an external script from a malicious site. This proves the vulnerability's impact, such as potential data theft or session hijacking.

## Requirements

1. Injected payload in the message system
2. Browser access to view the message
3. Hosted POC script at the specified URL

## Defense

Defensive measures and detection strategies:

- Use XSS protection headers like X-XSS-Protection
- Implement strict CSP to block unauthorized scripts
- Monitor network traffic for requests to suspicious domains

## Objectives

1. Trigger payload execution
2. Verify script loading and functionality
3. Document impact for reporting

## Instructions

### Step 1: View Injected Message

**Context**: Access the message to trigger rendering.

Log into the Social Club and view the message containing the payload.

> The browser will render the normalized script tag.

### Step 2: Verify Script Execution

**Context**: Use developer tools to confirm script load.

Open browser console and network tab to observe the request to //evil.site/poc.js and any executed code.

> Look for alerts, logs, or other indicators from the POC script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xss]]
- [[Execution]]
