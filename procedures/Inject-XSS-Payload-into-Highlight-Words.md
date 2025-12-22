---
id: 123e4567-e89b-12d3-a456-426614174002
name: Inject-XSS-Payload-into-Highlight-Words
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:53.315Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - stored-xss
  - payload-injection
  - slack
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: low
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject-XSS-Payload-into-Highlight-Words

## Summary

This procedure details the injection of a stored XSS payload into Slack's highlight words field, exploiting insufficient sanitization to close the textarea and insert executable JavaScript.

## Description

The highlight words feature in Slack's preferences stores user input in a textarea without proper escaping, allowing attackers to inject `</textarea><script>payload</script>`. This results in the script being stored and reflected on page load, executing JavaScript in the user's context. In a self-XSS scenario, it affects only the injector unless shared via social engineering. Prerequisites include an authenticated session on the preferences page.

## Requirements

1. Access to the Slack preferences page from the previous procedure
2. Knowledge of basic HTML/JavaScript for payload crafting
3. Browser developer tools for inspection (optional)

## Defense

Defensive measures and detection strategies:

- Sanitize and encode user input in textareas, preventing tag closure
- Implement server-side validation for highlight words content
- Log and alert on script tag presence in stored preferences

## Objectives

1. Bypass textarea sanitization with tag closure
2. Store malicious script for persistent execution
3. Demonstrate potential for cookie exfiltration

## Instructions

### Step 1: Enter Payload

**Context**: Locate the highlight words textarea and input the crafted payload.

No command; manual input:

- Paste `</textarea><script>prompt(document.cookie);</script>` into the textarea
- Click save or update preferences

> The payload closes the textarea early and injects the script. Saving stores it without validation errors.

### Step 2: Confirm Storage

**Context**: Verify the payload is persisted by checking the field post-save.

Reload the page partially or inspect the stored value.

> If the field shows the payload (possibly broken layout due to tag closure), injection succeeded.

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
- [[payload-injection]]
- [[slack]]
