---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - csrf
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:42.361Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Vulnerable-CSRF-Forms

## Summary

This procedure involves inspecting web forms on a target site like uberps.com to detect the absence of CSRF protections, such as tokens, enabling potential exploitation for unauthorized actions.

## Description

In a CSRF attack scenario, the first step is reconnaissance to confirm vulnerabilities. On uberps.com, forms lacked CSRF tokens, allowing forged requests from malicious sites. This procedure uses browser tools to analyze forms, check for protections, and document exploitable endpoints. Prerequisites include access to the site and basic web development knowledge. Expected outcomes: A list of vulnerable forms ready for PoC crafting.

## Requirements

1. Browser with developer tools (e.g., Chrome DevTools)
2. Access to https://uberps.com while authenticated
3. Knowledge of HTML form structures

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all forms
- Use SameSite cookies to restrict cross-site requests
- Monitor for anomalous form submissions from unexpected referers

## Objectives

1. Confirm lack of CSRF protections on target forms
2. Identify sensitive form actions (e.g., transactions)
3. Document endpoints for exploitation

## Instructions

### Step 1: Inspect Site Forms

**Context**: Navigate to uberps.com and use developer tools to locate all forms.

Open the browser console and query for forms:

```javascript
// Run in browser console on uberps.com
let forms = document.querySelectorAll('form');
forms.forEach((form, index) => {
  console.log(`Form ${index}: Action = ${form.action}, Method = ${form.method}`);
  let tokens = form.querySelectorAll('input[name*="csrf"], input[name*="token"]');
  console.log(`Tokens found: ${tokens.length}`);
});
```

> This logs form details and checks for token inputs. If zero tokens, the form is vulnerable.

### Step 2: Test Form Submission

**Context**: Manually submit a form and inspect the network request for token inclusion.

Use the Network tab in DevTools to monitor a submission. Look for POST requests without CSRF headers or params.

**Expected Output**: Request details showing missing protections.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-recon]]
