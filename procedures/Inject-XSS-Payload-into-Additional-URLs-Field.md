---
id: p-inject-xss-payload-additional-urls
tags:
  - xss
  - payload-injection
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
updated_at: '2025-12-14T03:16:20.636Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Additional-URLs-Field

## Summary

This procedure involves injecting a crafted JavaScript payload into the Additional URLs field of the Concrete CMS Location dialog, exploiting insufficient input sanitization to enable stored XSS execution upon rendering.

## Description

The Additional URLs field in the Location dialog accepts user input without proper escaping, allowing a payload to break out of the surrounding JavaScript object literal in the renderPagePath function. The specific payload `1',row:1}));alert("xss in path");debugger;(({y:'1` closes the string and object, injects an alert and debugger, confirming execution in the browser context for subsequent users.

## Requirements

1. Open Location dialog for a page.
2. Authenticated session with page edit permissions.
3. Knowledge of JavaScript payload crafting for XSS.

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in JavaScript contexts using libraries like DOMPurify.
- Validate URL formats strictly to reject non-URL strings.

## Objectives

1. Bypass input validation in the URLs field.
2. Craft payload to escape JavaScript context.
3. Set up for payload persistence and execution.

## Instructions

### Step 1: Initiate URL Addition

**Context**: Prepare the input field for payload entry.

Click the 'Add URL' button in the Location dialog.

> A new text input field appears for the additional URL.

### Step 2: Enter Crafted Payload

**Context**: Inject the XSS string to exploit the rendering flaw.

Type the following into the input field: `1',row:1}));alert("xss in path");debugger;(({y:'1`

> The field accepts the input without rejection, as it lacks URL validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- payload-injection
- concrete-cms
