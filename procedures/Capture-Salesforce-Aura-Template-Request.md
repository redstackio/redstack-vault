---
id: proc-uuid-2
name: Capture-Salesforce-Aura-Template-Request
tags:
  - salesforce
  - aura-api
  - request-capture
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Salesforce
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:13.206Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Vulnerability Scanning]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Capture-Salesforce-Aura-Template-Request

## Summary

This procedure involves navigating to a public Salesforce developer edition to trigger and capture a sample Aura API request, providing a template for modification in exploitation scenarios.

## Description

By visiting a template instance like https://aaroncostello-developer-edition.eu45.force.com/, user interactions (e.g., loading a page with Lightning components) generate POST requests to the Aura endpoint. These are intercepted in Burp Suite's Proxy history, serving as a base for crafting requests to the target instance. The target environment is any Salesforce org with Aura framework; outcomes include a reusable request structure with authentication placeholders that can be stripped for Guest access.

## Requirements

1. Burp Suite proxy active and browser routed through it
2. Access to a public Salesforce developer edition (no login needed for basic loads)
3. Knowledge of Aura endpoint (/s/sfsites/aura)

## Defense

Defensive measures and detection strategies:

- Restrict public access to developer editions or monitor unusual traffic to them
- Log API endpoint accesses and alert on high-volume template fetches
- Implement rate limiting on Aura endpoints

## Objectives

1. Obtain a valid Aura POST request template
2. Identify key parameters like 'message' for payload injection
3. Ensure template includes Lightning component descriptors

## Instructions

### Step 1: Navigate to Template Instance

**Context**: Load a page that triggers Aura requests to capture in Burp.

No command; browser action:
- Visit https://aaroncostello-developer-edition.eu45.force.com/ and interact (e.g., click elements) to generate traffic.

> Requests flow through Burp Proxy. Expected output: Multiple entries in HTTP history, including POST to /s/sfsites/aura.

### Step 2: Locate POST Request in History

**Context**: Filter and identify the relevant Aura API call.

No command; Burp GUI:
- Go to Proxy > HTTP history > Filter for POST requests to /s/sfsites/aura.
- Right-click the entry > Send to Repeater.

> Template request now in Repeater for editing. Expected output: Full request details visible, including JSON 'actions'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[salesforce]]
- [[aura]]
- [[template-capture]]
