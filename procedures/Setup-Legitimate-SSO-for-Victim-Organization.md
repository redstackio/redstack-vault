---
tags:
  - sso
  - saml
  - setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - SAML SSO
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:34.320Z'
sub_techniques: []
id: 2c94f48e-6242-4828-99aa-716e088b6dde
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Legitimate-SSO-for-Victim-Organization

## Summary

This procedure establishes a functional SAML-based SSO configuration for a Grammarly Business account, serving as the baseline to identify the exact entityId and verify normal authentication flow before exploiting the trimming inconsistency.

## Description

In the context of testing or simulating a victim environment, configure SSO using a controlled Identity Provider (IdP). This step captures the entityId without trailing spaces and confirms that authentication provisions users correctly to the organization. It's essential for reproducing the collision attack, as the flaw relies on matching this identifier precisely.

## Requirements

1. Access to Grammarly Business admin dashboard
2. Control over an IdP supporting SAML 2.0 (e.g., Okta, Azure AD)
3. Valid business account credentials

## Defense

Defensive measures and detection strategies:

- Enforce strict entityId validation with trimming on input and storage
- Monitor for multiple organizations with similar entityIds
- Log all SSO provisioning events for anomalies like unexpected organization redirects

## Objectives

1. Establish verifiable SSO baseline for the target organization
2. Extract the exact entityId for collision crafting
3. Confirm successful user authentication and provisioning

## Instructions

### Step 1: Access SSO Configuration

**Context**: Log in to the Grammarly Business admin panel and navigate to SSO settings to begin configuration.

No specific command; use the web interface to enable SAML SSO and input IdP details.

> Enter the IdP metadata, including the entityId (e.g., 'myentity'), and download Grammarly's SP metadata for your IdP.

### Step 2: Configure IdP and Test Authentication

**Context**: Set up the IdP with the downloaded metadata and perform a test login to validate the flow.

No command; initiate SSO login via the IdP, ensuring the SAML response issuer matches the entityId.

> Successful login redirects to the organization dashboard; user is provisioned if new.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[sso]]
- [[saml]]
- [[setup]]
