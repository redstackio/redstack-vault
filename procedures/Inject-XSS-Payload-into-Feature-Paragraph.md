---
id: proc-inject-xss-payload-feature-paragraph
tags:
  - xss
  - stored-xss
  - javascript
  - concrete-cms
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
updated_at: '2025-12-14T03:15:35.539Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Feature-Paragraph

## Summary

This procedure details the injection of a malicious JavaScript payload into the Feature Paragraph input field of Concrete CMS, exploiting poor sanitization to store executable code for later execution.

## Description

The Feature Paragraph feature in Concrete CMS fails to escape user-supplied HTML attributes and tags, allowing attackers to inject scripts that persist in the database and execute in the context of any user viewing the page. This procedure uses a simple onerror handler payload to demonstrate the vulnerability. Prerequisites include access to the input field from the prior procedure. Outcomes include successful storage of the payload, enabling attacks such as session hijacking or phishing when the page is rendered.

## Requirements

1. Access to the Feature Paragraph input field via authenticated editing session
2. Knowledge of basic HTML/JavaScript for crafting payloads
3. Web browser developer tools for testing (optional)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs using HTML entity encoding on output
- Use libraries like DOMPurify for client-side cleaning
- Implement web application firewall (WAF) rules to block common XSS patterns

## Objectives

1. Bypass input validation to insert executable JavaScript
2. Ensure the payload closes HTML context properly for execution
3. Store the malicious code persistently in the CMS database

## Instructions

### Step 1: Prepare the Payload

**Context**: Craft a payload that evades basic filtering and triggers on render.

Use the payload `"><img src=x onerror=alert(1)>` to close any enclosing quotes/attributes and inject a script via an invalid image source.

> This payload is short and effective for proof-of-concept, alerting '1' on execution.

### Step 2: Enter Payload into Input Field

**Context**: Insert the payload directly into the vulnerable text field.

Paste the payload into the Feature Paragraph input and ensure it is accepted without truncation or error.

> The field accepts the input, displaying the raw HTML without rendering it immediately.

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
- [[JavaScript]]
- [[concrete-cms]]
