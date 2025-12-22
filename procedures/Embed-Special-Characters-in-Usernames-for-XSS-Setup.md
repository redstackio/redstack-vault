---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - xss-setup
  - username-injection
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
updated_at: '2025-12-13T23:52:38.777Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Embed-Special-Characters-in-Usernames-for-XSS-Setup

## Summary

This procedure leverages a prior vulnerability in ok.ru's username creation to embed special characters that can be used to inject script-like content into private messages, setting up the foundation for XSS exploitation.

## Description

In the context of ok.ru, a previous unpatched bug allowed users to create nicknames with special characters, such as numbers and letters that mimic script elements (e.g., '79601920522' or '90177715q'). These usernames are displayed unsanitized in message threads, enabling attackers to chain this with messaging flaws for XSS. The outcome is a persistent setup where username display injects partial payloads, executed when combined with message content.

## Requirements

1. Valid ok.ru account created during the vulnerable period allowing special characters
2. Web browser access to ok.ru
3. Knowledge of special character combinations that evade basic checks

## Defense

Defensive measures and detection strategies:

- Patch username creation to sanitize special characters
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous username patterns in logs

## Objectives

1. Establish usernames with injectable content for message embedding
2. Verify display without sanitization
3. Prepare for payload chaining in subsequent steps

## Instructions

### Step 1: Select or Create Vulnerable Username

**Context**: Identify or use an existing account with special characters from the prior bug.

No command required; in the browser, log in to ok.ru and navigate to profile settings. Confirm username like '79601920522' displays raw special elements.

> Expected: Profile shows unsanitized display, no errors.

### Step 2: Test Username Embedding in Display

**Context**: Verify the username renders script-like content when used in contexts like messages.

In a test message to yourself, include the username. Observe if special characters appear raw in the recipient view.

> Expected: Raw display of characters, enabling payload setup.

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
- [[web-vulnerability]]
