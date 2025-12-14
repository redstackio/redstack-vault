---
tags:
  - vulnerable-config
  - ejs
  - fastify
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:54.790Z'
sub_techniques: []
id: 887ec339-9444-4e11-81bc-2a22b49f9f9b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Create-Vulnerable-Fastify-Server

## Summary

This procedure configures a Fastify server that exposes the RCE vulnerability by using reply.view({ raw: template }) with unsanitized user input in EJS templates, allowing arbitrary code execution.

## Description

Write a server.js file that registers @fastify/view with EJS and defines routes for rendering templates. The /render POST endpoint accepts user input as the raw template, passing it directly to EJS without validation, enabling injection of Node.js code like require('child_process').execSync(). This setup mimics a real-world scenario where untrusted data is rendered, leading to RCE. Prerequisites include the installed dependencies from prior setup.

## Requirements

1. Completed environment setup with dependencies installed
2. Text editor for creating JavaScript files
3. Basic knowledge of Fastify and EJS syntax

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before passing to template engines
- Use allowlists for permitted template content and disable raw rendering options
- Monitor for anomalous Node.js require calls in logs

## Objectives

1. Register EJS engine in Fastify without security controls
2. Expose endpoint vulnerable to template injection
3. Enable raw template rendering for exploitation

## Instructions

### Step 1: Write Server Configuration

**Context**: Define the Fastify app with plugin registration and vulnerable route.

**Command** (Manual file creation):
```javascript
// server.js content as described in attack chain
```

> Create server.js with the provided code, including GET / and POST /render. Also add empty .ejs files. Expected output: Files saved in project directory.

### Step 2: Verify Configuration

**Context**: Ensure the code includes the raw option and child_process potential.

**Instructions**: Review the code for reply.view({ raw: true }) usage with request.body.text.

> Expected output: Code confirms direct EJS compilation of user input.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/node]]

## Tags

- vulnerable-config
- ejs
- fastify
