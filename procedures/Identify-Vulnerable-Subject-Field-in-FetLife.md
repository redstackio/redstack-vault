---
tags:
  - xss
  - recon
  - angular
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
impact_level: low
detection_risk: low
sub_techniques: []
id: 5c913e03-a850-409b-90f0-5205e7bc0d2a
created_at: '2025-12-13T23:55:20.672Z'
updated_at: '2025-12-13T23:55:20.672Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify Vulnerable Subject Field in FetLife

## Summary

This procedure involves inspecting the private messaging interface on FetLife to identify the Subject field as a vector for stored XSS via Angular expression injection, confirming lack of input sanitization.

## Description

In the context of web application security testing on FetLife, this step focuses on the private conversation feature where user-supplied input in the Subject field is rendered without proper escaping for Angular templates. The procedure requires a valid user account and uses browser tools to analyze the field's handling, revealing that Angular expressions like `{{ }}` are interpreted and executed client-side. Prerequisites include access to the FetLife web app and basic knowledge of Angular. Expected outcomes include confirmation of the vulnerability, setting the stage for payload injection.

## Requirements

1. Valid FetLife account with messaging privileges
2. Modern web browser with developer console (e.g., Chrome DevTools)
3. Network access to FetLife's web application

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side input validation to escape Angular expressions in user inputs
- Use Angular's built-in sanitization (e.g., DomSanitizer) for dynamic content rendering
- Monitor for anomalous JavaScript execution in browser logs or via Content Security Policy (CSP) violations

## Objectives

1. Confirm the Subject field renders user input without sanitization
2. Identify potential for Angular expression execution in recipient views
3. Document the vulnerability location for exploitation planning

## Instructions

### Step 1: Access Private Messaging Interface

**Context**: Log in and navigate to the feature to expose the Subject field for inspection.

Open FetLife in your browser, log in with a test account, and click on the messaging icon to start a new private conversation. Locate the Subject input field in the compose form.

### Step 2: Inspect Rendering with Developer Tools

**Context**: Analyze how the input is processed and rendered to detect sanitization gaps.

Right-click the Subject field and select "Inspect Element." Enter a test Angular expression like `{{7*7}}` and submit a message to a test recipient. On the recipient side, inspect the rendered subject in the conversation list or view, checking if the expression evaluates (e.g., displays "49" instead of literal text).

> If the expression evaluates, the field is vulnerable to injection.

### Step 3: Validate Lack of Escaping

**Context**: Confirm no escaping mechanisms are in place by testing DOM insertion.

Use the browser console on the recipient's view to query the subject's DOM node (e.g., `document.querySelector('.subject-class').innerHTML`) and verify raw input is inserted into an Angular template context.

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
- [[recon]]
- [[angular]]
