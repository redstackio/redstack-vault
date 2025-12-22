---
tags:
  - xss
  - payload-injection
  - javascript-uri
type: procedure
tools:
  - '[[tools/Custom-Links-App]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 48540740-67da-4b4c-b703-d70ef7aaabb7
created_at: '2025-12-13T23:56:03.577Z'
updated_at: '2025-12-13T23:56:03.577Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-JavaScript-Link

## Summary

This procedure creates a custom link in Stripe products using a javascript: URI payload to test for stored XSS, exploiting insufficient URL validation.

## Description

Within the Stripe dashboard's products section, the Custom Links app allows users to define hyperlinks. By inputting a javascript: scheme like 'javascript://%0aalert(1)', the payload is stored and potentially clickable by other users. The root cause is lack of sanitization for non-http schemes. If CSP is bypassed, this executes JavaScript in the dashboard context, risking data theft or session hijacking for team members. Requires the app installed and product edit access.

## Requirements

1. Installed Custom Links app
2. Access to edit products in Stripe dashboard
3. Knowledge of JavaScript payloads for testing

## Defense

Defensive measures and detection strategies:

- Validate and whitelist URL schemes to http/https only
- Strengthen CSP to block javascript: URIs explicitly
- Audit custom link creations for malicious patterns via logs

## Objectives

1. Store a malicious javascript: payload in a dashboard link
2. Demonstrate reflection without immediate sanitization
3. Highlight risks to shared organizational views

## Instructions

### Step 1: Access Products Section

**Context**: Navigate to the area where custom links can be added.

No command required; go to https://dashboard.stripe.com/products and select a product to edit.

> The Custom Links app interface should appear for adding links.

### Step 2: Input Malicious Payload

**Context**: Enter the javascript: URI as the link URL to inject the payload.

No command required; in the link creation form, set the URL field to `javascript://%0aalert(1)` and save.

> The link saves without error, storing the payload for later triggering.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Links-App]]

## Tags

- [[xss]]
- [[payload-injection]]
- [[javascript-uri]]
