---
tags:
  - rce
  - xssi
  - chaining
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: a0c86e44-0a6e-4369-8e27-ee4392e2bbe1
created_at: '2025-12-14T03:46:37.605Z'
updated_at: '2025-12-14T03:46:37.605Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Execute-Chained-XSS-for-RCE

## Summary

This procedure chains the initial XSS to load an external script that performs same-origin manipulation via iframe, modifying a PHP plugin file to achieve RCE on the target WordPress site.

## Description

Once the XSS payload executes, it uses document.write to inject and load wp-rce.js from an attacker-controlled server. The script exploits the same-origin policy bypass via XSSI by creating a hidden iframe to the local admin plugin editor, automating form submission to inject PHP code (e.g., phpinfo()) into hello.php, and finally executing it. This requires the victim to be an admin and the site running on localhost:8090 for testing, but adapts to production.

## Requirements

1. Successful XSS execution
2. External server hosting wp-rce.js with iframe automation logic
3. Target site accessible via same-origin (e.g., 127.0.0.1:8090)
4. Admin privileges on victim

## Defense

Defensive measures and detection strategies:

- Restrict iframe creation and external script loads with strict CSP
- Audit plugin editor access and log file modifications
- Disable or protect plugin-editor.php with authentication checks
- Use file integrity monitoring (FIM) for core/plugin files
- Detect anomalous JS execution in browser via endpoint protection

## Objectives

1. Load and execute external RCE script
2. Automate iframe-based file editing
3. Inject and save malicious PHP code
4. Execute the modified file for RCE

## Instructions

### Step 1: Payload Triggers Script Load

**Context**: XSS onerror executes document.write with atob-decoded script tag.

No command required; the payload automatically loads http://159.203.190.123/.../wp-rce.js.

> Script injects into page and begins execution.

### Step 2: Iframe Creation and Modification

**Context**: wp-rce.js creates iframe to plugin editor and modifies content.

No command required; script appends iframe to body, sets #newcontent to '<?php phpinfo();', clicks #submit after 2s delay.

> Form submits, saving changes to hello.php.

### Step 3: Execute Modified File

**Context**: After 4s delay, redirect to execute the injected code.

No command required; script redirects to /wp-content/plugins/hello.php.

> Page loads with phpinfo() output, confirming RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[xss-chain]]
