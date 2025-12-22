---
id: proc-uuid-1
tags:
  - ssrf
  - code-review
  - shopify
type: procedure
tools:
  - '[[tools/pry]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/require-shopify-api]]'
verified: false
platforms:
  - Ruby
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:18.776Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Analyze-Shopify-API-SDK-for-Input-Validation-Flaws

## Summary

This procedure involves static code analysis of the Shopify API Ruby SDK to identify improper input validation in the Session.setup method, specifically for 'port' and 'protocol' parameters, revealing opportunities for SSRF via arbitrary domain injection.

## Description

In a Ruby environment with the Shopify API SDK, review the source code focusing on Session.setup, prepare_url, and access_token_request methods. The prepare_url method appends the port directly to the shop URL without sanitization, while access_token_request uses URI.parse on the resulting string, allowing attackers to exploit URI parsing behaviors (e.g., '@' to override host) to redirect HTTP requests to arbitrary endpoints like localhost, exfiltrating sensitive OAuth data.

## Requirements

1. Ruby installed with Shopify API SDK gem (gem install shopify_api)
2. Access to SDK source code (e.g., via bundle show shopify_api)
3. Pry for interactive inspection if needed

## Defense

Defensive measures and detection strategies:

- Implement strict regex validation on port (e.g., /^[0-9]+$/ ) and protocol (e.g., /^(http|https)$/) in SDK
- Use URL parsing libraries with safe defaults to prevent injection
- Monitor for anomalous internal HTTP requests to localhost or private IPs

## Objectives

1. Identify validation gaps in SDK methods
2. Understand URI parsing exploitation vectors
3. Prepare for targeted testing of injection points

## Instructions

### Step 1: Load SDK in Interactive Shell

**Context**: Start a pry session to load and inspect SDK classes and methods.

**Command** ([[commands/require-shopify-api]]):
```ruby
require 'shopify_api'
```

> Loads the ShopifyAPI module, enabling access to Session class. Expected output: true.

### Step 2: Review Key Methods

**Context**: Manually inspect prepare_url and access_token_request for validation logic.

**Instructions**: In pry, use method_source or read source files to check for sanitization. Look for direct string concatenation in prepare_url and URI.parse usage in access_token_request.

**Expected Output**: No validation found; port appended as-is, protocol used in URI construction.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/require-shopify-api]]

## Tools Used

- [[tools/pry]]

## Tags

- ssrf
- code-review
- shopify
