---
id: proc-self-xss-injection
tags:
  - self-xss
  - xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-submit-self-xss-form]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.681Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate-Self-XSS-Injection

## Summary

This procedure demonstrates injecting a JavaScript payload into a web form's first_name field on a DoD site, resulting in self-XSS execution upon user submission and response viewing, limited to the attacker's own browser session.

## Description

The target form at https://███████/ lacks input sanitization, allowing script tags in the first_name parameter to reflect and execute in the POST response. This is self-XSS because it requires the user to submit and view the result themselves. Prerequisites include browser access to the site; no authentication is needed for the public form. Expected outcome: Alert with document.cookie upon execution, confirming arbitrary JS capability.

## Requirements

1. Web browser with developer tools
2. Access to the target URL https://███████/
3. Basic knowledge of HTML forms and JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity encoding) on form responses
- Use Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous JavaScript alerts or cookie access in logs

## Objectives

1. Inject and confirm self-XSS payload execution
2. Verify reflection in form response
3. Highlight sanitization gaps for reporting

## Instructions

### Step 1: Access the Form and Prepare Payload

**Context**: Load the form and craft the XSS payload to break out of string context.

No command needed; manually navigate to https://███████/ and prepare payload: 'test"; <script>alert(document.cookie)</script>'.

> This payload closes a potential quote and injects a script tag.

### Step 2: Submit Form with Payload

**Context**: Use curl to simulate POST submission with the malicious first_name.

**Command** ([[commands/curl-submit-self-xss-form]]):
```bash
curl -X POST https://██████████/ -d "first_name=test\";<script>alert(document.cookie)</script>&middle_name=&last_name=" -H "Content-Type: application/x-www-form-urlencoded" --cookie "session=your_session_cookie"
```

> This sends the form data; replace session cookie if authenticated. Expected output: HTTP response with reflected payload in HTML.

### Step 3: View Response to Trigger Execution

**Context**: Submit via browser and observe the response page to execute the self-XSS.

**Command**: Use browser form submission after injecting payload.

> Upon page load post-submission, the script executes, alerting cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-submit-self-xss-form]]

## Tools Used


## Tags

- [[self-xss]]
- [[xss]]
- [[web]]
