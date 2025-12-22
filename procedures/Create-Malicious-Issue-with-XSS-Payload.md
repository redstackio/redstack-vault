---
tags:
  - xss
  - payload-injection
  - markdown
  - gitlab-issue
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.320Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d54f2407-c5cd-421a-ae07-d05cfdf18a9b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Issue-with-XSS-Payload

## Summary

This procedure demonstrates injecting a stored XSS payload into a GitLab issue's description field using unsanitized Markdown image syntax, storing malicious JavaScript for later execution.

## Description

GitLab renders Markdown in issue descriptions without fully sanitizing HTML attributes in image tags, allowing attackers to inject an 'onload' event handler. The payload `![xss\" onload=alert(1);//](a)` creates an img tag with executable JavaScript. This targets the issue creation form, exploiting the vulnerability discovered in testing with Firefox and Chrome, where the payload executes on the details page view.

## Requirements

1. Authenticated session in a GitLab project with issue creation permissions
2. Web browser supporting JavaScript (Firefox or Chrome recommended)
3. Access to the project's Issues section

## Defense

Defensive measures and detection strategies:

- Implement strict Content Security Policy (CSP) to block inline JavaScript execution
- Sanitize Markdown inputs server-side to strip dangerous attributes like onload
- Monitor issue descriptions for suspicious patterns (e.g., escaped quotes in image syntax) using automated scanners

## Objectives

1. Store XSS payload in a new issue without triggering sanitization
2. Ensure payload persists in the database for viewing by other users
3. Validate injection success before triggering

## Instructions

### Step 1: Navigate to Issues

**Context**: Access the issue management interface in the target project.

From the project dashboard, click 'Issues' in the left sidebar.

> Issues list loads; if empty, proceed to creation.

### Step 2: Open New Issue Form

**Context**: Initiate creation of a vulnerable issue.

Click the 'New issue' button at the top of the issues page.

> Form opens with fields for title and description.

### Step 3: Inject Payload

**Context**: Enter the malicious Markdown in the description to bypass sanitization.

Set title to 'PoC' and description to `![xss\" onload=alert(1);//](a)`. Click 'Submit issue'.

> Issue saves; payload is stored as-is in the description field.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- xss-injection
- gitlab
- markdown-exploit
