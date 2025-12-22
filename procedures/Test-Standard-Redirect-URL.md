---
id: proc-test-standard-redirect
tags:
  - open-redirect
  - validation-test
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:23.517Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Standard-Redirect-URL

## Summary

This procedure tests the Khan Academy login page's handling of a standard external redirect URL in the 'continue' parameter to confirm that validation blocks legitimate external redirects, setting the stage for bypass attempts.

## Description

In the context of identifying open redirect vulnerabilities, this initial test accesses the login endpoint with a properly formatted HTTP URL. The application should reject the redirect to prevent navigation away from trusted domains, but this confirms the presence of validation logic that can potentially be bypassed. This is crucial for web security assessments targeting phishing vectors post-authentication.

## Requirements

1. Internet access to khanacademy.org
2. Web browser or curl tool
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation allowing only whitelisted domains
- Log all redirect attempts and monitor for anomalies in 'continue' parameters
- Use Content Security Policy (CSP) to restrict navigation

## Objectives

1. Verify that standard external redirects are blocked
2. Establish baseline for bypass testing
3. Identify validation mechanism for exploitation

## Instructions

### Step 1: Access Login with Standard URL

**Context**: Send a request to the login page with a standard 'continue' parameter pointing to an external HTTP site to test blocking.

**Command** ([[commands/curl-access-url]]):
```bash
curl -L "https://www.khanacademy.org/login?continue=http://www.olivierbeg.nl"
```

> This command follows redirects (-L) and attempts to access the malformed URL. Expected output is a block or error response, confirming validation without redirection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[open-redirect]]
- [[validation-test]]
