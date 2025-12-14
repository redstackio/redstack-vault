---
tags:
  - recon
  - web
  - xss
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 51742b42-a1c5-4985-ada0-31d138f87a05
created_at: '2025-12-13T23:52:50.057Z'
updated_at: '2025-12-13T23:52:50.057Z'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Account-Deletion-Form

## Summary

This procedure involves locating and inspecting the account deletion form on a web application like account.acronis.com to identify potential injection points for XSS payloads.

## Description

In the context of discovering stored XSS vulnerabilities, this step focuses on reconnaissance of user-facing forms that process and store input for administrative review. The target environment is a web application where account management features lack input sanitization. Expected outcomes include mapping form fields and confirming lack of client-side validation, setting up for payload injection.

## Requirements

1. Valid user account on the target site (e.g., account.acronis.com)
2. Web browser with developer tools enabled
3. Basic knowledge of HTML form inspection

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side input validation on all forms
- Use Content Security Policy (CSP) to restrict script execution
- Log and monitor form submissions for anomalous input patterns

## Objectives

1. Locate the account deletion interface
2. Identify unsanitized input fields
3. Prepare for vulnerability testing

## Instructions

### Step 1: Access Account Management

**Context**: Log in to the user portal and navigate to account settings to find the deletion option.

No specific command; use browser navigation:

- Visit account.acronis.com and authenticate.
- Go to profile or settings > Account Deletion.

> This reveals the form structure; inspect elements to note fields like 'reason' or 'comments'.

### Step 2: Inspect Form Fields

**Context**: Use developer tools to analyze input handling.

Open browser console (F12) and examine the form's HTML:

- Look for `<input>` or `<textarea>` tags without `type="hidden"` or sanitization attributes.
- Test basic input to see if it's reflected or stored.

> Successful inspection shows fields accepting JavaScript without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
- [[xss]]
