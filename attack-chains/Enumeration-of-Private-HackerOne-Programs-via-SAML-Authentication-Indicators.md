---
tags:
  - saml
  - information-disclosure
  - enumeration
  - hackerone
  - reconnaissance
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Detect-Private-Programs-through-SAML-Indicators]]'
step_count: 1
techniques:
  - '[[Account Discovery]]'
description: >-
  A reconnaissance technique exploiting information disclosure in SAML
  authentication to detect the existence of private programs on HackerOne,
  bypassing intended privacy controls.
skill_level: intermediate
impact_level: medium
id: 2ac050bf-3fed-4e45-a73e-428a821b8f48
created_at: '2025-12-14T17:29:36.766Z'
updated_at: '2025-12-14T17:29:36.766Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumeration of Private HackerOne Programs via SAML Authentication Indicators

## Overview

This attack chain demonstrates a reconnaissance workflow that leverages an information disclosure vulnerability in HackerOne's SAML authentication system for private programs. By analyzing SAML-related indicators during authentication flows, attackers can enumerate the existence of private programs that are intended to remain hidden. The technique relies on detectable artifacts in SAML responses or metadata that reveal program details without direct access. This was reported in HackerOne report #167828 and led to system improvements for better obfuscation of SAML usage.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Authenticate via SAML] --> B[Analyze Indicators]
    B --> C[Enumerate Private Programs]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or a web proxy like Burp Suite for inspecting network traffic

### Target Environment

- HackerOne platform (web-based)
- SAML-enabled authentication for private programs
- No special ports required; standard HTTPS (443)

### Initial Access Requirements

- Valid HackerOne account (public or invited)
- Ability to initiate SAML authentication flows
- Network access to HackerOne's web services

## Detailed Attack Procedures

### Step 1: SAML Authentication Analysis
procedure: [[procedures/Detect-Private-Programs-through-SAML-Indicators]]

**Objective**: Identify and analyze SAML indicators to detect the presence of private programs without explicit access.

**Instructions**: Initiate a SAML authentication attempt on HackerOne, targeting areas associated with program access. Use browser developer tools to inspect network requests and responses for SAML assertions, entity IDs, or metadata that inadvertently reveal private program names or existence. Look for patterns such as unique SAML endpoints or response attributes that differ for private vs. public programs.

**Expected Output**: Network logs or captured SAML XML showing indicators like program-specific identifiers in assertions.

**Success Indicators**:
- Detection of SAML artifacts tied to undocumented private programs
- Confirmation of program existence through non-obfuscated indicators

## Attack Chain Summary

### Key Achievements

1. Successful enumeration of private program existence via SAML disclosure
2. Bypassing privacy controls intended for HackerOne private programs
3. Highlighting the need for SAML obfuscation in authentication systems

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01*
