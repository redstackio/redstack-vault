---
id: proc-003
tags:
  - xss
  - execution
  - web
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
updated_at: '2025-12-13T23:52:44.503Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Viewing-Comment

## Summary

This procedure demonstrates triggering the stored XSS by loading the comment, causing the injected JavaScript to execute in the viewer's browser context.

## Description

Viewing the blog post renders the stored comment, loading the img tag and firing the onload event to run the JavaScript. This affects any user, including site visitors, but is particularly dangerous for admins. The attack relies on the lack of attribute sanitization, allowing event handlers like onload. Expected outcome is immediate JS execution, confirming the vuln.

## Requirements

1. Malicious comment successfully posted
2. Access to the blog post URL
3. Victim browser without strict XSS protections

## Defense

Defensive measures and detection strategies:

- Implement strict HTML parsing libraries (e.g., DOMPurify)
- Enable XSS Auditor or similar browser protections
- Log and alert on suspicious JS executions in comments

## Objectives

1. Execute the stored payload
2. Verify arbitrary code execution
3. Observe impact like popups or data access

## Instructions

### Step 1: Load the Page

**Context**: Visit the blog to render the comment.

Open the blog post URL in a browser where the malicious comment is visible.

> The img src loads, triggering onload automatically.

### Step 2: Observe Execution

**Context**: Confirm the JS runs.

Look for the alert() popup or inspect console for errors/output.

> In a real scenario, check attacker server for exfiltrated data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[web]]
