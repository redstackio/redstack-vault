---
tags:
  - xss
  - stored-xss
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:22.120Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 32ed53c5-91c9-4c69-ac81-22ab989b4594
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# View-Vulnerable-User-Profile-for-XSS

## Summary

This procedure details the identification and viewing of a user profile on Judge.me containing a stored XSS payload in the bio, triggering JavaScript execution in the attacker's browser to demonstrate the vulnerability.

## Description

Judge.me's profile pages, accessible via /reviews/users/... endpoints, fail to sanitize user-submitted bios, allowing stored XSS. By viewing a profile like 'HackerTwo' with an injected payload such as <script>alert(1)</scrip, arbitrary JavaScript executes in the context of the viewer's session. This can lead to cookie theft, session hijacking, or phishing. The procedure assumes prior access to the Discover People page and uses manual browser navigation.

## Requirements

1. Access to the Discover People page from the previous procedure
2. Web browser capable of executing JavaScript
3. Knowledge of the vulnerable profile slug (e.g., 'HackerTwo')

## Defense

Defensive measures and detection strategies:

- Escape HTML entities in user bios before rendering
- Use DOMPurify or similar libraries for client-side sanitization
- Log and alert on script tag detections in user inputs

## Objectives

1. Locate and access the injected profile to trigger XSS
2. Observe JavaScript execution confirming the vulnerability
3. Assess impact on viewer sessions

## Instructions

### Step 1: Locate the Vulnerable Profile

**Context**: From the Discover People page, identify the profile with potential injection.

Search or scroll to find the 'HackerTwo' profile in the list.

> The profile name indicates testing for vulnerabilities; bios may show suspicious content.

### Step 2: Navigate to Profile Details

**Context**: Click into the profile to render the full bio and trigger the payload.

Click on the 'HackerTwo' profile link, leading to a URL like https://judge.me/reviews/users/protocol_subdomain_rootdomain_tld_slug_articlepermalink.

> The bio section renders the payload <script>alert(1)</scrip, executing an alert if vulnerable.

### Step 3: Validate Execution

**Context**: Confirm XSS by checking for payload effects.

Inspect the page source or observe pop-ups/behavior changes in the browser.

> An alert box or console errors indicate successful JavaScript injection and execution.

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
- [[stored-xss]]

