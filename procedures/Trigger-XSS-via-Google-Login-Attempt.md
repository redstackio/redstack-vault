---
tags:
  - xss
  - execution
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d160e381-c871-437e-a4f9-cc8a7c308cbe
created_at: '2025-12-14T00:11:16.770Z'
updated_at: '2025-12-14T00:11:16.770Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS via Google Login Attempt

## Summary

This procedure triggers the reflected XSS by clicking the Google login button on the manipulated page, executing the injected JavaScript.

## Description

Upon clicking 'Log in with Google', the unsanitized google_apps_uri executes the payload, allowing theft of cookies or domain info. This completes the exploit in the victim's browser context.

## Requirements

1. Manipulated URL loaded
2. Web browser

## Defense

Defensive measures and detection strategies:

- Validate and encode URI parameters
- Monitor for anomalous JavaScript execution

## Objectives

1. Execute payload
2. Steal sensitive data
3. Confirm vulnerability

## Instructions

### Step 1: Click Login Button

**Context**: Interact with the page to trigger the XSS.

Click 'Log in with Google'.

> Payload executes, showing prompt with data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss
- execution
