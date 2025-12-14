---
id: proc-inject-xss-branches-001
name: Inject-XSS-Payload-into-Branches-Field
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:16:37.459Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - payload-injection
  - stored-xss
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject-XSS-Payload-into-Branches-Field

## Summary

This procedure injects a JavaScript payload into the optional Branches textfield during Slack's GitHub integration setup, exploiting insufficient sanitization to store malicious code for later execution.

## Description

The Branches field is meant for specifying branch names but accepts arbitrary input without HTML/JS escaping. By closing the input tag and adding an onerror event on an image, the payload breaks out of the context and executes JS when rendered. This stored XSS affects users viewing the integration settings page. Requires prior integration setup steps.

## Requirements

1. Active GitHub integration configuration form in Slack
2. Knowledge of XSS payloads (e.g., img onerror)
3. Browser developer tools for testing (optional)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding or libraries like DOMPurify
- Implement Content Security Policy (CSP) to block inline scripts
- Validate branch names against expected patterns (e.g., regex for alphanumeric)

## Objectives

1. Bypass input validation in the Branches field
2. Store executable JavaScript in the integration config
3. Set up for execution on save and render

## Instructions

### Step 1: Locate Branches Field

**Context**: Identify the vulnerable optional textfield in the form.

Scroll to the 'Branches (optional)' section in the GitHub integration setup.

### Step 2: Enter Payload

**Context**: Insert the XSS payload to inject and execute JS.

Type or paste: `'><img src=x onerror=alert(document.domain);>'` into the field.

> The field accepts the input without rejection, storing it as-is for later rendering.

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
- [[payload-injection]]
- [[stored-xss]]
