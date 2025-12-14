---
tags:
  - xss
  - oauth
  - redirect
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-oauth-access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:07.909Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f6d57ac1-529b-40b8-a35d-d1c029c74bbd
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-OAuth-Authorization-Redirect

## Summary

Access the OAuth endpoint with the malicious redirect_uri to load the authorization page, setting up the redirect that will execute the XSS payload upon user interaction.

## Description

By accessing the crafted URL, the endpoint processes the request and displays an authorization consent page. Clicking Allow or Deny initiates a 302 redirect to the unvalidated redirect_uri via Location header. In vulnerable browsers, this executes the javascript: payload directly; otherwise, a fallback HTML error page includes a clickable link to the URI, enabling manual execution.

## Requirements

1. Crafted URL from prior procedure
2. Vulnerable browser (e.g., Opera Mini, older Firefox)
3. No authentication required for testing

## Defense

Defensive measures and detection strategies:

- Enforce user confirmation for redirects to non-standard schemes
- Log and alert on javascript: or data: URIs in OAuth requests
- Disable auto-follow for 302 redirects in client configurations

## Objectives

1. Load the authorization interface
2. Simulate user consent to trigger redirect
3. Confirm redirect to malicious URI

## Instructions

### Step 1: Access the Endpoint

**Context**: Navigate to the OAuth URL to initiate the flow.

**Command** ([[commands/curl-oauth-access]]):
```bash
curl -i "https://login.uber.com/oauth/authorize?client_id=MXeE1dl-5R3yTCbufMHsfz3KhfY2UGyS&response_type=code&scope=profile&redirect_uri=javascript:%2F%2Fgoog.com%2F%250Aalert%28document.domain%29%3B%2F%2F"
```

> Use curl for initial verification (check for 200 OK and consent page HTML). For execution, open in browser. Expected: Consent page HTML in response.

### Step 2: Interact with Page

**Context**: Click button to trigger redirect.

Open the URL in browser and click Allow or Deny.

> Expected: 302 response with Location: javascript:... header.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-oauth-access]]

## Tools Used


## Tags

- xss
- redirect
- oauth
