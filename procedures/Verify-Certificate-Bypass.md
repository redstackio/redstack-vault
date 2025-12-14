---
id: proc-uuid-004
tags:
  - verification
  - bypass-confirm
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Internet-Explorer]]'
  - '[[tools/Microsoft-Edge]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Windows
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:28:12.457Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Verify-Certificate-Bypass

## Summary

Reload the target site to confirm the certificate override has been applied, allowing insecure connections to proceed without warnings.

## Description

Post-clickjacking, the browser treats the mismatched certificate as trusted for the session, loading content from the redirected IP. This validates the full bypass, demonstrating potential for session hijacking or data exfiltration.

## Requirements

1. Successful override from previous steps
2. Same browser session active
3. Kaspersky installed but bypassed

## Defense

Defensive measures and detection strategies:

- Enforce per-session certificate revalidation
- Monitor for unusual overrides in security logs
- Use HSTS to prevent downgrade to insecure loads

## Objectives

1. Confirm no recurring warnings on reload
2. Validate secure connection to attacker IP
3. Assess impact on other Kaspersky features

## Instructions

### Step 1: Reload Target URL

**Context**: Test if the bypass persists.

**Instructions**: In the same browser, navigate again to https://www.google.com/.

> Site should load without interception.

### Step 2: Check Content Load

**Context**: Verify resolution to redirected IP.

**Instructions**: Observe the page content (e.g., example.com's 'Not Found' instead of Google).

> Indicates successful hijack; check browser dev tools for connection details.

### Step 3: Test Extended Impact

**Context**: Optionally verify on Safe Money or phishing pages.

**Instructions**: Repeat with banking site redirection to confirm disablement.

> Warnings bypassed, exposing financial data.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Internet-Explorer]]
- [[tools/Microsoft-Edge]]

## Tags

- verification
- bypass-confirm
