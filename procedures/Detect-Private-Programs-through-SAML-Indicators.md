---
tags:
  - saml
  - information-disclosure
  - enumeration
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 886b0d55-2a32-49b6-a9c8-5cf6eac07e31
created_at: '2025-12-14T17:29:36.761Z'
updated_at: '2025-12-14T17:29:36.761Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Detect-Private-Programs-through-SAML-Indicators

## Summary

This procedure exploits an information disclosure in HackerOne's SAML authentication for private programs by analyzing authentication flows to detect indicators of hidden programs' existence, such as unique entity IDs or response attributes, without requiring direct access or credentials for those programs.

## Description

In the context of HackerOne's platform, private programs are designed to be non-discoverable to maintain confidentiality for bug bounty teams. However, SAML authentication handling exposes subtle indicators—like specific SAML metadata or assertion patterns—that reveal these programs during login attempts. The attacker monitors web traffic during SAML SSO flows, identifying discrepancies that confirm private program presence. This technique is passive reconnaissance, relying on standard web interactions, and was mitigated by HackerOne through enhanced SAML obfuscation.

## Requirements

1. Access to a HackerOne account capable of initiating SAML authentication
2. Tools for web traffic inspection (e.g., browser dev tools or proxy)
3. Knowledge of SAML protocol basics to parse responses

## Defense

Defensive measures and detection strategies:

- Obfuscate SAML endpoints and metadata to avoid unique identifiers for private entities
- Implement rate limiting on authentication attempts to hinder enumeration
- Monitor for anomalous SAML request patterns or traffic inspection attempts via WAF logs

## Objectives

1. Enumerate existence of private HackerOne programs
2. Gather intelligence on target program's privacy status
3. Validate non-discoverability assumptions in SAML-based systems

## Instructions

### Step 1: Initiate SAML Authentication Flow

**Context**: Start a login process on HackerOne that triggers SAML authentication, targeting program selection or access points.

Navigate to the HackerOne login page and select SAML SSO. Observe the redirect to the identity provider and back. No specific command; use manual browser interaction.

> During this, SAML requests will be sent over HTTPS; ensure proxy interception if needed.

### Step 2: Inspect SAML Responses for Indicators

**Context**: Capture and analyze the SAML assertion or metadata in the authentication response for private program hints.

Use developer tools (F12 in browser) to monitor the Network tab. Filter for SAML-related endpoints (e.g., /saml or ACS URLs). Look for XML elements containing program names, IDs, or attributes unique to private setups.

> Expected: XML like <saml:Attribute Name="program_id">private-program-slug</saml:Attribute> or similar non-obfuscated data.

### Step 3: Correlate and Validate Findings

**Context**: Cross-reference detected indicators against known public programs to confirm private status.

Manually note any discrepancies, such as unexpected entityIDs or audience restrictions pointing to private teams. Repeat for multiple login attempts if needed to build a list.

> Success: List of inferred private programs based on SAML artifacts.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[saml]]
- [[information-disclosure]]
- [[enumeration]]
- [[hackerone]]
