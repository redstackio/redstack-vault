---
tags:
  - oauth-testing
  - valid-scope
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-visit-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.493Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c546f42e-8a77-4a5b-b222-b7ec9abc74e5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Shopify-OAuth-with-Valid-Scope

## Summary

This procedure tests the standard OAuth authorization flow on a Shopify store using a valid scope to confirm that redirect URI hostname validation prevents external redirections under normal conditions.

## Description

Using the client ID from the created app, construct the OAuth authorize URL with a valid scope (e.g., read_customers) and the malicious redirect URI. Accessing this URL should trigger validation, resulting in no redirection to the external site. This step validates the baseline behavior before exploiting the vulnerability. Target is a Shopify store's admin OAuth endpoint. Prerequisites include the app client ID. Expected outcome: Error response confirming URI validation.

## Requirements

1. Valid client ID from created app
2. Target Shopify store URL (e.g., prans.myshopify.com)
3. Tool for HTTP requests (curl or browser)

## Defense

Defensive measures and detection strategies:

- Log all OAuth authorize requests and alert on valid scope with suspicious URIs
- Enforce strict hostname whitelisting for all redirect URIs
- Monitor for repeated testing patterns from the same IP

## Objectives

1. Confirm normal validation of redirect URI with valid scope
2. Establish baseline for vulnerability comparison
3. Identify any pre-existing misconfigurations

## Instructions

### Step 1: Construct Valid Scope URL

**Context**: Build the OAuth URL with read_customers scope to test enforcement.

**Command** ([[commands/curl-visit-url]]):
```bash
curl "https://prans.myshopify.com/admin/oauth/authorize?client_id=616ce3efcd495007438000ad958a6629&scope=read_customers&redirect_uri=http://www.facebook.com/abc/"
```

> This sends a GET request to the endpoint. Expected output: HTTP response with validation error, no Location header redirect to external site.

### Step 2: Analyze Response

**Context**: Review the response to confirm no bypass occurred.

No command; inspect output manually.

> Look for error messages related to invalid redirect URI. Expected output: Standard Shopify error page or JSON error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-visit-url]]

## Tools Used


## Tags

- oauth-testing
- valid-scope
- shopify
