---
id: proc-uuid-placeholder-001
tags:
  - web
  - javascript
  - credential-exposure
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
  - '[[Software]]'
updated_at: '2025-12-14T17:31:11.014Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[Software]]'
---
# Inspect-Client-Side-JavaScript-for-Exposed-Passcode

## Summary

This procedure involves manually inspecting the source code of a web page to identify exposed credentials, such as plain text passcodes stored in client-side JavaScript variables. It is particularly useful for discovering improper authentication in non-critical features like Easter eggs, as seen on bonjour.uber.com, where the passcode 'abcde' enables triggering a test error without guessing or authentication.

## Description

In web applications, sensitive data like authentication passcodes should never be stored in plain text on the client side, as it is accessible to anyone via browser tools. This procedure targets public-facing web pages, using built-in browser features to view and analyze JavaScript code. The attack scenario applies to reconnaissance phases, where attackers scan for low-hanging fruit like exposed variables. Prerequisites include basic web browsing knowledge; no advanced tools are needed. Expected outcomes include extraction of credentials and validation of their functionality, though impact is typically low for non-production features.

## Requirements

1. Web browser with source viewing capability (e.g., Chrome, Firefox)
2. Public access to the target URL (e.g., bonjour.uber.com)
3. Basic understanding of HTML/JavaScript structure

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove unnecessary client-side credentials; store sensitive data server-side only.
- Implement Content Security Policy (CSP) to restrict script execution and source inspection impacts.
- Monitor for anomalous browser interactions or error triggers like 'sentry test' in logs.

## Objectives

1. Extract plain text passcodes from JavaScript source.
2. Validate the passcode by triggering associated functionality (e.g., error simulation).
3. Assess the vulnerability's scope and report it informatively.

## Instructions

### Step 1: Access the Target Page

**Context**: Load the target web page to prepare for source inspection.

Navigate to the URL (e.g., bonjour.uber.com) using a web browser.

**Expected Output**: The page loads normally, displaying the Easter egg feature interface.

### Step 2: View Page Source

**Context**: Examine the raw HTML and embedded JavaScript to locate exposed variables.

Right-click on the page and select 'View Page Source' (or use keyboard shortcut Ctrl+U). Scroll through the document to the JavaScript section, typically in <script> tags or external files referenced inline.

**Expected Output**: Full source code visible, including JavaScript variables like the passcode 'abcde' defined as a string (e.g., var passcode = 'abcde';) and event listeners (e.g., keypress checks to match the code and throw new Error('sentry test')).

### Step 3: Extract and Validate Passcode

**Context**: Copy the identified passcode and test its functionality to confirm exposure.

Note the passcode value. To validate, open the browser console (F12 > Console tab) and simulate keypresses or directly execute the event logic if visible.

**Expected Output**: Successful match triggers the 'sentry test' error in the console, confirming the passcode works without authentication.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery
- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Credentials In Files]] Credentials In Files
- [[Software]] Software

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- javascript
- credential-exposure
- reconnaissance
