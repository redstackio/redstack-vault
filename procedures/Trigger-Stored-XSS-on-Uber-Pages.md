---
id: proc-uuid-3
tags:
  - stored-xss
  - dom-injection
  - uber
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.446Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS on Uber Pages

## Summary

This procedure demonstrates how the injected Tealium tag executes as stored XSS on Uber domains, injecting content into the DOM for any visiting user.

## Description

Uber pages load utag.js from tags.tiqcdn.com, which includes the malicious tag. Upon loading, the JavaScript runs in the page context, allowing arbitrary DOM alterations, script execution, or data exfiltration affecting all users without further interaction.

## Requirements

1. Published malicious tag in target account
2. Access to Uber domain (e.g., uber.com)
3. Browser to observe execution

## Defense

Defensive measures and detection strategies:

- Audit third-party scripts like utag.js for anomalies
- Enforce strict CSP to block inline scripts
- Monitor client-side errors and unexpected DOM changes

## Objectives

1. Load affected page to trigger execution
2. Verify injection impacts DOM
3. Assess scope across Uber subdomains

## Instructions

### Step 1: Visit Affected Domain

**Context**: Initiate page load to fetch utag.js.

Open a browser and navigate to an Uber page (e.g., https://www.uber.com).

> Page loads normally, but utag.js is fetched in the background.

### Step 2: Observe Execution

**Context**: Monitor for payload activation.

Open developer tools (F12) and watch the console/network tab as the page renders.

> Malicious script executes, showing alerts or DOM changes.

### Step 3: Validate Impact

**Context**: Confirm stored nature and broad effect.

Inspect the DOM for injected elements and test on multiple Uber subdomains.

> Injected content persists across sessions and users.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- stored-xss
- dom-injection
- uber
