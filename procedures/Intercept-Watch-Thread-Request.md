---
tags:
  - recon
  - intercept
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:28.991Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 31262e2d-7b2b-48fe-aea5-5bd212acd18b
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Intercept-Watch-Thread-Request

## Summary

This procedure uses a proxy tool to capture the HTTP POST request sent to the Chameleon API when a user clicks 'Watch Thread' in TopCoder forums, revealing the structure of the vulnerable endpoint for IDOR exploitation.

## Description

The 'Watch Thread' action in TopCoder forums sends a POST request to https://fast.trychameleon.com/observe/v2/profiles/{uid}, including user profile data. Intercepting this request allows inspection of parameters like 'uid', which can later be manipulated. Burp Suite's Proxy and Repeater modules are essential for this non-destructive reconnaissance step. Prerequisites include an active TopCoder session and proxy configuration in the browser.

## Requirements

1. Burp Suite installed and running
2. Browser proxy set to Burp (e.g., 127.0.0.1:8080)
3. Logged-in TopCoder forum session

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and certificate pinning to prevent proxy interception
- Log and alert on proxy-like User-Agent strings or unusual request patterns
- Use Web Application Firewall (WAF) to detect interception attempts

## Objectives

1. Capture the legitimate API request payload
2. Identify the 'uid' parameter for modification
3. Forward request to Repeater for tampering

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept traffic from the browser.

Launch Burp Suite, ensure Proxy listener is on port 8080, and configure browser to use it as HTTP proxy.

**Expected Output**: Traffic routed through Burp.

### Step 2: Trigger Watch Thread

**Context**: Perform the action that generates the API call.

In the forum thread, click the 'Watch Thread' button while Intercept is enabled in Burp Proxy.

**Expected Output**: Request paused in Burp with POST to /observe/v2/profiles/.

### Step 3: Forward to Repeater

**Context**: Prepare the request for modification.

In Burp, forward the intercepted request and send it to the Repeater tab.

**Expected Output**: Request loaded in Repeater with full headers and body.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- recon
- intercept
