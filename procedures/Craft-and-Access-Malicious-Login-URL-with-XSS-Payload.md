---
tags:
  - xss
  - payload-injection
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: e8a2accb-132e-4597-8100-13c4980f9bb3
created_at: '2025-12-14T00:11:16.772Z'
updated_at: '2025-12-14T00:11:16.772Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft and Access Malicious Login URL with XSS Payload

## Summary

This procedure involves crafting a malicious URL by injecting a JavaScript payload into the google_apps_uri parameter of the Shopify login endpoint.

## Description

The lack of sanitization in the google_apps_uri parameter allows injection of javascript: URIs. This sets up the reflected XSS attack, targeting the /services/login/identity endpoint. Expected outcome is a loaded page ready for trigger.

## Requirements

1. Knowledge of the target Shopify login URL
2. Web browser
3. Google Apps enabled

## Defense

Defensive measures and detection strategies:

- Input sanitization on URI parameters
- Content Security Policy (CSP) implementation

## Objectives

1. Inject XSS payload
2. Load manipulated URL
3. Prepare for execution

## Instructions

### Step 1: Construct Payload URL

**Context**: Modify the parameter with a JavaScript payload.

Use a URL like:

```bash
https://app.shopify.com/services/login/identity?destination_uuid=79b5c315-b5ac-4b19-bd33-13554433fa31&google_apps_uri=javascript:prompt(document.domain)&return_to=...
```

> Replace with actual payload such as javascript:prompt(document.cookie).

### Step 2: Access URL

**Context**: Load the URL in the browser.

Navigate to the crafted URL.

> Page loads with injected parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss
- payload-injection
