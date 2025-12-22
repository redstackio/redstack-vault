---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - xss
  - execution-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-05T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.300Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-WordPress-Themes-Page

## Summary

This procedure triggers the stored XSS by navigating to the WordPress admin themes page, where the malicious folder name is reflected and executed as JavaScript in the browser context.

## Description

The wp-admin/themes.php page scans for themes and displays broken ones with their folder names in error messages. Without proper escaping, the payload executes when an admin (including the attacker) views the page, demonstrating the self-XSS nature in a privileged context.

## Requirements

1. Authenticated session in WordPress admin
2. Malicious broken theme folder present
3. Browser without XSS protections disabled

## Defense

Defensive measures and detection strategies:

- Patch WordPress core to encode theme names (e.g., via esc_html() in templates)
- Use Content Security Policy (CSP) to block inline scripts in admin
- Monitor browser console for unexpected JS errors or alerts

## Objectives

1. Execute the stored payload in admin browser
2. Confirm vulnerability impact
3. Highlight self-XSS limitations

## Instructions

### Step 1: Access Themes Page

**Context**: Load the vulnerable view.

Log in to /wp-admin/ and go to Appearance > Themes.

### Step 2: Observe Execution

**Context**: Trigger the reflection.

The page lists themes; broken ones show the folder name, firing the onerror alert.

> Verify in browser dev tools: JS executes in wp-admin domain.

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
- execution-trigger
