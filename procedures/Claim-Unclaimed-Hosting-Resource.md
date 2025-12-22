---
id: p-claim-unclaimed-resource
tags:
  - subdomain-takeover
  - exploitation
  - hosting-service
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
updated_at: '2025-12-14T04:38:49.240Z'
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
# Claim Unclaimed Hosting Resource

## Summary

This procedure registers an unclaimed resource on a third-party hosting service to takeover a dangling subdomain, granting full control over traffic to the trusted domain.

## Description

Once verified, claim the resource via the service's interface, as in the firefox.com incident where ███████ allowed registration. This leads to DNS propagation and control, enabling malicious content hosting. No technical barriers beyond account creation.

## Requirements

1. Account on the third-party service (e.g., ███████)
2. Verified unclaimed target
3. Basic web navigation skills

## Defense

Defensive measures and detection strategies:

- Implement automated alerts for subdomain claims
- Rotate or remove expired CNAMEs promptly
- Partner with hosting providers for takeover notifications

## Objectives

1. Secure ownership of the dangling resource
2. Propagate DNS to route traffic to attacker-controlled server
3. Establish persistent access

## Instructions

### Step 1: Access Service Dashboard

**Context**: Log in and search for the resource.

No command; navigate to ███████ login, create account if needed, and search for 'target-resource'.

> Expected: Option to claim/register.

### Step 2: Register and Verify

**Context**: Complete registration and test resolution.

Use [[commands/dig-dns-lookup]] post-claim:

```bash
dig +short subdomain.firefox.com
```

> Output should now point to your claimed resource.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[exploitation]]
