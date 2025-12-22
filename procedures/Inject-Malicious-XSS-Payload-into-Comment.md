---
tags:
  - xss-injection
  - javascript-payload
  - stored-xss
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
updated_at: '2025-12-13T23:52:33.753Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 939cc86d-19f7-4fab-8ccb-fb371cbdcc5a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-XSS-Payload-into-Comment

## Summary

This procedure focuses on crafting and entering a stored XSS payload into the comment field of Starbucks career pages, leveraging the lack of input sanitization to store executable HTML and JavaScript.

## Description

The vulnerability stems from unescaped user input in comments, allowing arbitrary HTML/JS storage. The payload combines a visible div, CSS to obscure other content, and a script for redirection. Upon storage and page reload, it executes for all users, enabling attacks like phishing on job seekers or cookie theft. This targets the public comment feature without authentication.

## Requirements

1. Open comment form on a vulnerable page
2. Knowledge of XSS payloads
3. Web browser for manual input

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with HTML entity encoding (e.g., &lt; for <)
- Validate and escape outputs in comment rendering
- Implement CSP headers to block inline scripts

## Objectives

1. Deliver executable code via comment
2. Hide malicious elements while ensuring execution
3. Set up for persistent impact on visitors

## Instructions

### Step 1: Craft the Payload

**Context**: Build a payload that evades basic checks and achieves redirection.

Prepare the string: `<div style="position:fixed;bottom:0;left:0;color:#000000;background:#dddddd;padding:1em;z-index:1000000000000000;"><h2><strong><a href="https://www.hackerone.com">hackerone</a></strong></h2></div><style>p{ display:none !important; } </style><script> location.href="https://hackerone.com"; </script>`.

> This creates a fixed notice div, hides paragraphs, and redirects.

### Step 2: Enter Payload in Comment Field

**Context**: Place the code into the textarea without triggering client-side filters.

Copy-paste the payload into the Comment field.

> The field should accept the full string; watch for truncation.

### Step 3: Preview for Issues

**Context**: Ensure the payload is intact before proceeding.

Review the entered text for completeness.

> No errors if payload displays as raw HTML/JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[javascript-payload]]
- [[stored-xss]]
