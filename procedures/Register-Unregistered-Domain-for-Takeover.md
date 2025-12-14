---
id: proc-register-domain-takeover
tags:
  - domain-registration
  - infrastructure-acquisition
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Resource Development]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1583.001]]'
updated_at: '2025-12-14T05:32:23.353Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Resource Development]]'
mitre_techniques:
  - '[[T1583.001]]'
---
# Register Unregistered Domain for Takeover

## Summary

This procedure involves claiming an unregistered domain identified from a dangling DNS record, granting control over the associated target subdomain.

## Description

Once a dangling CNAME is discovered (e.g., mozaws.net subdomain pointing to unregistered-domain.com), the attacker registers the domain via a public registrar. This step requires no technical exploits but timely action before others claim it. In the Mozilla case, registration allowed reconfiguration of DNS to intercept traffic. Prerequisites: Payment method and registrar account. Outcomes: Ownership of the domain, enabling further hosting setup.

## Requirements

1. Identified dangling domain from prior reconnaissance
2. Account on a domain registrar (e.g., GoDaddy)
3. Funds for registration (typically $10-20/year)

## Defense

Defensive measures and detection strategies:

- Monitor for new registrations of known dangling targets using services like DomainTools
- Proactively register potentially dangling domains
- Implement certificate transparency monitoring for subdomains

## Objectives

1. Acquire the dangling domain
2. Gain DNS control for the target subdomain
3. Enable content hosting under the original domain

## Instructions

### Step 1: Search for Domain Availability

**Context**: Confirm the domain is still available post-discovery.

Navigate to a registrar's search page (e.g., godaddy.com) and enter the domain name. If available, proceed to checkout.

### Step 2: Complete Registration

**Context**: Purchase and configure initial DNS settings.

Provide contact info, select privacy options, and pay. After confirmation, access the DNS management panel to prepare for hosting aliasing.

### Step 3: Verify Ownership

**Context**: Test that the registration is active and resolvable.

Use [[commands/dig-query]] to check NS records:

```bash
dig +short NS unregistered-domain.com
```

> Expected output: Registrar's nameservers, confirming control transfer.

## MITRE ATT&CK Mapping

### Tactics

- [[Resource Development]] Resource Development

### Techniques

- [[T1583.001]] Acquire Infrastructure: Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[domain-registration]]
- [[subdomain-takeover]]
