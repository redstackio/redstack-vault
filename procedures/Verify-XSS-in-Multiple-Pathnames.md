---
id: proc-acronis-verify-pathnames-001
tags:
  - xss
  - vulnerability-verification
  - scope-expansion
type: procedure
tools:
  - '[[tools/VPN]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.673Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-XSS-in-Multiple-Pathnames

## Summary

This procedure tests the reflected XSS vulnerability across various pathnames on the Acronis site by injecting payloads into general query parameters, confirming site-wide impact and potential for broader exploitation.

## Description

The initial vulnerability in the trial page suggests poor query parameter handling site-wide. By testing payloads like 'tomblorg`(alert)();//' on URLs such as https://www.acronis.com/, attackers can verify execution in different contexts. Use VPN for non-USA testing. This expands the attack surface for data collection or manipulation.

## Requirements

1. VPN for location simulation
2. List of target pathnames (e.g., homepage, other products)
3. Browser tools for inspection

## Defense

Defensive measures and detection strategies:

- Centralized input validation for all query parameters
- Regular vulnerability scanning with tools like OWASP ZAP
- Implement strict output encoding across the entire application

## Objectives

1. Confirm XSS trigger in non-trial pathnames
2. Assess site-wide risk
3. Identify patterns in reflection for advanced payloads

## Instructions

### Step 1: Select Test Pathnames

**Context**: Choose diverse URLs to test parameter handling consistency.

Target examples: https://www.acronis.com/, https://www.acronis.com/products/other/.

> Focus on pages that accept arbitrary query parameters.

### Step 2: Inject and Test Payload

**Context**: Append payloads to query parameters and verify execution.

Using VPN (non-USA), load https://www.acronis.com/?tomblorg`(alert)();//' and check for alert execution. Repeat for other paths.

> Expected: Consistent JS alerts, indicating global vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/VPN]]

## Tags

- [[xss]]
- [[verification]]
