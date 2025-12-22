---
tags:
  - http-post
  - exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 81ea6eea-2005-49ac-98b1-74095424207a
created_at: '2025-12-11T03:47:39.227Z'
updated_at: '2025-12-11T03:47:39.227Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Send Forged SAML Response via HTTP POST

## Summary

This procedure sends the base64-encoded forged SAML response via an HTTP POST request to the plugin's endpoint, exploiting the bypass to receive authentication cookies.

## Description

Using curl, the request targets the /onelogin_saml.php?acs endpoint with RelayState and SAMLResponse parameters, resulting in unauthorized login. This affects WordPress sites like Uber's.

## Requirements

1. Base64-encoded XML variable
2. Target URL with vulnerable plugin
3. Curl installed

## Defense

Defensive measures and detection strategies:

- Patch the plugin to require signatures
- Log and alert on unsigned SAML requests

## Objectives

1. Deliver exploit payload
2. Obtain authentication cookies
3. Achieve initial access

## Instructions

### Step 1: Execute Curl Request

**Context**: POST the parameters to the endpoint.

**Command** ([[commands/curl-send-forged-saml]]):
```bash
curl -v 'https://newsroom.uber.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs' --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
```

> Expect a 302 response with Set-Cookie headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

- [[commands/curl-send-forged-saml]]

## Tools Used

- #curl

## Tags

- #http-post
- [[Exploit]]
