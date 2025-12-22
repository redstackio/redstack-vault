---
tags:
  - xss
  - injection
  - gitlab
type: procedure
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
updated_at: '2025-12-14T03:16:20.330Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a0c78965-d427-4ba9-bc37-cc17bacb7f67
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Username-for-Stored-XSS-in-GitLab

## Summary

This procedure involves setting a GitLab user's username to a malicious string containing an HTML/JavaScript payload, such as an <img> tag with an onerror event, to store the payload for later execution in vulnerable UI components like the project deletion modal.

## Description

In vulnerable GitLab versions (<10.7), the username is stored and rendered without proper escaping in certain modals using jQuery's .html() method, allowing HTML interpretation and JavaScript execution. This stored XSS targets users with Master access viewing the affected project details. The attack requires authenticated access to edit the profile but can impact other users when they interact with the project. Expected outcomes include alert popups or more severe actions like cookie theft if escalated.

## Requirements

1. Valid GitLab account with profile edit permissions
2. Web browser for navigation and payload testing
3. Knowledge of basic JavaScript payloads for XSS

## Defense

Defensive measures and detection strategies:

- Enable Content Security Policy (CSP) to block inline scripts
- Sanitize and escape user inputs in all UI renders, preferring .text() over .html()
- Monitor for anomalous username changes via audit logs
- Use web application firewalls (WAF) to detect XSS payloads in profile updates

## Objectives

1. Store a JavaScript-executable payload in the username field
2. Prepare for rendering in project-related UI
3. Achieve execution in victim browsers without direct interaction

## Instructions

### Step 1: Navigate to User Profile Settings

**Context**: Access the username edit field to inject the payload.

Log in to GitLab and click the profile avatar > Edit Profile.

**Expected Output**: Profile settings page loads with editable fields.

### Step 2: Update Username with Payload

**Context**: Enter the malicious string that includes an HTML element triggering JavaScript on error.

In the Username field, enter: `<img src=x onerror=alert(document.domain)> foo / bar`

Save the changes.

**Expected Output**: Success message confirming username update; payload stored but not executed yet.

### Step 3: Verify Storage

**Context**: Confirm the payload is saved without immediate execution.

View the updated profile or any page rendering the username to ensure it's displayed as text.

**Expected Output**: Malicious string visible in username display.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[xss]]
- [[stored-xss]]
- [[gitlab]]
