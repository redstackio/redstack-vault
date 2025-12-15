---
tags:
  - source-code-audit
  - javascript-analysis
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/javascript-onclick-fa-call]]'
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 8d1d6854-3e57-4399-b80e-7d48a8a33991
created_at: '2025-12-14T17:28:36.455Z'
updated_at: '2025-12-14T17:28:36.455Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Conduct-Source-Code-Audit-for-JavaScript-Functions

## Summary

This procedure involves auditing TikTok's frontend JavaScript to identify the usage of the 'live' parameter in onClick functions, revealing potential points for API parameter tampering.

## Description

In the context of auditing TikTok's frontend, examine JavaScript bundles or use browser dev tools to search for event handlers related to live shopping ads. The goal is to find hardcoded parameters like 'live' that can be replicated or modified in API calls, leading to business logic flaws. This step is crucial for understanding client-side logic before attempting backend exploitation. Prerequisites include access to the TikTok web application and basic JavaScript knowledge.

## Requirements

1. Access to TikTok frontend (browser or downloaded JS files)
2. Developer tools (e.g., Chrome DevTools) or text editor for code search
3. Knowledge of JavaScript event handlers

## Defense

Defensive measures and detection strategies:

- Obfuscate frontend code to hinder static analysis
- Implement client-side integrity checks to detect tampering attempts
- Monitor for unusual API parameter values in logs

## Objectives

1. Identify 'live' parameter in client-side analytics calls
2. Map parameter to potential API endpoints
3. Establish basis for parameter manipulation testing

## Instructions

### Step 1: Inspect Frontend Code

**Context**: Load the TikTok Shop Seller dashboard and use dev tools to search for onClick functions.

**Command** ([[commands/javascript-onclick-fa-call]]):
```javascript
onClick:function(){Fa('self-promotion','live','live_dashboard'), (0, de.xw)(m)}
```

> This JavaScript snippet shows the Fa() call with 'live' parameter for live shopping ads. Expected output: Confirmation of parameter usage in event handling.

### Step 2: Document Findings

**Context**: Note the context of the parameter to hypothesize backend behavior.

No specific command; manually record the snippet and its role in navigation to live dashboard.

> Expected output: Documented evidence of 'live' as a boolean filter for active products.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-onclick-fa-call]]

## Tools Used


## Tags

- source-code-audit
- javascript
