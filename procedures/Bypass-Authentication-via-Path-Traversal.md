---
tags:
  - auth-bypass
  - access-control
  - onelogin
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-path-traversal-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:44.967Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3fb0e36f-225e-4226-8d2b-0e9852cca277
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Authentication via Path Traversal

## Summary

This procedure exploits a path traversal vulnerability to circumvent OneLogin authentication in a multi-layered web architecture, granting unauthorized access to protected subdomain resources on uberinternal.com.

## Description

In architectures integrating OneLogin for authentication, the web server may not enforce checks on traversed paths, allowing direct access to internal subdomains. By manipulating file paths to escape boundaries, attackers can view sensitive content without credentials. This targets improper access control where authentication is only applied to standard paths. Prerequisites: Confirmed path traversal vulnerability and knowledge of subdomain structure. Outcomes include exposure of internal data, potentially leading to further compromise.

## Requirements

1. Valid path traversal exploit confirmed from prior procedure
2. Identification of protected subdomain paths (e.g., via reconnaissance)
3. HTTP client capable of handling redirects and cookies

## Defense

Defensive measures and detection strategies:

- Enforce authentication at the application layer for all paths, including traversed ones
- Use path normalization and canonicalization to prevent traversal
- Implement logging and alerting for requests bypassing auth flows, such as direct subdomain hits

## Objectives

1. Access protected resources without OneLogin intervention
2. Extract sensitive internal content from subdomains
3. Validate the bypass for potential escalation

## Instructions

### Step 1: Craft Traversal to Authenticated Path

**Context**: Use traversal to directly target a resource behind OneLogin without hitting the login endpoint.

**Command** ([[commands/curl-path-traversal-test]]):
```bash
curl -X GET "https://uberinternal.com/path?file=../../protected.subdomain.internal/resource.html" -v
```

> The response should return the resource content directly. If redirected to login, increase traversal depth or encode payloads (e.g., %252e%252e%252f for double-encoded '../').

### Step 2: Verify and Extract Content

**Context**: Confirm no authentication is required and retrieve full content.

**Command** ([[commands/curl-path-traversal-test]]):
```bash
curl -X GET "https://uberinternal.com/path?file=../../protected.subdomain.internal/sensitive/data" --output extracted_content.txt -v
```

> Save output to a file for analysis. Success shows no 401/403 errors and valid data in the response body.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-path-traversal-test]]

## Tools Used


## Tags

- auth-bypass
- access-control
