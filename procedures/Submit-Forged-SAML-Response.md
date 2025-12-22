---
tags:
  - exploit
  - access-gain
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/submit-saml-response]]'
platforms:
  - Web
  - GitHub Enterprise Server
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: d32d138b-627f-4b62-9673-f0df64de3399
created_at: '2025-12-13T09:01:26.755Z'
updated_at: '2025-12-13T09:01:26.755Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit Forged SAML Response

## Summary

This procedure covers submitting the forged SAML response to the GHES instance to achieve unauthorized access without authentication.

## Description

By posting the wrapped XML to the SAML assertion consumer service, attackers bypass verification and gain access to targeted accounts, enabling full control over the instance.

## Requirements
1. Forged SAML response XML
2. Access to the GHES SAML endpoint
3. Proxy tools for submission

## Defense

Defensive measures and detection strategies:
- Enforce strict SAML response validation
- Log and alert on unexpected user provisioning

## Objectives
1. Gain unauthorized access
2. Provision or access admin accounts
3. Validate successful exploitation

## Instructions

### Step 1: Submit Response

**Context**: Send the forged XML to the ACS endpoint.

**Command** ([[commands/submit-saml-response]]):
```bash
curl -X POST https://target-ghes.example.com/saml/acs -d @forged.xml --header 'Content-Type: application/xml'
```

> This submits the response, triggering the bypass and access grant.

### Step 2: Verify Access

**Context**: Confirm gained access by attempting privileged actions.

**Command** ([[commands/fetch-saml-metadata]]): (for verification)
```bash
curl -s https://target-ghes.example.com/api/v3/user --header 'Authorization: Bearer gained-token'
```

> Retrieves user details to confirm admin privileges.

## MITRE ATT&CK Mapping

### Tactics
- [[Initial Access]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/submit-saml-response]]

## Tools Used
- [[tools/Burp-Suite]]

## Tags
- [[exploit]]
- [[access-gain]]
