---
id: proc-uuid-2
tags:
  - subdomain-takeover
  - registration
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.884Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register Dangling Record on External Service

## Summary

This procedure claims control of a dangling DNS record by registering the associated resource on the external service provider, effectively taking over the subdomain.

## Description

Once a dangling record is identified (e.g., CNAME to an unused Heroku app), the attacker registers a new instance on that service matching the record name. This redirects the subdomain traffic to the attacker's controlled resource. For mozaws.net, this grants control over a Mozilla-owned subdomain. No authentication is typically needed beyond a free account on the provider.

## Requirements

1. Account on the target service provider (e.g., free Heroku account)
2. Identified dangling service from prior recon
3. Web browser for registration

## Defense

Defensive measures and detection strategies:

- Monitor for new registrations on third-party services using the organization's domain
- Implement certificate pinning or HSTS to limit subdomain trust
- Conduct periodic subdomain audits and remove dangling records

## Objectives

1. Gain control over the subdomain DNS resolution
2. Redirect traffic to attacker-controlled server
3. Prepare for content hosting

## Instructions

### Step 1: Access Service Provider Dashboard

**Context**: Log in to the external service (e.g., Heroku) and create a new app with the exact name from the dangling record.

No command; manual step: Visit heroku.com, sign up/log in, and run `heroku create example-sub` in CLI if available.

> Expected: App created successfully.

### Step 2: Verify DNS Propagation

**Context**: Confirm the subdomain now points to your registered resource.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig example-sub.mozaws.net
```

> Query DNS after registration. Expected output: CNAME now resolves to your active service endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- None specific

## Tags

- [[subdomain-takeover]]
- [[DNS]]
