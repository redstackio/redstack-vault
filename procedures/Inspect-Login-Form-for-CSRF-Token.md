---
id: proc-uuid-001
tags:
  - csrf
  - web-inspection
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:03.595Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Inspect-Login-Form-for-CSRF-Token

## Summary

This procedure involves manually inspecting the HTML source of a web login form to check for the presence of CSRF protection tokens, which are essential for preventing cross-site request forgery attacks where malicious sites could trick users into unintended actions.

## Description

In web applications like Nextcloud, login forms should include unique CSRF tokens to validate that form submissions originate from the legitimate page. This procedure targets public-facing login endpoints, such as https://portal.nextcloud.com/login.php, to reveal if such protections are absent, potentially allowing attackers to craft malicious links or forms that submit credentials on behalf of users. The process requires only browser access and is a foundational reconnaissance step before attempting exploits.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Public URL access to the target login page
3. Basic knowledge of HTML form structures

## Defense

Defensive measures and detection strategies:

- Implement server-side CSRF token generation and validation on all state-changing forms
- Use Content Security Policy (CSP) headers to restrict form submissions
- Monitor for anomalous login attempts from unusual referer headers

## Objectives

1. Confirm absence of CSRF token fields in the login form
2. Document form submission details for further testing
3. Assess potential for CSRF-based credential submission attacks

## Instructions

### Step 1: Access and View Page Source

**Context**: Load the target login page and inspect its raw HTML to locate the form element.

No specific command required; use browser right-click > "View Page Source" or press Ctrl+U (Windows) / Cmd+U (Mac).

> Look for the <form> tag submitting to the login endpoint. In the Nextcloud case, the form includes fields like member_username and member_password but lacks any CSRF-related input.

### Step 2: Analyze Form Fields

**Context**: Search the HTML for token indicators to verify protection status.

Use browser search (Ctrl+F) for terms like "csrf", "token", or "_token".

> Expected finding: No hidden input fields for CSRF tokens, indicating potential vulnerability to forged requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-recon]]
