---
tags:
  - verification
  - xss
  - web
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: abff9362-29a4-4aa6-8b3f-512e1f4d5927
created_at: '2025-12-14T03:16:37.185Z'
updated_at: '2025-12-14T03:16:37.185Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Normal-Template-Rendering

## Summary

This procedure tests the application's rendering of benign inputs to confirm proper HTML escaping for standard characters, establishing a baseline before attempting malicious payloads.

## Description

Using a web browser, access the local server with a safe parameter like 'name=bl4de' to observe how bracket-template handles interpolation. The module should escape HTML entities, rendering the output as plain text. This step validates the setup and highlights the vulnerability's specificity to hex escapes. Target environment is localhost:8080; no credentials required.

## Requirements

1. Running Node.js server from prior setup
2. Web browser with developer tools
3. Localhost access

## Defense

Defensive measures and detection strategies:

- Log all template compilations and inputs for anomaly detection
- Use static analysis tools to scan for unsafe interpolation patterns
- Enforce input validation at the application layer

## Objectives

1. Confirm functional template rendering
2. Verify escaping for common characters
3. Identify safe vs. vulnerable input patterns

## Instructions

### Step 1: Access with Benign Input

**Context**: Load the endpoint with a normal query parameter to check output.

**Command** (Browser URL access):

Navigate to http://localhost:8080?name=bl4de in [[tools/Browser]].

> The page should display '<strong>Hello bl4de</strong>' with 'bl4de' as escaped text. Inspect the HTML source to confirm no unescaped tags.

### Step 2: Inspect Output

**Context**: Use browser dev tools to validate rendering.

**Command** (No CLI; browser action):

Open console and elements inspector.

> Expected: No JS execution; input treated as text. Success if output matches expected escaped HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- verification
- xss
- web
