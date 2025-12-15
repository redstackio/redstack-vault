---
tags:
  - saml
  - interception
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8dc1daea-c005-40d9-8572-b9089b325800
created_at: '2025-12-14T17:31:19.342Z'
updated_at: '2025-12-14T17:31:19.342Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept SAML Login Request with Burp Suite

## Summary

This procedure uses Burp Suite to capture the SAMLResponse during Rocket.Chat login, allowing extraction of the base64 URL-encoded response for modification.

## Description

The SAML flow involves posting a signed SAMLResponse to Rocket.Chat's login endpoint. Intercepting this with a proxy like Burp Suite enables viewing and altering the parameter. Prerequisites include SAML setup and Burp's CA certificate installed in the browser for HTTPS interception. This targets web-based SAML implementations.

## Requirements

1. Burp Suite running with proxy listener on port 8080
2. Browser configured to use Burp proxy (e.g., FoxyProxy extension)
3. Active SAML configuration in Rocket.Chat

## Defense

Defensive measures and detection strategies:

- Enforce HSTS and certificate pinning to hinder proxy interception
- Log and alert on proxy-like traffic patterns
- Use mutual TLS for SAML endpoints

## Objectives

1. Capture the legitimate SAMLResponse
2. Extract URL-encoded value for input to modification script
3. Ensure interception without disrupting the flow

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept traffic from the browser.

No command; in Burp, go to Proxy > Options, ensure Intercept is on, and set browser to proxy via 127.0.0.1:8080.

> Install Burp CA in browser trust store to decrypt HTTPS.

### Step 2: Initiate and Intercept Login

**Context**: Start SAML login and pause the request.

Navigate to Rocket.Chat login, select SAML, complete IdP auth if needed, and intercept the POST to /auth/saml.

> Request body contains SAMLResponse=... (base64 URL-encoded).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[saml]]
- [[interception]]
