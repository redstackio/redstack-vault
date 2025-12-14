---
id: proc-uuid-4
tags:
  - xss
  - rce
  - wordpress
  - escalation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/Exploit-CSRF-with-frs-save-Form]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[PowerShell]]'
updated_at: '2025-12-14T17:27:15.548Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[PowerShell]]'
---
# Inject JavaScript for Stored XSS and Escalation

## Summary

This procedure uses the CSRF-modified post to inject persistent JavaScript, creating stored XSS that affects all site viewers, and escalates via admin JS execution to achieve RCE through plugin/theme editors.

## Description

After content update, the unsanitized content field allows <script> tags to execute on load. For stealth, target old posts and use JS redirects. With admin visit, leverage browser context to access editors, injecting PHP for RCE even if editing is restricted, via vectors like wpengine-common.

## Requirements

1. Successful prior CSRF modification
2. Knowledge of admin editor access
3. Target post visible to all users

## Defense

Defensive measures and detection strategies:

- Sanitize post content with wp_kses_post
- Disable JS in editors for non-admins
- WAF rules to block malicious script injections
- Monitor for unexpected JS in posts

## Objectives

1. Achieve stored XSS for broad impact
2. Escalate to admin JS execution
3. Gain RCE via code injection

## Instructions

### Step 1: Inject XSS Payload

**Context**: Use prior form to embed JS in content.

**Command** ([[commands/Exploit-CSRF-with-frs-save-Form]]):

Update content to: <script>alert('XSS'); /* further payload */</script>

```html
// Same as prior, with JS in content
```

> Expected: Script runs on post view.

### Step 2: Escalate to RCE

**Context**: From XSS, access /wp-admin/plugin-editor.php or similar; inject PHP backdoor.

No specific command; use JS to navigate and submit forms.

> Expected: Server-side code execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[JavaScript]] JavaScript
- [[PowerShell]] PowerShell (adapted to PHP)

### Sub-Techniques

-

## Commands Used

- [[commands/Exploit-CSRF-with-frs-save-Form]]

## Tools Used

-

## Tags

- xss
- rce
- wordpress
- escalation
