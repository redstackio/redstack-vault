---
id: proc-analyze-shopify-js
tags:
  - reverse-engineering
  - javascript-analysis
  - postmessage
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/initialize-postmessage-handler]]'
  - '[[commands/analyze-message-handler]]'
  - '[[commands/analyze-dom-insertion]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.428Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Analyze-Shopify-Digital-Wallets-JavaScript

## Summary

This procedure involves reverse-engineering the minified JavaScript code of Shopify's /:id/digital_wallets/dialog endpoint to identify the postMessage listener lacking origin validation and trace how payloads are processed and inserted into the DOM.

## Description

In a browser environment targeting a Shopify shop, load the vulnerable endpoint and use developer tools to deobfuscate and analyze the JavaScript. Focus on the event listener for 'message' events, which processes payloads without checking event.origin, allowing cross-origin attacks. Examine functions responsible for validation (d), resetting DOM (g), updating elements (p), rendering tables (f), and templating rows (m), particularly how lineItems are escaped via u before insertion.

## Requirements

1. Browser with developer tools (e.g., Chrome)
2. Access to the target Shopify domain's /:id/digital_wallets/dialog endpoint
3. JavaScript knowledge for code inspection

## Defense

Defensive measures and detection strategies:

- Implement strict origin validation in postMessage handlers (e.g., if(event.origin !== expectedOrigin) return;).
- Use Content Security Policy (CSP) to restrict inline script execution.
- Monitor for anomalous postMessage events in browser logs or WAF.

## Objectives

1. Identify vulnerable postMessage handling without origin checks.
2. Map payload flow to DOM insertion points.
3. Confirm lineItems processing leads to innerHTML updates.

## Instructions

### Step 1: Load and Inspect Endpoint

**Context**: Navigate to the target endpoint (e.g., https://shop.myshopify.com/1337/digital_wallets/dialog) and open DevTools Sources tab to find the minified JS file.

**Command** ([[commands/initialize-postmessage-handler]]):
```javascript
this._messageHandler=function(event){if(event.data){if(event.data.type && event.data.digitalWalletsDialog){c(i, event.data.type, event.data.payload);}}} this._localWindow.addEventListener("message",this._messageHandler)
```

> This initializes the handler; paste into console to simulate and observe no origin check.

### Step 2: Trace Message Processing

**Context**: Search for function c and related helpers to understand type handling.

**Command** ([[commands/analyze-message-handler]]):
```javascript
function c(inst, type, payload){switch(type){case ze.DIALOG_CHANGE:if(d(payload)){g(inst) p(inst, payload)...
```

> Examines switch on type 'DigitalWalletsDialog:change', calls validation d, reset g, and update p.

### Step 3: Examine DOM Insertion

**Context**: Focus on p and f for lineItems rendering.

**Command** ([[commands/analyze-dom-insertion]]):
```javascript
function p(inst, payload){_(inst, t.icon) v(inst,"title", payload.title) if(payload.errors){...} if(payload.lineItems){v(inst,"errorList",f(payload.lineItems)) inst.staticElements.errorListContainer.classList.remove("hidden") v(inst,"dismissButton", payload.button ||"Close")}}

function f(payload){var table = document.createElement("table") table.className ="product-table" table.id ="dialog__product-table" table.innerHTML =T payload.forEach(function(lineItem){ table.tBodies[0].innerHTML +=m(lineItem)}) return table}
```

> Confirms lineItems create table with innerHTML += from m, vulnerable to unescaped input.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/initialize-postmessage-handler]]
- [[commands/analyze-message-handler]]
- [[commands/analyze-dom-insertion]]

## Tools Used


## Tags

- reverse-engineering
- javascript-analysis
