---
id: proc-kadira-cache-trigger
tags:
  - client-side-caching
  - kadira
  - api-key
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
  - Browser
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Archive Collected Data]]'
updated_at: '2025-12-14T17:32:01.712Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Archive Collected Data]]'
---
# Trigger-API-Key-Caching-in-Kadira

## Summary

This procedure simulates legitimate user interaction in Kadira's web application to trigger the caching of sensitive API keys client-side, exploiting the lack of proper Cache-Control headers to make keys recoverable from browser storage.

## Description

In Kadira's dashboard, users can input and save API keys via a dedicated button. The application's backend responds with the keys in plaintext without setting Cache-Control: no-cache, private, or no-store headers. As a result, modern browsers cache these responses in their HTTP cache or local storage, persisting the sensitive data. This procedure outlines how an attacker with device access can induce this caching, setting up for subsequent extraction. It targets web environments and assumes the victim has already interacted with or can be prompted to interact with the save feature. Expected outcomes include keys stored in accessible browser locations like Chrome's Cache folder or IndexedDB.

## Requirements

1. Access to the victim's browser session on Kadira's web app (https://kadira.io or similar)
2. Valid user credentials for the Kadira account (or social engineering to prompt saving)
3. Standard web browser (e.g., Chrome, Firefox) on the target device

## Defense

Defensive measures and detection strategies:

- Implement strict Cache-Control: no-store, private headers on all responses containing sensitive data
- Use HTTPS and Content-Security-Policy to limit client-side storage
- Monitor for anomalous browser cache access via endpoint detection tools like OSQuery

## Objectives

1. Induce storage of API keys in browser cache
2. Bypass implicit server-side protections against disclosure
3. Prepare for forensic recovery of keys

## Instructions

### Step 1: Access Kadira Dashboard

**Context**: Log in to the Kadira web application to reach the API key management section.

Navigate to the API settings page and prepare to input or edit keys.

### Step 2: Save API Keys

**Context**: Interact with the save button to trigger the vulnerable response.

Enter sample or real API keys in the form fields, then click the "Save" button. This sends a POST request to the backend, which echoes the keys in the response without cache protections.

**Expected Output**: Success message in the UI; keys now cached in browser.

### Step 3: Verify Caching

**Context**: Confirm the keys are stored client-side using dev tools.

Open browser DevTools (F12), navigate to Network tab, reproduce the save action, and inspect the response headers for missing Cache-Control directives.

**Expected Output**: Response body shows keys; cache entry visible in Application > Cache Storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Archive Collected Data]] Archive Collected Data (adapted for caching evasion)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[client-side-caching]]
- [[kadira]]
- [[api-key]]
