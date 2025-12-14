---
id: proc-intercept-instacart-login
tags:
  - traffic-interception
  - api-capture
type: procedure
tools:
  - '[[tools/BurpSuite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:41.841Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept Instacart Login Request

## Summary

This procedure captures a login request from the Instacart iOS app using a proxy, revealing the OAuth token endpoint and authentication parameters for subsequent analysis or exploitation.

## Description

The Instacart iOS app uses a POST request to https://www.instacart.com/oauth/token for authentication. By intercepting this with BurpSuite, testers can examine headers, body (typically JSON with username, password, grant_type=client_credentials or password), and responses (401 Unauthorized for failures, 200 OK with token for success). This step assumes proxy setup is complete and focuses on triggering the request via app interaction.

## Requirements

1. Proxy configured and trusted on iOS device
2. Instacart app installed and updated
3. Valid or test username for login attempt
4. BurpSuite running with interception enabled

## Defense

Defensive measures and detection strategies:

- Enforce SSL/TLS pinning to block proxy tools like Burp
- Log and alert on anomalous API request patterns from mobile clients
- Use behavioral analytics to detect repeated failed logins from proxied IPs

## Objectives

1. Capture the exact login endpoint and payload structure
2. Identify response codes for valid/invalid attempts
3. Prepare for request replay in brute force scenarios

## Instructions

### Step 1: Trigger Login in App

**Context**: Initiate a login to generate the request.

Open the Instacart app, navigate to the sign-in screen, enter a username/email and any password, and submit. Ensure the device is connected via the proxy.

### Step 2: View Intercepted Request in Burp

**Context**: Locate and analyze the captured traffic.

In BurpSuite Proxy > HTTP history, filter for POST requests to instacart.com. Select the /oauth/token request, inspect the raw view: headers (Authorization: Basic base64(client_id:secret), Content-Type: application/json), body ({"username":"test@example.com","password":"wrong","grant_type":"password"}), and response.

### Step 3: Forward and Verify

**Context**: Ensure the request completes without alerting the app.

If intercepted, forward the request in Burp to allow the app to receive the response. Check app behavior (e.g., error message for 401) to confirm seamless proxying.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/BurpSuite]]

## Tags

- [[traffic-interception]]
- [[api-capture]]
