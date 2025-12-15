---
tags:
  - saml
  - xml-manipulation
  - bypass
type: procedure
tools:
  - '[[tools/samlbypasspoc.py]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/samlbypasspoc-modify-response]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 979f6aeb-d446-4838-8b14-ae9193e92073
created_at: '2025-12-14T17:31:19.340Z'
updated_at: '2025-12-14T17:31:19.340Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Modify SAML Response Using Bypass POC Script

## Summary

This procedure uses a Python script to prepend a malicious unsigned SAML Response element to a valid signed one, altering assertions for authentication bypass in Rocket.Chat.

## Description

The script parses the input SAMLResponse XML, creates a fake Response with modified attributes (e.g., NameID=admin@domain.com, Email=admin@domain.com, OrganizationName=AdminOrg), and inserts it before the original. The original Signature remains valid for the second Response, but code in saml_utils.js (lines 316, 516) uses the first Response for assertions. This exploits the lack of signed element verification.

## Requirements

1. Python 3 environment with xml.etree.ElementTree
2. Intercepted URL-encoded SAMLResponse
3. Edit script for target-specific assertions

## Defense

Defensive measures and detection strategies:

- Validate that assertions match the signed Response element
- Use XML digital signature libraries with strict canonicalization
- Audit SAML logs for mismatched Response counts

## Objectives

1. Inject malicious assertions without invalidating signature
2. Preserve original XML structure for validation pass
3. Generate new encoded response for forwarding

## Instructions

### Step 1: Prepare Script

**Context**: Customize the POC script for target attributes.

Edit samlbypasspoc.py lines 25+ to set NameID, Email, etc., to desired values (e.g., admin).

> Ensure script handles base64 URL decoding/encoding correctly.

### Step 2: Execute Modification

**Context**: Run the script with intercepted input to generate bypassed response.

Execute [[commands/samlbypasspoc-modify-response]]:

```bash
python3 samlbypasspoc.py <URL_encoded_SAMLResponse>
```

> Input is the base64 URL-encoded string from Burp; output is new encoded string with prepended Response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/samlbypasspoc-modify-response]]

## Tools Used

- [[tools/samlbypasspoc.py]]

## Tags

- [[saml]]
- [[bypass]]
