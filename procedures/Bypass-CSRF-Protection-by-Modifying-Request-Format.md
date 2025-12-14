---
tags:
  - csrf
  - bypass
  - web
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
updated_at: '2025-12-14T17:28:36.408Z'
sub_techniques: []
id: 51de3d3c-27fd-4fd8-b7fb-8a41242907c3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-CSRF-Protection-by-Modifying-Request-Format

## Summary

This procedure demonstrates bypassing CSRF protection on the TikTok Shop ticket endpoint by removing the CSRF token and switching to x-www-form-urlencoded content type, allowing forged requests to be processed.

## Description

Targeting the ticket creation endpoint, this exploits improper validation by altering the request format. The attack scenario involves modifying intercepted requests in a proxy tool or DevTools. Prerequisites include knowledge of the legitimate format from prior analysis. Outcomes: Successful ticket creation without token validation, confirming the vulnerability.

## Requirements

1. Browser with interception capabilities (e.g., DevTools or Burp Suite)
2. Valid session to TikTok Shop
3. Documented legitimate request details

## Defense

Defensive measures and detection strategies:

- Enforce strict CSRF token validation regardless of content type
- Monitor for requests missing tokens or using unexpected content types

## Objectives

1. Remove CSRF token and alter content type to evade protection
2. Verify endpoint processes forged requests
3. Enable cross-site forgery

## Instructions

### Step 1: Intercept and Modify Request

**Context**: Capture a legitimate request and apply changes to test bypass.

In DevTools Network tab or a proxy, intercept the POST to https://vulnerableEndpoint. Edit headers: remove CsrfToken, set Content-Type: application/x-www-form-urlencoded. Convert JSON body to form-encoded (e.g., category_id=1&title=Test).

**Expected Output**: Modified request sent successfully.

### Step 2: Test and Confirm

**Context**: Submit variations to ensure acceptance.

Resubmit the altered request multiple times, adjusting encoding if needed. Check for ticket creation in the account.

**Expected Output**: Ticket created without token, proving bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[bypass]]
