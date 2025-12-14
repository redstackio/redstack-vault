---
tags:
  - interception
  - proxy
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:24:56.439Z'
sub_techniques: []
id: f3286ef0-48c4-4a89-8550-d8a883caddc9
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Intercept-HTTP-Request-with-Burp-Proxy

## Summary

This procedure captures HTTP requests to target web application endpoints using Burp Suite's proxy functionality, enabling further manipulation for vulnerability testing such as information disclosure in APIs.

## Description

In the context of testing Discourse forums, this step involves routing browser traffic through Burp Suite to intercept requests to JSON API endpoints like /c/beta-builds/38.json. It sets the foundation for fuzzing by providing a baseline request. Prerequisites include Burp Suite running and browser proxy settings configured to 127.0.0.1:8080. Expected outcome is a captured request revealing the structure, including the enumerable category ID parameter.

## Requirements

1. Burp Suite installed and running with Proxy listener active on port 8080
2. Browser (e.g., Firefox or Chrome) configured to use Burp as HTTP proxy
3. Network access to the target Discourse instance (e.g., community.brave.com)

## Defense

Defensive measures and detection strategies:

- Monitor proxy traffic anomalies or unusual request patterns in web application firewalls (WAFs)
- Implement client certificate pinning or HSTS to detect and block proxy interception

## Objectives

1. Capture a sample API request for enumeration setup
2. Verify endpoint accessibility and response format
3. Prepare for payload injection in subsequent steps

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Ensure Burp Suite is set up to intercept traffic from the browser.

Launch Burp Suite and navigate to the Proxy tab. Confirm the listener is running on 127.0.0.1:8080. No specific command needed as this is GUI-based.

> Burp Proxy intercepts all HTTP(S) traffic routed through it, logging requests in the Intercept or HTTP History sub-tabs.

### Step 2: Route Traffic and Intercept

**Context**: Trigger and capture the target request.

Configure your browser's proxy settings to use 127.0.0.1:8080. Navigate to a category page on the target forum (e.g., https://community.brave.com/c/beta-builds/38) to load the JSON endpoint. In Burp Proxy > Intercept, toggle Intercept on to pause the request, or view in HTTP History if off.

> Successful interception shows the full GET request, including headers and the URL path with category ID (e.g., GET /c/beta-builds/38.json).

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[interception]]
- [[proxy]]
