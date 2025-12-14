---
id: proc-trigger-logout-redirect
tags:
  - open-redirect
  - expedia
  - logout
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-logout-observe]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:34.976Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Open-Redirect-on-Logout

## Summary

This procedure demonstrates observing the default logout behavior on Expedia.com to identify the open redirect vulnerability in the rurl parameter, setting the stage for exploitation.

## Description

In the Expedia web application, logging out sends a GET request to /?logout=1, which redirects to the homepage. This normal flow reveals the lack of validation on URL parameters, allowing subsequent modification for arbitrary redirects. The target environment is the public-facing Expedia website, requiring only an authenticated session. Expected outcomes include confirming the redirect mechanism without errors, enabling phishing by tricking users into malicious URLs post-logout.

## Requirements

1. Valid Expedia account for authentication
2. Web browser or curl for request simulation
3. Internet access to www.expedia.com

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation to whitelist allowed domains for redirects
- Enforce URL encoding and sanitization on all redirect parameters
- Monitor for unusual redirect patterns in web logs

## Objectives

1. Confirm default logout redirect to homepage
2. Identify exploitable rurl parameter
3. Validate no immediate blocking of external URLs

## Instructions

### Step 1: Authenticate and Initiate Logout

**Context**: Log in to Expedia and trigger the logout to observe the request structure.

**Command** ([[commands/curl-logout-observe]]):
```bash
curl -X GET "https://www.expedia.com/?logout=1" -v
```

> This command sends the logout request and verbose output shows the 302 redirect to the homepage. Successful execution confirms the session ends and redirects properly.

### Step 2: Inspect Response Headers

**Context**: Analyze the Location header to understand the redirect target.

No specific command; review curl output for Location: https://www.expedia.com/.

> Expected: Clean redirect without parameter validation errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-logout-observe]]

## Tools Used


## Tags

- [[open-redirect]]
- [[expedia]]
