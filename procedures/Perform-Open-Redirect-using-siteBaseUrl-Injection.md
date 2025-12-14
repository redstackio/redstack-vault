---
tags:
  - open-redirect
  - xss
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-open-redirect]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
id: 5e032953-5200-4b39-8c5b-19be17329174
created_at: '2025-12-14T03:46:31.605Z'
updated_at: '2025-12-14T03:46:31.605Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Perform Open Redirect using siteBaseUrl Injection

## Summary

This procedure leverages the XSS breakout in siteBaseUrl to inject a script that redirects the victim's browser to an arbitrary external site, enabling phishing or further attacks.

## Description

Building on the context breakout, inject a <script> tag after %0a to set window.location to a malicious URL. This combines open redirect with XSS, bypassing any partial URL validation. The victim is seamlessly redirected upon page load, useful for delivering malware or stealing credentials on a fake site.

## Requirements

1. Confirmed XSS breakout capability
2. Control over a redirect target (e.g., attacker server)
3. Browser testing environment

## Defense

Defensive measures and detection strategies:

- Enforce strict URL validation for siteBaseUrl (e.g., only subdomains of starbucks.com)
- Implement referrer checks on redirects
- Detect script injections via WAF rules on parameters

## Objectives

1. Redirect to external domain
2. Maintain stealth via JS execution
3. Facilitate phishing chains

## Instructions

### Step 1: Inject Redirect Payload

**Context**: Replace prompt with location change in script.

**Command** ([[commands/curl-test-open-redirect]]):
```bash
curl -G "https://openapi.starbucks.com/searchasyoutype/v1/search" -d "query=coffee" -d "siteBaseUrl=http://googl.com/%0a<script>window.location='https://google.com';</script>" --header "x-api-key: YOUR_API_KEY"
```

> Load in browser; page should redirect immediately to google.com.

### Step 2: Test with Malicious Target

**Context**: Swap URL to attacker-controlled site.

Use the same command, changing 'https://google.com' to your domain.

> Verify redirect lands on target without alerts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

-

## Commands Used

- [[commands/curl-test-open-redirect]]

## Tools Used

-

## Tags

- [[open-redirect]]
- [[xss]]
- [[Phishing]]
