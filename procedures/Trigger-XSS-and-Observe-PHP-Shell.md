---
tags:
  - xss-trigger
  - php-shell
  - rce-potential
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
updated_at: '2025-12-14T03:46:37.436Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5c53ed31-2db7-4b62-899a-d23ab9e37a23
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-and-Observe-PHP-Shell

## Summary

This procedure accesses the uploaded HTML file either via the details page link or direct URL, executing the stored XSS payload for immediate impact and checking for PHP shell interpretation leading to potential RCE.

## Description

In vulnerable web apps serving uploaded HTML without sanitization, clicking the file link or visiting its direct path (e.g., /$FILE/unsure1.html) renders the content, triggering embedded JavaScript for XSS effects like session theft. If the server is misconfigured to process .html as PHP, the shell code executes, allowing command injection via parameters. This exploits both client-side rendering and server-side execution flaws.

## Requirements

1. Link to the uploaded file from details page
2. Direct URL knowledge (e.g., via document ID)
3. Browser for XSS observation; potential server access for RCE

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user-uploaded content before rendering
- Disable server-side scripting in uploaded file directories
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous JavaScript execution or PHP processes from uploads

## Objectives

1. Execute stored XSS for client-side compromise
2. Validate PHP shell functionality for server-side RCE
3. Demonstrate full impact of the upload vulnerability

## Instructions

### Step 1: Access via Details Page

**Context**: Trigger payload through application interface.

On the request details page, scroll down and click the 'unsure1.html' link.

> Page renders, executing XSS JavaScript (e.g., alert popup or cookie theft).

### Step 2: Access Direct URL

**Context**: Bypass views for direct exploitation.

Navigate to the file's direct path, such as http://target.com/4f4d0c69ea2b33a58525858a001e2b8c/$FILE/unsure1.html.

> Same XSS triggers; inspect for PHP processing (e.g., append ?cmd=whoami to URL for shell test).

### Step 3: Observe Exploitation

**Context**: Confirm impacts.

Watch for XSS effects and test shell by appending commands (if PHP executes).

> Successful XSS shows script output; RCE returns command results like system info.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[php-shell]]
