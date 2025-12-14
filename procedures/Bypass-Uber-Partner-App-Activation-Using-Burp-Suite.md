---
tags:
  - privilege-escalation
  - auth-bypass
  - api-tampering
  - mobile-security
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
updated_at: '2025-12-14T17:28:36.543Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: cb7b08a8-80d3-413b-aaab-580671623219
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Modify Authentication Process]]'
---
# Bypass-Uber-Partner-App-Activation-Using-Burp-Suite

## Summary

This procedure demonstrates how to escalate privileges in the Uber Partner iOS app by tampering with login API requests and responses using Burp Suite, allowing non-activated users to access the app interface despite server-side activation requirements.

## Description

The Uber Partner iOS app performs activation checks during login via API calls, but these rely on client-submitted parameters and responses that can be intercepted and modified. By using a proxy tool like Burp Suite, attackers can alter the 'allowNotActivated' parameter in requests and automate changes to the server's 'isActivated' response from false to true. This grants interface access but does not enable full functionality like going online, as those are enforced server-side. The procedure targets mobile API endpoints and requires proxy configuration on the iOS device.

## Requirements

1. iOS device with Uber Partner app installed and proxy-enabled (e.g., via Burp's CA certificate installed in device trust store)
2. Non-activated Uber Partner account credentials
3. Burp Suite running on a connected machine to intercept mobile traffic
4. Network access to the Uber backend API (typically over HTTPS)

## Defense

Defensive measures and detection strategies:

- Implement server-side re-verification of activation status independent of client parameters
- Use certificate pinning in the iOS app to prevent proxy interception
- Monitor for anomalous API requests with tampered parameters via rate limiting and anomaly detection
- Enforce end-to-end encryption and validate all client inputs on the server

## Objectives

1. Bypass client-side activation checks to gain unauthorized app access
2. Demonstrate insufficient validation in mobile API authentication
3. Expose potential information disclosure in the app interface for non-activated users

## Instructions

### Step 1: Install and Configure the App for Proxy Interception

**Context**: Set up the environment to capture app traffic.

Install the Uber Partner app from the App Store. Configure the iOS device to use Burp Suite as a proxy by installing Burp's CA certificate and setting the proxy in Wi-Fi settings to point to the Burp host (e.g., IP:8080).

### Step 2: Intercept and Modify the Login Request

**Context**: Tamper with the request to attempt bypassing the activation parameter.

Launch the app and start the login process with non-activated credentials. In Burp Suite's Proxy > Intercept tab, capture the login API request (typically a POST to an endpoint like /login). Edit the JSON body to change '"allowNotActivated": false' to '"allowNotActivated": true', then forward the request.

### Step 3: Observe Initial Failure and Set Up Response Tampering

**Context**: The server rejects due to activation status; automate response modification.

After forwarding, the server responds with '"isActivated": false', causing failure. In Burp Suite, go to Proxy > Options > Match and Replace, add a rule: Type=Response body, Match=\"false\", Replace=\"true\" (regex-enabled to target boolean values in JSON).

### Step 4: Retry Login with Combined Tampering

**Context**: Apply both modifications for successful escalation.

Repeat the login: intercept the request, set 'allowNotActivated' to true, forward it. The rule will automatically alter the response's 'isActivated' to true, allowing the app to proceed with login.

**Expected Output**: Successful login screen transition and access to the app dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Modify Authentication Process]] Modify Authentication Process

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- privilege-escalation
- auth-bypass
- api-tampering
- mobile-security
