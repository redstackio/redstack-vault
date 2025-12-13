---
tags:
  - saml
  - recon
  - authentication
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
id: ac2e63e2-d801-4f79-a34d-cfdc9bf62c2d
created_at: '2025-12-13T09:01:26.608Z'
updated_at: '2025-12-13T09:01:26.608Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify SAML Authentication Endpoint

## Summary

This procedure involves identifying and mapping the SAML authentication endpoints in a web application, specifically targeting services like OneLogin to understand the authentication flow for potential exploitation.

## Description

In this procedure, the attacker intercepts traffic to the target application to capture SAML requests and responses. This is crucial for understanding how authentication is handled and identifying weaknesses in verification processes, such as those found in Uber's uchat.uberinternal.com.

## Requirements
1. Access to a web proxy tool like Burp Suite
2. Network access to the target URL
3. Basic knowledge of SAML protocol

## Defense

Defensive measures and detection strategies:
- Implement strict SAML signature validation
- Monitor for anomalous authentication attempts in logs

## Objectives
1. Map the SAML authentication flow
2. Capture request/response data
3. Identify potential bypass points

## Instructions

### Step 1: Set Up Proxy

**Context**: Configure a proxy to intercept traffic to the target.

Configure [[tools/Burp-Suite]] to intercept requests to https://uchat.uberinternal.com.

> This allows visibility into the authentication process.

### Step 2: Capture SAML Traffic

**Context**: Initiate login and capture SAML data.

Navigate to the login page and submit credentials to trigger the SAML flow, capturing the XML assertions.

> Expected: SAMLResponse parameter in the POST request.

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
- saml
- recon
