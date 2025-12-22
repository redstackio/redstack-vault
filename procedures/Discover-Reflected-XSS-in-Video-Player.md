---
id: 123e4567-e89b-12d3-a456-426614174001
name: Discover-Reflected-XSS-in-Video-Player
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.669Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - xss
  - reflected-xss
  - discovery
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Discover-Reflected-XSS-in-Video-Player

## Summary

This procedure outlines the process of identifying a reflected XSS vulnerability in the video player feature of a web application, where user input is directly reflected into the page without proper sanitization, enabling potential JavaScript injection.

## Description

In the context of the Rockstar Games Red Dead Redemption site, the video player accepts user-controlled parameters (e.g., video URLs or search queries) that are echoed back in the HTML response. By inspecting the reflection point using browser tools, attackers can confirm if inputs are sanitized. This vulnerability allows arbitrary JavaScript execution in the browser of users who visit a maliciously crafted link, leading to risks like session hijacking or phishing attacks. Prerequisites include basic knowledge of web vulnerabilities and access to the target site.

## Requirements

1. Web browser with developer console (e.g., Chrome or Firefox)
2. Public access to the target URL: www.rockstargames.com/reddeadredemption
3. Understanding of HTML/JS and common XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict script execution
- Use input validation and output encoding (e.g., HTML entity encoding) on all user inputs
- Monitor for anomalous JavaScript execution via web application firewall logs

## Objectives

1. Confirm reflection of user input without sanitization in the video player
2. Validate potential for XSS payload execution
3. Assess the vulnerability's scope for reporting

## Instructions

### Step 1: Inspect Video Player Inputs

**Context**: Access the video player page and examine how parameters are handled to identify reflection points.

Navigate to www.rockstargames.com/reddeadredemption and interact with the video player. Open developer tools (F12), go to the Network tab, and submit inputs like video search terms. Check the response HTML for direct reflection of the input.

### Step 2: Test Basic XSS Payload

**Context**: Inject a simple payload to verify execution without triggering errors.

In the input field (e.g., video URL parameter), enter `<script>alert('XSS')</script>` and submit. Refresh or replay the request if needed, then check the console for the alert popup.

> If the alert triggers, the input is unsanitized, confirming the reflected XSS.

### Step 3: Analyze Reflection Point

**Context**: Determine the exact location and context of the reflection to understand exploit potential.

View page source (Ctrl+U) or Elements tab in dev tools to locate where the input appears (e.g., in a src attribute or innerHTML). Note if it's in a JavaScript context, which would allow code execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[Discovery]]
