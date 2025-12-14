---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - subdomain-takeover
  - exploitation
  - dns
  - web
type: procedure
tools:
  - '[[tools/GitHub-Recon-Techniques]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.606Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm and Demonstrate Subdomain Takeover

## Summary

This procedure confirms control over dangling subdomains by claiming associated services and serving arbitrary content, exploiting server fallback routing that preserves the original Host header for unauthorized access.

## Description

Targeting subdomains of {REDACTED}.data.gov, this exploits dangling DNS records combined with a static site host's routing, which treats unknown subdomains as fallbacks to the main domain while proxying the Host header. Attackers claim the pointed service (e.g., unused GitHub Page), configure custom content, and demonstrate via HTTP requests. This leads to phishing or reputation damage on government domains. Prerequisites: Identified dangling subdomains; outcomes: Full control verified by content serving.

## Requirements

1. Access to claim the dangling service (e.g., GitHub account for Pages)
2. HTTP client for testing (browser or curl)
3. Knowledge of the target's routing behavior

## Defense

Defensive measures and detection strategies:

- Implement wildcard DNS blocking or strict subdomain validation
- Monitor for anomalous content on subdomains via WAF logs
- Rotate and audit all DNS records periodically

## Objectives

1. Claim control of the dangling service
2. Serve and verify arbitrary content on the subdomain
3. Assess impact like phishing potential

## Instructions

### Step 1: Claim the Dangling Service

**Context**: Register or take over the unused service pointed by the CNAME, such as creating a GitHub repository matching the dangling record.

Using [[tools/GitHub-Recon-Techniques]], configure the service to host custom content, e.g., a simple HTML page with proof-of-control text.

> Update the service's DNS or config to point correctly; wait for propagation (TTL ~5-10 min).

### Step 2: Test Takeover with HTTP Request

**Context**: Send a request to the subdomain to confirm fallback routing delivers your content via preserved Host header.

Use a browser or curl to access `http://sub.{REDACTED}.data.gov`:

```bash
curl -H "Host: sub.{REDACTED}.data.gov" http://www.{REDACTED}.data.gov
```

> Expected output: Your arbitrary content (e.g., "Taken over by researcher") instead of 404 or default page. Repeat for all 7 subdomains to confirm.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GitHub-Recon-Techniques]]

## Tags

- [[subdomain-takeover]]
- [[exploitation]]
