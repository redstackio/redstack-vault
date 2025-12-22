---
tags:
  - xss
  - payload-injection
  - javascript
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-14T03:15:53.289Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 7b47b3cd-0a43-4388-8d26-8a15577fffe1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Search-Field

## Summary

This procedure involves entering a malicious JavaScript payload into the search input field on smarthistory.khanacademy.org, exploiting improper input sanitization to reflect the code back into the page DOM.

## Description

The search functionality reflects user input without escaping HTML or JavaScript attributes, allowing injection of event handlers like onclick or onfocus. The payload `" onclick="alert(1)"` breaks out of a quoted attribute and injects executable code. This step submits the search, embedding the payload in the response, which can then be triggered. Prerequisites include access to the search page; outcomes enable client-side code execution in the user's session context, risking data theft.

## Requirements

1. Loaded search-results.html page
2. [[tools/Firefox]] with Developer Tools enabled for inspection
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs using libraries like DOMPurify
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for suspicious payloads in search logs

## Objectives

1. Inject unsanitized JavaScript into the search query
2. Confirm reflection in the page response
3. Set up for payload triggering without immediate execution

## Instructions

### Step 1: Enter and Submit Payload

**Context**: Locate the search input and insert the payload to test reflection.

No command required; manual input:

In the search field, type `" onclick="alert(1)"` and click the search button or press Enter to submit.

> The page refreshes with search results, and inspecting the source (Ctrl+U or Developer Tools) shows the payload reflected, e.g., in a value attribute like value="\" onclick=\"alert(1)\""

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- xss
- injection
