---
id: proc-inject-xss-search-title
tags:
  - xss
  - injection
  - concrete-cms
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
updated_at: '2025-12-14T03:15:35.575Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Malicious Payload into Search Title Field

## Summary

This procedure involves entering a malicious JavaScript payload into the Search Title input field of Concrete CMS, exploiting the lack of proper sanitization to prepare for stored XSS execution.

## Description

In Concrete CMS, the Search Title feature allows users to configure search result page titles, but user input is not escaped or validated, permitting HTML and JavaScript injection. This step focuses on crafting and injecting a payload like "><img src=x onerror=alert(1)>", which closes any open tags and triggers script execution on render. The attack targets authenticated users with access to search configuration, setting up persistence for broader impact on unsuspecting viewers.

## Requirements

1. Authenticated access to Concrete CMS admin panel
2. Web browser for manual input
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and HTML escaping (e.g., using htmlspecialchars in PHP)
- Use Content Security Policy (CSP) to restrict inline scripts and img src attributes
- Monitor admin logs for suspicious input patterns like <script> or onerror

## Objectives

1. Bypass input sanitization to embed JavaScript in the title field
2. Prepare payload for persistent storage
3. Validate payload acceptance without immediate errors

## Instructions

### Step 1: Access Search Configuration

**Context**: Log in to the Concrete CMS dashboard and navigate to the search feature settings to locate the title input field.

No command required; use the browser to go to the admin search config page.

> Expected: Search configuration form loads with title input visible.

### Step 2: Enter XSS Payload

**Context**: Input the malicious payload directly into the Search Title field to test for sanitization flaws.

Use the following payload in the title field:

```"><img src=x onerror=alert(1)>
```

> This payload closes a presumed opening tag (e.g., from the form), loads a non-existent image, and executes alert(1) on error. Expected output: Payload accepted and echoed back in the field without stripping.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
