---
id: proc-register-dangling-subdomain
tags:
  - domain-registration
  - subdomain-hijacking
  - resource-development
type: procedure
tactics:
  - '[[Resource Development]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1583.001]]'
updated_at: '2025-12-14T05:32:23.375Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Resource Development]]'
mitre_techniques:
  - '[[T1583.001]]'
---
# Register and Claim Dangling Subdomain

## Summary

This procedure claims control of a dangling subdomain by registering the associated resource with the third-party DNS provider, effectively hijacking the subdomain under the target's domain.

## Description

Once a dangling DNS record is identified, such as a CNAME under mozaws.net pointing to an unregistered service, the attacker registers the resource on the provider's platform. This leverages the DNS propagation to redirect traffic to the attacker's controlled endpoint, enabling further exploitation like phishing.

## Requirements

1. Account on the third-party service (e.g., Heroku, AWS)
2. Exact subdomain name from the dangling record
3. Public internet access for registration

## Defense

Defensive measures and detection strategies:

- Delete unused DNS records promptly
- Use domain monitoring tools to alert on takeovers
- Implement strict DNS record management policies

## Objectives

1. Gain control over the subdomain
2. Redirect DNS traffic to attacker-controlled resources
3. Prepare for content hosting

## Instructions

### Step 1: Access Provider Dashboard

**Context**: Log in to the third-party service identified in the DNS record.

Navigate to the registration or app creation page on the provider's website.

### Step 2: Create Resource with Subdomain Name

**Context**: Register a new resource using the dangling subdomain as the identifier.

Enter the subdomain (e.g., vulnerable.mozaws.net) during setup; the provider will associate it automatically.

### Step 3: Verify DNS Resolution

**Context**: Confirm the takeover by querying DNS.

Wait for propagation and test resolution to ensure it points to your new resource.

## MITRE ATT&CK Mapping

### Tactics

- [[Resource Development]] Resource Development

### Techniques

- [[T1583.001]] Acquire Infrastructure: Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[dns-hijack]]
