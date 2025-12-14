---
tags:
  - intercept
  - http
  - twitter
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 86b9c683-a404-40ca-8798-ac6a1ed89d0b
created_at: '2025-12-14T17:26:56.517Z'
updated_at: '2025-12-14T17:26:56.517Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Moment-Creation-Request

## Summary

This procedure captures the HTTP POST request for creating a Twitter Moment using Burp Suite, enabling subsequent modification to bypass validation limits.

## Description

In the context of exploiting Twitter's Moments API, interception allows visibility into the JSON payload sent during Moment creation. The target environment is the Twitter web platform, requiring an authenticated session. Expected outcomes include a captured request ready for editing, setting the stage for input validation bypass attacks leading to DoS.

## Requirements

1. Burp Suite installed and running as a proxy
2. Browser configured to route traffic through Burp (e.g., 127.0.0.1:8080)
3. Authenticated Twitter account with access to create Moments
4. Access to https://twitter.com/{username}/moments

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or tool signatures like Burp's CA certificate
- Implement client-side certificate pinning to prevent MITM interception
- Rate-limit API requests to detect anomalous patterns

## Objectives

1. Capture the exact Moments creation endpoint and payload structure
2. Identify frontend-enforced fields like title and description
3. Prepare for payload manipulation without alerting the server

## Instructions

### Step 1: Configure Proxy and Navigate

**Context**: Set up interception by proxying browser traffic through Burp Suite to capture authenticated requests.

In Burp Suite, ensure the Proxy tab is active and listening on the default port. Configure your browser's proxy settings to 127.0.0.1:8080, install Burp's CA certificate if needed, and log in to Twitter.

### Step 2: Initiate Moment Creation

**Context**: Trigger the request by attempting to create a new Moment, allowing Burp to intercept it.

Navigate to https://twitter.com/{username}/moments in the proxied browser. Click the create Moment button (small icon in the middle-right). Burp will intercept the POST request to the Moments creation endpoint.

**Expected Output**: Intercepted request showing JSON payload: {"title":"","description":"","is_production_only":true,"has_owner_granted_location_permission":true}.

### Step 3: Verify and Pause

**Context**: Confirm the request details before proceeding to modification.

In Burp's Intercept tab, inspect the request headers, method (POST), and body. Drop or forward if needed to test, but pause for editing in the next procedure.

**Expected Output**: Request paused with full details visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[http]]
- [[twitter]]
