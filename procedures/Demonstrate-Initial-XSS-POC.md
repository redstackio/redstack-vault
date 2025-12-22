---
id: proc-initial-xss-poc
tags:
  - xss
  - poc
  - auditor-disable
type: procedure
tools:
  - '[[tools/Internet-Explorer-11]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/twitter-initial-xss-poc-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.793Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate-Initial-XSS-POC

## Summary

This procedure tests basic JavaScript injection via the HTML vulnerability, requiring manual disablement of IE's XSS Auditor to execute the script in the 404 page context.

## Description

Builds on HTML injection by inserting <script> tags. Auditor blocks by default, so disable via IE settings. Expected: JS runs, alerting or acting in twitter.com context.

## Requirements

1. IE 11 with admin to disable auditor
2. Successful HTML injection
3. POC URL access

## Defense

Defensive measures and detection strategies:

- Enable and configure XSS auditors/CSRF tokens
- Script blocking via CSP
- Monitor JS execution in error pages

## Objectives

1. Inject and execute basic JS
2. Confirm XSS with auditor off
3. Identify need for bypass

## Instructions

### Step 1: Disable XSS Auditor

**Context**: Turn off protection in IE settings.

**Command** (IE Settings):
```settings
Internet Options > Security > Custom Level > Miscellaneous > Disable "Enable XSS Filter"
```

> Apply and restart IE. Expected output: Auditor inactive.

### Step 2: Run POC

**Context**: Load script-injecting URL.

**Command** ([[commands/twitter-initial-xss-poc-url]]):
```url
http://secgeek.net/POC/Twitter-XSS-POC.php
```

> Expected output: Script executes, e.g., alert pops.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/twitter-initial-xss-poc-url]]

## Tools Used

- [[tools/Internet-Explorer-11]]

## Tags

- xss
- poc
- auditor-disable
