---
id: proc-uuid-15125-step1
tags:
  - xss
  - code-review
  - javascript
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:36.058Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Analyze JavaScript for XSS Vulnerabilities

## Summary

This procedure involves inspecting client-side JavaScript code to identify reflected XSS opportunities, specifically targeting parameter handling in web players like Twitter's Amplify, where values are inserted into HTML without sanitization.

## Description

In the context of the Twitter Amplify web player, load the source.html endpoint and examine the minified JavaScript file (amplify-web-player.min.js). Look for parameters like 'image_src' that are directly concatenated into DOM elements, such as img src attributes, allowing data URI-based JS injection. This targets public-facing web applications vulnerable to client-side injection, with outcomes including identification of exploitable sinks for further payload crafting.

## Requirements

1. Web browser with developer tools
2. Access to the target URL: https://amp.twimg.com/amplify-web-player/prod/source.html
3. Basic knowledge of JavaScript and DOM manipulation

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to block inline scripts and data URIs
- Sanitize all user inputs before insertion into HTML attributes
- Use static analysis tools like ESLint with security plugins to flag unsafe concatenations

## Objectives

1. Locate vulnerable parameter handling in JS code
2. Confirm lack of escaping for HTML attributes
3. Prepare for payload injection based on findings

## Instructions

### Step 1: Load and Inspect the Target Page

**Context**: Access the web player endpoint to retrieve and analyze the associated JavaScript.

Open the URL https://amp.twimg.com/amplify-web-player/prod/source.html in a browser. Use developer tools (F12) to view the Network tab and identify amplify-web-player.min.js.

> Download or view the JS file contents.

### Step 2: Search for Parameter Usage

**Context**: Review code for unsafe handling of query parameters.

In the JS file, search for 'image_src'. Note assignment to variable 'h' and direct use in document.createElement('img').setAttribute('src', h) without validation.

> Expected: Identification of concatenation vulnerability allowing data: URIs.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[code-review]]
