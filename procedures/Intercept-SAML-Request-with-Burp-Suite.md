---
tags:
  - intercept
  - proxy
  - burp
  - saml
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.055Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: 63cf61f7-ff55-4759-aa40-f779c9657b84
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Intercept-SAML-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture and forward an outgoing SAML authentication request to the Repeater module, allowing inspection and modification for XSS injection.

## Description

During the SAML authentication process, the POST request to the ACS endpoint contains the SAMLResponse parameter, which is vulnerable to reflection. By proxying traffic through Burp Suite, attackers can pause the request, analyze its structure, and prepare for payload insertion. This targets web applications like the DoD's Cisco-integrated SAML setup. Prerequisites: Burp Suite installed and browser proxy configured to 127.0.0.1:8080. Expected outcome: Request isolated in Repeater for safe editing without completing the flow.

## Requirements

1. Burp Suite Professional or Community Edition
2. Browser proxy settings configured
3. Target application accessible

## Defense

Defensive measures and detection strategies:

- Deploy proxy detection via HTTP headers (e.g., check for Burp's User-Agent)
- Log all intercepted or delayed requests in authentication endpoints
- Enforce certificate pinning to block proxy tools

## Objectives

1. Capture the SAML POST request
2. Forward to Repeater without execution
3. Identify the SAMLResponse parameter for targeting

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept browser traffic.

Launch Burp Suite and ensure Proxy listener is on port 8080.

Configure browser: Set HTTP proxy to 127.0.0.1:8080.

> Expected output: Traffic routes through Burp; no direct connections to target.

### Step 2: Capture and Forward Request

**Context**: Intercept during authentication submission.

With Intercept on in Proxy > Intercept tab, submit the logon form.

In Burp, click 'Forward' to send to Repeater, or directly 'Send to Repeater'.

> The request to `/+CSCOE+/saml/sp/acs?tgname=a` appears in Repeater. Expected output: Full HTTP request details visible, including body with SAMLResponse.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[saml]]
