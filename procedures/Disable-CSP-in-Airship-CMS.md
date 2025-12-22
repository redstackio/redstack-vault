---
id: proc-uuid-1
tags:
  - csp-bypass
  - airship-cms
  - configuration
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
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T03:15:47.048Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Disable-CSP-in-Airship-CMS

## Summary

This procedure disables the Content Security Policy (CSP) in Airship CMS v2.0.0 to allow unsafe inline JavaScript, enabling subsequent XSS exploitation by removing restrictions on script execution.

## Description

Airship CMS includes a configurable CSP in its admin settings. By accessing the bridge admin panel and enabling 'allow unsafe inline' under JavaScript settings, attackers with admin access can weaken security controls. This is a prerequisite for exploiting reflected or stored XSS payloads that rely on inline event handlers. The target environment is a web-based CMS with default anonymous comment features, and outcomes include unblocked JavaScript execution across the application.

## Requirements

1. Administrative credentials or session to access /bridge/admin/settings
2. Network access to the Airship CMS instance
3. Web browser for navigation and form submission

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP policies with no unsafe-inline allowances
- Monitor admin panel access logs for unauthorized changes to security settings
- Use role-based access control to limit CSP modifications to trusted admins

## Objectives

1. Remove CSP restrictions to permit inline JavaScript
2. Prepare the environment for XSS payload execution
3. Increase exploit success rate without policy violations

## Instructions

### Step 1: Access Admin Panel

**Context**: Log in and navigate to the settings page to reach CSP controls.

Navigate to `/bridge/admin/settings` in your browser after authenticating as an admin.

> Locate the JavaScript section and check the 'allow unsafe inline' option under CSP settings. Save changes.

### Step 2: Verify CSP Disablement

**Context**: Confirm the policy update to ensure inline scripts are permitted.

Open browser developer tools (F12), inspect network requests to the site, and check response headers for CSP directives. Test with a simple inline script like `<script>alert('test')</script>` on a test page.

> Expected: No CSP violation errors in console; script executes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Disable or Modify Tools]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csp-bypass]]
- [[airship-cms]]
