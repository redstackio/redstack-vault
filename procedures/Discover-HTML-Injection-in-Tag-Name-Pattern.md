---
tags:
  - xss
  - html-injection
  - discovery
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - GitHub Enterprise Server
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.396Z'
sub_techniques: []
id: 79e32c8e-1ecc-487a-9bec-6f0d4a2145bf
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Discover HTML Injection in Tag Name Pattern

## Summary

This procedure identifies an HTML injection vulnerability in GitHub's tag protection settings by testing the tag name pattern field, where error responses from the check_pattern endpoint are unsafely inserted into the DOM.

## Description

In the attack scenario, an authenticated user navigates to the repository's tag protection new page. Entering invalid patterns triggers an AJAX call to the check_pattern endpoint, whose error message is injected via innerHTML without sanitization, allowing arbitrary HTML execution. This is a self-XSS variant requiring user action but can be weaponized via social engineering. Expected outcomes include confirmed injection leading to JavaScript execution in the GitHub domain context.

## Requirements

1. Authenticated GitHub session with repository access
2. Browser with developer tools enabled
3. No external dependencies; uses GitHub's web interface

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before DOM insertion, using textContent instead of innerHTML
- Implement strict CSP policies blocking inline scripts
- Monitor for anomalous JavaScript execution in admin panels via browser security logs

## Objectives

1. Confirm unsanitized error response injection
2. Validate HTML rendering in the DOM
3. Establish foundation for self-XSS exploitation

## Instructions

### Step 1: Navigate to Target Page

**Context**: Access the vulnerable settings page to prepare for testing.

Navigate to `/<username>/<reponame>/settings/tag_protection/new` in your browser.

> Ensure you are logged in and have edit permissions on the repository.

### Step 2: Test Injection Point

**Context**: Trigger the check_pattern endpoint with a malicious payload to observe DOM insertion.

Enter a payload such as `<b>Injected</b><script>alert('XSS')</script>` in the tag name pattern field and submit or blur the field to trigger validation.

> Open developer console (F12) to inspect the network request to check_pattern and the resulting DOM changes. Look for the error div where innerHTML is set to the raw response.

### Step 3: Verify Execution

**Context**: Confirm the injection leads to executable HTML/JS.

If the alert fires or HTML renders (e.g., bold text), the vulnerability is confirmed.

> Check the console for any errors; successful injection shows no sanitization artifacts.

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
- [[html-injection]]
