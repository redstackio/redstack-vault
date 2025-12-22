---
tags:
  - api-key-exposure
  - information-disclosure
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:48.260Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: b4933de4-ab8d-4a9e-aa29-2a6099d96fc9
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Discover-Exposed-API-Keys-in-Client-Side-Code

## Summary

This procedure outlines how to inspect publicly accessible client-side JavaScript files to discover embedded API keys, such as Google Maps API keys, that lack proper restrictions. It focuses on source code review to identify information disclosure vulnerabilities that could lead to unauthorized service abuse and billing impacts.

## Description

In web applications, API keys are sometimes embedded directly in client-side JavaScript for convenience, but without restrictions like IP allowlists or HTTP referrer limits, they become vulnerable to extraction and misuse. This procedure simulates reconnaissance by loading the target site, inspecting loaded scripts, and searching for key patterns. In the reported case, the key in █.8x8.vc/index.js was unrestricted, allowing potential quota exhaustion on Google Maps services. Prerequisites include basic web access; no authentication is needed. Expected outcomes include key extraction and validation via Google's API console.

## Requirements

1. Web browser with Developer Tools (e.g., Chrome DevTools)
2. Access to the public target URL (e.g., https://█.8x8.vc/)
3. Optional: Command-line tools like curl and grep for automated searching

## Defense

Defensive measures and detection strategies:

- Implement API key restrictions (e.g., HTTP referrers, IP allowlists) in Google Cloud Console
- Use server-side proxying for API calls to hide keys from client-side code
- Regularly scan JavaScript files for sensitive strings using tools like git-secrets or TruffleHog
- Monitor API usage for anomalous patterns indicating abuse

## Objectives

1. Extract unrestricted API keys from client-side resources
2. Assess potential for service abuse and quota exhaustion
3. Report the vulnerability to prevent billing impacts

## Instructions

### Step 1: Load and Inspect the Target Website

**Context**: Access the target site to identify loaded JavaScript files containing potential secrets.

Open the target URL in a browser and use Developer Tools to view the Sources or Network tab. Look for files like index.js.

No specific command, but manually right-click the page > View Page Source, or use browser console to log scripts.

> Expected output: List of JS files; download index.js for review.

### Step 2: Search for API Key Patterns

**Context**: Scan the JavaScript content for Google API key signatures to confirm exposure.

Download the file if needed, then search for 'AIzaSy' patterns.

Using curl and grep (if on a terminal):

```bash
curl https://█.8x8.vc/index.js -s | grep -i 'AIzaSy'
```

> This command fetches the JS file silently and greps for the key prefix. Expected output: Lines containing the full API key, e.g., var apiKey = 'AIzaSyD...'; Confirm by testing the key in a Google Maps embed URL.

### Step 3: Validate Key Restrictions

**Context**: Check if the extracted key has limitations to assess abuse potential.

Paste the key into Google's API key restriction settings (via Cloud Console, if accessible) or test by making unauthorized API calls, e.g., via curl to maps.googleapis.com.

```bash
curl "https://maps.googleapis.com/maps/api/geocode/json?address=Test&key=YOUR_EXTRACTED_KEY"
```

> Expected output: Successful JSON response if unrestricted, indicating vulnerability. Error if restricted.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[api-key-exposure]]
- [[information-disclosure]]
