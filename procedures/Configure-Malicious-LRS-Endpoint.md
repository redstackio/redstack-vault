---
tags:
  - ssrf
  - lrs-config
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:10.046Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 5478e8b2-d9b9-4889-b5e1-da146b982adc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Malicious-LRS-Endpoint

## Summary

This procedure injects the SSRF payload by configuring an LRS endpoint with the AWS metadata URL and basic authentication, exploiting the lack of URL validation in the input field.

## Description

The LRS Configurations feature allows specifying an endpoint URL for xAPI statements, but without allowlisting or validation, internal IPs like 169.254.169.254 can be used. Setting basic auth to dummy values ('test:test') ensures the config saves. This positions the server to make unauthorized requests during testing, targeting AWS-hosted apps. Outcomes include a persisted malicious config ready for triggering.

## Requirements

1. Existing product with access to LRS section
2. Knowledge of AWS metadata endpoint (http://169.254.169.254/latest/meta-data?)
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Validate and allowlist LRS URLs to external domains only
- Block internal IP ranges (e.g., 169.254.0.0/16) in URL parsing
- Log and alert on config attempts with internal hosts

## Objectives

1. Persist SSRF payload in application config
2. Bypass URL validation for internal access
3. Set up for server-side request execution

## Instructions

### Step 1: Access LRS Configurations

**Context**: Navigate to the configuration interface for the product.

After product creation, click 'New Configuration' under the LRS Configurations section.

**Expected Output**: Form for LRS details loaded.

### Step 2: Enter Malicious URL and Auth

**Context**: Input the SSRF payload and credentials.

Set LRS URL to 'http://169.254.169.254/latest/meta-data?' (question mark is crucial for path traversal), enter 'test' for Basic Auth User and Password, then click 'Create new LRS configuration'.

**Expected Output**: Configuration created and listed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- lrs-config
- payload-injection
