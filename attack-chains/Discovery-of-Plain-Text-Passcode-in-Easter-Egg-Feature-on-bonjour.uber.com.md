---
id: ac-uuid-placeholder-001
tags:
  - web
  - javascript
  - authentication-bypass
  - credential-exposure
  - easter-egg
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inspect-Client-Side-JavaScript-for-Exposed-Passcode]]'
step_count: 1
techniques:
  - '[[Credentials In Files]]'
  - '[[Software]]'
updated_at: '2025-12-14T17:31:11.018Z'
description: >-
  A reconnaissance-focused chain demonstrating the discovery of an improper
  authentication vulnerability in a client-side Easter egg feature by inspecting
  JavaScript source code.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[Software]]'
---
# Discovery of Plain Text Passcode in Easter Egg Feature on bonjour.uber.com

## Overview

This attack chain outlines a simple reconnaissance technique to identify an improper authentication vulnerability in the Easter egg feature of bonjour.uber.com. The passcode 'abcde' is stored in plain text within client-side JavaScript, allowing anyone to view the source code and extract it without authentication. This enables triggering a 'sentry test' error but has minimal impact as it affects only a non-critical, non-functional feature. The chain is informative and demonstrates basic web vulnerability discovery.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Inspect Source Code] --> B[Discovery: Extract Passcode]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox) with developer tools

### Target Environment

- Web platform
- Publicly accessible URL: bonjour.uber.com
- No specific services or ports required beyond standard HTTP/HTTPS (port 80/443)

### Initial Access Requirements

- Internet access
- No credentials or prior access needed; the site is public-facing

## Detailed Attack Procedures

### Step 1: Source Code Inspection
procedure: [[procedures/Inspect-Client-Side-JavaScript-for-Exposed-Passcode]]

**Objective**: Analyze the page source to identify and extract the plain text passcode used in the Easter egg feature.

**Instructions**: Navigate to bonjour.uber.com in a web browser. Right-click on the page and select 'View Page Source' (or use Ctrl+U on Windows/Linux, Cmd+Option+U on macOS). Scroll down to locate the JavaScript code section containing the passcode variable and the keypress event listener. The passcode 'abcde' will be visible as a plain text string, along with logic to check keypresses and trigger a 'sentry test' error upon match.

**Expected Output**: Visible JavaScript variables and functions in the source code, including the passcode 'abcde' and event listener code.

**Success Indicators**:
- Passcode 'abcde' identified in source
- Keypress event listener logic confirmed
- Ability to manually trigger the Easter egg by entering the passcode in the browser console or via keyboard simulation

## Attack Chain Summary

### Key Achievements

1. Successful extraction of the plain text passcode from client-side JavaScript.
2. Understanding of the Easter egg mechanism, including the 'sentry test' error trigger.
3. Confirmation of minimal impact, suitable for informative reporting.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Credentials In Files]] Credentials In Files
- [[Software]] Software

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
