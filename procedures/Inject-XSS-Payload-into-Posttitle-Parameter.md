---
id: proc-1043804-posttitle-xss
tags:
  - xss
  - dom-xss
  - posttitle
  - javascript-injection
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/execute-form-submission-js]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:55:06.609Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Inject-XSS-Payload-into-Posttitle-Parameter

## Summary

This procedure exploits a reflected DOM-based XSS vulnerability in the posttitle parameter of IntenseDebate's getCommentLink.php endpoint by injecting a JavaScript payload that executes upon URL loading, allowing arbitrary code execution in the browser context.

## Description

The vulnerability arises from improper sanitization of the user-controlled posttitle parameter, which is reflected back into the DOM without escaping. An attacker crafts a URL with parameters acct, postid, posturl, and a malicious posttitle containing a payload like "><img src=x onerror=alert(document.domain)>. When loaded in a browser, the script executes, popping an alert and enabling further attacks like cookie theft or form manipulation. This was discovered in the HackerOne report #1043804 and affects the web platform running PHP and JavaScript.

## Requirements

1. Access to a web browser like Firefox
2. Knowledge of the target endpoint and required parameters (acct, postid, posturl)
3. Optional: Authenticated session for impact demonstration

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to restrict inline scripts
- Sanitize and escape all user inputs before DOM insertion
- Monitor for anomalous JavaScript execution or alert triggers in browser logs

## Objectives

1. Trigger arbitrary JavaScript execution via reflected input
2. Verify vulnerability by observing alert popup
3. Enable escalation to data theft or unauthorized actions

## Instructions

### Step 1: Craft the Malicious URL

**Context**: Prepare the endpoint URL with the XSS payload in posttitle, URL-encoding special characters to bypass basic filters.

**Command** ([[commands/execute-form-submission-js]] variant for testing):

No bash command; use browser URL bar.

Crafted URL example:

```url
https://www.intensedebate.com/js/getCommentLink.php?acct=example&postid=123&posturl=https://example.com&posttitle=%3Cimg%20src=x%20onerror=alert(document.domain)%3E
```

> This injects the payload, causing the img tag to fail loading and execute the onerror handler, alerting the domain.

### Step 2: Load URL in Browser

**Context**: Navigate to the crafted URL to trigger the reflection and execution.

Use [[tools/Firefox]] to open the URL.

**Expected Output**: Alert popup with the document domain (e.g., www.intensedebate.com).

> Successful execution confirms the DOM-based XSS; inspect the page source to see the reflected payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Initial Access]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/execute-form-submission-js]]

## Tools Used

- [[tools/Firefox]]

## Tags

- xss
- dom-xss
- injection
