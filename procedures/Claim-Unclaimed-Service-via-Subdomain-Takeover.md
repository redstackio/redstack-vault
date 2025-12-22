---
tags:
  - subdomain-takeover
  - dns
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.536Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8dfd7d2d-5b5a-4c4d-b5ed-cd11bc6eda3d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim Unclaimed Service via Subdomain Takeover

## Summary

This procedure claims ownership of an unclaimed third-party service referenced by a target's dangling CNAME record, effectively taking over the subdomain for malicious use.

## Description

Once a dangling CNAME is identified, the attacker registers the exact hostname on the external service provider. For Uber's case, subdomains pointed to unused Heroku-like services, allowing quick registration. This grants control over traffic to the subdomain, enabling phishing or defacement. Requires identifying the service type from the CNAME.

## Requirements

1. Identified dangling CNAME from prior enumeration
2. Account creation capability on the third-party service (e.g., Heroku, GitHub)
3. Basic web access to service dashboards

## Defense

Defensive measures and detection strategies:

- Automate CNAME cleanup on service deletion
- Use DNS security extensions (DNSSEC) to prevent hijacking
- Alert on new registrations matching owned domains

## Objectives

1. Register the dangling hostname on the external service
2. Verify subdomain resolution to the claimed resource
3. Establish persistent control over the subdomain

## Instructions

### Step 1: Identify Service Provider

**Context**: Determine the platform from the CNAME (e.g., .herokuapp.com indicates Heroku).

No command; manual review of CNAME output.

> Expected: Confirmation of service type.

### Step 2: Register the Hostname

**Context**: Create and claim the specific app/site matching the dangling name.

Navigate to the service dashboard (e.g., heroku.com) and run:

```bash
heroku create unclaimed-app
```

> If CLI available; otherwise, use web UI. Expected: Ownership confirmation.

### Step 3: Verify Takeover

**Context**: Confirm DNS propagation and control.

Query DNS:

```bash
dig +short de.uber.com
```

> Expected: Resolves to your claimed service IP or hostname.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cname-takeover]]
- [[service-claim]]
