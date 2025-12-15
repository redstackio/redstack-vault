---
id: uuid-1
tags:
  - open-redirect
  - web-vulnerability
  - uber
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
updated_at: '2025-12-14T17:24:27.240Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Discover Open Redirect on Uber Domain

## Summary

This procedure identifies an open redirect vulnerability in the uber.com path handling, allowing redirection to arbitrary external domains without validation, which can be used as a foundation for phishing or resource loading attacks.

## Description

The uber.com application processes paths like /en//example.com/ by issuing an HTTP 301 redirect to //example.com/ without checking the domain. This enables attackers to trick users into visiting malicious sites under the guise of legitimate redirects. The vulnerability stems from unvalidated path manipulation in the redirect logic.

## Requirements

1. Web browser with network inspection capabilities
2. Direct access to uber.com over HTTPS
3. URL encoding knowledge for path testing

## Defense

Defensive measures and detection strategies:

- Implement domain whitelisting for all redirects
- Validate redirect targets against a strict allowlist
- Log and monitor unusual redirect patterns in access logs

## Objectives

1. Confirm open redirect functionality
2. Document the exact path format for chaining
3. Assess potential for phishing impact

## Instructions

### Step 1: Construct and Access Test URL

**Context**: Build a path that traverses to an external domain and trigger the request to observe the redirect behavior.

No specific command; use browser or curl equivalent:

```http
GET https://www.uber.com/en//example.com/
```

> The server responds with HTTP 301 and Location: //example.com/, causing the browser to follow the redirect to the external site.

### Step 2: Validate Redirect

**Context**: Inspect the response to ensure no validation blocks the external domain.

Use browser developer tools to check the network tab for the 301 status and Location header.

**Expected Output**: Redirect completes, loading example.com without uber.com domain restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[web]]
- [[uber]]
