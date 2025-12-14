---
id: proc-saml-bypass-improper-verif
tags:
  - saml
  - auth-bypass
  - verification-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.624Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-SAML-Authentication-via-Improper-Verification

## Summary

This procedure exploits improper verification of SAML assertions in the authentication flow of web applications like uchat.uberinternal.com, allowing attackers to bypass identity providers such as OneLogin and gain unauthorized access to protected resources, such as internal chat systems.

## Description

In SAML-based single sign-on (SSO), the service provider (SP) relies on the identity provider (IdP) to authenticate users via XML assertions. If the SP fails to properly validate signatures, issuers, or other assertion elements, an attacker can intercept the SAML response, tamper with it (e.g., remove the signature or forge attributes), and submit a modified version to impersonate a valid user. This was the case in Uber's internal chat app, where bug bounty testing revealed the flaw, leading to full access without legitimate credentials. The attack targets the Assertion Consumer Service (ACS) endpoint and requires intercepting the POST request during login. Expected outcomes include session establishment and access to sensitive data.

## Requirements

1. Proxy tool like Burp Suite for traffic interception and modification
2. Network access to the target SP endpoint (e.g., https://uchat.uberinternal.com/)
3. Knowledge of SAML flow: Ability to initiate login and identify the SAML response
4. Browser configured for proxying (e.g., Firefox with FoxyProxy)

## Defense

Defensive measures and detection strategies:

- Enforce strict SAML signature validation and certificate pinning on the SP
- Implement XML signature canonicalization and schema validation to prevent tampering
- Monitor for anomalous login patterns, such as rapid successive login attempts or unexpected IP sources
- Use IdP-side logging to detect forged assertions and integrate with SIEM for alerts on bypass attempts

## Objectives

1. Intercept and modify SAML response to evade authentication checks
2. Establish a valid session on the target application
3. Access protected internal resources, such as chat communications

## Instructions

### Step 1: Configure Proxy Interception

**Context**: Set up Burp Suite to capture HTTPS traffic during the SAML login flow, ensuring all requests to the target domain are intercepted.

No specific command; configure Burp listener on port 8080 and set browser proxy accordingly.

> Launch Burp Suite, enable Intercept in Proxy tab, and import CA certificate into browser trust store. Expected: All traffic routed through Burp.

### Step 2: Initiate SAML Login Flow

**Context**: Start the authentication process to trigger the SAML redirect to OneLogin and back, allowing capture of the response.

Navigate to https://uchat.uberinternal.com/ in the proxied browser and click login.

> The flow redirects to OneLogin; do not complete legitimate auth. Expected: Intercept points at IdP redirect and ACS POST.

### Step 3: Intercept and Modify SAML Response

**Context**: Capture the SAML assertion POST to the ACS endpoint, then tamper with the XML to bypass verification (e.g., remove <Signature> element).

In Burp Repeater or Intruder:

1. Forward initial requests until SAML response is captured.
2. Edit the raw POST body: Locate the SAMLResponse base64, decode, remove or alter the ds:Signature section.
3. Re-encode and forward.

> Example modification: Change <saml:Assertion> attributes to forge user ID or remove signature validation requirements. Expected: Server accepts tampered assertion without error.

### Step 4: Validate Access

**Context**: Confirm bypass by checking for successful session and resource access.

Post-forward, observe redirect to app dashboard.

> Expected: Access to internal chats without OneLogin credentials. If failed, iterate on modifications (e.g., issuer mismatch fix).

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
- [[auth-bypass]]
- [[web]]
