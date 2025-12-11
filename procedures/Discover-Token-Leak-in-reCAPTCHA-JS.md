---
tags:
  - token-leak
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Unsecured Credentials]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4a4ecbbe-1195-4f88-995d-212f142f748a
created_at: '2025-12-11T03:47:56.765Z'
updated_at: '2025-12-11T03:47:56.765Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1552]]'
---
# Discover Token Leak in reCAPTCHA JS

## Summary

This procedure involves identifying the leakage of sensitive tokens in a JavaScript file used by reCAPTCHA, which can be exploited via cross-site inclusion.

## Description

The vulnerable JavaScript file exposes unique tokens that are used in POST requests for solving CAPTCHA challenges. This information disclosure allows attackers to include the file cross-site and extract tokens without proper protections.

## Requirements

1. Access to web browser developer tools or inspection scripts.

2. Knowledge of the target reCAPTCHA implementation URL.

3. No special credentials needed.

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to prevent cross-site script inclusion.

- Monitor for unusual cross-origin requests to sensitive JS files.

## Objectives

1. Locate and confirm token exposure in JS file.

2. Verify tokens are unique and reusable.

3. Prepare for extraction in subsequent steps.

## Instructions

### Step 1: Inspect JS File

**Context**: Manually or automatically inspect the reCAPTCHA JS file for exposed tokens.

No specific command; use browser tools to view source and search for token variables.

> Expected: Find sensitive tokens in plain view within the JS content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #token-leak
- #information-disclosure
