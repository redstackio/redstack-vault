---
id: proc-006
tags:
  - replace-state
  - alternative-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/attack-trigger-replacestate-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:18.389Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Alternative-Trigger-via-replaceState

## Summary

Modify the postMessage to use Shopify.API.replaceState for triggering the path traversal without altering browser history.

## Description

Similar to pushState but uses replaceState in the JSON message, providing an alternative exploitation vector with the same pathname traversal to load XSS.

## Requirements

1. Original trigger page
2. Admin tab open

## Defense

- Same as pushState: validate all API calls
- Audit replaceState usage

## Objectives

1. Provide stealthier trigger
2. Maintain XSS execution
3. Avoid history pollution

## Instructions

### Step 1: Update Trigger Data

**Context**: Edit the JSON in attack script.

**Command** ([[commands/attack-trigger-replacestate-xss]]):
```javascript
data =JSON.stringify({message:'Shopify.API.replaceState',data:{pathname:"/../pages/xss"}});ctx.postMessage(data)
```

> Replace in setInterval. Expected output: Route replaces successfully.

### Step 2: Execute

**Context**: Run updated trigger.

**Instructions**: Click attack button.

> XSS loads without history change.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/attack-trigger-replacestate-xss]]

## Tools Used


## Tags

- replace-state
- alternative-trigger
