---
tags:
  - saml
  - authentication
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:20.058Z'
skill_level: beginner
impact_level: low
sub_techniques: []
id: 3044bcb6-5cd0-4950-a55f-f52876608840
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-SAML-Authentication-Flow

## Summary

This procedure accesses the logon page of a web application using SAML authentication, initiating the flow that exposes the vulnerable SAMLResponse parameter for subsequent interception and exploitation.

## Description

In the context of exploiting reflected XSS in SAML endpoints, this step navigates to the target's logon page with specific parameters to start the authentication process. The U.S. Department of Defense application in question uses a Cisco-based path (`+CSCOE+`), and the flow generates a POST request to the SAML assertion consumer service (ACS) endpoint. Prerequisites include network access to the target URL; no credentials are needed as this is the unauthenticated entry point. Expected outcome is the preparation of a modifiable SAML request.

## Requirements

1. Web browser (e.g., Firefox or Chrome)
2. Network connectivity to the target domain
3. Proxy configuration if interception is planned immediately after

## Defense

Defensive measures and detection strategies:

- Implement URL access controls and rate limiting on logon pages
- Monitor for unusual parameter values in authentication logs
- Use web application firewalls (WAF) to block anomalous access patterns

## Objectives

1. Trigger the SAML authentication initiation
2. Generate the vulnerable POST request
3. Position for request interception without alerting defenses

## Instructions

### Step 1: Access Logon Page

**Context**: Directly navigate to the logon endpoint to begin the SAML flow.

No specific command; use browser URL bar:

Open `https://███/+CSCOE+/logon.html?a0=15&a1=&a2=&a3=1`

> This loads the page and prepares the authentication submission. Expected output: Page renders with logon form; inspect network tab to see the impending POST request.

### Step 2: Submit Initial Request

**Context**: Proceed with the logon to generate the SAML POST, ready for proxy capture.

No command; interact with the form:

Click submit or equivalent to send the request to `/+CSCOE+/saml/sp/acs?tgname=a`

> The request body includes the SAMLResponse parameter. Do not complete authentication; intercept instead.

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

- [[saml]]
- [[authentication]]
