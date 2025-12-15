---
tags:
  - saml
  - encoding
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/base64-encode-saml]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.136Z'
sub_techniques: []
id: 9b619192-4233-44d2-a0f8-8e10e16989d8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Base64-Encode-SAML-Response

## Summary

This procedure base64-encodes the crafted SAML XML response to format it for HTTP POST transmission in the SAMLResponse parameter.

## Description

SAML responses must be base64-encoded before URL-encoding and sending via POST. This step uses shell commands to read the XML file and encode its contents, preparing it for the curl exploitation step. In the context of the auth bypass, it ensures the forged response is properly formatted for the plugin's endpoint. Prerequisites: response.xml file; outcomes: encoded string ready for submission.

## Requirements

1. Bash shell environment
2. Crafted response.xml file
3. Base64 utility (standard on Linux/macOS)

## Defense

Defensive measures and detection strategies:

- Validate SAMLResponse length and decoding on ingestion
- Log base64 decoding attempts for anomalies
- Implement request size limits on ACS endpoints

## Objectives

1. Convert XML to base64 string
2. Store in variable for reuse
3. Ensure no corruption during encoding

## Instructions

### Step 1: Encode the XML File

**Context**: Read and base64-encode the entire contents of response.xml.

**Command** ([[commands/base64-encode-saml]]):

```bash
xml=`base64 response.xml`
```

> This captures the base64 output in the 'xml' variable. Expected output: Variable 'xml' contains the encoded string, e.g., starting with 'PHNhb...'

### Step 2: Verify Encoding

**Context**: Decode to confirm integrity.

```bash
echo $xml | base64 -d > test.xml && diff response.xml test.xml
```

> No differences indicate successful encoding. Expected output: Empty diff.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/base64-encode-saml]]

## Tools Used


## Tags

- [[saml]]
- [[encoding]]
