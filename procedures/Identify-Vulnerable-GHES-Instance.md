---
tags:
  - recon
  - saml
  - github-enterprise
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/fetch-saml-metadata]]'
platforms:
  - Web
  - GitHub Enterprise Server
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3b698691-ce4f-4861-8558-37828ed74b72
created_at: '2025-12-13T09:01:26.765Z'
updated_at: '2025-12-13T09:01:26.765Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable GHES Instance

## Summary

This procedure involves reconnaissance to identify GitHub Enterprise Server instances vulnerable to XML signature wrapping by locating publicly exposed signed federation metadata XML and confirming SAML configuration weaknesses.

## Description

In this procedure, attackers scan for GHES instances using specific identity providers where SAML metadata is publicly accessible. The focus is on verifying improper validation that allows signature wrapping attacks, setting the stage for forging responses to gain unauthorized access.

## Requirements
1. Network access to the target GHES instance
2. Tools for fetching and analyzing XML data
3. Knowledge of SAML authentication flows

## Defense

Defensive measures and detection strategies:
- Restrict public exposure of SAML metadata XML
- Implement strict signature validation and anti-wrapping protections in SAML processing

## Objectives
1. Confirm vulnerability in SAML setup
2. Retrieve necessary metadata for exploitation
3. Identify target user accounts for access

## Instructions

### Step 1: Fetch SAML Metadata

**Context**: Download the publicly exposed metadata to analyze for vulnerabilities.

**Command** ([[commands/fetch-saml-metadata]]):
```bash
curl -s https://target-ghes.example.com/saml/metadata -o metadata.xml
```

> This command retrieves the XML file containing federation details, which can be inspected for signed elements vulnerable to wrapping.

### Step 2: Analyze Metadata

**Context**: Examine the XML for IdP configurations and signature validation points.

**Command** ([[commands/modify-xml-signature]]): (for analysis, not modification here)
```bash
xmlstarlet sel -t -v '//Signature' metadata.xml
```

> This extracts signature elements to confirm they are present and potentially wrappable.

## MITRE ATT&CK Mapping

### Tactics
- [[Initial Access]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/fetch-saml-metadata]]

## Tools Used
- [[tools/Burp-Suite]]

## Tags
- [[recon]]
- [[saml]]
