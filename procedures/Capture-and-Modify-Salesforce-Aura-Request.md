---
tags:
  - request-interception
  - aura-endpoint
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/Capture-Salesforce-Aura-POST-Request]]'
verified: false
platforms:
  - Web
  - Salesforce
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:18.151Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f71c87bf-fd5e-48da-b3c2-445fae97fac6
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-and-Modify-Salesforce-Aura-Request

## Summary

This procedure intercepts a legitimate POST request to Salesforce Aura endpoints after login, analyzes its structure including aura.token and actions, and prepares it for modification to bypass access controls.

## Description

Post-login, portal interactions trigger POSTs to endpoints like /███████?r=3&ui-comm-runtime-components-aura-components-siteforce-controller.PubliclyCacheableAttributeLoader.getComponentAttributes=1. These include JSON actions for getComponentAttributes, returning up to 2000 records with sequential Salesforce IDs. Capturing reveals the format for exploitation, exploiting lack of verification.

## Requirements

1. Active Burp Suite proxy configured in browser
2. Authenticated session from prior registration
3. Knowledge of HTTP request structure

## Defense

Defensive measures and detection strategies:

- Implement request signing or additional auth headers beyond aura.token
- Log and alert on anomalous POST modifications or high-volume queries
- Use Salesforce sharing rules to restrict object access by user profile

## Objectives

1. Capture baseline request to extract tokens and parameters
2. Identify sequential ID pattern for enumeration
3. Modify action to switch to getItems for data retrieval

## Instructions

### Step 1: Trigger and Intercept Request

**Context**: Perform a portal action to generate a legitimate Aura POST, then capture it in Burp.

**Command** ([[commands/Capture-Salesforce-Aura-POST-Request]]):

Use Burp Suite's Proxy to intercept while loading a page.

> The captured request includes message with getComponentAttributes, aura.context in PROD mode, and returns records. Note the endpoint and token for reuse.

### Step 2: Analyze and Prepare Modification

**Context**: Examine the request body to understand JSON structure for alteration.

No command; manually inspect in Burp Repeater.

> Verify response includes up to 2000 records and sequential IDs, confirming enumeration feasibility. Drop the getComponentAttributes action and prepare getItems payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/Capture-Salesforce-Aura-POST-Request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-interception
- aura-endpoint
- burp-suite
