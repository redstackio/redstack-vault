---
tags:
  - xss
  - injection
type: procedure
tools:
  - '[[tools/js-xss]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/xss-payload-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.208Z'
sub_techniques: []
id: 6cdc230c-bb8b-4e36-a9f2-3b5dd6e2115a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Email-Template

## Summary

This procedure injects a crafted XSS payload into Judge.me's email template HTML, exploiting a misconfiguration in the js-xss library's onIgnoreTag function to bypass sanitization during preview.

## Description

The attack targets the email template editor where HTML input is sanitized using a custom js-xss configuration. By abusing parsing differences between js-xss and browsers for tags starting with '<! [', the payload evades filtering. When previewed, it executes JavaScript in the judge.me domain context, enabling self-XSS. Prerequisites include access to a Judge.me shop account with template editing rights.

## Requirements

1. Valid Judge.me shop admin access
2. Knowledge of target template ID
3. Browser for editing

## Defense

Defensive measures and detection strategies:

- Update js-xss to latest version and review custom onIgnoreTag implementations
- Implement server-side sanitization in addition to client-side
- Monitor for anomalous template saves and preview accesses

## Objectives

1. Insert executable HTML payload
2. Bypass client-side filtering
3. Set up for self-XSS on preview

## Instructions

### Step 1: Access Template Editor

**Context**: Navigate to the edit page for the target email template.

**Command** ([[commands/xss-payload-injection]]):
```html
<! [endif]--onerror="<! [endif]-->"onload="<img src=1 onerror='alert(1)'/>"
```

> Paste this payload into the HTML field at `https://www.judge.me/shop/emails/[ID]/edit`. The payload exploits IE comment parsing differences, returning unsanitized content via onIgnoreTag.

### Step 2: Verify Insertion

**Context**: Check if the payload is visible without triggering sanitization.

No command needed; reload the editor to confirm persistence.

> Expected: Payload remains in the field.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/xss-payload-injection]]

## Tools Used

- [[tools/js-xss]]

## Tags

- [[xss]]
- [[injection]]
