---
id: proc-frame-jump-hackerone
tags:
  - xss
  - frame-jumping
  - hash-navigation
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.973Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Frame-Jump-to-HackerOne-Contact-Form

## Summary

This procedure uses the XSS payload in the Marketo iframe to open a new window to HackerOne's contact form, leveraging URL hash to auto-trigger form loading.

## Description

From the executed JS in Marketo's context, create a link or window.open to navigate to the target site with #contact, which HackerOne's code checks to call LoadContactForm(). This chains the XSS to the victim's domain without direct vuln there. Prerequisites: Successful XSS trigger. Outcome: Contact form loads in new tab.

## Requirements

1. XSS execution in prior step
2. No additional tools; browser-based
3. Victim's browser allows popups

## Defense

Defensive measures and detection strategies:

- Block or monitor unexpected window.open from iframes
- Sanitize URL hashes in client-side routing
- Disable auto-form load without user confirmation

## Objectives

1. Open target page with hash trigger
2. Load integrated Marketo form
3. Position for further injection

## Instructions

### Step 1: Inject Navigation Code

**Context**: In the JSONP payload, add code to open the target URL.

Modify jsonp.php payload:

```javascript
// JSONP callback
(function() {
  var link = document.createElement('a');
  link.href = 'https://www.hackerone.com/product/overview#contact';
  link.target = 'b';
  link.click(); // Or window.open(...)
})();
```

> Triggers new window; verify by checking opened tab.

### Step 2: Verify Form Load

**Context**: Confirm hash-based form initialization.

In browser console of new tab:

```javascript
// HackerOne code snippet for reference
if (/^#contact/.test(window.location.hash)) {
  LoadContactForm();
}
```

> Expected: Marketo iframe loads in the contact section.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[frame-jumping]]
- [[hash-navigation]]
