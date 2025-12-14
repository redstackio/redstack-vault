---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - api-key-leak
  - information-disclosure
  - web-inspection
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
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:10.876Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Inspect-Web-Application-for-Exposed-API-Keys

## Summary

This procedure outlines how to manually inspect a web application's client-side code and network traffic to discover exposed API keys, such as the Google Maps API key in Uber's application. It focuses on identifying hardcoded or leaked credentials in JavaScript or HTTP requests, which can lead to unauthorized access if not properly restricted.

## Description

In web applications, API keys are sometimes embedded directly in client-side JavaScript or transmitted in network requests without server-side proxying or IP/domain restrictions, violating best practices. This procedure simulates a security reviewer's approach: loading the application, using browser developer tools to examine source code and monitor network activity, and extracting any visible keys. For the Uber case, the key was found in the application's source code or requests, allowing potential misuse for API queries. Prerequisites include basic knowledge of browser tools; outcomes include key extraction and validation of exposure level (e.g., checking Google's console for restrictions).

## Requirements

1. Modern web browser (e.g., Chrome, Firefox) with developer tools enabled
2. Public access to the target web application (no authentication needed for initial inspection)
3. Basic understanding of HTTP requests and JavaScript

## Defense

Defensive measures and detection strategies:

- Implement server-side API proxying to hide keys from client-side exposure
- Apply Google API restrictions (e.g., HTTP referrers, IP allowlists) to limit key usage
- Use code obfuscation or build tools to remove keys from production bundles; monitor for leaks with static analysis tools like grep or secrets scanners
- Enable API usage alerts in Google Cloud Console to detect anomalous activity

## Objectives

1. Locate and extract the exposed API key from client-side assets
2. Assess the key's restrictions to determine exploitability
3. Document the finding for vulnerability reporting

## Instructions

### Step 1: Load and Inspect Source Code

**Context**: Begin by examining the application's HTML and JavaScript for hardcoded keys, as they may be directly visible in the page source.

Open the target web application (e.g., Uber's site) in your browser. Right-click the page and select "View Page Source" or press Ctrl+U. Search (Ctrl+F) for terms like "AIzaSy" (common Google API key prefix) or "google.maps" to locate embedded keys in script tags or external JS files.

> If a key is found, note its format and context (e.g., passed to new google.maps.Map()). This indicates exposure without restrictions.

### Step 2: Monitor Network Requests

**Context**: API keys often appear in URL parameters during runtime interactions, such as loading maps.

With the page loaded, open Developer Tools (F12). Switch to the Network tab, filter by "XHR" or "JS", and interact with map features (e.g., search for a location in Uber). Look for requests to maps.googleapis.com; inspect the request URL or payload for the API key.

> Successful identification shows the key in query strings like ?key=AIzaSy..., confirming client-side leakage.

### Step 3: Validate Key Exposure

**Context**: Confirm if the key is usable by testing a basic API call, revealing if restrictions mitigate the issue.

Copy the extracted key and test it against a simple Google Maps Geocoding API endpoint (e.g., via browser or curl, if available). Check Google's API console for the key's project to see applied restrictions.

> Expected outcome: If unrestricted, the API responds with data; otherwise, it errors with permission denied.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[api-key-leak]]
- [[information-disclosure]]
- [[web-inspection]]
