---
tags:
  - xml-wrapping
  - saml-forgery
type: procedure
tools:
  - '[[tools/XML-Editor]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/modify-xml-signature]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: fffc9e91-d3be-4cdf-8ed4-7b48578418a2
created_at: '2025-12-13T09:01:26.759Z'
updated_at: '2025-12-13T09:01:26.759Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Craft Forged SAML Response

## Summary

This procedure details the creation of a forged SAML response using XML signature wrapping to bypass verification and insert malicious claims for unauthorized user access.

## Description

Attackers manipulate the XML structure to wrap the original signature around forged elements, allowing the response to appear valid while granting access to any user, including administrators, in vulnerable GHES instances.

## Requirements
1. Retrieved SAML metadata XML
2. XML editing tools
3. Understanding of XML signature wrapping techniques

## Defense

Defensive measures and detection strategies:
- Use XML schema validation to prevent wrapping
- Monitor for anomalous SAML responses in logs

## Objectives
1. Forge a valid-looking SAML response
2. Target specific user accounts
3. Ensure signature bypass

## Instructions

### Step 1: Modify XML Structure

**Context**: Alter the XML to wrap the signature around forged assertions.

**Command** ([[commands/modify-xml-signature]]):
```bash
xmlstarlet ed -u '//Assertion/ID' -v 'forged-id' -i '//Assertion' -t elem -n 'MaliciousClaim' -v 'admin-access' metadata.xml > forged.xml
```

> This command inserts malicious claims while preserving the signature.

### Step 2: Validate Forged XML

**Context**: Test the forged XML for structural integrity.

**Command** ([[commands/submit-saml-response]]): (for local validation)
```bash
xmllint --schema saml-schema.xsd forged.xml
```

> Ensures the XML conforms to SAML schema without triggering errors.

## MITRE ATT&CK Mapping

### Tactics
- [[Privilege Escalation]]

### Techniques
- [[Valid Accounts]]

### Sub-Techniques

## Commands Used
- [[commands/modify-xml-signature]]

## Tools Used
- [[tools/XML-Editor]]

## Tags
- [[xml-wrapping]]
- [[saml-forgery]]
