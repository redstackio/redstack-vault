---
id: proc-relateiq-identify-custom-server
tags:
  - ssrf
  - registration
  - gwt
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:20.613Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Custom Server Option in Registration

## Summary

This procedure involves inspecting the RelateIQ registration process to identify the custom server URL option in the Office365 integration, which lacks validation and enables SSRF exploitation.

## Description

In the RelateIQ web application, the registration feature includes an Office365 account validation step. The custom server option allows users to specify an arbitrary URL, which is forwarded to the validateOffice365Account RPC method without checks on host or port. This reconnaissance step uncovers the vulnerability entry point for SSRF-based attacks, targeting GWT-based endpoints.

## Requirements

1. Access to the public RelateIQ registration page at https://app.relateiq.com
2. Web browser with developer tools to inspect forms and network requests
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement URL allowlisting in registration forms to restrict custom server inputs to trusted domains
- Monitor RPC endpoint logs for unusual URL patterns or localhost references
- Use web application firewalls (WAF) to block requests with internal IP addresses

## Objectives

1. Locate the vulnerable custom server parameter
2. Understand the RPC method invocation
3. Prepare for crafting exploit requests

## Instructions

### Step 1: Access Registration Page

**Context**: Navigate to the RelateIQ signup to expose the Office365 integration form.

No command needed; use browser to visit https://app.relateiq.com and start registration.

> Inspect the form HTML for input fields related to 'custom server' or Office365 URL.

### Step 2: Inspect Network Requests

**Context**: Trigger the validation to observe the backend RPC call.

Use browser dev tools (Network tab) while submitting a test registration with a custom URL.

> Look for POST requests to /app/GWT.rpc; note the payload structure including validateOffice365Account.

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
- registration
- reconnaissance
