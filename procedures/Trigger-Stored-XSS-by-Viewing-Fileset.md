---
id: proc-concrete-trigger-xss-view
tags:
  - stored-xss
  - javascript-execution
  - concrete-cms
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.560Z'
skill_level: basic
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Viewing-Fileset

## Summary

This procedure triggers the execution of a stored XSS payload by navigating to the fileset management page in Concrete CMS 5.7.3, where the unsanitized fileset name renders and executes JavaScript in the authenticated user's browser.

## Description

Once a fileset with an XSS payload is added via CSRF, viewing /dashboard/files/sets causes the backend to output the malicious name without escaping, leading to DOM-based JavaScript execution. The payload demonstrates proof-of-concept with an alert but could be escalated for cookie theft or keylogging. Targets authenticated web sessions in CMS environments.

## Requirements

1. Authenticated session to Concrete CMS 5.7.3
2. Malicious fileset already added from prior procedure
3. Access to /dashboard/files/sets endpoint

## Defense

Defensive measures and detection strategies:

- Output encode all user-controlled data in HTML contexts
- Deploy XSS auditors or WAF rules for script tags/img onerror
- Log and alert on JavaScript errors in browser consoles
- Regular scanning for stored payloads in database

## Objectives

1. Execute arbitrary JavaScript in victim context
2. Demonstrate payload viability (e.g., location disclosure)
3. Enable further attacks like session hijacking

## Instructions

### Step 1: Navigate to Fileset Page

**Context**: Load the page where filesets are listed and names are rendered.

Use browser to visit http://target/conc573/index.php/dashboard/files/sets as an authenticated user.

> Expected: Page loads with fileset list; XSS payload in name triggers immediately.

### Step 2: Observe Execution

**Context**: Verify JavaScript runs via alert or console.

Monitor browser dev tools (Console tab) for errors or alerts. The payload <img src=0 onerror=alert(location)> should pop an alert with the URL.

> Expected: Alert box with current location; potential for more complex payloads.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- stored-xss
- javascript-execution
