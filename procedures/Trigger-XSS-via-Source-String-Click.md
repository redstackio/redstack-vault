---
tags:
  - xss
  - trigger
  - self-xss
  - weblate
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.093Z'
sub_techniques: []
id: 69e10a73-8cf2-421f-812b-b77ed6478f58
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS via Source String Click

## Summary

This procedure triggers the stored self-XSS by clicking a source string location in Weblate's translation interface, causing the JavaScript payload from the Editor Link to execute in the user's browser.

## Description

Weblate constructs navigation links to source files using the user's Editor Link preference. When a source location like 'main.c' is clicked, the javascript: URI is invoked, executing the payload in the context of the authenticated session. This results in self-XSS effects, such as running arbitrary JS, but confined to the user's own actions.

## Requirements

1. Payload injected and saved in Editor Link
2. Translation page loaded with source strings
3. Interactive browser session

## Defense

Defensive measures and detection strategies:

- Escape or validate link constructions to prevent scheme execution
- Implement Content Security Policy (CSP) to block inline JavaScript
- Detect and alert on javascript: scheme usage in logs

## Objectives

1. Retrieve and execute the stored payload
2. Confirm JavaScript runs in Weblate context
3. Demonstrate self-XSS impact

## Instructions

### Step 1: Identify Source Location

**Context**: Locate a clickable element that uses the Editor Link for navigation.

On the translation page, find a source string's file location, such as 'main.c'.

> These are typically hyperlinks or buttons leading to the source code view.

### Step 2: Click to Execute

**Context**: Interact with the link to invoke the payload.

Click the source string location (e.g., 'main.c').

> The browser executes the javascript: payload, showing a confirm dialog with the domain (e.g., demo.weblate.org), confirming successful XSS.

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
- trigger
- self-xss
- clickjacking
