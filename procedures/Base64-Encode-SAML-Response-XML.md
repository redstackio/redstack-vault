---
tags:
  - encoding
  - saml
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: bd6090ca-529d-440f-ae8b-6db35b057b9f
created_at: '2025-12-11T03:47:39.234Z'
updated_at: '2025-12-11T03:47:39.234Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Base64 Encode SAML Response XML

## Summary

This procedure base64 encodes the forged SAML response XML to prepare it for URL encoding in an HTTP request, facilitating the authentication bypass exploit.

## Description

Encoding is necessary to safely transmit the XML data in POST parameters. This step uses the base64 tool in a shell environment to convert the response.xml file into a base64 string stored in a variable.

## Requirements

1. Forged response.xml file
2. Bash shell with base64 utility
3. Variable assignment for encoded data

## Defense

Defensive measures and detection strategies:

- Monitor HTTP requests for base64-encoded payloads
- Validate all SAML responses server-side

## Objectives

1. Encode XML for transmission
2. Prepare payload for curl request
3. Enable exploit delivery

## Instructions

### Step 1: Encode the XML File

**Context**: Use base64 to encode the file and store in a variable.

**Command** ([[commands/base64-encode-xml]]):
```bash
xml=`base64 response.xml`
```

> This creates a base64 string of the XML content for use in SAMLResponse parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

## Commands Used

- [[commands/base64-encode-xml]]

## Tools Used

- #base64

## Tags

- #encoding
- [[commands/curl-send-forged-saml]]
