---
tags:
  - csp-bypass
  - leakage
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/iframe-content-leakage]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:44.173Z'
sub_techniques: []
id: d35bad77-879f-4db1-88de-04dfe0ecefa6
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Bypass-CSP-with-Iframes-for-Content-Leakage

## Summary

From the XSS context on www.judge.me, load same-origin iframes to leak authenticated content, bypassing frame-ancestors CSP via subdomain allowance.

## Description

CSP whitelists subdomains, allowing iframes from www to judge.me. Use postMessage or direct access to read innerHTML from victim-authenticated pages.

## Requirements

1. Active XSS execution
2. Victim authenticated in iframe
3. JS access to DOM

## Defense

- Tighten CSP to block subdomain embedding
- Use unique origins for sensitive pages
- Monitor iframe creations

## Objectives

1. Load restricted iframes
2. Access cross-frame content
3. Exfiltrate HTML

## Instructions

### Step 1: Create Iframes

**Context**: Dynamically add iframes to victim's settings page.

```javascript
document.body.innerHTML += '<iframe src="https://judge.me/settings"></iframe>';
```

> Loads authenticated content.

### Step 2: Leak Content

**Context**: Read from iframe DOM.

**Command** ([[commands/iframe-content-leakage]]):
```javascript
parent.frames[0].document.body.innerHTML
```

> Returns full HTML string for exfiltration.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/iframe-content-leakage]]

## Tools Used


## Tags

- [[csp-bypass]]
- [[leakage]]
