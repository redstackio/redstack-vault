---
id: proc-001
tags:
  - intercept
  - access-token
  - cognito
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.449Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Intercept-Flickr-Login-to-Obtain-Access-Token

## Summary

This procedure intercepts the Flickr login request to extract an AWS Cognito access token, enabling subsequent API interactions for account manipulation.

## Description

Flickr uses AWS Cognito for authentication without UI support for email changes, but the API allows it. By intercepting the login POST to https://identity.flickr.com/, an attacker obtains a bearer token to call Cognito endpoints. This step requires a proxy like Burp Suite and the attacker's own credentials. Prerequisites include a valid Flickr account.

## Requirements

1. Proxy tool (e.g., Burp Suite) for request interception
2. Attacker's Flickr email and password
3. Network access to identity.flickr.com

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or intercepted requests in web application firewalls
- Enforce certificate pinning to prevent MITM interception
- Log and alert on access token usage patterns

## Objectives

1. Obtain valid Cognito access token
2. Enable API access to user attributes
3. Prepare for email manipulation

## Instructions

### Step 1: Configure Proxy and Login

**Context**: Set up interception to capture the authentication flow.

Intercept the POST request to https://identity.flickr.com/ with body including AuthFlow: USER_PASSWORD_AUTH, ClientId: 3ck15a1ov4f0d3o97vs3tbjb52, and AuthParameters: USERNAME (attacker's email), PASSWORD, DEVICE_KEY.

> Submit the login form through the proxy. The response will include the access token in AuthenticationResult.AccessToken.

### Step 2: Extract Token

**Context**: Parse the response to isolate the token.

Copy the AccessToken value (starts with eyJraWQiOiJPVj...).

> Ensure the token is valid by testing a simple API call if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[intercept]]
- [[access-token]]
- [[cognito]]
