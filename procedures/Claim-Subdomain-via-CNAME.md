---
tags:
  - subdomain-takeover
  - cname
  - account-compromise
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - DNS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T04:38:39.870Z'
sub_techniques: []
id: 522dbbe4-1c3b-454d-bfa7-ad8e4e51e9a8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Manipulation]]'
---
# Claim-Subdomain-via-CNAME

## Summary

This procedure claims control of a dangling subdomain by adding the target CNAME in the external service's dashboard, achieving full takeover.

## Description

With an account on the service, attackers add the subdomain's CNAME record, hijacking traffic. This leads to control over HTTP/HTTPS content, emails, and security features. Verification involves re-querying DNS and loading the subdomain.

## Requirements

1. Active account on the external service (e.g., Brandpad.io)
2. Dashboard access for DNS settings
3. Target subdomain details from prior steps

## Defense

Defensive measures and detection strategies:

- Implement automated DNS cleanup scripts
- Use subdomain takeover scanners like subjack in CI/CD
- Alert on DNS changes via services like Cloudflare

## Objectives

1. Redirect subdomain traffic to attacker-controlled content
2. Enable follow-on attacks like phishing or XSS
3. Demonstrate impact with proof (e.g., video)

## Instructions

### Step 1: Add CNAME Record

**Context**: In the service dashboard, configure the subdomain CNAME.

No command required; navigate to domain settings in Brandpad.io and add CNAME for brand.zen.ly pointing back to Brandpad's endpoint.

> Save changes; DNS propagation may take minutes.

### Step 2: Verify Takeover

**Context**: Re-query DNS and test access to confirm control.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig brand.zen.ly
```

> Output should now reflect control under your account; visit https://brand.zen.ly/ to see custom content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Manipulation]] Account Manipulation: Subdomain

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[subdomain-takeover]]
- [[DNS]]
