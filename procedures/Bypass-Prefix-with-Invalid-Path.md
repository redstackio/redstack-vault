---
id: proc-007
tags:
  - bypass
  - invalid-path
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/attack-trigger-invalid-path-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:18.384Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Bypass-Prefix-with-Invalid-Path

## Summary

Use an invalid pathname in replaceState to bypass prefix checks, causing a redirect that exposes the admin panel (e.g., to /password).

## Description

By sending 'invalid' as pathname, the route handling fails validation but triggers a redirect, potentially revealing admin interface for further attacks.

## Requirements

1. replaceState trigger setup
2. Password page enabled on store

## Defense

- Handle invalid paths gracefully without exposure
- Redirect to safe error pages
- Log invalid route attempts

## Objectives

1. Bypass traversal limitations
2. Expose admin for injection
3. Demonstrate broader vuln

## Instructions

### Step 1: Set Invalid Path

**Context**: Update postMessage payload.

**Command** ([[commands/attack-trigger-invalid-path-bypass]]):
```javascript
data =JSON.stringify({message:'Shopify.API.replaceState',data:{pathname:"invalid"}});ctx.postMessage(data)
```

> Inject into trigger. Expected output: Redirect to /password.

### Step 2: Observe Exposure

**Context**: Trigger and check admin.

**Instructions**: Activate; watch for redirect.

> Admin at /admininvalid -> /password. Expected output: Interface exposed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/attack-trigger-invalid-path-bypass]]

## Tools Used


## Tags

- bypass
- invalid-path
