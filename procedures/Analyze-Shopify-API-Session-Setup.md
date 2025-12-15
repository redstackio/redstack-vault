---
id: proc-analyze-shopify-001
tags:
  - code-analysis
  - shopify
  - ssrf
type: procedure
tools:
  - '[[tools/pry]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:28.691Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
---

# Analyze-Shopify-API-Session-Setup

## Summary

This procedure involves statically reviewing the Shopify API Ruby SDK code to uncover improper input validation in the Session.setup method, specifically targeting the prepare_url and access_token_request methods for SSRF vulnerabilities.

## Description

In a Ruby environment using the Shopify API SDK, attackers or researchers analyze the source code to identify how unvalidated 'port' and 'protocol' parameters are handled. The prepare_url method appends port directly to the host without sanitization, while access_token_request uses URI.parse on the constructed URL, allowing injections like '@host' to override the target. This enables SSRF by redirecting OAuth token requests to arbitrary hosts, leaking client_id, client_secret, and code in POST data. Prerequisites include access to the SDK source or a decompiler.

## Requirements

1. Ruby environment with Shopify API gem installed
2. Access to SDK source code (e.g., via gem contents)
3. Basic Ruby and URI parsing knowledge

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and whitelisting for port (numeric only) and protocol (http/https only) in SDK configurations
- Monitor for anomalous outbound requests from application servers to internal or unexpected hosts
- Use network segmentation to limit SSRF impact on internal services

## Objectives

1. Identify validation gaps in Session.setup parameters
2. Understand URI parsing tricks enabling host override
3. Prepare for dynamic exploitation testing

## Instructions

### Step 1: Review prepare_url Method

**Context**: Examine how port and protocol are incorporated into the URL without checks.

No specific command; manually inspect SDK source:

- Locate ShopifyAPI::Session class
- Note stripping of protocol, host extraction, and direct port append

> Expected: Confirmation that port is string-appended without type validation.

### Step 2: Review access_token_request Method

**Context**: Analyze URL re-parsing that allows injection exploitation.

No specific command; inspect the method:

- Observe URI construction and POST to /admin/oauth/access_token
- Identify vulnerability to injected '@' in port overriding host

> Expected: Recognition of SSRF vector via URI.parse.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/pry]]

## Tags

- code-analysis
- shopify
- ssrf

---
