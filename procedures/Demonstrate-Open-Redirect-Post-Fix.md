---
id: uuid-open-redirect
tags:
  - open-redirect
  - phishing
  - bypass
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:26:36.791Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate-Open-Redirect-Post-Fix

## Summary

This procedure demonstrates the open redirect vulnerability that persists even after adding try/catch to handle DoS, by using crafted relative URLs starting with '//' that resolve to arbitrary external sites per URL spec behavior.

## Description

After mitigating the crash with try/catch, the redirect logic still allows '//a//youtube.com/%2e%2e%2f%2e%2e' to bypass base URL restrictions. The URL API treats '//' as protocol-relative, enabling redirects to sites like YouTube without proper validation or slash counting.

## Requirements

1. Fastify server restarted with try/catch around URL constructor.
2. Web browser (Chrome, Firefox, etc.) for navigation.
3. Local server on port 3000.

## Defense

Defensive measures and detection strategies:

- Strictly validate redirect targets against a whitelist of allowed domains.
- Count and normalize slashes in paths to prevent relative URL tricks.
- Implement Content Security Policy (CSP) to block unauthorized redirects.
- Log all redirect attempts and monitor for external domain patterns.

## Objectives

1. Redirect users to arbitrary external sites for phishing.
2. Bypass any naive mitigations like try/catch.
3. Verify cross-browser consistency.

## Instructions

### Step 1: Prepare Mitigated Server

**Context**: Add try/catch to index.js line 439 to prevent crashes, then restart using [[commands/bash-run-sh]].

**Command**:
```bash
# Edit code to include try/catch, then
bash run.sh
```

> Ensure server starts without crashing on valid requests.

### Step 2: Navigate to Crafted URL

**Context**: Use a browser to access the malicious path, exploiting URL resolution.

**Instructions**: Open [[tools/Web-Browser]] and enter: http://localhost:3000//a//youtube.com/%2e%2e%2f%2e%2e

> The path resolves relative to the base but bypasses to https://www.youtube.com/.. due to '//' handling. Expected: Redirect to YouTube.

### Step 3: Verify Across Browsers

**Context**: Test in multiple browsers to confirm universal exploitability.

**Instructions**: Repeat in Firefox, Safari, Opera, Edge.

> Success if all redirect as expected.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- open-redirect
- phishing
- bypass
