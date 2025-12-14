---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - subdomain-takeover
  - verification
  - tumblr
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-http-check]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:10.687Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify Unused Subdomain on Third-Party Service

## Summary

This procedure checks if a subdomain pointed by a dangling CNAME is actively used on the third-party service, confirming availability for takeover.

## Description

Targeting services like Tumblr, this step involves probing the subdomain URL to ensure no existing content or blog exists, allowing subsequent registration. In the Shopify case, ux.shopify.com resolved to Tumblr but had no active blog, making it claimable. This prevents wasted effort on protected subdomains and confirms the misconfiguration.

## Requirements

1. Valid CNAME pointer from prior DNS recon
2. Web access to the subdomain
3. Knowledge of the service's claim process

## Defense

Defensive measures and detection strategies:

- Monitor third-party service logs for claim attempts
- Proactively claim or delete unused subdomains during migrations
- Use subdomain monitoring tools to alert on takeovers

## Objectives

1. Confirm subdomain is unclaimed
2. Identify any redirects or existing content
3. Prepare for registration

## Instructions

### Step 1: Probe Subdomain

**Context**: Send an HTTP request to the subdomain to check for active content.

**Command** ([[commands/curl-http-check]]):
```bash
curl -I http://ux.shopify.com
```

> This HEAD request checks headers; a 301/302 to Tumblr or empty response indicates availability. No active blog means it's unused.

### Step 2: Manual Verification

**Context**: Access the URL in a browser to search for or confirm no blog exists on the service.

No command; use web browser to visit http://ux.shopify.com and check Tumblr's interface.

> Expected: Page indicating subdomain is available or no content.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-http-check]]

## Tools Used

- None

## Tags

- [[subdomain-takeover]]
- [[verification]]
