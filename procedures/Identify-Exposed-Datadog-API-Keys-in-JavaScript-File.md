---
tags:
  - information-disclosure
  - api-key-exposure
  - datadog
  - javascript
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:32:29.272Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: eda63838-0a27-4030-a99b-448b63689241
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Identify-Exposed-Datadog-API-Keys-in-JavaScript-File

## Summary

This procedure involves inspecting publicly accessible JavaScript files on a target website to discover embedded Datadog API and application keys, which can lead to unauthorized access to monitoring services.

## Description

In this attack scenario, client-side JavaScript code on the website █████ inadvertently exposes sensitive Datadog credentials. By viewing the source code of these files, an attacker can extract the keys and use them to interact with the Datadog API. The target environment is a web application using Datadog for monitoring, with no server-side protection for the JS assets. Expected outcomes include obtaining the full API key and application key, enabling subsequent validation of access. Prerequisites include basic web browsing capabilities and knowledge of common credential patterns.

## Requirements

1. Access to the target website over the internet
2. Browser with developer tools enabled
3. Familiarity with JavaScript and API key formats

## Defense

Defensive measures and detection strategies:

- Remove sensitive keys from client-side code and use server-side proxies
- Implement Content Security Policy (CSP) to restrict JS execution
- Regularly scan public repositories and assets for exposed credentials using tools like TruffleHog

## Objectives

1. Locate and extract Datadog API and application keys
2. Confirm the keys are functional for Datadog services
3. Assess potential impact on the monitoring instance

## Instructions

### Step 1: Access the Target JavaScript File

**Context**: Navigate to the target website and identify publicly accessible JS files that may contain monitoring integrations.

Open the website █████ in a browser and use developer tools (F12) to inspect network requests or view page source.

### Step 2: Inspect and Search for Keys

**Context**: Examine the JS file content for embedded credentials.

In the Sources tab, locate the relevant JS file (e.g., main.js or analytics.js). Search for terms like 'Datadog', 'apiKey', or 'DD_API_KEY'.

**Expected Output**: Lines of code revealing keys, e.g., `apiKey: 'aa123...'` and `applicationKey: 'app456...'`, providing potential unauthorized access to DatadogHQ services.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[api-key-exposure]]
- [[datadog]]
- [[JavaScript]]
