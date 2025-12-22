---
id: proc-steal-csrf-token-iframe
tags:
  - csrf
  - token-theft
  - iframe
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/Steal-CSRF-Token-via-Iframe]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-13T23:56:03.464Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Cloud Instance Metadata API]]'
---
# Steal CSRF Token using Iframe

## Summary

This procedure uses XSS to inject an iframe loading the edit registrations page and extracts the authenticity_token for CSRF bypass.

## Description

From the XSS context, create an iframe to /widgets/twitter_registrations/edit, wait for load, and query the form for the hidden authenticity_token. This steals the token needed for state-changing requests, escalating the XSS to CSRF attacks in the same-origin context.

## Requirements

1. Active XSS execution in victim browser
2. Same-origin policy allows iframe access (target is same domain)
3. Browser supports document.contentDocument access

## Defense

Defensive measures and detection strategies:

- Use frame-ancestors CSP to block unauthorized iframes
- Rotate CSRF tokens frequently
- Monitor for cross-frame DOM access in JS errors

## Objectives

1. Load sensitive page in iframe
2. Extract CSRF token
3. Use for subsequent requests

## Instructions

### Step 1: Inject Iframe via XSS

**Context**: Use XSS to replace body with iframe targeting the edit page.

Execute [[commands/Steal-CSRF-Token-via-Iframe]]:

```javascript
document.body.innerHTML="<iframe id=ifr src=/widgets/twitter_registrations/edit></iframe>";
setTimeout(function(){
 alert(ifr.contentDocument.getElementsByName("authenticity_token")[0].value);
},1337);
```

> Iframe loads after injection. Expected: Page shows edit form in frame.

### Step 2: Extract and Alert Token

**Context**: After timeout, access and display the token.

The setTimeout triggers the alert.

> Token value alerted. Success: Valid token string displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript
- [[Cloud Instance Metadata API]] RCE Software

### Sub-Techniques


## Commands Used

- [[commands/Steal-CSRF-Token-via-Iframe]]

## Tools Used


## Tags

- csrf
- iframe
- token-theft
