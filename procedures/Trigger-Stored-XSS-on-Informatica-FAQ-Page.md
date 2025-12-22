---
id: proc-trigger-xss-informatica-faq
tags:
  - xss
  - payload-trigger
  - javascript-execution
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-14T03:16:25.168Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-on-Informatica-FAQ-Page

## Summary

This procedure accesses a specific FAQ page in the same browser session, causing the stored XSS payload from the search injection to be reflected and executed as JavaScript, resulting in arbitrary code execution in the victim's browser.

## Description

After the payload is stored in the session during the search step, the FAQ page at /faq/1/Pages/17033.aspx renders the tainted `varSearchResultURL` variable inside a JavaScript block without escaping. This leads to the execution of the injected `alert(1)` or any other JS payload. The attack targets .NET ASPX pages on port 7001 and can lead to session hijacking or data theft. It requires the prior injection step in the same session.

## Requirements

1. Active browser session with the injected payload (from previous procedure)
2. Access to https://kb.informatica.com on port 7001
3. Firefox or similar browser to observe the alert

## Defense

Defensive measures and detection strategies:

- Sanitize session-stored data before embedding in JavaScript (e.g., escape quotes and semicolons)
- Implement strict CSP headers to block unsafe-inline scripts
- Log and alert on JavaScript errors or unexpected alert executions in web apps

## Objectives

1. Execute the stored payload for immediate JS control
2. Demonstrate impact like session theft in a real attack
3. Highlight persistence of stored XSS across pages

## Instructions

### Step 1: Navigate to FAQ Page

**Context**: In the same browser session, visit the FAQ page that pulls and renders the session-stored search URL in JS.

No command-line tool is used; perform this in the browser.

> Visit the following URL in Firefox: https://kb.informatica.com/faq/1/Pages/17033.aspx?docid=17033&type=external&isSearch=external

> The page renders: var varSearchResultURL = "http://kb.informatica.com:7001/kbexternal/Pages/KBSearchResults.aspx?k=Support Console&fromsource=11171";alert(1)//535"; This breaks out of the string, executes alert(1), and comments out the rest.

### Step 2: Observe Execution

**Context**: Verify the payload triggers by watching for the alert popup.

> An alert box with "1" should appear immediately upon page load, confirming JS execution in the browser context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- xss
- execution
