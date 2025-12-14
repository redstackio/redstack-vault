---
id: proc-uuid-3
tags:
  - source-inspection
  - access-control-bypass
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.671Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-HTML-Source-for-Exposed-Paths

## Summary

This procedure uses browser developer tools to examine the HTML source of a web page, identifying exposed administrative paths like WordPress's '../wp-admin/admin-ajax.html', which indicate improper access controls and potential for unauthorized administrative functions.

## Description

Web applications often leak sensitive paths in client-side code due to misconfigurations. On the MTN NIN site, the status page's source reveals the default WordPress admin AJAX endpoint, allowing attackers to infer the backend structure. This can lead to high-impact outcomes such as viewing sensitive data, stealing customer details, or installing backdoors. The technique relies on standard browser tools, requiring no advanced skills, but the discovery enables further exploitation.

## Requirements

1. Loaded target page in a browser with dev tools enabled
2. Basic familiarity with HTML inspection
3. No server-side access or tools

## Defense

Defensive measures and detection strategies:

- Remove or rename default admin paths in production
- Minify and obfuscate client-side code to hide endpoints
- Implement access controls on admin directories and log inspection attempts indirectly via analytics

## Objectives

1. Uncover misconfigured paths in HTML source
2. Assess potential for unauthorized access
3. Rate vulnerability severity based on exposure (high: 7.9)

## Instructions

### Step 1: Open Developer Tools

**Context**: Access the inspection interface to view raw HTML.

Right-click the MTN yellow bar at the top and select 'Inspect', or use keyboard shortcut (F12 or Ctrl+Shift+I).

> Dev tools panel opens with Elements tab active, showing the DOM tree.

### Step 2: Search for Exposed Paths

**Context**: Scan the source for indicators of admin exposure.

In the Elements tab, use Ctrl+F to search for 'wp-admin' or 'admin-ajax'.

> Expected: Discovery of '../wp-admin/admin-ajax.html' in script tags or attributes, confirming the vulnerability.

### Step 3: Validate Exposure

**Context**: Confirm the path leads to accessible admin functions.

Note the path and attempt direct navigation if possible (e.g., append to base URL).

> Successful validation shows potential for admin access without auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- source-inspection
- access-control-bypass
- wordpress
