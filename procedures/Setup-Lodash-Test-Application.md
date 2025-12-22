---
tags:
  - ssti
  - node-js
type: procedure
tools:
  - '[[tools/Node-js]]'
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-dependencies]]'
  - '[[commands/node-run-app]]'
platforms:
  - Node.js
  - Web
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1e38ed98-bc64-445e-9103-74a5dcbb183a
created_at: '2025-12-13T09:01:16.948Z'
updated_at: '2025-12-13T09:01:16.948Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Setup Lodash Test Application

## Summary

This procedure sets up a test Express.js application that uses lodash's _.template function to process user input, creating a vulnerable environment for demonstrating Server-side Template Injection.

## Description

The procedure involves installing necessary Node.js packages and running a simple web server that compiles user-supplied input into a template without proper validation, allowing potential code injection. This targets Node.js web applications using lodash version 4.17.15.

## Requirements

1. Node.js installed (v10.16.0 or compatible)
2. npm package manager (v6.9.0 or compatible)
3. Local machine with port 8000 available

## Defense

Defensive measures and detection strategies:

- Upgrade lodash to a version without this vulnerability or use safe template compilation
- Validate and sanitize all user input before template processing

## Objectives

1. Create a vulnerable test environment
2. Run the application on port 8000
3. Prepare for exploitation testing

## Instructions

### Step 1: Install Dependencies

**Context**: Install required packages for the application.

**Command** ([[commands/npm-install-dependencies]]):

```bash
npm install express lodash escape-html
```

> This installs Express.js for the web server, lodash for templating, and escape-html for basic escaping (which is insufficient here).

### Step 2: Create and Run Application

**Context**: Write and execute the application code.

**Command** ([[commands/node-run-app]]):

```bash
node app.js
```

> Use the provided app.js code to start the server listening on port 8000.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

## Commands Used

- [[commands/npm-install-dependencies]]
- [[commands/node-run-app]]

## Tools Used

- [[tools/Node-js]]
- [[tools/npm]]

## Tags

- [[ssti]]
- [[tools/Node-js]]
