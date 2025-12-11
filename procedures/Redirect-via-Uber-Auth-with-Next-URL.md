---
tags:
  - open-redirect
  - next-url
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Use Alternate Authentication Material]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f0e90eca-259f-4423-9c9e-2aa2ed7ed182
created_at: '2025-12-11T06:10:15.766Z'
updated_at: '2025-12-11T06:10:15.766Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0008]]'
mitre_techniques:
  - '[[T1550]]'
---
# Redirect via Uber Auth with Next URL

## Summary

This procedure handles the redirect from Facebook to Uber's auth endpoint using the next_url parameter to chain to the logout endpoint, exploiting open redirect vulnerability.

## Description

After Facebook authorization, the redirect hits auth.uber.com/login with next_url set to logout. The endpoint allows arbitrary internal chaining without validation, advancing the attack to the token-leaking stage.

## Requirements

1. Successful authorization code from prior step
2. Control over redirect_uri in initial request
3. No authentication needed as it's post-authorization redirect

## Defense

Defensive measures and detection strategies:

- Validate and restrict next_url parameters to safe endpoints
- Implement CSRF tokens for redirect chains

## Objectives

1. Chain redirect to internal logout endpoint
2. Maintain control over redirection flow
3. Prepare for Referer-based external redirect

## Instructions

### Step 1: Receive Facebook Redirect

**Context**: Facebook redirects to the crafted auth.uber.com URL with next_url.

The incoming request will be:

```
https://auth.uber.com/login?next_url=https://login.uber.com/logout&code=AUTH_CODE
```

> Uber processes this and redirects to next_url.

### Step 2: Monitor Redirect

**Context**: Ensure the chain proceeds without interruption.

No manual action needed; the server handles the redirect.

> Verify in browser tools or logs that redirect occurs to logout.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Use Alternate Authentication Material]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[open-redirect]]
- [[next-url]]
