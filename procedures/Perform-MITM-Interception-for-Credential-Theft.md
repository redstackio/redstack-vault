---
tags:
  - mitm
  - credential-theft
type: procedure
tools:
  - '[[tools/mitmproxy]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Adversary-in-the-Middle]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 91b64d01-5079-440b-afe5-5cafc53db6d2
created_at: '2025-12-13T09:01:26.392Z'
updated_at: '2025-12-13T09:01:26.392Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Perform MITM Interception for Credential Theft

## Summary

This procedure describes intercepting HTTP traffic during the Odnoklassniki SSO redirect to steal victim credentials, enabling Badoo account takeover.

## Description

Using a MITM position, the attacker captures the insecure HTTP request and spoofs the login page to phish credentials. These are then used to authenticate via SSO. The target environment is web-based SSO flows over unencrypted connections. Expected outcome is full access to the victim's Badoo account.

## Requirements

1. MITM tool like mitmproxy
2. Control over victim's network traffic
3. Ability to spoof web pages

## Defense

Defensive measures and detection strategies:

- Use HTTPS everywhere for authentication
- Implement certificate pinning
- Detect anomalous network traffic

## Objectives

1. Intercept and spoof login page
2. Capture credentials
3. Use credentials for takeover

## Instructions

### Step 1: Set Up MITM Proxy

**Context**: Position yourself to intercept traffic.

Configure and run [[tools/mitmproxy]] on the network.

> This allows capturing HTTP requests.

### Step 2: Present Fake Login Page and Capture Credentials

**Context**: Spoof Odnoklassniki login to phish credentials.

When the redirect is intercepted, serve a fake page and log entered credentials.

> Credentials are captured in plain text.

### Step 3: Use Captured Credentials for Login

**Context**: Authenticate to Badoo with stolen credentials.

Navigate to Badoo SSO and input the credentials.

> Attacker gains victim's session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Persistence]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/mitmproxy]]

## Tags

- [[mitm]]
- [[credential-theft]]
