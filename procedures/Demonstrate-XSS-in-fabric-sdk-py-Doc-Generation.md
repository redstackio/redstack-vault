---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Demonstrate XSS in fabric-sdk-py Doc Generation
tags:
  - xss
  - dom-xss
  - jquery
  - python
  - fabric-sdk-py
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/pip-install-vulnerable-package]]'
  - '[[commands/build-sphinx-docs]]'
  - '[[commands/open-html-file]]'
verified: false
platforms:
  - Python
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:31.358Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate XSS in fabric-sdk-py Doc Generation

## Summary

This procedure demonstrates a DOM-based Cross-Site Scripting (XSS) vulnerability in older versions of the fabric-sdk-py package by exploiting an outdated jQuery dependency during documentation generation. Malicious scripts injected into doc source are executed via unsafe jQuery methods like .html() and .append(), even after basic HTML sanitization, potentially allowing code execution in browser contexts where the generated docs are viewed.

## Description

The fabric-sdk-py package, part of the Hyperledger Fabric ecosystem, uses an outdated version of jQuery (prior to 3.5) in its documentation generation process, likely via Sphinx or similar tools. Methods such as .html() and .append() are used to manipulate DOM elements with user-supplied or template HTML, which can lead to script execution if sanitization is insufficient. This vulnerability was identified through source code review and poses risks in environments where documentation is built and served dynamically. The procedure involves setting up a vulnerable environment, injecting a test payload, building the docs, and verifying execution in a browser. Prerequisites include a Python setup capable of installing packages and building docs; no remote access is needed, but it simulates an attack on local or CI/CD doc generation pipelines.

## Requirements

1. Python 3.x environment with pip installed
2. Access to the fabric-sdk-py source code or ability to install vulnerable versions
3. Sphinx documentation builder (included in many Python projects)
4. A web browser to load and inspect generated HTML

## Defense

Defensive measures and detection strategies:

- Upgrade to latest fabric-sdk-py versions with patched jQuery (>=3.5)
- Implement strict Content Security Policy (CSP) in doc hosting environments to block inline scripts
- Use modern sanitization libraries like DOMPurify before passing HTML to jQuery
- Scan source code for vulnerable jQuery usage with tools like Retire.js or Snyk
- Monitor doc generation logs for anomalous script execution or build failures

## Objectives

1. Exploit the jQuery DOM manipulation flaw to execute injected JavaScript
2. Validate the vulnerability in a controlled doc generation setup
3. Assess potential impact on users viewing the generated documentation

## Instructions

### Step 1: Install Vulnerable Package

**Context**: Set up the environment with the affected version of fabric-sdk-py to ensure the outdated jQuery is present in the doc generation dependencies.

**Command** ([[commands/pip-install-vulnerable-package]]):
```bash
pip install fabric-sdk-py==1.5.3  # Replace with confirmed vulnerable version from report
```

> This installs the package, pulling in the vulnerable jQuery. Expected output: Installation logs showing dependencies resolved, no errors.

### Step 2: Inject Payload into Doc Source

**Context**: Modify a documentation file (e.g., index.rst) to include a malicious HTML payload that will be processed by jQuery during build.

**Command** (Manual edit; no CLI command):

Edit the .rst file:
```rst
Payload Test
============

Content with script: <script>console.log('XSS Triggered'); alert('DOM XSS via jQuery');</script>
```

> Save the file. This simulates untrusted input; in a real attack, this could come from tainted data sources.

### Step 3: Build Documentation

**Context**: Generate the HTML docs, triggering jQuery's DOM methods to insert the payload.

**Command** ([[commands/build-sphinx-docs]]):
```bash
cd docs  # Navigate to docs directory in package
make html
```

> Builds the Sphinx HTML output. Expected output: _build/html directory created with index.html containing the processed payload.

### Step 4: Verify Execution

**Context**: Load the generated HTML in a browser to confirm script execution.

**Command** ([[commands/open-html-file]]):
```bash
open _build/html/index.html  # macOS; use 'xdg-open' on Linux or 'start' on Windows
```

> Opens the file in default browser. Expected output: Page loads, and the alert pops or console shows the log, indicating successful XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/pip-install-vulnerable-package]]
- [[commands/build-sphinx-docs]]
- [[commands/open-html-file]]

## Tools Used


## Tags

- xss
- dom-xss
- jquery
- python
- fabric-sdk-py
