---
id: proc-003
tags:
  - xss
  - execution
  - browser
type: procedure
tools:
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.754Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Directory-Listing

## Summary

This procedure accesses the vulnerable directory listing in a web browser, causing the stored XSS payload in the malicious filename to execute arbitrary JavaScript in the viewer's context.

## Description

Upon navigating to the server's root URL (http://127.0.0.1:6060/), the 'public' module generates an HTML directory index without escaping filenames. The injected payload '"><svg onload=alert(3);' closes the <a> tag prematurely and inserts an <svg> element that triggers on load, executing the alert. This demonstrates the impact: arbitrary JS execution, which could be escalated to steal sessions, keystrokes, or redirect users.

## Requirements

1. Server running on port 6060 with malicious file in root
2. Web browser (e.g., Chrome) with JavaScript enabled
3. Local network access to the server
4. No ad-blockers interfering with SVG execution

## Defense

Defensive measures and detection strategies:

- Implement strict HTML entity encoding for all user-controlled data in outputs
- Use modern servers with built-in XSS protections (e.g., Express.js with helmet)
- Monitor browser console for unexpected script executions
- Educate users on avoiding untrusted directory listings

## Objectives

1. Load the directory index to render the payload
2. Confirm JS execution via alert or console
3. Assess potential for further exploitation

## Instructions

### Step 1: Access the Directory

**Context**: Open the browser to the server's root, triggering the vulnerable HTML generation and payload execution.

**Command** (No CLI command; browser action):
Navigate to `http://127.0.0.1:6060/` in [[tools/Chrome]].

> The page loads the directory listing. The malicious filename injects the SVG, firing onload=alert(3). Expected output: Alert dialog with '3'; inspect source to see broken <a> tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]

## Tags

- xss-trigger
- browser-execution
