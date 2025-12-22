---
tags:
  - xss
  - stored-xss
  - crowdsignal
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f4c21f41-7d91-442d-9089-0c9d4b8a84e8
created_at: '2025-12-13T23:52:49.686Z'
updated_at: '2025-12-13T23:52:49.686Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Poll-in-Crowdsignal

## Summary

This procedure involves creating a poll in the Crowdsignal dashboard with a malicious JavaScript payload embedded in an answer field, exploiting insufficient sanitization to store XSS for later execution when embedded elsewhere.

## Description

Crowdsignal, a polling service integrated with WordPress, fails to properly escape user input in poll answers, allowing HTML and JavaScript attributes to be injected. The attacker navigates to the dashboard, sets up a basic poll question, and inserts a payload like an onmouseover event in an answer option. This payload remains dormant until the poll is viewed and interacted with in a browser context, such as hovering over results. Prerequisites include a free Crowdsignal account; the procedure targets web-based poll creation and assumes no authentication bypass is needed.

## Requirements

1. Active Crowdsignal account with dashboard access
2. Web browser for navigation and input
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output escaping for all user-supplied content in poll fields
- Use Content Security Policy (CSP) to restrict inline JavaScript execution
- Monitor for unusual poll creation patterns or embedded scripts via logging

## Objectives

1. Store malicious JavaScript in a poll answer without immediate execution
2. Generate a shareable link for embedding in external sites like WordPress
3. Prepare for victim-side triggering to collect browser data

## Instructions

### Step 1: Access Crowdsignal Dashboard

**Context**: Log in to initiate poll creation.

Navigate to https://app.crowdsignal.com/dashboard and click to create a new poll.

### Step 2: Configure Poll with Malicious Payload

**Context**: Set up the poll question and inject the payload in an answer.

Enter a neutral question like "What is your favorite color?" and in one answer field, input the payload: `style="position:fixed;top:0;left:0;border:999em solid green;" onmouseover="alert(document.cookie)"`. This uses a CSS style for visual distraction and onmouseover to trigger the alert with cookies.

### Step 3: Save and Share Poll

**Context**: Finalize the poll and obtain the embed link.

Complete poll setup, save it, then go to the 'Share Your Poll' section to copy the generated shareable link.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[crowdsignal]]
- [[payload-injection]]
