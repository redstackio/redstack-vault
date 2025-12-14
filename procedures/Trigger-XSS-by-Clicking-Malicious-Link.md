---
id: proc-uuid-004
name: Trigger-XSS-by-Clicking-Malicious-Link
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.534Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss-execution
  - javascript-trigger
  - drive-by
commands: []
platforms:
  - Web
  - Browser
tools: []
skill_level: beginner
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Trigger-XSS-by-Clicking-Malicious-Link

## Summary

This procedure executes the stored XSS payload by clicking the malicious link in the directory listing, triggering JavaScript in the browser context.

## Description

The vulnerable <a> tag, due to unsanitized output in simplehttpserver.js, allows the javascript: URI to run on click, executing arbitrary JS like an alert or more dangerous actions (e.g., loading external iframes for malware). This targets any user accessing the listing. Prerequisites: Loaded directory page from prior step. Outcomes include confirmed execution, with potential for session hijacking or downloads.

## Requirements

1. Directory listing open in browser
2. No browser extensions blocking JS URIs
3. Victim-like interaction (clicking links)

## Defense

Defensive measures and detection strategies:

- Educate users on avoiding suspicious links in directory listings
- Browser settings to warn on javascript: navigation
- Server-side logging of clicked links or JS errors
- Endpoint protection to detect anomalous JS execution

## Objectives

1. Achieve client-side code execution
2. Demonstrate impact like alerts or resource loading
3. Highlight risks of unsanitized outputs

## Instructions

### Step 1: Interact with the Link

**Context**: Click the rendered link to invoke the JS payload.

**Command** (Browser action):
No command; manual click.

> Locate the malicious file link in the listing and click it. Expected output: Browser executes the JS, showing an alert 'You are pwned!'. For advanced payloads, inspect network tab for iframe loads or downloads.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[javascript-trigger]]
- [[drive-by]]
